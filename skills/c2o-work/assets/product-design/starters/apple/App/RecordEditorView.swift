import SwiftUI
import StarterCore

@MainActor
struct RecordEditorView: View {
    @EnvironmentObject private var model: StarterAppModel
    @Environment(\.dismiss) private var dismiss
    @State private var draft: LifestyleRecord
    @State private var saveError: String?
    @State private var confirmDiscard = false
    @FocusState private var titleFocused: Bool
    private let original: LifestyleRecord?

    init(record: LifestyleRecord?) {
        original = record
        _draft = State(initialValue: record ?? LifestyleRecord(title: ""))
    }

    private var isDirty: Bool {
        guard let original else {
            return !draft.title.isEmpty || !draft.notes.isEmpty || draft.isFavorite
        }
        return draft.title != original.title || draft.notes != original.notes
            || draft.isFavorite != original.isFavorite
    }

    var body: some View {
        NavigationStack {
            Form {
                Section("Thông tin") {
                    TextField("Tên mục", text: $draft.title)
                        .focused($titleFocused)
                    Toggle("Yêu thích", isOn: $draft.isFavorite)
                }
                Section("Ghi chú") {
                    TextEditor(text: $draft.notes)
                        .frame(minHeight: 160)
                        .accessibilityLabel("Ghi chú")
                }
                if let error = saveError {
                    Section {
                        Label("Chưa lưu được. Bản nháp vẫn ở đây.", systemImage: "exclamationmark.triangle")
                        Text(error).font(.callout).foregroundStyle(.secondary)
                    }
                }
            }
            .navigationTitle(original == nil ? "Mục mới" : "Sửa mục")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Hủy") {
                        if isDirty { confirmDiscard = true } else { dismiss() }
                    }
                    .keyboardShortcut(.cancelAction)
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Lưu", action: save)
                        .keyboardShortcut(.defaultAction)
                        .disabled(draft.title.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty)
                }
            }
            .confirmationDialog("Bỏ các thay đổi chưa lưu?", isPresented: $confirmDiscard,
                titleVisibility: .visible) {
                Button("Bỏ thay đổi", role: .destructive) { dismiss() }
            } message: {
                Text("Bản đã lưu trước đó vẫn được giữ nguyên.")
            }
        }
        .interactiveDismissDisabled(isDirty)
        .onAppear { titleFocused = original == nil }
        #if os(macOS)
        .frame(minWidth: 380, idealWidth: 480, minHeight: 400)
        #endif
    }

    private func save() {
        do {
            try model.saveRecord(draft)
            model.openRecord(id: draft.id)
            dismiss()
        } catch {
            saveError = error.localizedDescription
        }
    }
}
