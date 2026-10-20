import SwiftUI
import StarterCore

@MainActor
struct LifestyleCollectionRoot: View {
    @EnvironmentObject private var model: StarterAppModel

    var body: some View {
        if StarterDevice.usesPhoneNavigation {
            NavigationStack(path: $model.recordPath) {
                CollectionListView(usesSelection: false)
                    .navigationDestination(for: UUID.self) { id in
                        RecordDetailView(id: id)
                    }
            }
        } else {
            NavigationSplitView {
                CollectionListView(usesSelection: true)
            } detail: {
                if let id = model.selectedRecordID {
                    RecordDetailView(id: id)
                } else {
                    ContentUnavailableView("Chọn một mục", systemImage: "square.stack",
                        description: Text("Mở một mục trong bộ sưu tập hoặc tạo mục mới."))
                }
            }
            .navigationSplitViewStyle(.balanced)
        }
    }
}

@MainActor
private struct CollectionListView: View {
    @EnvironmentObject private var model: StarterAppModel
    let usesSelection: Bool

    var body: some View {
        list
            .navigationTitle("Bộ sưu tập")
            .searchable(text: $model.recordQuery, prompt: "Tìm tên hoặc ghi chú")
            .toolbar {
                ToolbarItemGroup(placement: .primaryAction) {
                    StarterSettingsControl()
                    Button { model.editRecord(nil) } label: {
                        Label("Thêm mục", systemImage: "plus")
                    }
                    .disabled(!model.collectionReady)
                }
            }
            .overlay { statusOverlay }
    }

    @ViewBuilder
    private var list: some View {
        if usesSelection {
            List(selection: $model.selectedRecordID) { rows }
        } else {
            List { rows }
        }
    }

    private var rows: some View {
        ForEach(model.filteredRecords) { record in
            NavigationLink(value: record.id) {
                HStack(alignment: .top) {
                    VStack(alignment: .leading, spacing: 4) {
                        Text(record.title).font(.headline)
                        if !record.notes.isEmpty {
                            Text(record.notes)
                                .foregroundStyle(.secondary)
                                .lineLimit(2)
                        }
                    }
                    Spacer()
                    if record.isFavorite {
                        Image(systemName: "star.fill")
                            .foregroundStyle(.tint)
                            .accessibilityLabel("Yêu thích")
                    }
                }
            }
            .tag(record.id)
        }
    }

    @ViewBuilder
    private var statusOverlay: some View {
        if let error = model.collectionLoadError {
            LoadFailureView(title: "Chưa đọc được bộ sưu tập", detail: error,
                retry: model.loadCollection)
        } else if model.records.isEmpty {
            ContentUnavailableView {
                Label("Bắt đầu bộ sưu tập", systemImage: "square.stack")
            } description: {
                Text("Lưu một mục với tên, ghi chú và dấu yêu thích.")
            } actions: {
                Button("Thêm mục đầu tiên") { model.editRecord(nil) }
                    .buttonStyle(.borderedProminent)
            }
        } else if model.filteredRecords.isEmpty {
            ContentUnavailableView {
                Label("Không có kết quả", systemImage: "magnifyingglass")
            } description: {
                Text("Thử tên khác hoặc xóa nội dung tìm kiếm.")
            } actions: {
                Button("Xóa tìm kiếm") { model.recordQuery = "" }
            }
        }
    }
}

@MainActor
private struct RecordDetailView: View {
    @EnvironmentObject private var model: StarterAppModel
    let id: UUID
    @State private var confirmDelete = false

    var body: some View {
        if let record = model.record(id: id) {
            ScrollView {
                VStack(alignment: .leading, spacing: 20) {
                    Text(record.title)
                        .font(.title)
                        .textSelection(.enabled)
                    if record.isFavorite {
                        Label("Yêu thích", systemImage: "star.fill")
                            .foregroundStyle(.tint)
                    }
                    LabeledContent("Cập nhật") {
                        Text(record.updatedAt, format: .dateTime.day().month().year().hour().minute())
                    }
                    Divider()
                    Text("Ghi chú").font(.headline)
                    if record.notes.isEmpty {
                        Text("Chưa có ghi chú.").foregroundStyle(.secondary)
                    } else {
                        Text(record.notes).textSelection(.enabled)
                    }
                }
                .frame(maxWidth: .infinity, alignment: .leading)
                .padding()
            }
            .navigationTitle("Chi tiết")
            .toolbar {
                ToolbarItemGroup(placement: .primaryAction) {
                    Button {
                        do { try model.toggleFavorite(id: id) }
                        catch { model.actionError = error.localizedDescription }
                    } label: {
                        Label(record.isFavorite ? "Bỏ yêu thích" : "Yêu thích",
                            systemImage: record.isFavorite ? "star.fill" : "star")
                    }
                    .disabled(!model.collectionReady)
                    Button("Sửa") { model.editRecord(record) }
                        .disabled(!model.collectionReady)
                    Menu {
                        Button("Xóa mục", role: .destructive) { confirmDelete = true }
                    } label: {
                        Label("Thao tác khác", systemImage: "ellipsis.circle")
                    }
                    .disabled(!model.collectionReady)
                }
            }
            .confirmationDialog("Xóa mục này?", isPresented: $confirmDelete, titleVisibility: .visible) {
                Button("Xóa mục", role: .destructive) {
                    do { try model.deleteRecord(id: id) }
                    catch { model.actionError = error.localizedDescription }
                }
            } message: {
                Text("Tên và ghi chú của mục sẽ bị xóa khỏi thiết bị này.")
            }
        } else {
            ContentUnavailableView("Không tìm thấy mục", systemImage: "square.stack",
                description: Text("Mục có thể đã bị xóa. Hãy chọn một mục khác."))
        }
    }
}
