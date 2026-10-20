# Chọn và thiết kế data view

**C2O Design v1.2.0.** Data view quyết định cách đọc, tìm, so sánh hoặc thao tác với dữ liệu. Dùng [catalog](../catalog/data-view-patterns.md) để chọn và [mẫu DV-01](../templates/data-view.md) để ghi hợp đồng. Đây là hướng dẫn, chưa phải thư viện UI đã triển khai.

## 1. Đi từ câu hỏi tới biểu diễn

Nêu việc cần hoàn thành: tìm một đối tượng, so thuộc tính, phát hiện thay đổi, theo dõi tiến trình, phân bổ nguồn lực hay hiểu quan hệ. Sau đó xác định một item/mark đại diện cho gì, ID nào giữ danh tính và dữ liệu nào thực sự có. Chọn biểu diễn, tương tác và [layout](layout.md) phù hợp; dùng [component](components.md) để thực hiện hành vi.

Các lựa chọn có thể phối hợp: danh sách trong list–detail, metric trong card, timeline trong detail. Card đóng nhóm, CSS grid sắp xếp, ARIA grid có hợp đồng tương tác riêng. Không coi chúng là một cây phân loại cứng hoặc mặc định mọi dữ liệu cần dashboard.

So lựa chọn trên cùng task/dataset/state theo [exploration](exploration.md). Giữ thông tin đủ để nhận diện và quyết định; cho đường đọc phần còn lại. Khi cần so nhiều thuộc tính, kiểm tra khả năng quét card trước khi chọn.

## 2. Hợp đồng dữ liệu

| Cần chốt | Quyết định phải có |
| --- | --- |
| Đối tượng và độ hạt | Mỗi hàng, ô, điểm, sự kiện là cá thể, giao dịch hay một nhóm đã tổng hợp? ID ổn định; nhãn hiển thị không thay ID. |
| Trường và ý nghĩa | Nhãn, kiểu, đơn vị, định dạng và quy tắc làm tròn. Phân biệt giá trị nguồn với giá trị suy ra; chỉ ra nơi tính. |
| Thời gian | Ngày thuần hay thời điểm; múi giờ, khoảng thời gian, thứ tự và cách xử lý sự kiện cùng thời điểm. |
| Giá trị thiếu | `0`, chưa biết, chưa nhập, không áp dụng và không có quyền xem là những trạng thái khác nhau. Ghi copy và hành vi tương ứng. |
| Tập dữ liệu | Phạm vi truy vấn, quyền, filter và phần đã tải. Tổng toàn bộ, tổng sau lọc và số đang hiển thị phải phân biệt được. |
| Tổng hợp | Công thức, nhóm, mẫu số và đơn vị thời gian; chọn cách xử lý dữ liệu thiếu/trùng. Không cộng các tỷ lệ có mẫu số khác nhau thành một tỷ lệ mới. |
| Nguồn và thời điểm | Nguồn, mức chắc chắn, thời điểm cập nhật và ý nghĩa của stale nếu có. Dữ liệu local không tự là dữ liệu cũ chỉ vì offline. |
| Quyền và thay đổi | Ai được đọc/sửa; thao tác ghi gì; điều kiện thành công, phục hồi và xung đột có áp dụng không? |

Hợp đồng này tham chiếu model/spec hiện có; không tạo định nghĩa nghiệp vụ song song. Fixture giữ nhãn giả định và đủ trường để tái hiện tác vụ.

## 3. Tương tác gắn với tập dữ liệu

Chọn chức năng giúp task: search/filter/sort/group, expand/select, drill-down/edit/export. Ghi cách reset, quay lại và đổi view. Sort phù hợp kiểu dữ liệu, có quy tắc cho giá trị bằng nhau/thiếu và giữ danh tính selection.

Với phân trang, tải thêm hoặc virtualization, nói rõ truy vấn/sắp xếp áp dụng toàn tập hay phần đã tải. “Chọn tất cả” cần chỉ ra chọn trang hiện tại, kết quả lọc hay toàn bộ kho; đổi filter phải có quy tắc giữ/bỏ selection. Bulk action nêu đối tượng, quyền, kết quả từng phần và retry khi có thể thất bại một phần. Export giữ đúng phạm vi đã hứa.

Loading ban đầu, refresh và tải thêm có thể xuất hiện cùng dữ liệu đang xem. Giữ nội dung, focus, vị trí và công việc chưa lưu theo hợp đồng; thông báo lỗi ở đúng phạm vi. Không mặc định mỗi lần refresh phải thay toàn view bằng skeleton.

## 4. Đọc số liệu và quan hệ đúng nghĩa

Biểu đồ bắt đầu từ quan hệ cần thấy và loại dữ liệu; ONS cũng dùng hai câu hỏi này để chọn chart [DV-S3]. Trong C2O, ghi metric, scope, kỳ đo/kỳ so sánh, phép tổng hợp, đơn vị và nguồn trước khi chọn mark. Nhãn/scale/legend phải đủ để đọc kết luận; không nối qua khoảng thiếu hoặc biến missing thành zero khi chưa có quy tắc nghiệp vụ.

Nêu baseline, scale và phần trục bị cắt. Bar so độ lớn dùng baseline zero; khi cần xem chênh lệch nhỏ trên khoảng hẹp, xét dạng khác như dot plot [DV-S4]. Phân biệt số tại một thời điểm với lượng phát sinh trong một khoảng. Có cách đọc giá trị ngoài tooltip/màu. Tương quan không tự chứng minh nguyên nhân.

Với cây/graph, định nghĩa node ID, loại và hướng của edge, vai trò đầu/cuối, nhiều cha, chu trình và mức chắc chắn. Node rời có thể là không có quan hệ, chưa nhập hoặc bị lọc; biểu diễn đúng trường hợp. Graph layout không được tự tạo quan hệ hoặc ngụ ý thứ bậc mà dữ liệu không có. Xem chi tiết và cách tìm node phải giữ được khi mạng lớn hoặc bị thu gọn.

## 5. Semantics và thích ứng nền tảng

Trên web, ưu tiên HTML table cho dữ liệu hàng/cột phù hợp. Bảng vẫn có thể chứa link, button hoặc control sắp xếp; sự có mặt của chúng không buộc cả bảng thành grid [DV-S1]. ARIA grid là widget tổng hợp, có điều hướng nội bộ và quản lý focus; chỉ gán role khi triển khai hợp đồng ấy [DV-S2]. CSS grid không tự cung cấp hành vi này.

Trên native, chọn control/API theo [profile SwiftUI](../profiles/swiftui.md), deployment target và tác vụ. Giữ ý nghĩa selection, đọc/sửa và hành động khi chuyển sang cách trình bày khác. Hẹp có thể ưu tiên các trường chính rồi mở detail; nếu cần so hàng/cột trực tiếp, một vùng cuộn hai chiều có thể phù hợp hơn việc phá quan hệ thành card. Kiểm tra chữ lớn, keyboard, assistive technology và đường đọc đầy đủ.

## 6. State và evidence

Phân biệt: chưa có dữ liệu; filter không có kết quả; dữ liệu thiếu một phần; tải lỗi; không có quyền; stale khi áp dụng. Selected, focused, expanded, editing và saving là các chiều tương tác khác, có thể cùng tồn tại. Ghi những tổ hợp liên quan đến task, không nhân toàn bộ state thành checklist chung.

Verify bằng fixture để đối chiếu ID, giá trị, phép tính và scope; chạy tương tác, render cấu hình đã chọn. Ghi kết quả/giới hạn theo [evidence contract](evidence.md). `DV-01`, `DVP-*`, layout/component IDs là tham chiếu review; checker không tự kiểm semantics, phép tính hoặc biểu diễn. Chưa chạy giữ `not-tested` cùng lý do trong nguồn kết quả hiện có; `NOT_RUN` chỉ thuộc profile JSON tùy chọn.

## Nguồn tham khảo

- [DV-S1 — W3C APG: Table pattern](https://www.w3.org/WAI/ARIA/apg/patterns/table/).
- [DV-S2 — W3C APG: Grid pattern](https://www.w3.org/WAI/ARIA/apg/patterns/grid/).
- [DV-S3 — ONS: Choosing a chart type](https://service-manual.ons.gov.uk/data-visualisation/chart-types/choosing-a-chart-type).
- [DV-S4 — ONS: Bar charts](https://service-manual.ons.gov.uk/data-visualisation/chart-types/bar-charts).

Đọc ngày 20/10/2026. Catalog và hợp đồng bên trên là tổng hợp thiết kế cho C2O; các nguồn hỗ trợ semantics web và cách đặt câu hỏi chọn chart, không xác nhận một implementation đã đạt.
