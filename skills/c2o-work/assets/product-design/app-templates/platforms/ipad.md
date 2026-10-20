# iPad — bố cục thích ứng với cửa sổ và cách nhập

**Baseline source: iPadOS 17+.** Dùng chung domain và action contracts với iPhone; tổ chức lại không gian theo tác vụ. Đây là hợp đồng platform, không phải bằng chứng native đã chạy. Đọc cùng [iPhone](iphone.md), [SwiftUI profile](../../profiles/swiftui.md) và [UI composition](../../core/ui-composition.md).

## Không gian thuộc cửa sổ hiện tại

Kích thước màn hình không cho biết kích thước phần app đang dùng. Thiết kế theo available width/height, safe area, cỡ chữ và bàn phím. iPad có thể thay đổi không gian trong lúc người dùng đang làm việc; hướng portrait/landscape chỉ là một tác nhân. Apple hướng dẫn bố cục đáp ứng cửa sổ co giãn, giữ control hệ thống và hỗ trợ pointer. [P1]

| Tác vụ | Khi đủ chỗ | Khi hẹp |
| --- | --- | --- |
| Lifestyle collection | Collection cạnh detail bằng `NavigationSplitView` | Split collapse thành navigation stack; người dùng vẫn tới list/detail và quay lại được |
| Utility có history | History ở leading column, workbench ở detail | Workbench giữ input/result; history vẫn tới được qua navigation phù hợp |
| Utility không cần history | Workbench tập trung; giới hạn dòng đọc hợp lý | Reflow input/options/result theo chiều dọc |
| Xem nhiều thuộc tính để so sánh | `Table` có thể là lựa chọn sau khi chọn rõ cột và sort | Ưu tiên trường quan trọng và đường xem chi tiết; không nhét nguyên bảng rộng vào card hẹp |
| Chỉnh metadata cạnh nội dung | Inspector hoặc panel phụ nếu mang lại giá trị | Chuyển sang presentation phù hợp; thao tác chính vẫn truy cập được |

`NavigationSplitView` hỗ trợ hai/ba cột và có hành vi collapse ở môi trường hẹp; width preference của cột không phải kích thước tuyệt đối. [P2] Starter dùng split cho collection và history/workbench; table, inspector và ba cột là lựa chọn mở rộng, chưa được triển khai mặc định.

Chọn sidebar, tabs hoặc một task duy nhất theo cấu trúc nội dung. Không có số lượng tab bắt buộc cho iPad. Không giữ sidebar rộng cố định chỉ vì đang chạy trên thiết bị iPad; cũng không tự xóa chức năng khi cột tạm ẩn.

## State phải sống qua collapse và resize

Selection giữ bằng ID ổn định. Query, draft và kết quả utility thuộc owner của tác vụ, không thuộc nhánh layout xuất hiện tạm thời. Khi co cửa sổ rồi nới lại, detail phải còn trỏ cùng record; draft không được lấy lại bản persisted và đè input đang sửa.

Ghi rõ cột nào được ưu tiên khi split collapse. Có thể dùng `preferredCompactColumn` nếu navigation yêu cầu điều khiển này; kiểm tra cả back và thay selection, không chỉ tình huống mở app lần đầu. Không dùng việc cột biến mất như bằng chứng người dùng đã hủy sửa. Nội dung rỗng của detail phải chỉ cách chọn mục, còn lỗi đọc là state riêng.

Thử cả chiều cao thấp khi có bàn phím, không chỉ chiều rộng. Form và sheet phải còn đường tới field lỗi, Lưu/Hủy. Trong một vùng cuộn, xác định control nào đứng yên, control nào đi theo nội dung; tránh lồng các scroll vùng lớn khi người dùng không đoán được nơi thao tác.

## Touch, pointer và keyboard

Pointer bổ sung cách thao tác; các hành động quan trọng vẫn tìm thấy và thực hiện được bằng touch. Hover dùng để phản hồi vị trí/chức năng, không làm cổng duy nhất tới một action. Apple cũng mô tả pointing device là cách nhập bổ sung trên iPad. [P3]

Dùng controls native để nhận hành vi selection, focus và nhập liệu phù hợp. Đặt keyboard shortcut cho action có giá trị lặp lại, gắn tới cùng action với toolbar/menu và tôn trọng shortcut hệ thống. Bảo đảm focus đi vào vùng nội dung đúng sau khi chọn record, mở/đóng editor hoặc thu cột. Thử keyboard navigation theo tính năng đã cam kết; chưa thử không được báo hỗ trợ đầy đủ.

Menu bar, tab/sidebar adaptation và window controls trên OS mới có API/availability riêng. Source baseline 17 không giả định các API mới ấy tồn tại. Khi nâng SDK/target, đối chiếu safe area, control placement và menus trên OS mới thay vì giữ screenshot của baseline làm chuẩn duy nhất. [P1]

## Một scene trong starter

Generator đặt `UIApplicationSupportsMultipleScenes = false` trong scene manifest. Đây là giới hạn có chủ ý của starter local: một cửa sổ app hoạt động, vẫn phải thích ứng kích thước. Nó không triển khai nhiều scene cùng sửa một kho dữ liệu.

Muốn bật multiwindow, trước hết chốt owner dùng chung của persistence, quy tắc serialize/merge write, selection/draft riêng mỗi scene và phục hồi scene. `WindowGroup` có thể tạo nhiều cửa sổ cùng cấu trúc nhưng mỗi cửa sổ có view state riêng; đây không phải cơ chế tự giải quyết tranh chấp lưu. [P4] Không chỉ đổi manifest sang `true` rồi coi tính năng đã hoàn thành.

## Các quan sát cần chọn khi Verify

| Chuyển tiếp | Điều cần giữ |
| --- | --- |
| Rộng → hẹp → rộng khi đang sửa | Cùng selection/draft; có đường quay lại collection và commit đúng record |
| Bàn phím xuất hiện trong cửa sổ thấp | Field/action không bị kẹt; cuộn và focus không mất |
| Touch → pointer → keyboard | Action cùng nghĩa; không có chức năng chỉ xuất hiện lúc hover |
| Search rồi chọn record | Query không mất ngoài chính sách đã ghi; detail đúng ID |
| App đang mở rồi nhận widget route | Không tạo thêm scene ngoài cấu hình; draft theo chính sách của app |

Kiểm tra trên baseline và ít nhất cấu hình OS mới mà sản phẩm định hỗ trợ khi phát hành. Bảng này là tập gợi ý chọn coverage theo scope. Bộ starter chưa có evidence simulator/device cho các chuyển tiếp này.

## Nguồn Apple

Đối chiếu ngày 2026-10-20; tài liệu OS mới dùng để nhận diện việc cần thích ứng, không nâng deployment target ngầm.

- [P1 — WWDC25: Elevate the design of your iPad app](https://developer.apple.com/videos/play/wwdc2025/208/)
- [P2 — SwiftUI: NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview)
- [P3 — HIG: Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)
- [P4 — SwiftUI: WindowGroup](https://developer.apple.com/documentation/swiftui/windowgroup)
