# Hướng hình ảnh

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-DESIGN-DIRECTION` |
| Phiên bản template | `1.1.0` |
| Mục đích | Cụ thể hóa hướng hình ảnh phục vụ task và nối các lựa chọn visual với token, component, asset và baseline. |
| Dùng khi | Cần chọn, diễn đạt hoặc điều chỉnh một hướng visual để các màn giữ cùng hierarchy và quy ước phù hợp nền tảng. |
| Đầu vào | Brief/experience, baseline và decision, layout proposals, reference và các component/data view liên quan. |
| Đầu ra / bàn giao | Hướng visual có lý do, mapping token/component/asset và các câu hỏi phải review bằng artifact phù hợp. |
| Nguồn chuẩn | Chỉ giữ lựa chọn visual được đăng ký cho file/section này; baseline chỉ ra revision áp dụng, còn hành vi và domain giữ nguồn riêng. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Hướng hình ảnh, màn đại diện, baseline revision, appearance và platform] |

[Chuẩn template](../documentation/template-standard.md).

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Placeholder chỉ là chỗ điền, không phải bằng chứng hay sự kiện đã xảy ra. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu theo dõi bản đã điền của dự án. Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, độc lập với trạng thái quyết định, verdict review và verification; `accepted` không tự ghi nhận phê duyệt của người dùng, kết quả kiểm chứng hoặc quyền phát hành.

- Baseline / revision và decision liên quan:
- Layout proposals liên quan:
- Data view, component contract và screen composition liên quan nếu cần:
- Màn/reference đại diện cho phạm vi ở hợp đồng tài liệu:

## Cơ sở lựa chọn

- Nhiệm vụ và ngữ cảnh:
- Tone và cảm giác cần tạo, cùng lý do:
- Mật độ thông tin và hierarchy:
- Existing pattern cần giữ:

## Hệ thống hình ảnh

| Thành phần | Quyết định | Tác dụng với task | Điều chỉnh theo platform |
| --- | --- | --- | --- |
| Type | | | |
| Màu theo vai trò | | | |
| Spacing/layout | | | |
| Shape/surface | | | |
| Icon/imagery | | | |
| Motion | | | |

## Mapping token và component

Nêu token semantic, component dùng lại và phần bổ sung. Giá trị brand phải được kiểm tra trong từng appearance áp dụng; không suy ra accessibility chỉ từ nguồn reference.

Chỉ định asset slots, icon family, source thật so với illustration, crop/fallback và link tới asset brief/manifest nếu có. Text, control và dữ liệu thuộc implementation. Đánh dấu số đo từ concept là ước lượng; ghi khác biệt có chủ đích khi triển khai theo nền tảng.

## Reference nếu cần

Nguồn, khía cạnh tham khảo, khía cạnh cần chuyển đổi và lý do. Ghi rõ khi reference mô tả website nhưng đầu ra là native app.

## Điều cần review bằng artifact

Người dùng nhận ra task chính; thứ tự thông tin; khả năng đọc; dấu hiệu thao tác; trạng thái thật; phù hợp với theme, nội dung dài và kích thước liên quan. Không dùng một số điểm visual tổng để thay thế các câu hỏi này.

## Kiểm tra trước bàn giao

- [ ] Tone, hierarchy và density có lý do gắn với task thay vì chỉ mô tả phong cách.
- [ ] Type, color roles, spacing, shape, imagery và motion nối được tới baseline/token/component đang dùng.
- [ ] Reference có nguồn và phạm vi chuyển đổi; concept, số đo ước lượng và render thật được phân biệt.
- [ ] Appearance, nội dung dài, text size và điều chỉnh nền tảng cần xét được nêu cụ thể.
- [ ] Asset slots/fallback và các câu hỏi review bằng artifact đã rõ; không suy accessibility hoặc hiệu quả từ điểm visual.
