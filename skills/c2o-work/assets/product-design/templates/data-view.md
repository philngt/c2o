# Data view DV-01

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-DATA-VIEW` |
| Phiên bản template | `1.1.0` |
| Mục đích | Chọn và đặc tả cách biểu diễn dữ liệu giúp người dùng trả lời đúng câu hỏi hoặc thực hiện đúng tác vụ. |
| Dùng khi | Thiết kế hoặc đổi list, table, chart, tree, graph hay view có query, selection hoặc phạm vi dữ liệu đáng kể. |
| Đầu vào | Task/criterion, model và query nguồn, fixture, baseline/layout, platform và data state trong scope. |
| Đầu ra / bàn giao | Hợp đồng DV về biểu diễn, tương tác, phạm vi dữ liệu và cách kiểm tra các phép đọc/tính có ảnh hưởng. |
| Nguồn chuẩn | Chỉ giữ hợp đồng biểu diễn và tương tác của view khi được đăng ký canonical; nghĩa domain, model/query và phép tính dẫn về nguồn sở hữu chúng. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Data view và task; tham chiếu dataset/query, state và nền tảng tại các mục bên dưới] |

[Chuẩn template](../documentation/template-standard.md).

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Placeholder chỉ là chỗ điền, không phải bằng chứng hay sự kiện đã xảy ra. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu theo dõi bản đã điền của dự án. Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, độc lập với trạng thái quyết định, verdict review và verification; `accepted` không tự ghi nhận phê duyệt của người dùng, kết quả kiểm chứng hoặc quyền phát hành.

## Phạm vi

- Task và kết quả cần đạt; criterion IDs như `C-001`:
- Decision / baseline revision / layout region liên quan:
- Pattern `DVP-*` đang xét hoặc tái sử dụng:
- Nền tảng, input, locale và không gian hỗ trợ:
- Artifact hiện tại: mô tả / prototype / implementation:

## Hợp đồng dữ liệu

- Nguồn canonical của model/query và fixture:
- Một item/mark đại diện cho gì; ID ổn định:
- Phạm vi toàn tập, quyền, phần sau lọc và phần đã tải:
- Thời gian, timezone, thứ tự và giá trị bằng nhau:
- Phép tổng hợp, nhóm, mẫu số và nơi tính nếu có:

| Trường / quan hệ | Ý nghĩa, đơn vị, nguồn | Hiển thị / định dạng | Thiếu, unknown hoặc hạn chế quyền |
| --- | --- | --- | --- |
| | | | |

Tree/graph: thêm type/hướng/role của edge, nhiều cha/chu trình, confidence, node rời. Chart/metric: thêm kỳ đo, scale, baseline, kỳ so sánh.

## Lựa chọn biểu diễn

| Ứng viên | Cách hỗ trợ cùng task/dataset | Đánh đổi / phần chưa biết |
| --- | --- | --- |
| | | |

- Hướng chọn và lý do; điều kiện xem lại:
- Component IDs và trách nhiệm; phần do layout xử lý:
- Thông tin phải luôn nhận diện được; phần mở trong detail:
- Thích ứng khi hẹp/chữ lớn; thông tin và context cần giữ:

## Tương tác và trạng thái

| Hành động / tình huống áp dụng | Phạm vi dữ liệu và chuyển trạng thái | Focus, selection, draft / phục hồi |
| --- | --- | --- |
| Search / filter / reset | | |
| Sort / group / expand | | |
| Open / back / đổi view | | |
| Select / bulk action nếu có | | |
| Edit / save / lỗi nếu có | | |
| Initial load / refresh / tải thêm nếu có | | |
| Empty / không khớp / partial / quyền | | |

Giữ các hàng áp dụng. Ghi pagination/virtualization, phạm vi “chọn tất cả” và export. Stale/offline phụ thuộc nguồn và lời hứa sản phẩm.

## Semantics và kiểm chứng

- Native control hoặc HTML semantics; lý do dùng custom interaction:
- Thứ tự đọc/focus, keyboard, tên/giá trị/trạng thái cần cung cấp:
- Cách đọc giá trị/quan hệ khi không dùng hình, màu hoặc tooltip:
- Fixture để đối chiếu ID, phép tính, missing và phạm vi truy vấn:
- Thao tác, cấu hình, state cần kiểm tra theo criterion:
- Evidence thực đã có; điều chưa đo/chưa chạy:

`DV-01`, `DVP-*`, `CMP-*` là tham chiếu review; checker không tự kiểm dữ liệu, semantics hay chuỗi ID. Ghi kết quả theo criterion trong verification report; chưa chạy giữ `not-tested`.

## Kiểm tra trước bàn giao

- [ ] Lựa chọn biểu diễn có lý do theo cùng task và cấu trúc dữ liệu cần xem.
- [ ] Identity, toàn tập, phần đã lọc/đã tải, quyền và missing/unknown được phân biệt.
- [ ] Đơn vị, thời gian, tổng hợp, mẫu số và quan hệ có nguồn; số đo hoặc phép tính có cách đối chiếu.
- [ ] Search/sort/selection, phạm vi bulk action, back/đổi view và context cần giữ đã rõ theo flow.
- [ ] Semantics, cách đọc không phụ thuộc màu/tooltip, fixture và coverage liên quan có kế hoạch; kết quả thật dẫn về verification report.
