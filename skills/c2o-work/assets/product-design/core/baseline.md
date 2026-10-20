# Bản định hướng thiết kế dùng chung

Baseline là tập quyết định đang được dùng làm chuẩn cho một phạm vi của dự án. Nó nối phương án đã chọn với layout, hành vi, token, nội dung và asset của các màn sau. Dùng [mẫu baseline](../templates/baseline.md), hoặc dẫn chiếu các tài liệu hiện có nếu chúng đã giữ được các quyết định này.

## 1. Chốt điều gì

| Nhóm | Quyết định cần giữ |
| --- | --- |
| Outcome và domain | Tác vụ ưu tiên, đối tượng chính, thuật ngữ, ý nghĩa dữ liệu và điều chưa biết |
| Experience | Vai trò màn hình, navigation, selection, lưu/hủy, draft và phục hồi |
| Data view | ID, nghĩa trường, đơn vị, scope, nguồn/uncertainty và tương tác truy vấn; dẫn chiếu hợp đồng dữ liệu canonical |
| Component/composition | Trách nhiệm, semantics, event, state owner, variant và cách phối hợp trong màn; không nhân bản business rule vào từng component |
| Visual | Hierarchy, mật độ, typography, vai trò màu, spacing, shape, imagery và motion |
| Platform | Control và pattern nền tảng; các biến thể theo không gian, input và accessibility |
| Assets | Vai trò hình ảnh, icon family, chất liệu/góc nhìn, crop, appearance và fallback |
| Evidence | Criterion và phương pháp kiểm tra; artifact nào chỉ là concept, cái nào là render thật |

Nhận diện baseline bằng phạm vi, nguồn quyết định và phiên bản đang áp dụng theo quy ước dự án. Có thể dùng ID/revision của mẫu khi cần quản lý riêng; đoạn nhỏ trong nguồn hiện có không bắt buộc thêm metadata. `selected` cho biết hướng đang dùng; không có nghĩa đã kiểm thử, có người dùng xác nhận hoặc được phép phát hành. Không tạo một vòng phê duyệt mới nếu nhiệm vụ đã giao quyền lựa chọn.

## 2. Dùng reference đúng vai trò

Một màn đại diện hoặc reference sheet giúp giữ đặc trưng hình ảnh: silhouette, palette roles, type treatment, icon family và chất liệu. Ghi điều lấy từ reference, điều phải điều chỉnh theo nhiệm vụ và điều không kế thừa. Khi chưa có ảnh, một token/component system đang hoạt động và bản hợp đồng hành vi rõ vẫn có thể làm chuẩn.

Ảnh tham chiếu đi cùng các quyết định semantic. Một ảnh đẹp không quy định được data ownership, trạng thái lỗi, cỡ chữ lớn hay keyboard behavior. Kích thước suy từ ảnh được ghi là ước lượng cho tới khi đo trên artifact phù hợp. Reference của app khác, screenshot sinh bằng AI hoặc crop không trở thành bằng chứng về nhu cầu người dùng hay tính đúng của native UI.

Khi sinh hoặc chỉnh ảnh, chỉ đưa các reference liên quan tới nhiệm vụ và khả năng công cụ. Reference có thể là một vùng để định hình asset hoặc nhiều ảnh để giữ nhân vật/đối tượng; không đặt số ảnh, biên crop hay một backend làm luật chung. Việc sử dụng nội dung phải phù hợp nguồn và quyền đã có; không ghi thông tin xác thực vào prompt hoặc hồ sơ.

## 3. Giữ nhất quán qua nhiều màn

Trước khi thiết kế màn mới, đọc baseline đang áp dụng và các component gần nhất. Dẫn tới quyết định, layout, component/data view, asset và criterion liên quan bằng đường dẫn hoặc ID dự án đã có; chỉ thêm ID mới khi có ích cho việc đối chiếu. Dẫn tới [hợp đồng component](components.md), [data view](data-views.md) và [composition](ui-composition.md) khi cần quy định mới. Không cần tạo tài liệu màn riêng chỉ để liệt kê metadata; evidence checker cũng không tự hiểu các quan hệ này.

Review theo ba câu hỏi:

1. Cùng ý nghĩa có giữ thuật ngữ, hành động và phản hồi tương ứng không?
2. Hierarchy và cách dùng token/component có bám quy ước của scope không?
3. Biến thể có được giải thích bằng tác vụ, nội dung, nền tảng hoặc khả năng tiếp cận không?

Giữ tính nhất quán theo ý nghĩa và hành vi. Một list trên phone có thể chuyển thành list-detail khi đủ không gian; thay đổi cấu trúc này cần giữ selection và công việc chưa lưu. Không lấy sự giống hình học giữa hai ảnh làm tiêu chí duy nhất.

## 4. Thay đổi và ngoại lệ

Ghi khác biệt có chủ đích cùng lý do, phạm vi và criterion bị ảnh hưởng. Nếu thay đổi chỉ áp dụng một màn, ghi ngoại lệ tại màn và dẫn chiếu baseline. Nếu thay đổi quy tắc chung, tăng revision của baseline và cập nhật những nơi phụ thuộc; tránh tạo hai tài liệu cùng tuyên bố là nguồn chuẩn.

Khi baseline/reference/token/asset/layout đổi, xác định những màn, state và evidence phải xem lại. Nếu chọn profile JSON, hash chỉ phát hiện thay đổi của file đã khai báo; không tìm được mọi phụ thuộc bị bỏ sót. Không thay hash để giữ một kết luận cũ khi quyết định đã đổi.

## Đầu ra tối thiểu

Một bản định hướng có phạm vi và revision, nguồn quyết định, các đường dẫn canonical, reference có vai trò rõ, những khác biệt được chấp nhận và tiêu chí còn cần kiểm chứng. Nhiệm vụ nhỏ có thể dùng một đoạn trong tài liệu hiện có thay vì một file mới.
