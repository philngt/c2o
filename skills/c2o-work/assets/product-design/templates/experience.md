# Hợp đồng experience

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-EXPERIENCE` |
| Phiên bản template | `1.1.0` |
| Mục đích | Nối task với flow màn, UI state, transition và ownership để người dùng hoàn tất việc mà không mất ngữ cảnh hoặc dữ liệu. |
| Dùng khi | Thêm/đổi flow, navigation, trạng thái hoặc hành vi xuyên màn cần làm rõ trước khi thiết kế hay triển khai. |
| Đầu vào | Brief, domain/feature spec hiện có, baseline/decision, criterion và artifact liên quan. |
| Đầu ra / bàn giao | Hợp đồng flow/UI state có trách nhiệm từng màn, hành động hợp lệ, phục hồi và component/criterion refs. |
| Nguồn chuẩn | Chỉ giữ screen flow, UI state và ownership khi được đăng ký canonical; ENT/BR và hành vi nghiệp vụ dẫn về domain/feature spec hiện có. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Flow, màn, UI state, platform và criterion trong nhiệm vụ] |

[Chuẩn template](../documentation/template-standard.md).

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Placeholder chỉ là chỗ điền, không phải bằng chứng hay sự kiện đã xảy ra. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu theo dõi bản đã điền của dự án. Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, độc lập với trạng thái quyết định, verdict review và verification; `accepted` không tự ghi nhận phê duyệt của người dùng, kết quả kiểm chứng hoặc quyền phát hành.

Nếu domain/feature spec đã có, dùng nguồn chuẩn đó cho ENT/BR và hành vi tác vụ. Khi được đăng ký canonical, hợp đồng này giữ flow màn/UI state/ownership và các refs liên quan; xem [hệ thống tài liệu](../documentation/README.md). Không chép rule kinh doanh thành một bản khác.

- Outcome và baseline revision: [scope theo hợp đồng tài liệu và brief/feature nguồn].
- Decision, layout proposals và asset manifest liên quan nếu có:

## Domain và ownership

| Đối tượng | Ý nghĩa, ID | Dữ liệu đọc/ghi | Quy tắc cần giữ |
| --- | --- | --- | --- |
| | | | |

## Flow trong scope

Ghi entry point, chuỗi hành động, kết quả dữ liệu và cách trở lại. Có thể dùng danh sách hoặc sơ đồ khi nhánh và thứ tự quan trọng.

## Trách nhiệm màn hình

| Screen | Người dùng cần biết/làm gì | Nội dung chính | Hành động | Điểm đến |
| --- | --- | --- | --- | --- |
| | | | | |

## State và transition

| State | Trigger/điều kiện | UI và copy | Hành động hợp lệ | Phục hồi/kết quả |
| --- | --- | --- | --- | --- |
| Empty | | | | |
| Ready | | | | |
| Processing nếu có | | | | |
| Error nếu có | | | | |
| Offline/stale/permission nếu có | | | | |

## Hợp đồng component cần thay đổi

| Component | Variant/state áp dụng | Semantics và input | Token role | Tiêu chí liên quan |
| --- | --- | --- | --- | --- |
| | | | | |

## Dữ liệu biên và kiểm tra

Tên dài, thiếu ảnh, ít/nhiều dữ liệu, bản dịch, chữ lớn, dữ liệu không hợp lệ và thay đổi chưa lưu: chọn trường hợp có ảnh hưởng đến flow. Ghi criterion ID cho từng nhóm, không mặc định mọi component có cùng tám state.

## Kiểm tra trước bàn giao

- [ ] Outcome/scope và ENT/BR/feature refs đúng nguồn, không chép rule nghiệp vụ thành nghĩa mới.
- [ ] Flow có entry, kết quả, điểm ghi dữ liệu và đường back/hủy/phục hồi phù hợp.
- [ ] Mỗi màn có trách nhiệm và hành động rõ; query, selection, draft và commit có owner cần thiết.
- [ ] State/transition chỉ giữ các trường hợp áp dụng, với trigger, copy, hành động và đường thoát.
- [ ] Component thay đổi, dữ liệu biên và criterion liên quan được nối; phần chưa kiểm chứng không được mô tả là đã đạt.
