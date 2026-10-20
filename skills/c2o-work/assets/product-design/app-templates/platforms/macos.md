# macOS — workspace native, commands và lifecycle

**Baseline source: macOS 14+.** Chia sẻ domain/actions với iPhone/iPad, chọn container và cách nhập riêng cho Mac. Đây là hợp đồng thiết kế và giới hạn của starter; chưa có bằng chứng Xcode build hoặc runtime. Xem thêm [SwiftUI profile](../../profiles/swiftui.md) và [UI composition](../../core/ui-composition.md).

## Cửa sổ chính được chọn có chủ ý

Starter dùng **một `Window` chính**, có `Settings` scene riêng. Một store domain chính phục vụ màn làm việc; Settings không dựng một bản sao độc lập rồi ghi đè kho record. Lựa chọn này giữ phạm vi persistence local đơn giản. Nó không phải quy tắc yêu cầu mọi ứng dụng Mac chỉ có một cửa sổ.

Apple mô tả `Window` là một cửa sổ duy nhất; `WindowGroup` cung cấp nhiều cửa sổ theo cùng cấu trúc và view state riêng. Apple thường khuyên dùng `WindowGroup` cho main scene; starter chủ ý chưa nhận thêm trách nhiệm multiwindow. Tài liệu `Window` cũng nêu lifecycle thoát app khi đóng primary window khác với `WindowGroup`. Cần thử đóng/mở lại và deep link trên app thực, kể cả khi Settings đang mở. [M1][M2]

Muốn chuyển thành `WindowGroup`, chốt persistence dùng chung, serialize/merge write, draft và selection theo window, điều kiện command theo focus, mở lại cửa sổ và xung đột cùng record. Đổi scene type không tự giải quyết hai bản sao state cùng ghi một file. `DocumentGroup` chỉ phù hợp khi sản phẩm có mô hình tài liệu thật, không thêm chỉ để có nhiều cửa sổ.

## Tổ chức workspace

| Vùng | Lifestyle | Utility |
| --- | --- | --- |
| Leading column | Collection searchable và selection | History nếu cần và đã bật; empty/disabled có nghĩa riêng |
| Main content | Detail; editor có Lưu/Hủy và lỗi giữ draft | Input/result và tham số nếu cần; kết quả đọc/chọn/copy thuận tiện bằng keyboard |
| Toolbar | Action của collection/selection đang xem | Chạy/Copy hoặc action thực sự của workbench |
| Settings | Thông tin app và cài đặt hành vi đã triển khai | Chính sách lưu history và hành vi xử lý đã triển khai |
| Inspector, tùy chọn | Thuộc tính phụ khi cần giữ detail trong tầm nhìn | Tham số phụ hoặc metadata kết quả khi có use case |

Dùng split/list theo nhiệm vụ ban đầu. Chọn `Table` khi cần so sánh nhiều trường có kiểu rõ ràng, sort và selection; không đổi mọi collection thành bảng chỉ vì có chuột. Không kéo rộng một form phone vô hạn: giới hạn chiều dài dòng đọc, cho vùng nội dung quan trọng hưởng diện tích thêm và giữ cửa sổ resize được. Width/minimum size là quyết định theo nội dung thật, không phải một kích thước Mac cố định áp cho mọi app.

Inspector là phần mở rộng có owner và semantics riêng, chưa có trong starter mặc định. Không lặp cùng input chỉnh sửa ở editor và inspector nếu chưa định nghĩa ai giữ draft và nơi commit. Resize hoặc ẩn sidebar không làm thay đổi domain state.

## Menu, toolbar và Settings

Native menu bar là một lối truy cập hành động. `commands`, `CommandGroup`/`CommandMenu` và `keyboardShortcut` gắn action vào cấu trúc menu hệ thống; `Settings` scene cung cấp cửa sổ cài đặt và menu tương ứng. [M3][M4]

| Action/nhóm | Hợp đồng khi triển khai |
| --- | --- |
| Thêm mục | Menu và toolbar gọi cùng action; không vừa ghi record trống vừa mở draft |
| Chạy utility | Chỉ chạy với input/validation phù hợp; không đọc một bản input khác với màn hiện tại |
| Copy | Dùng kết quả đang xem; trạng thái enabled khớp dữ liệu; không chiếm shortcut Copy của text field đang chọn |
| Search | Đưa focus vào search có scope đúng; shortcut chỉ thêm khi tìm kiếm tồn tại |
| View/sidebar | Cho người dùng tìm lại cột đã ẩn khi đó là chức năng đã hỗ trợ |
| Settings | Mở `Settings` scene qua đường native; không thay bằng một tab phone phóng to |

Bảng là hợp đồng cho những action được chọn, không tuyên bố tất cả menu/shortcut đã có source. Giữ các menu/shortcut chuẩn mà hệ thống cung cấp; thêm action theo mục đích. Action phụ thuộc selection/draft phải đọc ngữ cảnh đúng, đặc biệt khi Settings có focus. Khi mở rộng nhiều window, dùng cơ chế focused scene/view hoặc routing tương đương thay vì cho menu tác động một window ngẫu nhiên.

## Input, feedback và persistence

Phân biệt focus, selection và hover. Dùng native controls và selection model để người dùng nhận ra đối tượng đang thao tác. Bảo đảm Tab/Shift-Tab và phím điều hướng hoạt động ở vùng đã hỗ trợ; Return/Escape theo tác vụ, không đặt global handler làm hỏng nhập nhiều dòng. Context menu là đường bổ sung, không là nơi duy nhất có action thiết yếu.

Editor giữ draft khi write thất bại. Load/decode error không được coi như collection rỗng rồi cho ghi đè. Utility history có consent/setting riêng; dữ liệu người dùng nhập không tự đưa vào widget. Khi domain save thành công nhưng xuất bản widget lỗi, thông báo phản ánh đúng hai kết quả; không khiến người dùng lưu record lần nữa.

macOS native widget đọc snapshot từ container local của app Mac. Nó khác với iPhone widget được hệ thống trình bày từ xa trên Mac; cùng App Group ID không tạo đồng bộ giữa các thiết bị. [Widget contract](widgets.md) giữ ranh giới này.

## Kiểm tra native cần chọn

| Trường hợp | Điều cần quan sát |
| --- | --- |
| Cửa sổ hẹp/rộng, sidebar ẩn/hiện | Nội dung reflow hợp lý, selection/draft giữ nguyên, không tạo cuộn ngang ngoài ý muốn |
| Menu + toolbar + keyboard | Cùng action/state; enable/disable đúng; Copy không chiếm thao tác text đang chọn |
| Settings có focus | Menu không sửa nhầm context; settings không tạo writer record thứ hai |
| Đóng main window và mở lại bằng app/deep link | Lifecycle rõ, dữ liệu persisted còn, route tới đúng workspace |
| Load/write lỗi | Không ghi đè dữ liệu chưa đọc được; draft còn và retry có kết quả rõ |
| VoiceOver và appearance | Tên/value/focus hợp lý; readable ở light/dark và accessibility settings có liên quan |

Các phép kiểm tra này còn cần Xcode/macOS runtime. Tạo target, source hoặc entitlement file không chứng minh app đã native-ready; việc phát hành còn tùy app, capability, signing và các yêu cầu phân phối tại thời điểm đó.

## Nguồn Apple

Đối chiếu ngày 2026-10-20. API mới ngoài macOS 14 cần availability guard hoặc quyết định nâng baseline riêng.

- [M1 — SwiftUI: Window](https://developer.apple.com/documentation/swiftui/window)
- [M2 — SwiftUI: WindowGroup](https://developer.apple.com/documentation/swiftui/windowgroup)
- [M3 — Building and customizing the menu bar with SwiftUI](https://developer.apple.com/documentation/swiftui/building-and-customizing-the-menu-bar-with-swiftui)
- [M4 — SwiftUI: Settings](https://developer.apple.com/documentation/swiftui/settings)
