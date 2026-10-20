# Nguyên tắc C2O Design

## Mục đích

Biến một nhu cầu sản phẩm thành giao diện có thể sử dụng, triển khai và kiểm chứng trong hoàn cảnh thực. Dùng cùng một cách suy nghĩ giữa các dự án, đồng thời cho phép mỗi sản phẩm có phong cách và hành vi phù hợp.

Các mã D01–D12 là điểm tham chiếu ổn định cho hướng dẫn thiết kế tùy chọn. Profile và checklist giải thích cách áp dụng. Trong C2O, [outcome contract](../../../references/outcome-contract.md), chỉ dẫn người dùng, quyết định dự án và nguồn acceptance/evidence đã chọn tiếp tục giữ thẩm quyền; nguyên tắc này không tự tạo yêu cầu, workflow hoặc nguồn chuẩn cạnh tranh. Chỉ dùng phần liên quan đến tác vụ.

## D01. Bắt đầu từ việc người dùng cần hoàn thành

Mô tả actor, nhiệm vụ, hoàn cảnh, khó khăn hiện tại và kết quả quan sát được. Đọc dữ liệu, cấu trúc và quy ước đang có trước khi đặt mood hoặc chọn layout. Phân biệt sự thật, giả định và điều cần thử nghiệm; không biến persona do agent suy luận thành nghiên cứu đã thực hiện.

Ví dụ: “Tìm đúng cây và sửa vị trí lưu trong khi mất mạng” tạo ra yêu cầu khác với “thiết kế màn hình quản lý cây sang trọng”.

## D02. Tôn trọng cấu trúc sản phẩm đã hoạt động

Trước khi tạo mới, tìm component, flow, token, copy và tài liệu hiện có. Mở rộng chúng khi còn phù hợp. Chỉ thay nền tảng hoặc cấu trúc thông tin khi nhiệm vụ cung cấp lý do đủ rõ; giữ thay đổi có thể kiểm tra và đảo ngược ở phạm vi nhỏ.

Một thiết kế mới phải giải thích được nó cải thiện nhiệm vụ nào và gây thay đổi ở đâu. “Hiện đại hơn” riêng lẻ chưa đủ để thay navigation của cả sản phẩm.

## D03. Thiết kế flow và trạng thái trước khi trang trí

Mỗi màn hình có trách nhiệm, dữ liệu đầu vào, thao tác chính, điểm đến và cách phục hồi. Liệt kê trạng thái có thể xảy ra trong flow: rỗng, có dữ liệu, đang xử lý, lỗi, ngoại tuyến, dữ liệu cũ, bị hạn chế quyền hoặc thay đổi chưa lưu. Chỉ áp dụng trạng thái tương ứng với thực tế của sản phẩm.

Một nút bấm, toast hoặc spinner phải tương ứng với thay đổi trạng thái có thật. Không báo thành công khi thao tác chưa hoàn tất; không xóa draft khi có lỗi phục hồi được.

## D04. Hierarchy phục vụ nhiệm vụ

Mức nổi bật đi theo tầm quan trọng, tần suất và thời điểm của thông tin. Có thể có một hành động chính trong một ngữ cảnh; màn hình so sánh có thể cần các mục cùng trọng lượng. Chọn mật độ và cấu trúc dựa trên dữ liệu, thiết bị và kỹ năng người dùng.

Không có tỷ lệ heading/body, số card, số màu hay lượng khoảng trắng đúng cho mọi sản phẩm. Chọn rồi kiểm tra bằng việc người dùng có tìm và hoàn thành được việc cần làm hay không.

## D05. Token theo ý nghĩa, component theo hành vi

Tách giá trị nền, vai trò semantic và nhu cầu component khi mức tái sử dụng biện minh cho việc đó. Ví dụ vai trò: nền trang, chữ phụ, hành động chính, hành động phá hủy, cảnh báo, selection. Component dùng vai trò phù hợp; token phải có cách xử lý các appearance đã hỗ trợ.

Giữ mapping nhỏ và có tên rõ. Giá trị cố định có thể hợp lệ bên trong định nghĩa token, asset, phép tính hình học hoặc yêu cầu nền tảng. Lint phục vụ quy ước của dự án; không cấm mọi số literal bằng một regex chung.

## D06. Hành vi nền tảng là điểm xuất phát

Ưu tiên control, navigation, text style, input behavior và accessibility semantics sẵn có. Tùy biến khi nhu cầu chức năng hoặc hướng thiết kế có lý do rõ. Khi thay một control, chịu trách nhiệm về hành vi tương đương, focus, gesture, keyboard, screen reader và phản hồi trạng thái.

Mapping sang SwiftUI hoặc web là một phần thiết kế, không phải dịch đơn vị px sang pt một cách máy móc.

## D07. Accessibility và nội dung tham gia từ đầu

Xác định tên dễ hiểu, thứ tự đọc/focus, target dễ thao tác, thông tin không chỉ dựa vào màu, layout thích ứng với chữ lớn và chuyển động theo lựa chọn người dùng. Dùng dữ liệu và câu chữ đủ thực để lộ vấn đề về chiều dài, ngữ nghĩa và trường hợp rỗng.

Lựa chọn theme, locale, RTL, assistive technology và form factor cần kiểm tra phải xuất phát từ phạm vi hỗ trợ. Ghi rõ lý do khi một kiểm tra không áp dụng theo hợp đồng; không dùng điều đó để bỏ yêu cầu đã cam kết hoặc một phép kiểm tra khó chạy. Chỉ profile JSON tùy chọn dùng nhãn `NOT_APPLICABLE`, với điều kiện của [evidence profile](evidence.md).

## D08. Phong cách là quyết định theo dự án

Mood, palette, type, imagery, illustration, emoji, density và motion được chọn theo người dùng, nội dung, thương hiệu và ngữ cảnh. Các lựa chọn có thể điều chỉnh khi evidence hoặc thiết bị cho thấy chúng chưa phù hợp.

Một reference là điểm neo để thảo luận về cấu trúc hoặc cảm giác. Ghi rõ điều lấy, điều chuyển đổi và điều không phù hợp. Một preset phân tích website của thương hiệu không tự trở thành guideline cho ứng dụng native.

## D09. Kiểm chứng bằng phương pháp phù hợp với tiêu chí

Phân biệt ba câu hỏi:

| Câu hỏi | Bằng chứng phù hợp |
| --- | --- |
| Yêu cầu cụ thể có được đáp ứng? | Test, thao tác, dữ liệu và kết quả quan sát |
| Giao diện có render và tương tác đúng trong phạm vi hỗ trợ? | Build thực, screenshot đúng state, accessibility/keyboard/gesture checks |
| Thiết kế có đủ rõ và phù hợp mục tiêu? | Critique có lý do, task walkthrough, hoặc nghiên cứu theo mức bất định |

Lint source không chứng minh render; screenshot không chứng minh thao tác; exit code 0 không chứng minh mọi kiểm tra cần thiết đã chạy. Nêu phạm vi thực sự của từng bằng chứng.

## D10. Kết quả chưa đo phải hiện rõ

Báo cáo C2O giữ `pass`, `partial`, `fail`, `not-tested` theo tiêu chí và nguồn acceptance/evidence hiện có. Thiếu browser, simulator hoặc dữ liệu phải giữ lý do chưa kiểm tra; không biến coverage một phần thành `pass`. Năm nhãn viết hoa của gói cũ chỉ thuộc profile JSON được chọn rõ trong [evidence](evidence.md), không thay hệ trạng thái C2O. Không dùng phần trăm thẩm mỹ hoặc điểm tổng để bù cho lỗi chặn nhiệm vụ.

Bằng chứng cần được gắn với bản implementation, input, config và môi trường đã kiểm tra. Khi input thay đổi, kiểm tra lại phần bị ảnh hưởng. Cơ chế hash trong profile JSON tùy chọn chỉ theo dõi các file được khai báo, không chứng minh danh sách dependency là đầy đủ.

## D11. Phản biện theo brief và bằng chứng

Người review đọc mục tiêu, tiêu chí và artifact thực. Mỗi finding nêu vị trí, điều quan sát được, ảnh hưởng lên nhiệm vụ và cách kiểm tra bản sửa. Tách lỗi khỏi sở thích. Cho phép không có finding đáng sửa; không yêu cầu tạo đủ một số lượng lỗi cố định.

Trong production đã được giao, xử lý Critical/Major bắt buộc trong quyền hiện có rồi kiểm tra lại phần bị ảnh hưởng. Với review-only, báo finding và giới hạn, không tự sửa artifact. Chỉ thay scope/tiêu chí qua quyết định được phép và giữ nguồn thay đổi; không giảm acceptance để che lỗi. Agent được giải quyết lựa chọn nhỏ trong quyền hạn đã giao; không tự tạo vòng xin phép cho mọi bước.

## D12. Quy trình tỷ lệ với bất định và ảnh hưởng

Dùng mức can thiệp thấp nhất đủ theo [C2O framework](../../../references/framework.md). `quick`, `standard`, `deep` là nhãn lịch sử của bộ thiết kế, có thể dùng để mô tả mức đào sâu nhưng không phải mode bắt buộc, trường phải lưu hoặc vòng làm việc thứ hai. Dùng thử nghiệm nhỏ khi nói chuyện thêm không giải quyết được bất định. Tác vụ nhỏ có thể ở trong hội thoại; không cần `.design`, JSON, metadata hay template. Chỉ lưu quyết định và bài học có khả năng được dùng lại.

## Thứ tự xử lý khi có xung đột

1. Quyền hạn, chỉ dẫn của người dùng và các ràng buộc bắt buộc đã xác định trong dự án.
2. Mục tiêu, dữ liệu và hành vi đã chốt cho phạm vi hiện tại.
3. Nhu cầu accessibility và conventions của nền tảng đang áp dụng.
4. Tính nhất quán với các phần đang hoạt động của sản phẩm.
5. Hướng hình ảnh và sở thích thẩm mỹ của dự án.

Nếu hai ràng buộc không thể đồng thời đạt, ghi xung đột, tác động và một lựa chọn có thể kiểm tra. Không âm thầm giảm acceptance để tạo kết quả xanh.
