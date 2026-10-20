import SwiftUI
import StarterCore
#if os(iOS)
import UIKit
#elseif os(macOS)
import AppKit
#endif

@MainActor
struct UtilityWorkbenchRoot: View {
    @EnvironmentObject private var model: StarterAppModel
    @State private var pendingHistory: UtilityHistoryItem?
    @State private var confirmRestore = false
    @State private var preferredColumn: NavigationSplitViewColumn = .detail

    var body: some View {
        Group {
            if StarterDevice.usesPhoneNavigation {
                NavigationStack {
                    UtilityWorkbenchView()
                        .toolbar {
                            ToolbarItem(placement: .primaryAction) {
                                Button { model.sheet = .history } label: {
                                    Label("Lịch sử", systemImage: "clock")
                                }
                            }
                        }
                }
            } else {
                NavigationSplitView(preferredCompactColumn: $preferredColumn) {
                    UtilityHistoryView(onSelect: requestHistory)
                } detail: {
                    UtilityWorkbenchView()
                }
                .navigationSplitViewStyle(.balanced)
            }
        }
        .confirmationDialog("Thay văn bản hiện tại?", isPresented: $confirmRestore,
            titleVisibility: .visible) {
            restoreButton
        } message: {
            Text("Văn bản chưa lưu sẽ được thay bằng lần xử lý đã chọn.")
        }
        .confirmationDialog("Xóa văn bản hiện tại?", isPresented: $model.confirmNewText,
            titleVisibility: .visible) {
            Button("Tạo văn bản mới", role: .destructive) {
                model.clearText()
                preferredColumn = .detail
            }
        } message: {
            Text("Thao tác này xóa nội dung đang nhập và kết quả. Lịch sử đã lưu vẫn được giữ.")
        }
        .onChange(of: model.utilityNavigationRequest) { _, _ in
            confirmRestore = false
            pendingHistory = nil
            preferredColumn = .detail
        }
    }

    private var restoreButton: some View {
        Button("Thay văn bản", role: .destructive) {
            guard let item = pendingHistory else { return }
            restore(item)
        }
    }

    private func requestHistory(_ item: UtilityHistoryItem) {
        if !model.utilityInput.isEmpty && model.utilityInput != item.input {
            pendingHistory = item
            confirmRestore = true
        } else {
            restore(item)
        }
    }

    private func restore(_ item: UtilityHistoryItem) {
        model.restoreHistory(item)
        pendingHistory = nil
        confirmRestore = false
        preferredColumn = .detail
    }
}

@MainActor
struct UtilityHistorySheet: View {
    @EnvironmentObject private var model: StarterAppModel
    @Environment(\.dismiss) private var dismiss
    @State private var pendingHistory: UtilityHistoryItem?
    @State private var confirmRestore = false

    var body: some View {
        NavigationStack {
            UtilityHistoryView { item in
                if !model.utilityInput.isEmpty && model.utilityInput != item.input {
                    pendingHistory = item
                    confirmRestore = true
                } else {
                    model.restoreHistory(item)
                    dismiss()
                }
            }
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Xong") { dismiss() }
                }
            }
            .confirmationDialog("Thay văn bản hiện tại?", isPresented: $confirmRestore,
                titleVisibility: .visible) {
                Button("Thay văn bản", role: .destructive) {
                    guard let item = pendingHistory else { return }
                    model.restoreHistory(item)
                    dismiss()
                }
            } message: {
                Text("Văn bản chưa lưu sẽ được thay bằng lần xử lý đã chọn.")
            }
        }
    }
}

@MainActor
private struct UtilityWorkbenchView: View {
    @EnvironmentObject private var model: StarterAppModel
    @State private var copyStatus: String?

    var body: some View {
        Form {
            Section {
                TextEditor(text: $model.utilityInput)
                    .frame(minHeight: 180)
                    .accessibilityLabel("Văn bản đầu vào")
                TextStatisticsView(statistics: TextTools.statistics(model.utilityInput))
            } header: {
                Text("Văn bản đầu vào")
            } footer: {
                Text("Số từ được tính theo các phần tách bằng khoảng trắng.")
            }

            Section {
                Button("Chuẩn hóa khoảng trắng") { model.runTextTools() }
                    .buttonStyle(.borderedProminent)
                    .disabled(model.utilityInput.isEmpty)
            } footer: {
                Text("Gộp dấu cách, tab và ngắt dòng thành một dấu cách; bỏ khoảng trắng ở hai đầu.")
            }

            if model.hasUtilityResult {
                Section("Kết quả") {
                    if model.utilityOutput.isEmpty {
                        Text("Kết quả rỗng vì đầu vào chỉ chứa khoảng trắng.")
                            .foregroundStyle(.secondary)
                    } else {
                        Text(model.utilityOutput)
                            .frame(maxWidth: .infinity, alignment: .leading)
                            .textSelection(.enabled)
                    }
                    TextStatisticsView(statistics: TextTools.statistics(model.utilityOutput))
                    HStack {
                        Button(action: copyResult) {
                            Label("Sao chép", systemImage: "doc.on.doc")
                        }
                        ShareLink(item: model.utilityOutput) {
                            Label("Chia sẻ", systemImage: "square.and.arrow.up")
                        }
                    }
                    .disabled(model.utilityOutput.isEmpty)
                    if let status = copyStatus {
                        Text(status).font(.callout).foregroundStyle(.secondary)
                    }
                }
            } else if model.processedInput != nil {
                Section {
                    Text("Đầu vào đã thay đổi. Chạy lại để tạo kết quả mới.")
                        .foregroundStyle(.secondary)
                }
            }

            if let warning = model.historySaveWarning {
                Section {
                    Label(warning, systemImage: "exclamationmark.triangle")
                    if model.hasUtilityResult {
                        Text("Đầu vào và kết quả vẫn ở đây. Bạn có thể sao chép hoặc chia sẻ kết quả.")
                            .font(.callout).foregroundStyle(.secondary)
                    }
                }
            }
            if model.settingsLoadError != nil {
                Section {
                    Text("Chưa đọc được cài đặt nên tạm ngừng lưu lịch sử. Hãy mở Cài đặt để thử lại.")
                        .font(.callout)
                }
            }
        }
        .navigationTitle("Công cụ văn bản")
        .toolbar {
            ToolbarItemGroup(placement: .primaryAction) {
                Button { model.requestNewItem() } label: {
                    Label("Văn bản mới", systemImage: "square.and.pencil")
                }
                StarterSettingsControl()
            }
        }
        .onChange(of: model.utilityInput) { _, _ in copyStatus = nil }
        .onChange(of: model.utilityOutput) { _, _ in copyStatus = nil }
    }

    private func copyResult() {
        #if os(iOS)
        UIPasteboard.general.string = model.utilityOutput
        copyStatus = "Đã sao chép kết quả."
        #elseif os(macOS)
        NSPasteboard.general.clearContents()
        copyStatus = NSPasteboard.general.setString(model.utilityOutput, forType: .string)
            ? "Đã sao chép kết quả." : "Chưa sao chép được. Hãy thử lại."
        #endif
    }
}

@MainActor
private struct TextStatisticsView: View {
    let statistics: TextStatistics

    var body: some View {
        // Text wraps at large Dynamic Type sizes; these are counts, not a dashboard.
        Text("\(statistics.characters) ký tự · \(statistics.words) từ · \(statistics.lines) dòng")
            .font(.callout)
            .foregroundStyle(.secondary)
            .fixedSize(horizontal: false, vertical: true)
    }
}

@MainActor
private struct UtilityHistoryView: View {
    @EnvironmentObject private var model: StarterAppModel
    let onSelect: (UtilityHistoryItem) -> Void

    var body: some View {
        Group {
            if let error = model.historyLoadError {
                LoadFailureView(title: "Chưa đọc được lịch sử", detail: error, retry: model.loadHistory)
            } else {
                List {
                    Section {
                        Text(model.settings.keepUtilityHistory && model.settingsReady
                            ? "Đang lưu tối đa \(StarterAppModel.historyLimit) lần gần nhất trên thiết bị."
                            : "Lưu lịch sử đang tắt. Các lần đã lưu trước đây vẫn được giữ.")
                            .font(.callout).foregroundStyle(.secondary)
                    }
                    if model.history.isEmpty {
                        Text("Chưa có lần xử lý nào được lưu. Bạn có thể bật lưu lịch sử trong Cài đặt.")
                            .foregroundStyle(.secondary)
                    } else {
                        Section("Các lần đã lưu") {
                            ForEach(model.history) { item in
                                Button { onSelect(item) } label: {
                                    VStack(alignment: .leading, spacing: 4) {
                                        Text(preview(item)).lineLimit(2)
                                        Text(item.createdAt, format: .dateTime.day().month().hour().minute())
                                            .font(.caption).foregroundStyle(.secondary)
                                    }
                                    .frame(maxWidth: .infinity, alignment: .leading)
                                    .contentShape(Rectangle())
                                }
                                .buttonStyle(.plain)
                                .accessibilityHint("Mở lại đầu vào và kết quả của lần xử lý này")
                            }
                        }
                    }
                }
            }
        }
        .navigationTitle("Lịch sử")
    }

    private func preview(_ item: UtilityHistoryItem) -> String {
        let text = item.input.trimmingCharacters(in: .whitespacesAndNewlines)
        return text.isEmpty ? "Chỉ có khoảng trắng" : String(text.prefix(100))
    }
}
