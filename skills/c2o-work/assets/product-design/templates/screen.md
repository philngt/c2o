# Screen contract SCR-01

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-SCREEN` |
| Phiên bản template | `1.1.0` |
| Mục đích | Giao trách nhiệm cho một màn và nối composition, state ownership, hành vi xuyên màn với các hợp đồng đang dùng. |
| Dùng khi | Tạo hoặc thay một screen/surface cần thống nhất regions, hành động, điểm đến và thích ứng theo task. |
| Đầu vào | Task/outcome, criterion, feature/experience, baseline/decision, layout và component/data view refs. |
| Đầu ra / bàn giao | Hợp đồng SCR với composition, ownership, chuyển tiếp, adaptation và coverage cần kiểm chứng trong scope. |
| Nguồn chuẩn | Chỉ giữ trách nhiệm/composition/ownership của màn khi được đăng ký canonical; layout, component, data view, domain và acceptance vẫn dẫn về nguồn riêng. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Screen instance, task, platform, input, locale và state được hỗ trợ] |

[Chuẩn template](../documentation/template-standard.md).

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Placeholder chỉ là chỗ điền, không phải bằng chứng hay sự kiện đã xảy ra. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu theo dõi bản đã điền của dự án. Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, độc lập với trạng thái quyết định, verdict review và verification; `accepted` không tự ghi nhận phê duyệt của người dùng, kết quả kiểm chứng hoặc quyền phát hành.

- Tác vụ / outcome / criterion IDs:
- Platform, không gian, input, locale và state trong scope:
- Screen pattern tham khảo SP-xx nếu hữu ích:
- Decision / baseline và revision:
- Layout instance L-01 và tài liệu đang giữ regions/adaptation:
- Artifact hiện có: mô tả / wireframe / prototype / implementation:

## Composition

| Vùng | Vai trò và dữ liệu | Data view DV-xx | Component CMP-xx | Hành động / chuyển tiếp | Criterion |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Dẫn chiếu tài liệu gốc cho từng hợp đồng; chỉ tạo component/data-view file khi có ích. ID ở đây là liên kết review, không phải schema/quan hệ được checker tự xác minh.

## State và ownership

| State | Chủ sở hữu | Trigger / thay đổi | Giữ hoặc reset khi điều hướng/thích ứng | Phục hồi |
| --- | --- | --- | --- | --- |
| Query/filter/sort/selection nếu áp dụng | | | | |
| Draft và kết quả lưu nếu áp dụng | | | | |
| Data/loading/error/permission nếu áp dụng | | | | |

Phân biệt selection, focus, trạng thái domain và trạng thái tác vụ. Ghi scope của loading/error: một field, một vùng hay cả màn. Giữ criterion bắt buộc và dữ liệu người dùng khi thay view.

## Hành vi xuyên màn

- Điểm vào, định danh đối tượng và đường quay lại:
- Action, phản hồi và điều kiện coi là hoàn thành:
- Hủy/back/đổi đối tượng khi có việc chưa lưu:
- Focus, keyboard/assistive technology và vị trí cuộn:
- Asset, fallback và reference liên quan:

## Thích ứng và kiểm chứng

- Dẫn chiếu layout rules; phần đổi cấu trúc và dữ liệu/context phải giữ:
- Thông tin bắt buộc còn truy cập được bằng đường nào:
- Coverage bắt buộc; input và bằng chứng cần tạo:
- Điều đã đo, ước lượng, chưa đo; kết quả thật và giới hạn:

`selected` của decision/baseline là lựa chọn thiết kế, không phải trạng thái tài liệu hay kết quả kiểm chứng. Kiểm tra chưa làm hoặc thiếu môi trường giữ `not-tested` cùng lý do; evidence một phần giữ `partial` theo acceptance hiện có. Không dùng bản composition này để tự gán pass cho component hoặc screen.

## Kiểm tra trước bàn giao

- [ ] Screen phục vụ task/outcome rõ và dẫn đúng feature/experience, baseline cùng criterion hiện hành.
- [ ] Mỗi vùng có vai trò, dữ liệu, hành động và refs tới layout/data view/component phù hợp.
- [ ] Query, selection, focus, draft và committed data có owner; giữ/reset khi điều hướng hoặc đổi không gian đã rõ.
- [ ] Entry/back/hủy, việc chưa lưu và đường tới thông tin bắt buộc vẫn được xử lý theo adaptation đã chọn.
- [ ] Coverage và artifact/evidence có giới hạn thật; lựa chọn thiết kế không được dùng thay kiểm chứng component hoặc màn.
