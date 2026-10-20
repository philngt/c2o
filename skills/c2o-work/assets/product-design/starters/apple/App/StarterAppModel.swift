import Combine
import Foundation
import StarterCore
import WidgetKit

struct StarterSettings: Codable {
    var keepUtilityHistory = false
}

struct RecordEditorRequest: Identifiable {
    let id = UUID()
    let record: LifestyleRecord?
}

enum StarterSheet: Identifiable {
    case editor(RecordEditorRequest)
    case settings
    case history

    var id: String {
        switch self {
        case .editor(let request): return request.id.uuidString
        case .settings: return "settings"
        case .history: return "history"
        }
    }
}

private enum AppActionError: LocalizedError {
    case message(String)
    var errorDescription: String? {
        if case .message(let message) = self { return message }
        return nil
    }
}

/// A single app writer for a small, local starter. File operations are synchronous.
/// Move them to a serialized repository before introducing large data or sync.
@MainActor
final class StarterAppModel: ObservableObject {
    static let historyLimit = 50

    @Published private(set) var records: [LifestyleRecord] = []
    @Published private(set) var history: [UtilityHistoryItem] = []
    @Published private(set) var settings = StarterSettings()
    @Published private(set) var collectionReady = false
    @Published private(set) var historyReady = false
    @Published private(set) var settingsReady = false
    @Published private(set) var collectionLoadError: String?
    @Published private(set) var historyLoadError: String?
    @Published private(set) var settingsLoadError: String?

    @Published var selectedRecordID: UUID?
    @Published var recordPath: [UUID] = []
    @Published var recordQuery = ""
    @Published var sheet: StarterSheet?
    var pendingRoute: StarterRoute?

    @Published var utilityInput = ""
    @Published private(set) var utilityOutput = ""
    @Published private(set) var processedInput: String?
    @Published var confirmNewText = false
    @Published private(set) var utilityNavigationRequest = UUID()
    @Published var actionError: String?
    @Published var historySaveWarning: String?
    @Published var widgetWarning: String?

    private let store: LocalFileStore
    private let recordsFilename = "collection-v1.json"
    private let historyFilename = "utility-history-v1.json"
    private let settingsFilename = "app-settings-v1.json"

    init(store: LocalFileStore = LocalFileStore()) {
        self.store = store
        loadSettings()
        switch AppProfile.category {
        case .lifestyle: loadCollection()
        case .utility:
            loadHistory()
            publishWidgetSnapshot()
        }
    }

    var filteredRecords: [LifestyleRecord] {
        let query = recordQuery.trimmingCharacters(in: .whitespacesAndNewlines)
        return records.filter {
            query.isEmpty || $0.title.localizedCaseInsensitiveContains(query)
                || $0.notes.localizedCaseInsensitiveContains(query)
        }.sorted {
            if $0.updatedAt == $1.updatedAt { return $0.id.uuidString < $1.id.uuidString }
            return $0.updatedAt > $1.updatedAt
        }
    }

    /// An edit invalidates the visible result; old output cannot be copied as current.
    var hasUtilityResult: Bool {
        processedInput != nil && processedInput == utilityInput
    }

    func record(id: UUID) -> LifestyleRecord? {
        records.first { $0.id == id }
    }

    func loadSettings() {
        settingsReady = false
        do {
            settings = try store.load(StarterSettings.self, filename: settingsFilename)
                ?? StarterSettings()
            settingsLoadError = nil
            settingsReady = true
        } catch {
            settingsLoadError = error.localizedDescription
        }
    }

    func loadCollection() {
        collectionReady = false
        do {
            let loaded = try store.load([LifestyleRecord].self, filename: recordsFilename) ?? []
            guard Set(loaded.map(\.id)).count == loaded.count else {
                throw AppActionError.message("Có mã mục bị trùng trong dữ liệu đã lưu.")
            }
            records = loaded
            collectionLoadError = nil
            collectionReady = true
            if let id = selectedRecordID, record(id: id) == nil {
                selectedRecordID = nil
                recordPath = []
            }
            publishWidgetSnapshot()
        } catch {
            collectionLoadError = error.localizedDescription
        }
    }

    func loadHistory() {
        historyReady = false
        do {
            let loaded = try store.load([UtilityHistoryItem].self, filename: historyFilename) ?? []
            guard Set(loaded.map(\.id)).count == loaded.count else {
                throw AppActionError.message("Có mã lần xử lý bị trùng trong lịch sử.")
            }
            history = loaded.sorted { $0.createdAt > $1.createdAt }
            historyLoadError = nil
            historyReady = true
        } catch {
            historyLoadError = error.localizedDescription
        }
    }

    func setKeepUtilityHistory(_ enabled: Bool) throws {
        guard settingsReady else {
            throw AppActionError.message("Hãy thử đọc lại cài đặt trước khi thay đổi.")
        }
        guard !enabled || historyReady else {
            throw AppActionError.message("Hãy thử đọc lại lịch sử trước khi bật lưu.")
        }
        let next = StarterSettings(keepUtilityHistory: enabled)
        try store.save(next, filename: settingsFilename)
        settings = next
    }

    func saveRecord(_ draft: LifestyleRecord) throws {
        try requireCollectionReady()
        var saved = draft
        saved.title = draft.title.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !saved.title.isEmpty else {
            throw AppActionError.message("Nhập tên cho mục này trước khi lưu.")
        }
        saved.updatedAt = Date()
        var next = records
        if let index = next.firstIndex(where: { $0.id == saved.id }) {
            next[index] = saved
        } else {
            next.append(saved)
        }
        // Commit the file first. A failed write leaves model and editor draft intact.
        try store.save(next, filename: recordsFilename)
        records = next
        publishWidgetSnapshot()
    }

    func toggleFavorite(id: UUID) throws {
        guard var item = record(id: id) else {
            throw AppActionError.message("Mục này không còn trong bộ sưu tập.")
        }
        item.isFavorite.toggle()
        try saveRecord(item)
    }

    func deleteRecord(id: UUID) throws {
        try requireCollectionReady()
        let next = records.filter { $0.id != id }
        try store.save(next, filename: recordsFilename)
        records = next
        if selectedRecordID == id { selectedRecordID = nil }
        recordPath.removeAll { $0 == id }
        publishWidgetSnapshot()
    }

    func openRecord(id: UUID) {
        recordQuery = ""
        selectedRecordID = id
        recordPath = [id]
    }

    func editRecord(_ record: LifestyleRecord?) {
        guard collectionReady, sheet == nil else { return }
        sheet = .editor(RecordEditorRequest(record: record))
    }

    func requestNewItem() {
        switch AppProfile.category {
        case .lifestyle: editRecord(nil)
        case .utility:
            if utilityInput.isEmpty { clearText() }
            else { confirmNewText = true }
        }
    }

    func runTextTools() {
        let input = utilityInput
        let output = TextTools.normalizedWhitespace(input)
        utilityOutput = output
        processedInput = input
        historySaveWarning = nil

        // The result succeeds independently of the optional history transaction.
        if settingsReady && settings.keepUtilityHistory {
            if historyReady {
                let item = UtilityHistoryItem(input: input, output: output)
                let next = Array(([item] + history).prefix(Self.historyLimit))
                do {
                    try store.save(next, filename: historyFilename)
                    history = next
                } catch {
                    historySaveWarning = "Đã tạo kết quả, nhưng chưa lưu được lần này vào lịch sử. "
                        + error.localizedDescription
                }
            } else {
                historySaveWarning = "Đã tạo kết quả. Chưa lưu vào lịch sử vì dữ liệu cũ chưa đọc được."
            }
        }
        publishWidgetSnapshot()
    }

    func restoreHistory(_ item: UtilityHistoryItem) {
        utilityInput = item.input
        utilityOutput = item.output
        processedInput = item.input
        historySaveWarning = nil
        publishWidgetSnapshot()
    }

    func clearText() {
        utilityInput = ""
        utilityOutput = ""
        processedInput = nil
        historySaveWarning = nil
        publishWidgetSnapshot()
    }

    func clearHistory() throws {
        guard historyReady else {
            throw AppActionError.message("Hãy thử đọc lại lịch sử trước khi xóa.")
        }
        try store.save([UtilityHistoryItem](), filename: historyFilename)
        history = []
        historySaveWarning = nil
    }

    func navigate(to route: StarterRoute) {
        switch route {
        case .collection where AppProfile.category == .lifestyle:
            recordQuery = ""
            selectedRecordID = nil
            recordPath = []
        case .record(let id) where AppProfile.category == .lifestyle:
            guard collectionReady, record(id: id) != nil else {
                actionError = "Không mở được mục này. Mục có thể đã bị xóa hoặc dữ liệu chưa đọc được."
                return
            }
            openRecord(id: id)
        case .utility where AppProfile.category == .utility:
            // Navigation only: a deep link never clears or processes input.
            utilityNavigationRequest = UUID()
        case .settings:
            break // Presented by the scene through the native platform action.
        default:
            actionError = "Liên kết này không phù hợp với loại ứng dụng đang mở."
        }
    }

    /// A widget failure is not a rollback of an already committed local file.
    func publishWidgetSnapshot() {
        guard AppProfile.widgetsEnabled else { return }
        let snapshot: WidgetSnapshot
        switch AppProfile.category {
        case .lifestyle:
            guard collectionReady else { return }
            snapshot = WidgetSnapshot(category: "lifestyle",
                title: "\(records.count) mục", subtitle: "\(records.filter(\.isFavorite).count) yêu thích",
                updatedAt: Date(), route: "collection")
        case .utility:
            snapshot = WidgetSnapshot(category: "utility", title: "Công cụ văn bản",
                subtitle: hasUtilityResult ? "Đã tạo kết quả" : "Sẵn sàng xử lý",
                updatedAt: Date(), route: "utility")
        }
        do {
            try WidgetSnapshotStore.write(snapshot)
            WidgetCenter.shared.reloadTimelines(ofKind: AppProfile.widgetKind)
            widgetWarning = nil
        } catch {
            widgetWarning = "Chưa cập nhật được widget. Dữ liệu trong ứng dụng vẫn được giữ. "
                + error.localizedDescription
        }
    }

    private func requireCollectionReady() throws {
        guard collectionReady else {
            throw AppActionError.message("Hãy thử đọc lại bộ sưu tập trước khi thay đổi dữ liệu.")
        }
    }
}
