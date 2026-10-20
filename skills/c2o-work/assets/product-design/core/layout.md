# Đề xuất và kiểm tra bố cục

**C2O Design v1.2.0.** Dùng trong Design để sắp xếp nội dung và tương tác. Proposal có thể là bảng vùng, wireframe, mockup hoặc prototype tùy câu hỏi. Tái sử dụng proposal/baseline phù hợp. [Catalog bố cục](../catalog/layout-patterns.md) cung cấp 10 mẫu ban đầu; [UI composition](ui-composition.md) hướng dẫn ghép với data view và component.

## 1. Constraints trước hình thức

Đọc task/criterion, domain, flow và state trong experience contract. Ghi nội dung thiết yếu, hành động, platform, không gian cửa sổ, text size, input và những constraints thực sự áp dụng. Chọn dữ liệu đủ thật: tên dài, nhiều/ít item, thiếu ảnh hoặc lỗi nếu chúng ảnh hưởng flow.

Xác định phần phải thấy hoặc thao tác được tại thời điểm nào. Không mặc định mọi thứ phải nằm trên màn đầu, mọi dashboard cần KPI lớn, hoặc mọi màn phải có cùng loại hero. Khi không đủ chỗ, ưu tiên theo task và khả năng tìm lại thông tin.

## 2. Đề xuất các vùng

Mỗi vùng ghi vai trò, nội dung, mức ưu tiên, hành động và liên hệ với vùng khác. Tham chiếu `DV-*` cho hợp đồng dữ liệu và `CMP-*` cho component khi có; giữ định nghĩa dữ liệu/hành vi ở tài liệu canonical, không sao lại thành nhiều nguồn chuẩn. `LP-*` là mẫu catalog; `L-*` là proposal áp dụng trong dự án. Làm rõ:

- Thứ tự đọc và thứ tự thao tác; nơi người dùng biết đang xem đối tượng nào.
- Navigation, hành động chính/phụ và phản hồi sau thao tác.
- Phần cuộn, phần cố định, overlay; cách tránh che nội dung, focus hoặc thao tác khi bàn phím mở.
- Quy tắc co giãn, wrap, chiều rộng giới hạn và nhóm nội dung cần đi cùng nhau.
- State làm bố cục thay đổi: rỗng, lỗi, đang sửa, đang xử lý hoặc dữ liệu chưa đủ.

Chốt quan hệ và ràng buộc trước; lấy kích thước từ token, control nền tảng hoặc phép đo phù hợp. Giải thích thứ tự ưu tiên bằng nhiệm vụ.

## 3. Thích ứng theo không gian và nhiệm vụ

Thiết kế theo không gian thực có thể sử dụng, kể cả cửa sổ được resize, safe area, bàn phím và chữ lớn. Tên thiết bị là một phần của coverage, không thay cho quy tắc thích ứng.

Ví dụ giả định: danh sách và chi tiết cùng xuất hiện khi đủ chỗ để đọc và thao tác; không gian hẹp chuyển sang điều hướng tuần tự, vẫn giữ đối tượng đang chọn và bản nháp. Breakpoint được chọn từ giới hạn nội dung hoặc conventions nền tảng, không chỉ từ một frame đẹp.

Khi bố cục đổi, kiểm tra task, context và cách phục hồi vẫn còn. Không ép phiên bản chữ lớn hoặc cửa sổ hẹp khớp từng pixel với ảnh của phiên bản rộng.

## 4. Phối hợp layout với asset và baseline

Ghi vùng dành cho `A-01`: vai trò, tỷ lệ/cách fit, crop hoặc focal point, vùng trống cần giữ, fallback và tương tác liên quan. Nội dung chữ hoặc control cần thay đổi theo dữ liệu được triển khai thành thành phần UI thật. Ảnh mockup toàn màn chỉ dùng để thảo luận hướng, không thay một màn hình có semantics và trạng thái.

Baseline cung cấp direction, token, component behavior và reference/anchor. Dùng cùng các nguồn này cho màn tiếp theo; không để image reference tự thay tên app, navigation, ngữ nghĩa hành động hoặc dữ liệu. Một asset đẹp vẫn phải vừa vùng đã xác định và phục vụ task.

Giữ native metrics và quy tắc tương tác của platform khi mockup vẽ khác. Ghi deviation có chủ đích, lý do và criterion bị ảnh hưởng; cập nhật baseline nếu thay đổi trở thành quy tắc dùng chung.

## 5. So sánh và kiểm chứng

Nếu cần nhiều layout, đặt IDs `L-01`, `L-02` và liên kết option/decision tương ứng. Dùng cùng task, dữ liệu và fidelity theo [exploration](exploration.md). So khả năng tìm thông tin, thao tác, đọc, thích ứng và chi phí; không chọn chỉ vì một ảnh có artwork đẹp hơn.

Thông số từ mockup ghi **ước lượng**; số đo từ artifact ghi nguồn/điều kiện; phần **chưa đo** giữ rõ. Các nhãn nguồn này độc lập với trạng thái kiểm chứng của criterion trong nguồn acceptance/evidence đã chọn.

Khi có implementation, render đúng build/state và thử thao tác. Ghi viewport/device, appearance, text size và dữ liệu. Xem clipping, overlap, thứ tự focus, hit region, nội dung khi cuộn và trạng thái chưa lưu theo profile. Chỉ dùng pixel comparison khi fidelity với reference là một yêu cầu; ghi vùng không được đo và khác biệt đã chủ đích chấp nhận.

Đầu ra: constraints, vùng, adaptation, criteria/câu hỏi còn mở và decision/baseline liên quan. Ảnh đẹp chưa chứng minh flow hoàn thành được.
