# Kiểm chứng native cho starter

Các mục dưới đây là **kế hoạch**, chưa phải kết quả. Ghi cấu hình, bước thao tác, quan sát, file bằng chứng và criterion tương ứng trong dự án thật.

## Chung

| Phép kiểm tra | Điều phải quan sát |
| --- | --- |
| Build/launch | iOS Simulator, iPad runtime và native Mac target compile/launch; cấu hình thực được ghi lại |
| Window/input | Thu hẹp/mở rộng iPad/Mac; bàn phím phần cứng; focus không bị che; back giữ context |
| Accessibility | Dynamic Type/chữ dài, VoiceOver, keyboard, theme và vùng tương tác trong flow thật |
| Storage load failure | File lỗi decode/không đọc được hiển thị lỗi và retry; không ghi đè thành kho rỗng |
| Storage write failure | Draft/input còn; không báo lưu thành công; record khác không đổi |
| Deep link | Mở collection/utility/record/settings đúng context; URL sai bị bỏ qua, không có action ghi/xóa |
| Local data | Quit/reopen giữ dữ liệu đã commit; chưa có sync/backup thì copy không hứa đã sao lưu |

## Lifestyle

Tạo hai item cùng title nhưng ID khác; tìm/mở/sửa một item và xác nhận item kia không đổi. Thử title trống, tên/notes dài, favorite, sửa rồi cancel, lưu lỗi rồi retry, delete cancel/confirm và reopen. Thử điều hướng/deep link khi editor đang có draft. Xác nhận empty collection khác search không có kết quả; filter/selection có quy tắc rõ khi item bị xóa.

## Utility

Thử input rỗng, nhiều whitespace, xuống dòng CRLF/CR/LF, tiếng Việt có dấu, emoji ghép và văn bản dài vừa với scope. Output normalize phải gộp whitespace theo mô tả; count từ theo whitespace không được quảng bá thành phân tích ngôn ngữ. Copy/share phải dùng output thực đang hiển thị.

History mặc định tắt: thao tác nhiều lần, quit/reopen và xác nhận chưa lưu input/output như history. Bật history, xác nhận cap 50, mở mục cũ, clear history và tắt history theo copy đã chọn. Lỗi lưu history không làm mất input/output hoặc đổi phép tính thành thất bại. Không đưa văn bản này vào snapshot widget.

## Widget

Xác nhận bundle ID, extension embedding, entitlement và Info.plist group khớp. Kiểm tra mỗi family small/medium/large đã hỗ trợ trên từng nền tảng. Gallery placeholder có nhãn minh họa; khi chưa có snapshot không bịa số; khi đọc lỗi không hiển thị kết quả thành công; khi có snapshot thể hiện thời điểm dữ liệu và mở đúng route.

Sau thay đổi app, xác nhận snapshot đã commit rồi yêu cầu reload; quan sát kết quả theo lịch hệ thống. Không dùng một lần refresh nhanh để cam kết thời gian cho mọi lần. Chỉ số/tóm tắt không lộ title/notes hoặc input/output nhạy cảm. Thử mở widget khi app chưa chạy hoặc đang có draft.

Interactive widgets, App Intents, Control Center, Live Activities, notifications, cloud, purchases và nhiều cửa sổ chỉnh chung không nằm trong phép kiểm tra của source hiện tại; nếu thêm chúng, viết contract và test riêng trước khi kết luận.
