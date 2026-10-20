# Các phương án thiết kế

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-OPTIONS` |
| Phiên bản template | `1.1.0` |
| Mục đích | So sánh những phương án thiết kế thực sự khả thi theo cùng task, constraints và bằng chứng để hỗ trợ lựa chọn. |
| Dùng khi | Còn bất định có thể đổi hướng sản phẩm, experience, layout hoặc visual; có thể gộp vào brief nếu đủ rõ. |
| Đầu vào | Task/outcome, criterion, baseline, constraints và dữ liệu/state/fidelity dùng chung cho so sánh. |
| Đầu ra / bàn giao | Các option có đánh đổi, phần chưa biết, đề nghị tạm thời và decision ref hoặc thử nghiệm tiếp theo. |
| Nguồn chuẩn | Chỉ giữ mô tả option và phân tích so sánh khi được đăng ký canonical; lựa chọn có hiệu lực dẫn về decision/baseline, acceptance giữ ở nguồn acceptance đã chọn. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Câu hỏi lựa chọn, tầng thiết kế, task, options và constraints cần so sánh] |

[Chuẩn template](../documentation/template-standard.md).

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Placeholder chỉ là chỗ điền, không phải bằng chứng hay sự kiện đã xảy ra. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu theo dõi bản đã điền của dự án. Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, độc lập với trạng thái quyết định, verdict review và verification; `accepted` không tự ghi nhận phê duyệt của người dùng, kết quả kiểm chứng hoặc quyền phát hành.

Có thể gộp nội dung này vào brief và đăng ký section nguồn chuẩn. Lặp phần phương án theo nhu cầu; không có số lượng bắt buộc.

## Câu hỏi cần quyết định

- Task/outcome và criterion IDs, ví dụ `C-001`:
- Tầng đang so sánh: product / experience / layout / visual:
- Constraints phải giữ; baseline hiện tại nếu có:
- Điều muốn cải thiện và lý do cần xét lựa chọn khác:
- Dữ liệu, state và fidelity chung để so sánh:

## Phương án O-01

- Ý tưởng chính và cách hoàn thành task:
- Khác biệt có ý nghĩa so với phương án hiện tại/các lựa chọn khác:
- Layout `L-01`, asset `A-01`, reference hoặc artifact liên quan:
- Lợi ích dự kiến; chi phí và đánh đổi:
- Điều đã quan sát; giả định chưa thử; câu hỏi có thể bác bỏ phương án:

Reference: ghi nguồn, khía cạnh tham khảo và giới hạn. Đây là input, chưa phải chứng cứ hành vi người dùng.

## So sánh

| Yếu tố | Kết luận theo option ID | Căn cứ / điều chưa biết |
|---|---|---|
| Constraints bắt buộc | | |
| Hiệu quả với task | | |
| Khả năng đọc, thao tác, phục hồi | | |
| Thích ứng platform và nhất quán | | |
| Chi phí triển khai, duy trì | | |

Chọn các hàng liên quan; thêm tiêu chí riêng khi cần. Tách nhận xét chuyên môn khỏi dữ liệu nghiên cứu thật. Không lấy điểm visual bù yêu cầu bắt buộc.

## Kết luận tạm thời

- Option được đề nghị và lý do:
- Tradeoff; điều kiện khiến đề nghị đổi:
- Thử nghiệm nhỏ tiếp theo nếu chưa đủ rõ:
- Decision ID hoặc đường dẫn sau khi đã chọn:

IDs dùng để dẫn chiếu; checker chưa kiểm tra so sánh. Không ghi nghiên cứu/kiểm thử chưa thực hiện là đã đạt.

## Kiểm tra trước bàn giao

- [ ] Câu hỏi cần quyết định và những constraints bắt buộc được nêu rõ.
- [ ] Các option là lựa chọn thực, được so sánh trên task, dữ liệu, state và fidelity phù hợp.
- [ ] Lợi ích, chi phí, trade-off và phần chưa biết có lý do; điểm visual không bù yêu cầu bắt buộc.
- [ ] Quan sát, nhận xét chuyên môn và giả định/nghiên cứu chưa thực hiện được phân biệt.
- [ ] Đề nghị có điều kiện xem lại và decision ref hoặc thử nghiệm nhỏ tiếp theo; không tạo số phương án hay gate phê duyệt bắt buộc.
