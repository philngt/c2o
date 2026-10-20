# Hợp đồng component CMP-01

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-COMPONENT` |
| Phiên bản template | `1.1.0` |
| Mục đích | Định nghĩa trách nhiệm, anatomy, semantics, data/events và các state áp dụng của một component trong dự án. |
| Dùng khi | Tái sử dụng, thêm variant, compose hoặc tạo component có hành vi cần làm rõ hay dùng lại. |
| Đầu vào | Task, criterion, baseline, region sử dụng, component hiện có và catalog pattern phù hợp. |
| Đầu ra / bàn giao | Hợp đồng CMP đủ để triển khai và ghép vào flow, kèm quyết định reuse và phạm vi kiểm chứng. |
| Nguồn chuẩn | Chỉ giữ hợp đồng component khi được đăng ký canonical; domain rules, lựa chọn baseline và criterion results được tham chiếu từ nguồn riêng. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Component instance, variant/state, flow, platform và vùng sử dụng] |

[Chuẩn template](../documentation/template-standard.md).

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Placeholder chỉ là chỗ điền, không phải bằng chứng hay sự kiện đã xảy ra. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu theo dõi bản đã điền của dự án. Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, độc lập với trạng thái quyết định, verdict review và verification; `accepted` không tự ghi nhận phê duyệt của người dùng, kết quả kiểm chứng hoặc quyền phát hành.

- Tên / trách nhiệm:
- Mẫu catalog CP-xx đang áp dụng và phần thích ứng:
- Task và criterion IDs, ví dụ C-001:
- Baseline ID / revision; layout / vùng sử dụng:
- Component hiện có; chọn reuse / variant / compose / tạo mới và lý do:
- Quyết định áp dụng component và trạng thái proposed / selected tại nguồn decision/baseline:
- Implementation và evidence hiện có:

`selected` thuộc quyết định áp dụng, độc lập với trạng thái tài liệu; verification ghi riêng. Checker chưa tự xác minh CMP/CP IDs.

## Anatomy và semantics

| Phần | Nội dung / bắt buộc hay tùy chọn | Vai trò, tên, giá trị, trạng thái | Vùng tương tác |
| --- | --- | --- | --- |
| | | | |

## Data và events

| Input/value | Kiểu, format/đơn vị, null/unknown | Nguồn và ownership | Giới hạn |
| --- | --- | --- | --- |
| | | | |

| Event / ý định | Payload và scope | Ai xử lý; khi nào commit | Kết quả / lỗi |
| --- | --- | --- | --- |
| | | | |

Nêu ownership của draft, selection và dữ liệu đã lưu; API/props theo implementation.

## State và transition có áp dụng

| State / tổ hợp | Trigger / điều kiện | UI và hành vi | Focus / phục hồi | Criterion |
| --- | --- | --- | --- | --- |
| | | | | |

Xét state tương tác, dữ liệu, nghiệp vụ và khả năng thao tác; chọn tổ hợp có ảnh hưởng.

## Variants, adaptation và assets

- Variant và điều kiện dùng; phần semantics/behavior phải giữ:
- Token semantic, anatomy được thay và giới hạn nội dung:
- Chữ lớn, nội dung dài, locale, cửa sổ hẹp/rộng, input:
- Keyboard/focus, gesture và cách thao tác thay thế liên quan:
- Asset IDs, vùng đặt, provenance, fallback; phần UI-owned-by-code:

## Kế hoạch kiểm chứng

- Artifact/build, dataset, platform/configuration cần dùng:
- State/transition bắt buộc; kết quả cần quan sát:
- Kiểm tra riêng component và khi ghép trong flow/layout:
- Điều chưa đo/chưa chạy; evidence sẽ ghi tại đâu:

Khi sao mẫu, cập nhật đường dẫn [hợp đồng](../core/components.md). Kiểm tra chưa thực hiện giữ `not-tested`, nêu rõ chưa chạy hay bị chặn bởi môi trường; evidence một phần giữ `partial`.

## Kiểm tra trước bàn giao

- [ ] Trách nhiệm component và lý do reuse/variant/compose/tạo mới rõ; lựa chọn dẫn về decision hoặc baseline nguồn.
- [ ] Input, events, validation và thời điểm commit có owner; draft, selection và dữ liệu đã lưu không bị lẫn.
- [ ] State/transition có áp dụng, hành vi keyboard/focus và đường phục hồi đã được xác định.
- [ ] Anatomy, token, adaptation, nội dung biên và asset fallback có giới hạn cụ thể.
- [ ] Kiểm tra component riêng và khi ghép flow được phân biệt; artifact và evidence chỉ ghi phần thực có.
