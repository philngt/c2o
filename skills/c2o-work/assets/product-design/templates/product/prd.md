# PRD — [sản phẩm / phiên bản / scope]

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-PRD` |
| Phiên bản template | `1.1.0` |
| Mục đích | Chốt outcome, năng lực ưu tiên và yêu cầu của một phiên bản đủ cụ thể để chuyển sang thiết kế, triển khai và kiểm chứng. |
| Dùng khi | Nhiều feature cần cùng một nguồn ưu tiên, có đánh đổi scope hoặc cần thống nhất phạm vi phiên bản; thay đổi nhỏ có thể dùng brief và hợp đồng bị ảnh hưởng. |
| Đầu vào | [Brief](../brief.md), bằng chứng nhu cầu, [business design](business-design.md) nếu có, [product blueprint](product-blueprint.md), ràng buộc và phản hồi. |
| Đầu ra / bàn giao | Scope/priorities, F/REQ có điều kiện và kết quả rõ, liên kết criterion và dependency để bàn giao sang specs, delivery và validation. |
| Nguồn chuẩn | Khi được đăng ký, PRD giữ yêu cầu, ưu tiên và scope phiên bản. Brief giữ subset của nhiệm vụ; [domain model](domain-model.md), [feature spec](feature-spec.md), [experience](../experience.md) và [technical spec](technical-spec.md) giữ chi tiết. Nguồn acceptance đã chọn giữ criterion ID/nghĩa/tính bắt buộc. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Sản phẩm / phiên bản / OUT-01 / support contract và phần ngoài scope] |

[Chuẩn template](../../documentation/template-standard.md). Placeholder là chỗ cần điền, không phải bằng chứng. Phiên bản template theo dõi mẫu dùng chung; revision tài liệu theo dõi bản được điền cho dự án.

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, tách khỏi trạng thái quyết định và kết quả kiểm chứng. `accepted` nghĩa là chọn dùng tài liệu trong phạm vi quyền hạn hiện có; không chứng minh người dùng đã phê duyệt, test đã đạt hoặc có quyền phát hành.

Giữ nguồn chuẩn đã đăng ký trong [document index](document-index.md); không tự thay owner của thông tin chỉ vì sao chép template. Đọc [hướng dẫn bộ tài liệu](../../documentation/README.md) và cập nhật đường dẫn/ID mẫu thành tham chiếu thật của dự án.

## 1. Vấn đề và outcome có thể quan sát

- Actor, task và context: [tham chiếu brief; chỉ bổ sung context sản phẩm còn thiếu].
- Bằng chứng nhu cầu và giới hạn: [nguồn, ngày, loại evidence].
- Giả định còn dùng: [ASM-01 và nguồn đang giữ giả định].

| Outcome | Nguồn định nghĩa | Chỉ số / dấu hiệu thành công | Baseline đã đo hoặc chưa biết | Mục tiêu dự kiến / thời gian | Cách quan sát và giới hạn |
| --- | --- | --- | --- | --- | --- |
| OUT-01 | [brief / nguồn đã thống nhất] | [đơn vị, đối tượng, điều kiện] | | | [validation plan] |

Phân biệt mục tiêu sản phẩm với acceptance của implementation. Chỉ số cần người dùng thật hoặc dữ liệu sau phát hành phải có kế hoạch đo; chưa có dữ liệu thì giữ trạng thái chưa đo.

## 2. Phạm vi phiên bản

| Trong scope | Hoãn / ngoài scope | Lý do và điều kiện xem lại |
| --- | --- | --- |
| [khả năng và ranh giới cụ thể] | | |

- Platform/deployment target, locale, theme và điều kiện sử dụng hỗ trợ: [...].
- Giới hạn nguồn lực/thời gian hoặc dependency có thể đổi scope: [...].
- Những gì đã có cần giữ nguyên về hành vi/dữ liệu: [...].

## 3. Feature và ưu tiên

Dùng `Must` cho phần cần đạt outcome của scope, `Should` cho phần có thể hoãn có chủ đích, `Could` cho phần tùy chọn và `Deferred` cho ngoài phiên bản. Ghi lý do; nhãn ưu tiên không tự quyết định criterion nào là bắt buộc.

| ID | Feature / capability | Outcome và lý do | Ưu tiên | Requirement / dependency | Feature spec |
| --- | --- | --- | --- | --- | --- |
| F-01 | [năng lực người dùng cần] | OUT-01 | [chọn] | REQ-01; [dependency] | [đường dẫn] |

## 4. Yêu cầu và liên kết acceptance

| ID | Feature | Điều kiện + hành động + kết quả cần có | Loại / giới hạn đo | Domain / spec liên quan | Criterion IDs |
| --- | --- | --- | --- | --- | --- |
| REQ-01 | F-01 | [khi…, actor…, hệ thống…] | [functional / chất lượng / constraint] | BR-01; ENT-01; [spec] | C-001 |

Ghi yêu cầu về dữ liệu, khả năng tiếp cận, hiệu năng, quyền truy cập, offline hoặc nền tảng khi ảnh hưởng scope; thay từ “nhanh”, “đẹp”, “an toàn” bằng điều kiện và giới hạn kiểm tra được. Quy tắc `BR-01` chỉ được định nghĩa tại domain model, rồi tham chiếu ở đây.

Criterion phải có cùng ID và ý nghĩa trong nguồn acceptance đã chọn của dự án. Chỉ khi chủ động chọn profile JSON tùy chọn mới dùng [project template](../project.json); không cần JSON để dùng PRD này. Tái sử dụng namespace đang áp dụng: `C-`, `APP-`, `LIF-`, `UTL-`, `WID-`, `PL-`. Criterion mới còn là đề xuất cho tới khi được xử lý trong scope; `REQ-01` không thay cho criterion. Bảng này không ghi pass và không được coi là evidence.

## 5. Quyết định mở, phụ thuộc và thay đổi

| Vấn đề | Ảnh hưởng / REQ-xx | Nguồn theo dõi | Owner / bước tiếp theo | Có chặn slice hiện tại? |
| --- | --- | --- | --- | --- |
| | | [ASM-01 / ADR-01 / nguồn khác] | | [có/không + lý do] |

- Slice đầu và thứ tự: [delivery plan](delivery-plan.md), [SL-01 trong bản đã điền].
- Kế hoạch xác minh: [validation plan](validation-plan.md); [coverage và phương pháp cho từng criterion].
- Điều kiện phát hành/vận hành nếu thuộc nhiệm vụ: [release-operations](release-operations.md).
- Thay đổi so với revision trước: [REQ/F/OUT bị ảnh hưởng, lý do, spec/criteria cần cập nhật].

## Điều kiện kết thúc bản này

Scope và ưu tiên có lý do; yêu cầu bắt buộc cho slice đã rõ điều kiện/kết quả; acceptance liên kết về nguồn acceptance đã chọn; dependency chặn bước kế tiếp đã được giải quyết hoặc ghi rõ. Tài liệu định nghĩa việc cần làm, còn kết quả kiểm chứng được ghi riêng bằng evidence phù hợp với implementation.

## Kiểm tra trước bàn giao

- [ ] Outcome, bằng chứng và giả định có nguồn; baseline chưa đo không được thay bằng mục tiêu hoặc số minh họa.
- [ ] In/out scope, nền tảng và ưu tiên có lý do; brief của task chỉ lấy subset được giao.
- [ ] REQ cần cho slice có điều kiện/hành động/kết quả quan sát được; quality requirement có phạm vi và cách đo.
- [ ] BR/specs được dẫn chiếu đúng nguồn; criterion ID và ý nghĩa khớp nguồn acceptance đã chọn, nhãn Must không tự sửa tính bắt buộc.
- [ ] Dependency, thay đổi revision và câu hỏi chặn có owner; delivery/validation/release dùng đúng nguồn đã đăng ký.
