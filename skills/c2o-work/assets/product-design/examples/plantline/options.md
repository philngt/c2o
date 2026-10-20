# Plantline — Các phương án O-01…O-03

> Ví dụ giả định của **C2O Design v1.1.0**. Ba phương án cùng ở mức mô tả cấu trúc; chưa có mockup, ảnh thật, implementation hay nghiên cứu người dùng. Các nhận định bên dưới là suy luận thiết kế, chưa phải kết quả thử nghiệm.

## Câu hỏi và điều giữ cố định

Theo [brief](brief.md), người sưu tầm cần tìm đúng cá thể trong hồ sơ đã có, xem chi tiết, sửa vị trí/ghi chú rồi lưu offline. Câu hỏi ở đây là **cách trình bày danh sách**, không thay đổi tính năng hay mô hình dữ liệu. Áp dụng nhánh [Explore → Compare → Decide](../../core/exploration.md) trong Frame/Design.

Dùng cùng [fixture](experience.md): `PLT-014`, “Monstera bàn làm việc”, vị trí “Kệ đông”; `PLT-027` có cùng nhãn giống `Thai Constellation` nhưng là cá thể khác. Tác vụ chung: chọn `PLT-014`, đổi vị trí thành “Bàn làm việc”, lưu; `PLT-027` không đổi. Các trường chưa mô tả của `PLT-027` vẫn chưa được cung cấp, không bịa thêm để làm một phương án hấp dẫn hơn.

Mọi phương án giữ tìm theo tên/mã, mã nhìn thấy được, nhãn loài/giống chưa xác minh, chi tiết và flow lưu giống nhau. Nếu dựng thử, phải dùng cùng dữ liệu và cùng các điều kiện ảnh: có ảnh thật của cả hai cây; thiếu một ảnh; thiếu cả hai. Hiện chưa có ảnh nào, nên hiệu quả nhận diện bằng ảnh còn mở.

## Phương án có ý nghĩa

| ID | Cấu trúc đề xuất | Lợi ích dự kiến | Đánh đổi và phần chưa biết |
| --- | --- | --- | --- |
| O-01 | Danh sách chữ: tên, mã cá thể, vị trí; một hàng mở một hồ sơ. Không có thumbnail. | Quét mã/vị trí trực tiếp; cấu trúc ổn định khi thiếu ảnh. | Đòi hỏi người dùng nhớ hoặc đối chiếu mã/vị trí; chưa biết có đủ để nhận ra cây. |
| O-02 | Danh sách có ảnh thật của từng cá thể cạnh tên, mã và vị trí. Thiếu ảnh vẫn giữ thông tin chữ và vùng chọn. | Có thêm dấu hiệu hình ảnh mà vẫn so sánh mã theo hàng. | Cần ảnh đúng cá thể, đủ rõ; ảnh cũ hoặc góc chụp giống nhau có thể gây nhầm. Chưa biết ảnh có giúp hơn phần diện tích nó chiếm. |
| O-03 | Lưới ảnh thật, mỗi ô luôn có tên, mã và vị trí bên dưới; co về một cột khi cần. | Có thể phù hợp người nhận cây chủ yếu qua hình dáng. | Quét mã theo lưới và đọc nhãn dài cần kiểm tra; nhiều ảnh thiếu làm yếu lý do chọn lưới. |

Không phương án nào dùng ảnh giống cây đại diện để giả làm ảnh cá thể. Ảnh không chứng minh taxonomy hay quan hệ phả hệ. Trong cả ba phương án, ảnh chi tiết nếu có cũng là ảnh thật tùy chọn; nút, nhãn và dữ liệu vẫn là UI do code tạo.

## So sánh và lựa chọn minh họa

H-01 giả định mã giúp phân biệt; H-02 giả định sửa vị trí/ghi chú thường xuyên; H-03 giới hạn dữ liệu một thiết bị. Với phạm vi đó, **O-01** có ít phụ thuộc đầu vào nhất và đặt dấu hiệu đối chiếu trực tiếp tại danh sách. Đây là lý do chọn để hoàn thiện ví dụ, không phải khẳng định nhanh hơn hay được người dùng ưa thích hơn.

O-02 là ứng viên đáng thử nếu X-01 cho thấy người dùng cần ảnh để chọn đúng cây. O-03 đáng xét khi tác vụ thực tế thiên về duyệt bằng hình ảnh; chưa có bằng chứng cho hướng này. Không chấm điểm số khi chưa có cơ sở đo.

Chuyển lựa chọn sang [DEC-01](decision.md), [B-01 revision 1](baseline.md) và [L-01/L-02](layout.md). O-02/O-03 chưa được chọn, không tự bổ sung việc thu thập ảnh vào slice. PL-01…PL-08 đều **Proposed / NOT_RUN**; kiểm tra X-01 và X-02 vẫn chưa thực hiện.
