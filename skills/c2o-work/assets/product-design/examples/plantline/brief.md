# Plantline — Brief của một lát cắt

> Ví dụ giả định cho **C2O Design v1.2**. Chưa triển khai, nghiên cứu hay kiểm thử. Mọi tiêu chí: **Proposed / NOT_RUN**.

Ví dụ này chọn **profile JSON cũ, tùy chọn** để minh họa bản ghi tiêu chí trong [project.json](project.json) và kết quả trong [verification.json](verification.json). Phân công nguồn chuẩn chỉ có hiệu lực trong bộ ví dụ Plantline; sao chép một section không chuyển authority từ acceptance/evidence C2O hiện có sang JSON. Khi áp dụng cho dự án thật, giữ nguồn và các trạng thái C2O `pass / partial / fail / not-tested`; profile JSON không có nhãn `partial`, nên giữ bằng chứng một phần và giới hạn tại nguồn C2O, không đổi thành `PASS`. Xem [hướng dẫn evidence](../../core/evidence.md). Các tiêu chí và kiểm tra native của ví dụ vẫn chưa chạy.

## Outcome

Người sưu tầm tìm đúng cây, xem hồ sơ rồi sửa vị trí/ghi chú và lưu offline. Danh sách và chi tiết cùng hiển thị dữ liệu vừa lưu; hồ sơ cây khác không đổi.

**Đã biết từ concept:** Plantline quản lý cá thể cây hiếm và lịch sử nhân giống; cần phân biệt giâm cắt, tách bụi, gieo hạt, lai giống. Đây là định hướng sản phẩm, chưa phải bằng chứng về nhu cầu hay hành vi.

**Giả định:** H-01, mã cây giúp tránh nhầm cá thể có cùng giống. H-02, sửa vị trí/ghi chú là việc thường xuyên. H-03, slice dùng kho dữ liệu cục bộ trên một thiết bị; chưa có đồng bộ. Prefix `H-` dành cho giả định; `A-` dành cho asset.

**Cần thử:** X-01, người dùng chọn đúng cây bằng tên, mã và vị trí hay cần ảnh? X-02, thông báo lưu có khiến họ hiểu nhầm rằng dữ liệu đã được sao lưu?

## Ranh giới domain

| Khái niệm | Quyết định đề xuất |
|---|---|
| Cá thể cây | Một hồ sơ có mã ổn định; hai cây cùng giống vẫn là hai cá thể. |
| Loài / giống | Thuộc tính định danh, có thể chưa xác minh; không thay thế mã cá thể. |
| Nguồn mua/nhận | Người bán hoặc nơi nhận cây; tách khỏi cách cây được nhân giống. |
| Cách nhân giống | Giâm cắt, tách bụi, gieo hạt hoặc chưa rõ; liên kết cây nguồn nếu biết. |
| Quan hệ lai | Ghi cây mang hạt/cây cho phấn khi có bằng chứng. Một cây gieo hạt có thể thuộc phép lai; một cây giâm có thể lấy từ cây lai. Không coi “lai” và “gieo hạt” là hai loại loại trừ nhau. |

## Phạm vi

Trong slice: tìm danh sách, xem chi tiết, sửa vị trí/ghi chú, lưu/hủy. Nguồn gốc hiện tóm tắt, mức chắc chắn; không thêm quan hệ chưa biết.

Tiền điều kiện: đã có hồ sơ cây trong kho cục bộ. Ví dụ thiết kế này dùng fixture giả định; khi triển khai sản phẩm mới phải xác định đường tạo/import hồ sơ trước khi gọi đây là flow dùng được với dữ liệu người dùng.

Chưa đưa vào slice: thêm cây, sửa taxonomy, dựng đồ thị phả hệ, chỉnh sự kiện lai, đồng bộ nhiều thiết bị, tính toán di truyền. Ảnh nếu có là tài nguyên đã có; slice không bổ sung bước chụp/import/chỉnh ảnh.

## Quyết định và tài liệu nối tiếp

[Options](options.md) so sánh các hướng giả định; [DEC-01](decision.md) chọn **O-01: danh sách ưu tiên chữ** cho ví dụ này. Đây là quyết định minh họa trong bộ tài liệu, chưa được người dùng kiểm chứng và không đại diện cho lựa chọn của người dùng. [B-01 revision 1](baseline.md) giữ hướng dùng chung; [layout](layout.md) mô tả **L-01 danh sách** và **L-02 chi tiết/đọc+sửa**.

[Asset brief](asset-brief.md) và [manifest](assets.json) tách **A-01 ảnh thật của cá thể** tùy chọn ở chi tiết, **A-02 illustration trang trí empty-state** đang hoãn, và **A-03 glyph hệ thống**. Không có file ảnh đã tạo. Text, dữ liệu, control và phản hồi trạng thái do UI/code quản lý. Thiếu ảnh không ngăn tìm, đọc hoặc sửa hồ sơ.

v1.2 làm rõ [DV-01/02](data-views.md), [CMP-01…03](components.md) và [SCR-01/02](ui-composition.md): cách trình bày bộ sưu tập/hồ sơ, trách nhiệm hàng/trường/nút lưu, cùng chủ sở hữu query/selection/draft/commit. Đây là chi tiết hóa quyết định đang có, không thêm tính năng, không đổi B-01 revision 1 hay tiêu chí.

IDs xuyên tài liệu: **PL-01** tìm cây; **PL-02** hiểu đúng hồ sơ; **PL-03** lưu chỉnh sửa; **PL-04** xử lý chưa lưu/lỗi; **PL-05** dùng trên iPhone/iPad; **PL-06** hiểu nguồn gốc; **PL-07** tính thật, provenance, fallback và hiển thị asset trong app; **PL-08** nhất quán baseline/layout/state giữa các màn. [Experience](experience.md) định nghĩa tiêu chí; [review](review-example.md) và [verification](verification.json) giữ kế hoạch cùng trạng thái chưa chạy.
