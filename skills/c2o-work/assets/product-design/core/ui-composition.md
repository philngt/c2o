# Ghép giao diện từ tác vụ, dữ liệu và các phần tái sử dụng

**C2O Design v1.2.0.** Module này dùng trong Design của workflow hiện có. Nó cụ thể hóa Experience, Visual và Platform, rồi nối tới Evidence; không tạo thêm một lớp sản phẩm hoặc một quy trình phê duyệt.

## Các khái niệm và quan hệ

| Khái niệm | Trách nhiệm | Ví dụ |
| --- | --- | --- |
| Foundations / tokens | Vai trò chữ, màu, spacing, shape, motion và quy tắc thích ứng | text.secondary, action.destructive; mapping theo nền tảng |
| Component | Đơn vị có hợp đồng nội dung, semantics, trạng thái và sự kiện | Button, field, record row, status label |
| Interaction pattern | Phối hợp thành phần để thực hiện một ý định | Search + filter + results; sửa với draft và xử lý lỗi |
| Data view | Cách trình bày một tập/đối tượng/quan hệ để trả lời câu hỏi | List, table, timeline, graph, chart |
| Layout pattern | Cách tổ chức vùng, thứ tự, kích thước và scroll | Một cột, list–detail, canvas + inspector |
| Screen composition | Một màn hoặc workspace hoàn thành nhiệm vụ cụ thể | Chọn cá thể cây rồi sửa vị trí và lưu |

Các khái niệm là những góc nhìn có thể chồng lên nhau. Data table có thể được triển khai thành một composite component; list–detail là cách ghép vùng và điều hướng. Card là container/component, card grid có thêm quy tắc biểu diễn bộ sưu tập, còn CSS grid là cơ chế bố trí. Tên gọi không quyết định semantics hoặc mô hình keyboard.

Một màn tốt cần nối được **tác vụ → dữ liệu → cách biểu diễn/tương tác → vùng bố cục → component → kết quả**. Đây là liên kết để suy nghĩ và review, không phải lệnh bắt tạo các file theo thứ tự cứng. Có thể bắt đầu từ một màn đã hoạt động và chỉ sửa mắt xích chưa phù hợp.

## Chọn và ghép

1. Đọc task, actor, data ownership và acceptance. Nêu người dùng cần đọc chính xác, tìm, so sánh, theo dõi thay đổi, hiểu quan hệ hay chỉnh sửa điều gì.
2. Xác định đối tượng, ID, trường và ý nghĩa dữ liệu. Theo [data views](data-views.md), phân biệt không có record, không có kết quả lọc, giá trị chưa biết và lỗi đọc.
3. Chọn cách biểu diễn từ [catalog data view](../catalog/data-view-patterns.md). Giữ những phép biến đổi cần hiểu như filter, grouping, sort và aggregation; ghi điều bị lược bỏ.
4. Chọn cách chia vùng từ [catalog layout](../catalog/layout-patterns.md). Xem không gian, input, focus, cuộn, bàn phím, safe/reserved regions và chữ lớn theo target thực.
5. Chọn hoặc thích ứng [components](components.md) đang có. Ghi event và chủ sở hữu state; tránh để component vừa gửi hành động vừa tự sửa domain data theo một luật khác.
6. Ghi [screen contract](../templates/screen.md), hoặc đặt bảng mapping tương đương trong layout/spec hiện có. Dùng [screen patterns](../catalog/screen-patterns.md) làm điểm khởi đầu theo tác vụ.
7. Kiểm tra các chuyển tiếp bằng prototype/implementation phù hợp. Màn đẹp riêng lẻ chưa chứng minh selection, draft, filter hoặc focus còn đúng khi chuyển màn.

Nhánh [exploration](exploration.md) giải quyết lựa chọn còn bất định. [Baseline](baseline.md) giữ hướng đã chọn; [assets](assets.md) chỉ xử lý hình ảnh cần thiết. Không thêm chart, card, tab hoặc hero khi chưa có trách nhiệm rõ.

## Hợp đồng ghép của một màn

| Cần chỉ rõ | Câu hỏi kiểm tra |
| --- | --- |
| Vùng và dữ liệu | Vùng đang đọc tập nào, đối tượng nào, thời điểm nào? Kết quả là toàn bộ hay một phần? |
| Component và quyền sở hữu | Ai giữ query, selection, draft, sort và trạng thái lưu? Component phát event nào? |
| Sự kiện và kết quả | Chọn hàng chỉ đổi selection hay mở chi tiết? Lưu commit điều gì? Hủy trả về đâu? |
| Thông tin chung | Cùng ID, terminology, unit, status và source được giữ qua các view thế nào? |
| Adaptation | Khi đổi cấu trúc, tác vụ và thông tin bắt buộc còn dùng được bằng đường nào? |
| Evidence | Criterion nào cần render, thao tác, đối chiếu dữ liệu hoặc thử với người dùng? |

Query và sort là trạng thái của view; draft là dữ liệu đang sửa; trạng thái domain như “đã đóng gói” thuộc record. Chúng có thể cùng xuất hiện và cần owner riêng. Một lỗi ảnh không nhất thiết biến cả màn thành error; một lần refresh không được tự xóa draft. Chốt các quy tắc này theo mô hình của dự án.

## Catalog khác với instance trong dự án

| Catalog tham khảo | Instance được chọn | Nội dung cần liên kết |
| --- | --- | --- |
| CP-xx: component family | CMP-01 | Hợp đồng và implementation thật của dự án |
| DVP-xx: kiểu data view | DV-01 | Dataset, phép biến đổi, tương tác và giới hạn |
| LP-xx: layout pattern | L-01 | Các vùng và quy tắc adaptation của màn |
| SP-xx: screen pattern | SCR-01 | Task, composition và chuyển tiếp cụ thể |

IDs chỉ là gợi ý. Dùng tên đang có của dự án nếu rõ hơn. Catalog không phải component library đã cài, API được bảo đảm, schema hay lệnh agent tự thực thi. Checker của profile JSON tùy chọn chỉ kiểm tra project/verification JSON cùng hash được khai báo; các liên kết composition do người/agent review.

## Kiểm tra nhất quán khi ghép nhiều màn

Giữ ý nghĩa của action và dữ liệu: cùng “Lưu” phải có cùng lời hứa về persistence trong phạm vi liên quan; cùng status không đổi ý nghĩa khi đổi màu hoặc view. Giữ selection bằng ID, không dựa vào vị trí hàng sau sort/filter. Ghi việc mở/đóng panel, quay lại, đổi cửa sổ và lỗi sẽ tác động tới context ra sao.

Tái sử dụng component khi hợp đồng phù hợp. Tạo variant khi cùng trách nhiệm nhưng cần biến thể có tên và giới hạn rõ. Tạo component/pattern mới khi semantics hoặc hành vi khác đáng kể; ghi lý do, rồi dùng [evidence contract](evidence.md) kiểm chứng phần thay đổi.

## Bằng chứng và nguồn tham khảo

Sơ đồ tổ chức module và các catalog là đề xuất của C2O Design, không phải chuẩn chung đã chứng minh qua benchmark. Quy tắc về web semantics/keyboard đối chiếu [W3C APG](https://www.w3.org/WAI/ARIA/apg/), đặc biệt [table](https://www.w3.org/WAI/ARIA/apg/patterns/table/) và [grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/). Native dùng profile và API của target thực, không chuyển nguyên ARIA sang SwiftUI.
