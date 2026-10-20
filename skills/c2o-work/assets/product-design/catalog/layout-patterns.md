# Catalog bố cục

**C2O Design v1.2.0.** Các pattern là điểm khởi đầu cho [layout contract](../core/layout.md). Chúng có thể kết hợp và cùng chứa nhiều [data view](../core/data-views.md). Chọn theo tác vụ, thông tin và không gian; không dùng hình vẽ của một pattern làm bản đặc tả mọi màn.

## Chọn cấu trúc

| ID / pattern | Phù hợp khi | Các vùng chính | Thích ứng / điều cần tránh |
| --- | --- | --- | --- |
| LP-01 — Một luồng dọc | Đọc, xem chi tiết hoặc hoàn thành một việc có thứ tự ưu tiên rõ | Định danh, nội dung chính, nhóm hỗ trợ, hành động | Wrap/stack và cuộn; tránh nhồi mọi thứ vào màn đầu hoặc cố định quá nhiều thanh. |
| LP-02 — List–detail | Chọn một đối tượng rồi xem/sửa; cần đổi đối tượng thường xuyên | Bộ sưu tập/tìm kiếm và chi tiết của ID đang chọn | Rộng có thể cạnh nhau, hẹp chuyển màn; giữ selection/query/draft, có trạng thái chưa chọn. |
| LP-03 — Workspace có navigation và panel phụ | Nhiều khu vực công việc, nội dung chính và thuộc tính theo ngữ cảnh | Navigation, content, inspector tùy nhu cầu | Ghi panel nào được ẩn/chuyển thành màn hoặc sheet; không ép ba cột vào mọi cửa sổ. |
| LP-04 — Bộ sưu tập thích ứng theo ô | Quét các item có nội dung/hình ảnh tương đương về vai trò | Search/filter tùy task, vùng collection, controls liên quan | Số cột theo nội dung và không gian; thứ tự đọc/selection ổn định. Grid không tự làm mọi card thành control. |
| LP-05 — Form theo nhóm hoặc bước | Nhập/sửa dữ liệu có quan hệ và validation | Định danh, nhóm field, giải thích/lỗi, lưu/hủy | Một form hoặc chia bước theo phụ thuộc nhiệm vụ; giữ draft khi quay lại. Không chia chỉ để làm màn ngắn. |
| LP-06 — Tổng quan dẫn xuống chi tiết | Người dùng cần nhận ra vấn đề rồi hành động với dữ liệu gốc | Phạm vi/thời gian, tổng hợp liên quan, danh sách ưu tiên, đường drill-down | Giữ filter và phạm vi thống kê; không tự thêm hàng KPI, chart hoặc tab chỉ để giống dashboard. |
| LP-07 — Canvas và inspector | Thao tác trực tiếp với vị trí, đồ thị hoặc đối tượng không gian là tác vụ chính | Canvas, công cụ, selection, inspector, cách định vị/tìm | Có cách chọn/xem đối tượng ngoài pan/zoom/drag khi cần; panel không che vùng thao tác. Canvas không tạo ra quan hệ domain. |
| LP-08 — So sánh song song | Cần xem khác biệt giữa các đối tượng hoặc phiên bản theo cùng thuộc tính | Tiêu chí chung, các đối tượng, vùng khác biệt, hành động | Rộng có thể nhiều vùng; hẹp có thể giữ bảng cuộn hoặc chọn cặp xem. Không đổi thành card nếu mất khả năng đối chiếu cần thiết. |
| LP-09 — Các nhóm công việc/lane | Người dùng theo dõi các nhóm hoặc trạng thái và chuyển công việc khi được phép | Bộ lọc, lanes, item, feedback chuyển trạng thái | Hẹp có thể tập trung một lane hoặc dùng danh sách nhóm. Không để drag là đường duy nhất; chuyển lane phải theo business rule. |
| LP-10 — Tác vụ tập trung với lớp phụ | Một hành động ngắn cần ngữ cảnh đang xem hoặc một trình chỉnh sửa chuyên biệt | Nội dung tác vụ, hướng dẫn, xác nhận/hủy, context phù hợp | Chọn inline, panel, sheet, dialog hay màn riêng theo task/platform; tránh nhiều lớp modal lồng nhau. |

Các tên như list–detail, board hoặc overview có phần giao nhau với interaction/screen patterns. Catalog này mô tả tổ chức không gian và adaptation; luật dữ liệu và thao tác vẫn phải đặt trong hợp đồng tương ứng.

## Hợp đồng adaptation

Với mỗi pattern đã chọn, ghi: thông tin nào luôn cần truy cập, thứ tự đọc, vùng cuộn, nơi focus quay lại, panel ưu tiên, context giữ theo ID và điều kiện đổi cấu trúc. Breakpoint xuất phát từ nội dung/platform và được kiểm tra trên implementation, không lấy một số pixel mẫu làm luật cho mọi app.

Trên web, reflow có ngoại lệ cho phần nội dung thực sự cần hai chiều như bảng dữ liệu hoặc sơ đồ. Vì vậy không buộc mọi table thành card; cần kiểm tra đường đọc, header, cuộn và thao tác còn dùng được trong phạm vi accessibility đã chọn. Ngoại lệ không tự áp dụng cho mọi text/control xung quanh hoặc mọi ô riêng lẻ. [W3C Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

Với native, dùng layout/navigation của deployment target và kiểm tra khi cửa sổ đổi kích thước. Apple mô tả split-view navigation có thể tự hiện/ẩn cột theo không gian; hành vi lựa chọn và dữ liệu của app vẫn cần kiểm chứng. [Apple WWDC25 — What's new in SwiftUI](https://developer.apple.com/videos/play/wwdc2025/256/)

Safe area, vùng bị che hoặc reserved regions là input của layout ở thiết bị liên quan. Kiểm tra với API/cấu hình thực đang hỗ trợ; không suy ra mọi vùng dùng được từ chiều rộng/chiều cao ảnh chụp.

## Điểm dừng của proposal

Một L-01 đủ cho bước tiếp theo khi regions, data view, component responsibilities, actions, state và adaptation liên quan đã rõ. Hình học chưa đo vẫn ghi chưa đo; prototype/render bổ sung khi cần giải quyết bất định. Dùng [mẫu layout](../templates/layout.md), [mẫu screen](../templates/screen.md) và [baseline](../core/baseline.md) hiện có, không nhân bản cùng một quyết định ở nhiều nơi.
