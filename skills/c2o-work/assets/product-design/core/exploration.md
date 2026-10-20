# Khám phá và lựa chọn phương án

**C2O Design v1.1.0.** Explore → Compare → Decide là nhóm hoạt động tham khảo cho lựa chọn có thể thay đổi đáng kể trải nghiệm, dùng trong `c2o-decide` hoặc `c2o-create` và [vòng làm việc C2O hiện có](workflow.md). Không thêm stage, yêu cầu ba phương án hoặc quyết định lại khi hướng hiện tại đã đủ căn cứ. Thực hiện theo D01, D04, D08 và D12 trong [nguyên tắc](principles.md).

## Khi nào dùng

Dùng cho app mới chưa rõ hướng, flow có nhiều cách giải quyết, hoặc baseline không còn phù hợp. Chỉnh sửa hẹp có thể ghi lựa chọn ngay trong tài liệu đang dùng. Không bắt nhiều phương án hay một file mỗi bước.

## Explore — làm rõ lựa chọn

Ghi câu hỏi cần quyết định, task/criterion liên quan, constraints bắt buộc và điều chưa biết. Xác định đang so sánh ở tầng nào:

| Tầng | Điều thay đổi giữa các phương án |
|---|---|
| Product | Người dùng được phục vụ, việc cần hoàn thành, giá trị hoặc phạm vi sản phẩm. Thay đổi này được xử lý trong `c2o-shape`/`c2o-spec`, brief và quyền hiện có; không mở stage riêng. |
| Experience | Cách hoàn thành cùng nhiệm vụ: tìm kiếm, duyệt, thao tác trực tiếp, trình tự hoặc navigation. |
| Layout | Cách phân vùng, nhóm thông tin, ưu tiên hành động và thích ứng không gian cho flow đã xác định. |
| Visual | Type, màu, hình ảnh, vật liệu, shape và motion thể hiện cùng trải nghiệm. |

Ghi các tầng thay đổi để tránh quy kết lợi ích của flow cho màu sắc. Thay palette là biến thể visual. Đổi nhiệm vụ cần cập nhật brief trước khi so layout.

Mỗi phương án có ID, ý tưởng chính, cách phục vụ task, đánh đổi, giả định và artifact đủ để xem xét. Dùng `O-01`, `L-01`, `A-01` hoặc IDs của dự án. Không tạo lựa chọn yếu có chủ đích để làm phương án ưa thích nổi bật.

## Compare — giữ điều kiện tương đương

Cho các lựa chọn thực hiện cùng task, dùng cùng dữ liệu và những state ảnh hưởng đến quyết định. Giữ mức fidelity tương đương: wireframe có cùng nội dung, hoặc prototype có cùng tương tác cần xét. Một bên có artwork hoàn thiện và một bên còn placeholder sẽ làm khó việc so sánh cấu trúc.

Reference là input: ghi nguồn, khía cạnh tham khảo và điều chỉnh theo platform. Ảnh, phân tích đối thủ hay persona suy luận chưa phải nghiên cứu người dùng; nghiên cứu thực cần phương pháp và giới hạn riêng.

Đánh giá theo thứ tự:

1. Kiểm tra constraints bắt buộc: dữ liệu, hành vi, accessibility và platform của task.
2. So những khác biệt có ý nghĩa: khả năng tìm/thao tác, hiểu thông tin, phục hồi lỗi, phù hợp thương hiệu, chi phí triển khai và duy trì.
3. Tách quan sát từ artifact, suy luận, giả định chưa thử và sở thích. Nêu mức bất định bằng lý do cụ thể.

Không dùng điểm tổng bù yêu cầu bắt buộc bị vi phạm. Scoring để thảo luận cần căn cứ, chưa chứng minh phương án tốt hơn. Nếu evidence chưa phân biệt được lựa chọn, thử câu hỏi nhỏ nhất có thể thay đổi quyết định.

## Decide — chọn trong phạm vi đã giao

Ghi `DEC-01`: chọn option nào, vì sao, vì sao không chọn các option còn lại, đánh đổi chấp nhận, điều chưa rõ và điều kiện xem lại. Quyết định nhỏ có thể đảo ngược được agent xử lý theo quyền hạn hiện có. Chỉ hỏi người dùng khi lựa chọn quan trọng chưa được quyết định bởi context hoặc thử nghiệm phù hợp; không thêm vòng duyệt từng ảnh mặc định.

Chuyển hướng đã chọn thành [baseline](baseline.md): liên kết decision, layout, direction, token/component và asset/reference cần giữ. Ảnh anchor đi cùng hợp đồng hành vi và token; không quyết định mọi chi tiết của màn sau. Ghi khác biệt có chủ đích khi platform, dữ liệu hoặc chữ lớn đòi hỏi thích ứng.

`selected` mô tả quyết định, không chứng minh implementation hay nghiên cứu đã đạt. Kết quả kiểm chứng dùng [evidence contract](evidence.md). Các ID ở đây là liên kết dễ đọc; checker hiện tại không tự xác minh chuỗi option → decision → baseline.
