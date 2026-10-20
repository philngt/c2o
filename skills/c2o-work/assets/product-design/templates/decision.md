# Quyết định thiết kế DEC-01

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-DECISION` |
| Phiên bản template | `1.1.0` |
| Mục đích | Ghi câu hỏi, lựa chọn có căn cứ, đánh đổi và điều kiện xem lại một quyết định thiết kế. |
| Dùng khi | Một lựa chọn quan trọng cần được giải thích, giữ lại để tái sử dụng hoặc thay thế bằng lựa chọn khác. |
| Đầu vào | Brief/constraints, option hoặc cách làm hiện tại, evidence/giả định và baseline có thể bị ảnh hưởng. |
| Đầu ra / bàn giao | Decision có trạng thái lựa chọn riêng, lý do, tác động lên baseline/criteria và điều kiện mở lại. |
| Nguồn chuẩn | Chỉ giữ quyết định và lý do khi record được đăng ký canonical; outcome/scope, quy tắc và kết quả kiểm chứng vẫn nằm ở nguồn tương ứng. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Câu hỏi quyết định, task, constraints và phần thiết kế chịu ảnh hưởng] |

[Chuẩn template](../documentation/template-standard.md).

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Placeholder chỉ là chỗ điền, không phải bằng chứng hay sự kiện đã xảy ra. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu theo dõi bản đã điền của dự án. Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, độc lập với trạng thái quyết định, verdict review và verification; `accepted` không tự ghi nhận phê duyệt của người dùng, kết quả kiểm chứng hoặc quyền phát hành.

- Trạng thái quyết định: `proposed` / `selected` / `superseded`:
- Ngày và người/agent ghi quyết định:
- Task và criterion IDs: [phạm vi theo hợp đồng tài liệu và brief nguồn].
- Brief và quyết định có liên quan:

Trạng thái này mô tả lựa chọn thiết kế, độc lập với trạng thái kiểm chứng. `selected` không có nghĩa implementation pass, người dùng đã xác nhận hiệu quả hoặc được phép phát hành.

## Câu hỏi và constraints

Điều gì cần quyết định, vì sao cần lúc này, constraints nào bắt buộc? Phân biệt yêu cầu đã biết với giả định và sở thích. Dẫn chiếu brief thay vì tạo định nghĩa nhiệm vụ khác.

## Các lựa chọn đã xét

| Option ID | Chọn / không chọn / còn mở | Lý do, evidence hoặc giả định |
|---|---|---|
| O-01 | | |

Chỉ ghi các phương án thực sự đã xét. Một quyết định đơn giản có thể chỉ cần phương án hiện tại và lý do giữ nó; không tạo lựa chọn giả để đủ bảng.

## Lựa chọn và đánh đổi

- Phương án được chọn hoặc đề nghị:
- Căn cứ quan trọng nhất; loại evidence và giới hạn:
- Lợi ích dự kiến; đánh đổi chấp nhận:
- Điều chưa biết; thử nghiệm hoặc kiểm tra còn cần:
- Mức dễ đảo ngược và tác động nếu lựa chọn sai:

Chọn trong quyền hạn nhiệm vụ hiện có. Khi chưa thể chọn, ghi câu hỏi cụ thể cần giải quyết; không tạo yêu cầu duyệt mới cho mọi decision.

## Chuyển vào baseline

- Baseline ID/version `B-01` và đường dẫn theo hợp đồng baseline:
- Direction, layout IDs, token/component hoặc asset IDs được cập nhật:
- Reference/anchor cùng hợp đồng hành vi cần giữ:
- Deviation có chủ đích và lý do:
- Tài liệu/criteria bị ảnh hưởng, nơi duy trì thông tin chuẩn:

Nếu lựa chọn làm đổi outcome hoặc scope, xem lại Shape/Decide/Spec theo vòng C2O và xử lý trong quyền hiện có trước khi cập nhật acceptance. Không chỉ sửa tiêu chí để hợp thức hóa phương án đã chọn.

## Khi nào xem lại

Sự kiện hoặc bằng chứng nào sẽ khiến cần đánh giá lại? Ghi decision thay thế khi có; giữ liên kết về decision cũ và baseline bị ảnh hưởng.

IDs option/decision/baseline là traceability bằng tài liệu, chưa được checker tự kiểm tra. Kết quả triển khai phải có evidence riêng theo criterion; biên bản lựa chọn không thay thế bằng chứng đó.

## Kiểm tra trước bàn giao

- [ ] Câu hỏi và constraints bám scope nhiệm vụ; facts, giả định và sở thích được phân biệt.
- [ ] Các lựa chọn thực sự đã xét có lý do chọn/không chọn; không tạo phương án giả để đủ mẫu.
- [ ] Trạng thái quyết định, ngày và người ghi được giữ riêng với trạng thái/revision tài liệu.
- [ ] Lựa chọn hoặc đề nghị nêu đánh đổi, khả năng đảo ngược và tác động tới baseline cùng nguồn chuẩn liên quan.
- [ ] Điều kiện xem lại và phần chưa đủ bằng chứng được ghi rõ; quyết định không được dùng thay kết quả kiểm chứng hoặc quyền phát hành.
