# Đề xuất bố cục L-01

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-LAYOUT` |
| Phiên bản template | `1.1.0` |
| Mục đích | Đề xuất cấu trúc vùng nội dung và quy tắc thích ứng phục vụ một task trong không gian hiển thị cụ thể. |
| Dùng khi | Cần chọn hoặc thay bố cục, thứ tự đọc/thao tác, scroll hay cách giữ thông tin khi kích thước/state thay đổi. |
| Đầu vào | Screen/task, criterion, baseline/options, content/fixture, component/data view và constraints nền tảng. |
| Đầu ra / bàn giao | Proposal L với regions, ưu tiên, adaptation, asset/token refs và thông số có nguồn hoặc mức chưa biết. |
| Nguồn chuẩn | Chỉ giữ bố cục/regions/adaptation khi được đăng ký canonical; screen giữ composition, data view giữ nghĩa dữ liệu và component giữ hành vi. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Layout instance; screen/task và biến thể chi tiết tại mục Phạm vi và nguồn] |

[Chuẩn template](../documentation/template-standard.md).

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Placeholder chỉ là chỗ điền, không phải bằng chứng hay sự kiện đã xảy ra. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu theo dõi bản đã điền của dự án. Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, độc lập với trạng thái quyết định, verdict review và verification; `accepted` không tự ghi nhận phê duyệt của người dùng, kết quả kiểm chứng hoặc quyền phát hành.

## Phạm vi và nguồn

- Screen/task và criterion IDs:
- Pattern tham khảo `LP-*`; screen instance `SCR-*` khi có:
- Option `O-01`, decision `DEC-01`, baseline `B-01` liên quan:
- Platform, không gian cửa sổ và input cần xét:
- Content/dataset, state, text size, locale:
- Artifact hiện có và fidelity: mô tả / wireframe / mockup / prototype / implementation:

## Constraints

Thông tin và hành động nào cần có tại thời điểm nào? Điều gì phải giữ theo flow, platform hoặc baseline? Phần nào được cuộn, thu gọn, chuyển màn hay hoãn theo ngữ cảnh?

## Các vùng

| Vùng | Vai trò và nội dung | Data view / component | Ưu tiên / hành động | Scroll / cố định | Liên hệ vùng khác |
|---|---|---|---|---|---|
| R-01 | | DV-… / CMP-… nếu có | | | |

Mô tả thứ tự đọc/thao tác, cách nhóm, quy tắc co giãn/wrap. Data view giữ nghĩa/scope của dữ liệu; component giữ trách nhiệm và events; màn giữ composition cùng các owner liên quan. Dẫn tới tài liệu canonical, không sao chép toàn bộ hợp đồng vào layout. Đính kèm sketch hoặc prototype nếu cần thấy vị trí thực. Bảng vùng không tự chứng minh bố cục render đúng.

## Thích ứng và state

| Điều kiện | Bố cục thay đổi thế nào | Context/hành vi phải giữ |
|---|---|---|
| Không gian hẹp | | |
| Không gian rộng nếu áp dụng | | |
| Chữ lớn / bàn phím nếu liên quan | | |
| State làm đổi nội dung | | |

## Asset, token và reference

- Asset ID/vùng đặt; fit/crop/focal point; fallback:
- Token/component dùng lại và hành vi liên quan:
- Reference/anchor; điều lấy và deviation có chủ đích:

## Thông số và kiểm chứng

| Thông số / quan hệ | Giá trị hoặc quy tắc | Nguồn: đo / ước lượng / chưa đo | Artifact và điều kiện |
|---|---|---|---|
| | | | |

- Criterion và cách kiểm tra sau khi có artifact phù hợp:
- Overlap, clipping, scrolling, focus hoặc state cần chú ý:
- Quyết định còn mở; input cần để chốt:

Đây là proposal cho đến khi được chọn trong phạm vi nhiệm vụ. IDs không được checker tự xác minh; thông số ước lượng không biến thành phép đo thực.

## Kiểm tra trước bàn giao

- [ ] Mỗi vùng có vai trò và thứ tự đọc/thao tác, nối được tới screen, data view và component cần dùng.
- [ ] Thông tin/hành động bắt buộc, phần cuộn/thu gọn và constraints có lý do theo task.
- [ ] Thích ứng nêu cấu trúc thay đổi cùng context, dữ liệu và hành vi phải giữ.
- [ ] Thông số đo, ước lượng hoặc chưa đo được phân biệt; asset crop/fallback và token/reference có nguồn.
- [ ] Đề xuất/chọn dùng không bị nhầm với render đã kiểm chứng; overlap, clipping, focus và state cần xem lại có criterion hoặc bước tiếp theo.
