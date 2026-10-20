import SwiftUI
import StarterCore

@MainActor
struct StarterSettingsView: View {
    @EnvironmentObject private var model: StarterAppModel
    @State private var saveError: String?
    @State private var confirmClearHistory = false

    var body: some View {
        Form {
            Section("Ứng dụng") {
                LabeledContent("Tên", value: AppProfile.displayName)
                Text("Dữ liệu lưu riêng trên thiết bị này, chưa được đồng bộ hoặc sao lưu bởi ứng dụng.")
                    .font(.callout).foregroundStyle(.secondary)
            }

            if let error = model.settingsLoadError {
                Section("Chưa đọc được cài đặt") {
                    Text("Cài đặt cũ chưa bị thay thế. \(error)")
                    Button("Thử đọc lại") { model.loadSettings() }
                }
            }

            if AppProfile.category == .utility {
                Section {
                    Toggle("Lưu lịch sử trên thiết bị", isOn: Binding(
                        get: { model.settings.keepUtilityHistory },
                        set: { value in
                            do {
                                try model.setKeepUtilityHistory(value)
                                saveError = nil
                            } catch {
                                saveError = error.localizedDescription
                            }
                        }
                    ))
                    .disabled(!model.settingsReady ||
                        (!model.historyReady && !model.settings.keepUtilityHistory))
                    LabeledContent("Số lần đã lưu", value: model.historyReady
                        ? "\(model.history.count)" : "Chưa đọc được")
                    Button("Xóa toàn bộ lịch sử", role: .destructive) { confirmClearHistory = true }
                        .disabled(!model.historyReady || model.history.isEmpty)
                } header: {
                    Text("Lịch sử xử lý")
                } footer: {
                    Text("Mặc định tắt. Khi bật, lưu đầu vào và kết quả của tối đa \(StarterAppModel.historyLimit) lần gần nhất. Tắt tùy chọn chỉ dừng lưu thêm; dùng Xóa toàn bộ lịch sử để xóa các lần cũ.")
                }
                if let error = model.historyLoadError {
                    Section("Chưa đọc được lịch sử") {
                        Text("Dữ liệu cũ chưa bị thay thế. \(error)")
                        Button("Thử đọc lại") { model.loadHistory() }
                    }
                }
            }

            if AppProfile.widgetsEnabled {
                Section("Widget") {
                    Text("Widget chỉ hiển thị số lượng hoặc trạng thái. Tên mục, ghi chú và văn bản bạn xử lý không được đưa vào widget.")
                        .font(.callout).foregroundStyle(.secondary)
                }
            }
            Section("Hướng dẫn") {
                if AppProfile.category == .lifestyle {
                    DisclosureGroup("Sử dụng bộ sưu tập") {
                        Text("Dùng nút Thêm để tạo mục, nhập tên và ghi chú rồi chọn Lưu. Tìm kiếm khớp với tên hoặc ghi chú.")
                        Text("Mở một mục để sửa hoặc đánh dấu yêu thích. Lệnh Xóa nằm trong menu Thao tác khác và yêu cầu xác nhận.")
                        Text("Khi lưu thành công, thay đổi được giữ trên thiết bị. Nếu lưu lỗi, bản nháp vẫn ở màn hình chỉnh sửa để bạn thử lại.")
                        Text("Bản nháp chưa lưu không được giữ khi thoát ứng dụng. Mục đã xóa không có chức năng hoàn tác.")
                    }
                } else {
                    DisclosureGroup("Xử lý và chia sẻ văn bản") {
                        Text("Nhập hoặc dán văn bản để xem bộ đếm. Chọn Chuẩn hóa khoảng trắng để gộp dấu cách, tab và ngắt dòng thành một dấu cách, đồng thời bỏ khoảng trắng ở hai đầu.")
                        Text("Sao chép đưa kết quả vào bảng nhớ tạm. Chia sẻ mở bảng chia sẻ của hệ thống để bạn chọn nơi gửi. Khi sửa đầu vào, hãy chạy lại trước khi dùng kết quả mới.")
                        Text("Văn bản đang nhập và kết quả đang mở không được khôi phục khi thoát ứng dụng. Các lần đã lưu trong lịch sử vẫn có thể mở lại.")
                        Text("Lưu lịch sử mặc định tắt. Khi bật, ứng dụng giữ cả đầu vào và kết quả của tối đa \(StarterAppModel.historyLimit) lần gần nhất. Tắt tùy chọn dừng lưu thêm; Xóa toàn bộ lịch sử xóa các lần cũ.")
                    }
                    DisclosureGroup("Cách tính ký tự, từ và dòng") {
                        Text("Ký tự được tính theo cụm ký tự Unicode (grapheme): một chữ có dấu hoặc một emoji ghép thường được tính là một ký tự.")
                        Text("Số từ đếm các phần tách bằng khoảng trắng, tab hoặc ngắt dòng.")
                        Text("Dòng được đếm theo dấu xuống dòng LF; CRLF và CR được quy đổi về LF. Văn bản rỗng có 0 dòng. Một dấu xuống dòng ở cuối tạo thêm một dòng trống.")
                    }
                }
            }
            if let error = saveError {
                Section("Chưa lưu thay đổi") {
                    Text(error)
                    Text("Cài đặt và dữ liệu đã lưu trước đó vẫn được giữ nguyên.")
                        .font(.callout).foregroundStyle(.secondary)
                }
            }
        }
        .formStyle(.grouped)
        .navigationTitle("Cài đặt")
        .confirmationDialog("Xóa toàn bộ lịch sử đã lưu?", isPresented: $confirmClearHistory,
            titleVisibility: .visible) {
            Button("Xóa lịch sử", role: .destructive) {
                do {
                    try model.clearHistory()
                    saveError = nil
                } catch {
                    saveError = error.localizedDescription
                }
            }
        } message: {
            Text("Các lần xử lý đã lưu sẽ bị xóa. Văn bản đang mở trong bàn làm việc vẫn được giữ.")
        }
    }
}
