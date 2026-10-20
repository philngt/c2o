# Service blueprint — [dịch vụ / flow]

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-SERVICE-BLUEPRINT` |
| Phiên bản template | `1.1.0` |
| Mục đích | Làm rõ trải nghiệm từng chặng, công việc phía sau và người nhận trách nhiệm khi bàn giao hoặc gặp lỗi dịch vụ. |
| Dùng khi | Chỉ khi hành trình đi qua nhiều kênh, tổ chức, người vận hành hoặc dịch vụ hỗ trợ; app local không có các bàn giao này có thể không cần file. |
| Đầu vào | Flow đã chọn trong [product blueprint](product-blueprint.md), actor/requirements từ [PRD](prd.md), [domain model](domain-model.md), quy trình/kênh hỗ trợ và quan sát thực có. |
| Đầu ra / bàn giao | Bản đồ frontstage/backstage, hợp đồng nhận bàn giao, recovery/escalation và câu hỏi vận hành để nối experience, technical và release/operations. |
| Nguồn chuẩn | Khi được đăng ký, file này giữ quan hệ kênh/vai trò và hợp đồng bàn giao dịch vụ. [Experience](../experience.md) giữ UI state; domain giữ ENT/BR; [technical spec](technical-spec.md) giữ cơ chế; [release/operations](release-operations.md) giữ vận hành phiên bản. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Dịch vụ / flow tên + anchor / OUT-01 / F-01 / REQ-01 và phần ngoài scope] |

[Chuẩn template](../../documentation/template-standard.md). Placeholder là chỗ cần điền, không phải bằng chứng. Phiên bản template theo dõi mẫu dùng chung; revision tài liệu theo dõi bản được điền cho dự án.

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, tách khỏi trạng thái quyết định và kết quả kiểm chứng. `accepted` nghĩa là chọn dùng tài liệu trong phạm vi quyền hạn hiện có; không chứng minh người dùng đã phê duyệt, test đã đạt hoặc có quyền phát hành.

Giữ nguồn chuẩn đã đăng ký trong [document index](document-index.md); không tự thay owner của thông tin chỉ vì sao chép template. Đọc [hướng dẫn bộ tài liệu](../../documentation/README.md) và cập nhật đường dẫn/ID mẫu thành tham chiếu thật của dự án.

**OPTIONAL.** Nếu không có bàn giao dịch vụ đáng kể, bỏ mẫu này; chỉ ghi lý do trong context/index hiện có nếu nó giúp quyết định tiếp theo, và dùng experience contract khi cần; không tạo quy trình hỗ trợ giả chỉ để điền mẫu.

## 1. Phạm vi dịch vụ

- Người bắt đầu hành trình, nhu cầu và sự kiện khởi động: [...].
- Điểm kết thúc được người dùng hiểu là hoàn tất: [...].
- Kênh hiện có / kênh dự kiến, ai sở hữu từng kênh: [...].
- Quy trình hiện tại hay đề xuất tương lai: [ghi rõ; nguồn quan sát nếu là hiện tại].
- Chặng chưa thuộc scope và trách nhiệm bên ngoài: [...].

## 2. Các chặng và công việc phía sau

Frontstage là phần người dùng tiếp xúc hoặc nhìn thấy. Backstage là công việc hỗ trợ phía sau; ghi vai trò thực hiện và hệ thống cần dùng, không mặc định mọi chặng đều tự động.

| Chặng / tên bước | Hành động người dùng + kênh | Frontstage: phản hồi thấy được | Backstage / hệ thống hỗ trợ | Người chịu trách nhiệm | Đầu ra chuyển sang chặng kế tiếp |
| --- | --- | --- | --- | --- | --- |
| [tên bước theo flow] | | | | | [ENT-01 / trạng thái / kết quả] |

Liên kết bước có UI tới `SCR-01`/experience; bước nghiệp vụ tới `BR-01`; tương tác hệ thống tới technical spec. Một thông báo “đã nhận” phải được phân biệt với việc xử lý “đã hoàn tất”.

## 3. Hợp đồng bàn giao

| Từ → đến | Trigger và điều kiện nhận | Dữ liệu/ngữ cảnh cần chuyển | Nơi giữ trạng thái chuẩn | Xác nhận đã nhận / owner tiếp theo | Giới hạn chờ nếu đã cam kết |
| --- | --- | --- | --- | --- | --- |
| [vai trò/hệ thống] | [BR-01 nếu có] | [ENT-01; trường tối thiểu; quyền truy cập] | [nguồn chuẩn] | | [nguồn cam kết hoặc chưa chốt] |

- Làm sao nhận diện cùng một yêu cầu khi đổi kênh mà không bắt người dùng kể lại?
- Nếu bên nhận không xác nhận, ai theo dõi và người dùng được thông báo ở đâu?
- Quy tắc gửi lại/trùng lặp, quyền chia sẻ dữ liệu và thay đổi trạng thái trỏ tới spec nào?

## 4. Lỗi, hỗ trợ và khôi phục

| Tình huống | Ai phát hiện / nhận hỗ trợ | Người dùng thấy và làm được gì | Owner phục hồi / đường chuyển cấp | Dữ liệu và việc đã làm cần giữ | Điều kiện đóng yêu cầu |
| --- | --- | --- | --- | --- | --- |
| [chậm, lỗi, thiếu thông tin… có áp dụng] | | | | [ENT/BR hoặc spec] | |

Chỉ ghi giờ hỗ trợ, thời gian phản hồi hoặc mức dịch vụ có người chịu trách nhiệm và căn cứ. Nếu chưa có cam kết, nêu điều còn phải quyết định; không tự thêm hỗ trợ 24/7 hoặc SLA.

## 5. Đo lường và kiểm tra các bàn giao

| Câu hỏi / rủi ro | Chỉ số hoặc quan sát cần | Nguồn / cách kiểm tra | Mục tiêu dự kiến | Owner / criterion nếu áp dụng |
| --- | --- | --- | --- | --- |
| [bàn giao có bị bỏ sót? người dùng biết trạng thái?] | | | | [validation plan; C-/APP-/… đang có] |

Ghi kết quả thật trong báo cáo/evidence được dẫn từ [validation plan](validation-plan.md), kèm giới hạn. Một bảng quy trình hoàn chỉnh chưa chứng minh thời gian xử lý hoặc chất lượng hỗ trợ thực tế.

## Điều kiện kết thúc bản này

Mỗi bàn giao trong scope có bên nhận, dữ liệu cần, nguồn trạng thái và cách phục hồi; người dùng có đường biết kết quả hoặc tìm hỗ trợ; phần chưa có owner/cam kết được đánh dấu với tác động đến triển khai. Nếu phân tích cho thấy không có bàn giao dịch vụ đáng kể, dừng ở experience contract và ghi lý do không áp dụng.

## Kiểm tra trước bàn giao

- [ ] Đã xác định vì sao cần service blueprint; trạng thái hiện tại và phương án tương lai được phân biệt.
- [ ] Mỗi bàn giao có trigger, bên nhận, dữ liệu tối thiểu, nguồn trạng thái và cách xác nhận trách nhiệm.
- [ ] Đã phân biệt đã nhận với đã hoàn tất; người dùng có đường biết trạng thái và phục hồi khi chậm/lỗi.
- [ ] Giờ hỗ trợ, thời gian chờ hoặc SLA chỉ ghi khi có căn cứ và owner; chưa cam kết được để rõ là chưa chốt.
- [ ] UI/domain/technical/operations trỏ đúng nguồn; kết quả đo dẫn tới evidence/report, không suy từ bảng quy trình.
