# Báo cáo kiểm chứng và critique

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-REVIEW` |
| Phiên bản template | `1.1.0` |
| Mục đích | Ghi phạm vi review, quan sát có bằng chứng, findings và verdict để biết phần nào cần sửa hoặc còn chưa thể kết luận. |
| Dùng khi | Đánh giá thiết kế hoặc implementation theo criterion đã chọn, sau thao tác/quan sát hoặc khi phải ghi giới hạn kiểm chứng. |
| Đầu vào | Artifact/build và inputs thật, nguồn acceptance đã chọn, nguồn kết quả/evidence đã chọn nếu đã có, baseline và phương pháp/coverage liên quan. |
| Đầu ra / bàn giao | Review có observations/findings/giới hạn, verdict cho scope và tham chiếu report/evidence đủ để bàn giao bước tiếp theo. |
| Nguồn chuẩn | Chỉ giữ review verdict khi được đăng ký canonical cho scope, hoặc giữ quan sát chi tiết khi được đăng ký làm evidence; acceptance và kết quả theo criterion tiếp tục thuộc nguồn đã chọn của C2O/dự án. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Scope review; artifact/revision, tiêu chí và biến thể chi tiết tại mục Scope và môi trường] |

[Chuẩn template](../documentation/template-standard.md).

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Placeholder chỉ là chỗ điền, không phải bằng chứng hay sự kiện đã xảy ra. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu theo dõi bản đã điền của dự án. Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, độc lập với trạng thái quyết định, verdict review và verification; `accepted` không tự ghi nhận phê duyệt của người dùng, kết quả kiểm chứng hoặc quyền phát hành.

## Scope và môi trường

- Phiên bản/build hoặc input được kiểm tra:
- Platform/OS/device/viewport:
- Theme/text size/locale/dataset:
- Ngày và người/phương pháp kiểm tra:
- Criteria và tài liệu nguồn:
- Baseline/revision, layout và asset files có ảnh hưởng:
- Với screenshot diff: vùng đã đo/ngoài ảnh, masks/alignment/crop, checks bị skip và khác biệt có chủ đích:

## Kết quả theo tiêu chí

Nguồn acceptance đã chọn giữ criterion ID/nghĩa/tính bắt buộc; nguồn kết quả/evidence đã chọn giữ kết quả, rationale, artifact/revision và evidence refs hiện hành. Bảng dưới là summary/reference đến record nguồn, không giữ bộ trạng thái thứ hai. Khi review này được đăng ký làm evidence, ghi quan sát chi tiết cùng phạm vi ở đây và để nguồn kết quả/evidence đã chọn tham chiếu đúng artifact/revision hoặc observation; hash chỉ cần theo profile đã chọn; không chép cùng quan sát thành một nguồn cạnh tranh.

| ID | Record verification / trạng thái tại nguồn | Phương pháp và bước đã thực hiện | Quan sát / evidence ref | File bằng chứng |
| --- | --- | --- | --- | --- |
| [criterion ID thật] | [nguồn kết quả/evidence đã chọn → record theo ID criterion; đọc trạng thái tại nguồn] | [bước đã làm hoặc ref] | [tóm tắt có giới hạn hoặc vị trí quan sát chi tiết] | [file/revision] |

Chưa thực hiện hoặc thiếu điều kiện kiểm tra giữ `not-tested` cùng lý do ở nguồn kết quả đã chọn. Có evidence một phần giữ `partial`; lỗi đã quan sát giữ `fail`. Bảng tham chiếu này không tự xác nhận kiểm tra đã chạy.

## Findings

| ID | Severity | Vị trí/state | Quan sát | Ảnh hưởng lên nhiệm vụ | Cách sửa/kiểm tra lại |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Cho phép không có finding. Phân biệt defect với suggestion. Nhận xét về render hoặc tương tác phải dựa vào artifact/thao tác thật.

## Verdict cho scope

Dùng verdict tổng hợp C2O `pass / partial / fail / insufficient-evidence` theo contract và evidence hiện hành; criterion chưa kiểm tra giữ `not-tested` ở nguồn kết quả. Nếu dùng nhãn critique cũ `ready / rework / blocked`, ghi đó là khuyến nghị cục bộ, không thay verdict C2O. Giữ riêng tiến độ review, kết quả artifact và external delivery: review có thể hoàn thành khi subject fail. Review-only báo finding mà không sửa artifact; production chỉ sửa trong scope/quyền đã có. Verdict không cấp quyền publish/deploy.

## Giới hạn cụ thể

Những biến thể chưa chạy, công cụ không hoạt động hoặc điều không thể suy ra từ bằng chứng hiện có. Không biến giới hạn của công cụ thành lỗi của sản phẩm khi chưa có quan sát tương ứng.

## Quyết định hoặc bài học dùng lại

Chỉ ghi điều có khả năng ảnh hưởng lần làm tiếp theo và liên kết đến nơi duy trì context chính.

## Kiểm tra trước bàn giao

- [ ] Artifact/build, inputs, fixture, môi trường và thời điểm kiểm tra được nhận diện đúng phạm vi.
- [ ] Phương pháp/bước chỉ ghi việc đã thực hiện; skip, biến thể chưa chạy và giới hạn suy luận được nêu rõ.
- [ ] Bảng criterion dẫn tới nguồn kết quả/evidence đã chọn; nếu tài liệu giữ evidence chi tiết thì đã ghi vai trò/nguồn, không có status truth thứ hai.
- [ ] Finding có quan sát, vị trí/state, tác động và cách kiểm tra lại; defect được tách khỏi suggestion.
- [ ] Verdict phù hợp scope và evidence, nêu bước tiếp theo; document status/review verdict không suy thành authorization hay pass toàn sản phẩm.
