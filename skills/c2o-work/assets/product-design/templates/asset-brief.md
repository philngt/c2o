# Asset brief

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-ASSET-BRIEF` |
| Phiên bản template | `1.1.0` |
| Mục đích | Xác định vai trò, nội dung, ràng buộc xuất và cách kiểm tra một asset trước khi tạo hoặc tích hợp. |
| Dùng khi | Cần chọn, tạo, chỉnh sửa hoặc thay asset có ảnh hưởng tới một vùng UI hay outcome của nhiệm vụ. |
| Đầu vào | Brief nhiệm vụ, baseline đang dùng, layout/region, asset hiện có, reference và criterion liên quan. |
| Đầu ra / bàn giao | Hợp đồng asset đủ để sản xuất và tích hợp; file nguồn/biến thể/destination cùng giới hạn kiểm chứng. |
| Nguồn chuẩn | Chỉ giữ yêu cầu của asset khi file/section này được đăng ký canonical; dẫn nguồn baseline, manifest, provenance và kết quả trong nguồn kết quả/evidence đã chọn. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Asset, vùng hiển thị, màn, platform và state thuộc nhiệm vụ] |

[Chuẩn template](../documentation/template-standard.md).

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Placeholder chỉ là chỗ điền, không phải bằng chứng hay sự kiện đã xảy ra. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu theo dõi bản đã điền của dự án. Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, độc lập với trạng thái quyết định, verdict review và verification; `accepted` không tự ghi nhận phê duyệt của người dùng, kết quả kiểm chứng hoặc quyền phát hành.

- Asset ID: A-01
- Vai trò và mục đích của asset:
- Baseline / revision, layout / region:
- Criterion liên quan:
- Route: system / existing / authored_vector / generated_raster / real_capture / other
- Source, provenance và phạm vi sử dụng:

## Hợp đồng đầu ra

| Thuộc tính | Quyết định / chưa xác định | Nguồn đo hoặc lý do |
| --- | --- | --- |
| Nội dung phải đúng; chi tiết không được suy thêm | | |
| Vùng hiển thị và aspect | | |
| Kích thước hiển thị / kích thước xuất | | |
| Alpha / nền | | |
| Focal point, crop, vùng dành cho UI | | |
| Style family, palette role, chất liệu/góc nhìn | | |
| Appearance / state / locale | | |
| Fallback, accessibility semantics | | |
| Format, destination, source giữ lại | | |
| Motion, player, Reduce Motion nếu áp dụng | | |

## Reference và prompt nếu cần

- File reference, phạm vi lấy và điều phải giữ:
- Prompt file / revision; tool/model thực dùng nếu có:
- Điều được thay đổi, điều phải giữ ngoài vùng chỉnh:
- Dự kiến số lần gọi/ngân sách đã có; điểm dừng hoặc đổi cách làm:

## Ứng viên và lựa chọn

| File ứng viên | Quan sát / số đo có scope | Vấn đề | Quyết định và lý do |
| --- | --- | --- | --- |
| | | | |

## Kiểm chứng

Ghi file source/derived, thiết bị/môi trường, kích thước thực, background/appearance và state đã xem. Tách review file độc lập khỏi kiểm tra trong app; chỉ ghi kết quả đã thực hiện. Đưa kết quả theo criterion vào nguồn kết quả/evidence đã chọn. Điểm giống reference không thay cho kiểm tra nội dung và hành vi.

## Kiểm tra trước bàn giao

- [ ] Vai trò asset, region, baseline revision và criterion được nối đúng nguồn đang áp dụng.
- [ ] Nội dung, aspect, alpha, crop, appearance và fallback được xác định hoặc đánh dấu chưa biết.
- [ ] File nguồn, biến thể, destination và provenance có tham chiếu thật; phạm vi sử dụng được ghi rõ.
- [ ] Số đo thực và ước lượng được phân biệt; phương án chọn có lý do và điểm dừng phù hợp.
- [ ] Review file và kiểm tra trong app được phân biệt; kết quả theo criterion dẫn về nguồn kết quả/evidence đã chọn, phần chưa chạy được nêu rõ.
