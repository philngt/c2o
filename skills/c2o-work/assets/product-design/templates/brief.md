# Brief thiết kế

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-BRIEF` |
| Phiên bản template | `1.1.0` |
| Mục đích | Định hình outcome quan sát được, scope và tiêu chí của một nhiệm vụ đủ rõ để thực hiện bước tiếp theo. |
| Dùng khi | Yêu cầu mới còn cần làm rõ hoặc thay đổi hiện có chưa xác định được kết quả, phạm vi hay cách kiểm tra. |
| Đầu vào | Yêu cầu hiện tại, context dự án, scope sản phẩm đã có, artifact và bằng chứng có thể đọc được. |
| Đầu ra / bàn giao | Brief nhiệm vụ có in/out scope, giả định, platform/mức can thiệp hiện có, criterion refs và quyết định còn mở có tác động. |
| Nguồn chuẩn | Chỉ giữ outcome/scope nhiệm vụ khi được đăng ký canonical; dẫn scope phiên bản ở PRD/pack và các trường acceptance từ nguồn acceptance đã chọn. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Nhiệm vụ; tham chiếu phần trong/ngoài scope và nền tảng ở các mục bên dưới] |

[Chuẩn template](../documentation/template-standard.md).

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Placeholder chỉ là chỗ điền, không phải bằng chứng hay sự kiện đã xảy ra. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu theo dõi bản đã điền của dự án. Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, độc lập với trạng thái quyết định, verdict review và verification; `accepted` không tự ghi nhận phê duyệt của người dùng, kết quả kiểm chứng hoặc quyền phát hành.

Khi được đăng ký canonical, brief này giữ outcome/scope của nhiệm vụ. Khi cần business design, blueprint hoặc PRD cấp phiên bản, tham chiếu nguồn đã có hoặc chọn mẫu từ [hệ thống tài liệu](../documentation/README.md); không định nghĩa scope cạnh tranh.

## Outcome

[Actor] thực hiện [task] trong [context] và đạt [kết quả quan sát được].

## Context và bằng chứng đang có

| Loại | Nội dung | Nguồn hoặc cách kiểm tra |
| --- | --- | --- |
| Đã biết | | |
| Giả định | | |
| Cần thử nghiệm | | |

## Phạm vi

- Trong scope:
- Hoãn lại:
- Ràng buộc có ảnh hưởng:
- Tài liệu/code/design system đang dùng:

## Nền tảng và mức quy trình

- Platform và deployment target đã xác định trong dự án:
- Mức can thiệp C2O hiện có, chỉ ghi nếu ảnh hưởng bước tiếp theo; không cần chọn/lưu mode `quick / standard / deep`.
- Form factor, theme, locale, text size và data state cần xét:
- Lý do chọn phạm vi kiểm tra:

## Tiêu chí hoàn thành

| ID | Điều kiện và hành động | Kết quả cần quan sát | Phương pháp | Bắt buộc theo nguồn acceptance đã chọn |
| --- | --- | --- | --- | --- |
| C-001 | | | | [required tại nguồn] |

Nguồn acceptance đã chọn giữ ID, nghĩa, nguồn/rationale, tính bắt buộc và cách kiểm tra criterion. Bảng này dẫn các quyết định đó và mô tả scenario, không duy trì yêu cầu hoặc applicability cạnh tranh. Tiêu chí mới là đề xuất cho đến khi được xử lý trong context của nhiệm vụ; không ghi nghiên cứu hoặc test là đã thực hiện nếu chưa có evidence.

## Quyết định còn mở

Chỉ ghi quyết định có thể thay đổi bước tiếp theo; lựa chọn tạm thời, lý do và cách kiểm tra nếu cần.

## Kiểm tra trước bàn giao

- [ ] Outcome nêu actor, task, context và kết quả có thể quan sát.
- [ ] Scope nhiệm vụ là phần được giao, nhất quán với scope sản phẩm và không tự mở rộng sang phần hoãn lại.
- [ ] Điều đã biết, giả định và việc cần thử có nguồn hoặc cách làm rõ riêng.
- [ ] Criterion ID, ý nghĩa và tính bắt buộc đối chiếu đúng nguồn acceptance đã chọn; tiêu chí đề xuất chưa được trình bày là đã thông qua hay đã đạt.
- [ ] Platform/mức can thiệp hiện có, biến thể cần xét và quyết định đang cản bước tiếp theo được nêu đúng mức cần thiết.
