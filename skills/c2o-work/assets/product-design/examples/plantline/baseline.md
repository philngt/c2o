# Plantline — B-01, revision 1

> **selected cho ví dụ C2O Design, giữ nguyên từ v1.1.0 sang v1.2.0**; chưa có implementation hay kiểm chứng. Nguồn chọn: [DEC-01](decision.md), phương án O-01. Ngày ghi: 2026-10-20; agent biên soạn ví dụ.

Baseline này áp dụng cho L-01 danh sách và L-02 chi tiết/đọc/sửa trên iPhone/iPad, với hồ sơ đã có trên một thiết bị. Outcome là nhận đúng cá thể và lưu đúng chỉnh sửa offline. Áp dụng [hợp đồng baseline](../../core/baseline.md); không mở rộng sang thêm cây, quản lý ảnh hoặc đồ thị phả hệ.

## Nơi giữ thông tin chuẩn

| Chủ đề | Tài liệu canonical |
| --- | --- |
| Domain, scope, giả định H-01…H-03, câu hỏi X-01/X-02 | [brief.md](brief.md) |
| Fixture, flow, trạng thái và microcopy | [experience.md](experience.md) |
| Phương án và lựa chọn | [options.md](options.md), [decision.md](decision.md) |
| Vùng, thứ tự, co giãn và hành động từng màn | [layout.md](layout.md) |
| Diễn đạt dữ liệu và scope của DV-01/02 | [data-views.md](data-views.md), dẫn chiếu domain/fixture ở brief và experience |
| Trách nhiệm/events/state của CMP-01…03 | [components.md](components.md) |
| Ghép vùng, ownership và chuyển tiếp SCR-01/02 | [ui-composition.md](ui-composition.md) |
| Vai trò chữ/màu/component/motion | [design-direction.md](design-direction.md) |
| Vai trò, nguồn, fallback của A-01…A-03 | [asset-brief.md](asset-brief.md), [assets.json](assets.json) |
| Tiêu chí theo flow; bản ghi criterion; kết quả | [experience.md](experience.md); [project.json](project.json); [verification.json](verification.json) |

Anchor hiện là hợp đồng nội dung/hành vi và mô tả layout; chưa có mockup hoặc render thực. Dự kiến dùng typography, màu theo vai trò và controls hệ thống theo [profile SwiftUI](../../profiles/swiftui.md). Đây là định hướng, không phải bằng chứng kích thước, tương phản hay accessibility đã đạt.

## Quy ước xuyên màn

| Nhóm | Quy tắc B-01 |
| --- | --- |
| Cá thể và thuật ngữ | Tên gọi + mã ổn định nhận diện hồ sơ; loài/giống ở nhóm riêng. Giữ câu “Theo nhãn người bán, chưa xác minh”. Không dùng ảnh để xác nhận taxonomy. |
| Nguồn gốc | Phân biệt nguồn mua, cách nhân giống và quan hệ lai; ghi phần biết/chưa biết. Không suy ra bố mẹ từ tên giống, hình ảnh hoặc cách nhân giống. |
| Selection/navigation | Mọi hàng, chi tiết và bản nháp gắn với cùng mã. Hẹp: chuyển màn; đủ rộng: list–detail. Giữ selection và query khi bố cục đổi; draft chưa lưu cần xử lý trước khi đổi cây. |
| Lưu/hủy/lỗi | Chỉ sửa vị trí/ghi chú. Draft tách dữ liệu đã lưu. Sau commit cục bộ thành công mới báo “Đã lưu trên thiết bị này” và cập nhật list/detail. Lỗi giữ draft; hủy có thay đổi dùng lựa chọn trong experience. |
| Hierarchy | Tên/mã trước, vị trí/ghi chú tiếp, taxonomy và nguồn gốc theo nhóm. Danh sách không có thumbnail; A-01 nếu có nằm sau các nhóm dữ liệu chính ở chi tiết. |
| Visual/component | Typography co giãn theo hệ thống; màu nền/chữ/trạng thái theo vai trò, accent nhất quán. Dùng lại hàng, nhãn trường và hành động tương đương; glyph A-03 có nhãn UI và tên truy cập phù hợp. |
| Dữ liệu/asset thiếu | Chưa có ảnh khác với không đọc được ảnh; cả hai không chặn đọc/sửa/lưu. Không thay bằng ảnh cây cùng giống. A-02 hoãn; empty state vẫn giải thích bằng chữ. |
| Accessibility/offline | Chữ lớn được wrap và đổi bố cục; không thu chữ để giống một frame. State có chữ, không dựa riêng màu/motion. Không có mạng vẫn là trạng thái bình thường của slice. |

Khác biệt có chủ đích: list ưu tiên quét, detail cho đọc đầy đủ, edit ưu tiên nhãn/trường và giữ draft; rộng có hai vùng, hẹp chuyển màn. Những khác biệt này giữ cùng dữ liệu, ngôn ngữ và kết quả hành động. Ảnh tùy chọn không làm thay đổi thứ tự ưu tiên của thông tin.

## Revision và kiểm chứng

Revision 1 lập baseline đầu tiên, chưa thay thế bản nào. v1.2 làm rõ data-view/component/composition từ các quyết định này; không đổi outcome, scope, O-01, L-01/L-02 hoặc PL-01…08 nên giữ revision 1. Nếu khi triển khai chọn khác quy tắc đang ghi, phải xem lại revision và tiêu chí chịu ảnh hưởng. Các kích thước vùng, spacing, ngưỡng chuyển cột, màu cụ thể và thời lượng motion **chưa đo/chưa chốt trong runtime**. Không có con số pixel hoặc phần trăm giống ảnh được coi là bằng chứng.

PL-01…PL-08 đều **Proposed / NOT_RUN**. PL-08 sẽ đối chiếu B-01 với list/detail/edit, rỗng/lỗi/đang lưu và cấu hình đã chọn; PL-07 kiểm tra asset thực cùng fallback. Muốn thay quy tắc chung, cập nhật revision và rà L-01/L-02, direction, assets và evidence chịu ảnh hưởng. Muốn đổi tác vụ ưu tiên, xem lại DEC-01. ID/revision là liên kết review thủ công, không phải xác nhận tự động của checker.
