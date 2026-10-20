# Plantline — Quyết định DEC-01

- Trạng thái: **selected — chỉ cho ví dụ minh họa**.
- Ngày ghi: 2026-10-20; vai trò: agent biên soạn ví dụ, chưa có quyết định từ nghiên cứu người dùng.
- Nguồn: [brief](brief.md), [experience](experience.md), [O-01…O-03](options.md).
- Phạm vi: hồ sơ cục bộ có sẵn → tìm đúng cá thể → chi tiết → sửa vị trí/ghi chú → lưu offline.

`selected` mô tả hướng dùng trong tài liệu. Không có implementation, kết quả kiểm thử hoặc quyền phát hành được suy ra từ trạng thái này.

## Quyết định và căn cứ

Chọn **O-01: danh sách chữ**, dùng tên, mã và vị trí để đối chiếu. Mã cá thể không thay bằng loài/giống. Danh sách không phụ thuộc ảnh; chi tiết có thể đọc ảnh thật của cá thể nếu hồ sơ cục bộ đã có.

| Phương án | Kết luận cho ví dụ | Căn cứ và giới hạn |
| --- | --- | --- |
| O-01 | Chọn | Hợp với tác vụ tra cứu mã/vị trí đã đặt ra và dùng được khi chưa có ảnh. Căn cứ là phân tích phạm vi, chưa đo tốc độ hay độ chính xác. |
| O-02 | Giữ để xét lại | Ảnh thật cạnh mã có thể giúp nhận diện; chưa có ảnh và chưa biết lợi ích trong X-01. |
| O-03 | Chưa chọn | Phù hợp giả thuyết duyệt bằng ảnh hơn; chưa có bằng chứng tác vụ đó là ưu tiên của slice. |

Chấp nhận đánh đổi: người quen nhận cây bằng hình có thể phải đọc nhiều hơn. H-01/H-02 là giả định hành vi; H-03 là giới hạn dữ liệu của ví dụ. X-01 cần kiểm tra chọn đúng cây giữa hai cá thể cùng giống; X-02 cần kiểm tra cách hiểu “Đã lưu trên thiết bị này”. Chưa có người tham gia, quan sát hay kết quả cho hai thử nghiệm.

## Chuyển thành hợp đồng chung

[B-01 revision 1](baseline.md) giữ lựa chọn này. [L-01](layout.md#l-01--danh-sách) là danh sách; [L-02](layout.md#l-02--chi-tiết-và-sửa) dùng cùng hồ sơ ở trạng thái đọc/sửa. [Design direction](design-direction.md) giữ chữ hệ thống, màu theo vai trò và component nền tảng; chưa có ảnh chụp UI làm anchor.

Theo [asset brief](asset-brief.md) và [manifest](assets.json): A-01 là ảnh thật tùy chọn ở chi tiết; A-02 là minh họa rỗng đang hoãn; A-03 là bộ glyph hệ thống. Không tạo thumbnail cho danh sách đã chọn, không thêm flow chụp/import ảnh, không biến UI thành ảnh.

PL-01…PL-06 giữ nguyên. PL-07 thêm kiểm tra tính đúng của asset, provenance, fallback và hiển thị runtime; PL-08 thêm tính nhất quán giữa baseline, layout và state. [Experience](experience.md) diễn giải tiêu chí theo flow, [project.json](project.json) giữ bản ghi criterion, [verification.json](verification.json) giữ kết quả; tất cả **NOT_RUN**. IDs liên kết bằng tài liệu, checker chưa tự xác minh chuỗi quyết định.

## Điều kiện xem lại

Đánh giá lại nếu X-01 cho thấy mã/tên/vị trí không đủ nhận diện, ảnh thật trở thành dữ liệu sẵn có và có ích, hoặc tác vụ ưu tiên đổi sang duyệt bộ sưu tập. So sánh lại O-02/O-03 trên cùng dữ liệu trước khi đổi hướng. Thay đổi tương đối dễ đảo ngược vì mô hình cá thể và flow lưu giữ nguyên; chi phí xây, thu thập ảnh và kiểm tra lại chưa ước lượng.

Đổi quy tắc chung phải ghi decision thay thế và revision baseline mới, rồi rà L-01/L-02, asset và evidence liên quan. Nếu mở rộng sang tạo cây, đồng bộ hoặc phả hệ, quay về Frame để xác định scope thay vì ngầm thêm vào lựa chọn bố cục.
