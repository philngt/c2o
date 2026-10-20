# Business design — [tên sản phẩm]

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-BUSINESS-DESIGN` |
| Phiên bản template | `1.1.0` |
| Mục đích | Làm rõ ai nhận giá trị, ai quyết định sử dụng, ai trả tiền, cách tiếp cận họ và điều kiện để tiếp tục đầu tư. |
| Dùng khi | Sản phẩm mới hoặc thay phân khúc, phân phối, mô hình thu tiền; quyết định đang phụ thuộc giả định kinh doanh quan trọng. Dự án cá nhân/nội bộ có thể dùng một trang, không bắt buộc doanh thu. |
| Đầu vào | [Brief](../brief.md), bằng chứng nhu cầu/hành vi, ràng buộc nguồn lực và mô hình kinh doanh hiện có nếu áp dụng. |
| Đầu ra / bàn giao | Mô hình giá trị, giả định cần kiểm tra, điều kiện quyết định và hệ quả để bàn giao sang [PRD](prd.md), [validation plan](validation-plan.md) và slice phù hợp. |
| Nguồn chuẩn | Khi được đăng ký, tài liệu này giữ mô hình giá trị và giả định kinh doanh. PRD giữ yêu cầu/phạm vi phiên bản; [domain model](domain-model.md) giữ BR; kết quả kiểm tra dẫn tới evidence và report thật. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Sản phẩm / phân khúc / phiên bản / OUT-01 và phần ngoài scope] |

[Chuẩn template](../../documentation/template-standard.md). Placeholder là chỗ cần điền, không phải bằng chứng. Phiên bản template theo dõi mẫu dùng chung; revision tài liệu theo dõi bản được điền cho dự án.

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, tách khỏi trạng thái quyết định và kết quả kiểm chứng. `accepted` nghĩa là chọn dùng tài liệu trong phạm vi quyền hạn hiện có; không chứng minh người dùng đã phê duyệt, test đã đạt hoặc có quyền phát hành.

Giữ nguồn chuẩn đã đăng ký trong [document index](document-index.md); không tự thay owner của thông tin chỉ vì sao chép template. Đọc [hướng dẫn bộ tài liệu](../../documentation/README.md) và cập nhật đường dẫn/ID mẫu thành tham chiếu thật của dự án.

## 1. Người dùng, khách hàng và người trả tiền

Một người có thể giữ nhiều vai trò. Chỉ tách vai trò khi khác nhau về nhu cầu, quyền quyết định hoặc động cơ.

| Nhóm/vai trò | Việc cần làm và bối cảnh | Ai quyết định / ai trả tiền | Khó khăn đã quan sát | Nguồn hoặc ASM-xx |
| --- | --- | --- | --- | --- |
| [nhóm cụ thể] | | | | [nguồn; ngày; giới hạn] |

- Họ đang giải quyết việc này bằng cách nào, kể cả không dùng phần mềm?
- Giá trị kỳ vọng: [kết quả giúp họ tốt hơn; tham chiếu OUT-01].
- Lý do có thể chuyển sang giải pháp này; công sức/rủi ro khi chuyển: [...].
- Nhóm hoặc nhu cầu chưa phục vụ trong phiên bản này: [...].

## 2. Tiếp cận và duy trì sử dụng

| Chặng | Lựa chọn dự kiến | Bằng chứng / giả định | Dấu hiệu cần quan sát |
| --- | --- | --- | --- |
| Biết đến sản phẩm | [kênh và người có thể tiếp cận] | | |
| Bắt đầu nhận giá trị | [điều kiện dùng thử/onboarding phù hợp] | | |
| Tiếp tục dùng | [nhu cầu lặp lại hoặc tác vụ dùng một lần] | | |

Nêu ai thực hiện việc phân phối/hỗ trợ và giới hạn nguồn lực. Với app dùng riêng, có thể ghi “cài đặt cho chính mình”; không suy diễn thành kế hoạch tăng trưởng.

## 3. Thu nhập, chi phí và điều kiện bền vững

- Mục tiêu kinh tế: [thu tiền / tiết kiệm thời gian-chi phí / sử dụng cá nhân / khác].
- Người trả tiền, thứ họ trả cho, thời điểm và đơn vị tính nếu áp dụng: [...].
- Khoảng thời gian, đơn vị tiền tệ và phạm vi tính toán: [...].

| Thành phần | Công thức hoặc giả định | Nguồn / mức chưa biết | Ngưỡng để tiếp tục hoặc xem lại |
| --- | --- | --- | --- |
| Giá và doanh thu nếu có | [số đơn vị trả tiền × giá/đơn vị/kỳ] | | |
| Chi phí cố định | [phát triển, duy trì, vận hành theo kỳ] | | |
| Chi phí biến đổi | [lượt dùng × chi phí/lượt nếu có] | | |
| Giá trị phi doanh thu nếu có | [thời gian/chi phí giảm; cách đo] | | |

Để “chưa biết” khi chưa có dữ liệu. Giá, quy mô thị trường và chi phí ước lượng phải được ghi là giả định, kèm nguồn hoặc cách kiểm tra; không điền số để làm đầy bảng.

## 4. Giả định và thử nghiệm quyết định

| ID | Mệnh đề có thể bị bác bỏ | Ảnh hưởng nếu sai | Thử nghiệm / bằng chứng cần | Ngưỡng quyết định đặt trước | Owner / thời điểm |
| --- | --- | --- | --- | --- | --- |
| ASM-01 | [nhóm nào sẽ làm gì trong điều kiện nào] | | | | |

- Kết quả thực có: [tóm tắt, ngày, link bằng chứng và giới hạn; để trống khi chưa thực hiện].
- Quyết định sau bằng chứng: [giữ / sửa / dừng giả định; lý do].
- Hệ quả cần cập nhật: [F-01 / REQ-01 trong PRD; BR-01 trong domain model; quyết định liên quan].

## Điều kiện kết thúc bản này

Đã phân biệt vai trò, giá trị và các giả định đang dùng; bất định có thể đổi quyết định đầu tư có owner và bước kiểm tra; hệ quả sản phẩm đã được dẫn sang PRD. Chỉ giải quyết các bất định cản scope hiện tại, không bắt mọi giả định phải được xác nhận trước khi làm một slice nhỏ.

## Kiểm tra trước bàn giao

- [ ] Đã phân biệt người dùng, người quyết định và người trả tiền trong phạm vi cần thiết; giá trị nối với outcome thật.
- [ ] Đã phân biệt quan sát với ASM; nguồn, ngày và giới hạn được ghi, chưa đo vẫn được giữ là chưa đo.
- [ ] Giá, chi phí hoặc giá trị phi doanh thu có đơn vị/phạm vi/căn cứ; không dùng số mẫu làm dữ kiện.
- [ ] Giả định có thể đổi quyết định hiện tại có owner, bước kiểm tra và điều kiện xem lại; không chặn slice vì bất định ngoài scope.
- [ ] Hệ quả được dẫn về PRD/domain/validation đã đăng ký; điều kiện kết thúc bên trên không bị dùng như bằng chứng thị trường hoặc quyền phát hành.
