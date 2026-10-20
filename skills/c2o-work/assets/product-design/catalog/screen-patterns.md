# Catalog màn hình theo nhiệm vụ

**C2O Design v1.2.0.** Mỗi pattern gợi ý cách ghép [layout](layout-patterns.md), [data view](data-view-patterns.md) và [component](components.md). Đây là các câu hỏi thiết kế cần trả lời, không phải màn hình mẫu được code sẵn hay danh sách tính năng bắt buộc của app.

| ID / nhiệm vụ | Composition gợi ý | Điều phải làm rõ để dùng được |
| --- | --- | --- |
| SP-01 — Tìm/chọn trong bộ sưu tập | Search/filter khi cần + list/table/collection; LP-01/02/04 | Trường nào được tìm, filter nào đang bật, thứ tự, ID ổn định, không có dữ liệu khác không có kết quả; mở detail và quay lại giữ context. |
| SP-02 — Hiểu một đối tượng | Định danh + nhóm thuộc tính + status/source + hành động; LP-01/02 | Thông tin nào chưa biết/chưa xác minh; quyền đọc/sửa; dữ liệu đang hiển thị là phiên bản nào; chuyển sang sửa không đổi nhầm đối tượng. |
| SP-03 — Tạo/sửa và hoàn thành | Field group, validation, feedback và save/cancel; LP-05/10 | Owner của draft, thời điểm validation/commit, lỗi giữ input, duplicate submission, quay lại/hủy và phản hồi thành công. |
| SP-04 — Nhận ra vấn đề và xử lý | Phạm vi dữ liệu + tổng hợp có nghĩa + danh sách cần hành động; LP-06 | Định nghĩa metric/mẫu số, thời gian, độ mới, drill-down giữ scope; metric không tự thay kết luận hoặc hành động. |
| SP-05 — Lập kế hoạch/theo dõi công việc | Calendar, timeline, board hoặc grouped list theo câu hỏi; LP-01/09 với detail nếu cần | Ngày hạn khác thời gian thực hiện; timezone khi có; điều kiện chuyển trạng thái, tác động đổi lịch và phục hồi khi lưu lỗi. |
| SP-06 — Khám phá/chỉnh quan hệ hoặc không gian | Graph/map/canvas có selection và inspector; LP-07 | Loại cạnh/tọa độ, đơn vị, đường chọn/tìm, quan hệ chưa biết, cách lưu thao tác và đường dùng ngoài kéo thả. Không thay danh sách bằng graph nếu chưa có câu hỏi về quan hệ. |
| SP-07 — Cấu hình và tùy chọn | Nhóm setting, trạng thái hiện tại, mô tả hậu quả; LP-01/05 | Thay đổi có hiệu lực ngay hay cần lưu, phạm vi tài khoản/thiết bị/dự án, default và cách khôi phục khi tác vụ yêu cầu. |
| SP-08 — Bắt đầu hoặc phục hồi | Hướng dẫn đúng context, bước cần thực hiện, tiến trình nếu có; LP-01/05/10 | Người dùng cần làm gì để tiếp tục, có thể bỏ qua/quay lại không, quyền truy cập/dữ liệu cần thật sự là gì; không thêm onboarding bắt buộc chỉ vì template có sẵn. |

## Cách áp dụng

Chọn pattern theo nhiệm vụ và viết SCR-01 hoặc dùng tên màn hiện có. Chỉ lấy những vùng giải quyết outcome; một màn có thể kết hợp nhiều pattern. Ví dụ màn chi tiết có nhóm lịch sử và form sửa, nhưng lịch sử không tự mở thêm chức năng quản lý toàn bộ lịch.

Đặt các tình huống thay đổi composition vào [screen contract](../templates/screen.md): chưa chọn, rỗng, không tìm thấy, thiếu trường, partial/error/loading khi tồn tại, read/edit và trạng thái quyền áp dụng. Ghi một vùng lỗi ảnh cục bộ có ảnh hưởng vùng dữ liệu chính hay không; đừng mặc định mọi lỗi thay cả màn.

Khi screen cần thêm endpoint, quyền, dữ liệu hoặc domain action chưa có trong scope, quay lại Frame để làm rõ. Chọn một mẫu giao diện không tự cấp quyền xây tính năng mới.

## Review

Hỏi người dùng có biết đang xem gì, làm gì tiếp, điều gì sẽ xảy ra, kết quả đã đạt chưa và cách phục hồi khi không đạt hay không. Đối chiếu câu trả lời với artifact thực, criterion và [evidence contract](../core/evidence.md). Catalog này chưa là bằng chứng usability của một sản phẩm.
