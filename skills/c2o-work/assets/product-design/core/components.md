# Component: lựa chọn, hợp đồng và kiểm chứng

**C2O Design v1.2.0.** Component là đơn vị UI có trách nhiệm/hành vi xác định. Module hướng dẫn chọn và đặc tả trong năm lớp hiện có; chưa cung cấp code SwiftUI/React. Dùng [catalog](../catalog/components.md), [mẫu](../templates/component.md) và profile [SwiftUI](../profiles/swiftui.md)/[web](../profiles/web.md).

## 1. Xác định trách nhiệm trước hình thức

Chọn theo việc cần đọc, nhập, chọn, điều hướng hay hành động. Surface có góc bo chưa xác định được tương tác; badge “quá hạn” không tự thành control thay trạng thái.

Component có thể là field hoặc tổ hợp như bộ lọc. Data view mô tả cách biểu diễn dữ liệu; layout sắp xếp không gian. Bảng có thể là data view, được triển khai bằng composite component. Ghi rõ quyết định đang mô tả; các cách gọi này có thể giao nhau.

| Lựa chọn | Dùng khi | Điều cần giữ |
| --- | --- | --- |
| Reuse | Component hiện có đáp ứng cùng semantics, data và behavior. | Đọc hợp đồng, variants và evidence liên quan trước khi dùng. |
| Variant | Cùng trách nhiệm, cần khác appearance, density hoặc kích thước có lý do. | Giữ hành vi chung; nêu phạm vi thay đổi và kiểm tra lại. |
| Compose | Có thể ghép các phần đang hoạt động để giải quyết tác vụ mới. | Xác định ownership của state, focus và sự kiện giữa các phần. |
| Tạo mới | Thành phần hiện có không đáp ứng yêu cầu thực. | Giải thích khoảng trống; triển khai semantics, state và adaptation tương ứng. |

Nếu variants có cờ mâu thuẫn hoặc khác trách nhiệm, xem lại ranh giới component. Kiến trúc/code theo dự án; không áp một props API hoặc state management chung.

## 2. Hợp đồng tối thiểu

Ghi đủ để triển khai và đánh giá; việc nhỏ dùng spec đang có.

| Mục | Câu hỏi phải trả lời |
| --- | --- |
| Purpose và scope | Thành phần giúp hoàn thành việc gì; dùng ở đâu; criterion nào liên quan? |
| Semantics | Là nội dung, navigation, input hay action? Tên, giá trị, trạng thái truy cập là gì? |
| Anatomy | Các phần bắt buộc/tùy chọn; thứ tự; vùng tương tác; phần có thể thay nội dung. |
| Data | ID/value, định dạng, đơn vị, null/unknown, giới hạn và nguồn chân thực của giá trị. |
| Events | Tác động của chọn, đổi giá trị, submit, cancel; ai xử lý và khi nào commit? |
| States | Trạng thái áp dụng, tổ hợp hợp lệ, chuyển trạng thái, lỗi và phục hồi. |
| Adaptation | Wrap, co giãn, nội dung dài, input và appearance theo phạm vi. |
| Tokens/assets | Vai trò semantic, reference/baseline và trách nhiệm của asset. |

Data/props/events mô tả ý nghĩa; API cụ thể theo implementation. Component trình bày không tự suy nghiệp vụ, nguồn gốc cây hoặc thành công persistence từ màu/animation.

## 3. Các chiều trạng thái có thể cùng tồn tại

| Chiều | Ví dụ | Cần quyết định |
| --- | --- | --- |
| Tương tác | Focus, hover, pressed, expanded, checked/selected. | Phản hồi và cách nhập phù hợp platform. Hover không là đường duy nhất để biết hay thực hiện hành động. |
| Khả năng thao tác | Enabled, disabled, read-only. | Người dùng còn đọc/copy/focus được gì; điều kiện để thao tác và lý do nếu cần. |
| Dữ liệu/tác vụ | Empty, loading, refreshing, dirty, saving, error. | Nội dung giữ lại, chống gửi trùng, retry/cancel và quyền sở hữu draft. |
| Nghiệp vụ | Quá hạn, đã đóng gói, chưa xác minh nguồn. | Giá trị theo model/rule đã chốt; cách giải thích và hành động phù hợp. |

Một field có thể vừa focus vừa invalid; danh sách còn dữ liệu khi refresh lỗi. Chọn state/tổ hợp ảnh hưởng tác vụ, không ép mọi component có đủ mọi state.

Ví dụ lưu: nhận yêu cầu → đang ghi → thành công/thất bại. UI báo thành công sau commit; lỗi giữ draft và cho retry. Component phát ý định; tầng sở hữu dữ liệu cấp kết quả/state trở lại. Đây là phân chia trách nhiệm đề xuất, chưa có implementation.

## 4. Hành vi đi cùng semantics

Với web, button kích hoạt hành động; link tham chiếu/đi tới tài nguyên. Chọn phần tử native phù hợp. Đổi màu giống link không làm một action có cùng semantics với navigation. ARIA không tự thêm keyboard behavior; custom component phải thực hiện hành vi đã hứa. [S1–S3]

Ghi điểm focus sau khi mở/đóng overlay, thay selection, gửi form hoặc báo lỗi. Modal cần quản lý focus bên trong và trả focus về chỗ hợp lý khi kết thúc; không đánh dấu modal nếu nền vẫn tương tác như bình thường. Chuyển quy tắc này sang native bằng cơ chế nền tảng, không sao ARIA sang SwiftUI. [S4]

Row/card nhiều action phải xác định vùng mở chi tiết và nút phụ; tránh tương tác lồng nhau mơ hồ. Gesture/kéo thả cần cách thực hiện phù hợp các input và khả năng tiếp cận đã hỗ trợ.

## 5. Nhất quán và kiểm chứng

Dùng token theo vai trò, cùng ngữ nghĩa hành động và quy tắc trạng thái của [baseline](baseline.md). Mỗi appearance/density là lựa chọn có phạm vi. Kích thước control, vùng bấm và hit testing được chọn theo platform/context thực; không áp một số đo chung cho mọi component.

Kiểm tra content, semantics và transition trong component, rồi kiểm tra khi ghép vào [layout](layout.md): focus có bị che, label có wrap, lỗi có giữ input, selection có trỏ đúng record không? Render riêng giúp thấy một phần; flow thực mới cho thấy sự phối hợp.

Catalog dùng `CP-xx`; component dự án dùng `CMP-xx`, liên kết baseline, màn/vùng, criterion và artifact. IDs do người/agent review, checker chưa tự xác minh. Chỉ ghi `pass` theo acceptance hiện có và [hướng dẫn evidence](evidence.md) sau quan sát phù hợp; spec không chứng minh implementation đạt.

## Nguồn hành vi web

Đọc ngày 20/10/2026. APG là tham khảo cho web; chọn profile/SDK thực cho native.

- [S1 — W3C APG: Button](https://www.w3.org/WAI/ARIA/apg/patterns/button/)
- [S2 — W3C APG: Link](https://www.w3.org/WAI/ARIA/apg/patterns/link/)
- [S3 — W3C APG: Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)
- [S4 — W3C APG: Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
