# Lifestyle — blueprint theo tác vụ

**C2O Design v1.3.** Dùng tài liệu này để chọn một lát cắt sản phẩm, sau đó lập brief, screen contract và acceptance cho dự án. Đây là đề xuất thiết kế; việc có tên module trong blueprint không chứng minh module đã được triển khai hoặc chạy đạt trên thiết bị Apple.

## 1. Ý định sản phẩm và category trên App Store

Trong framework, Lifestyle là nhóm nhu cầu xoay quanh sở thích, bộ sưu tập, nhật ký sinh hoạt và tổ chức việc nhà. Apple có category **Lifestyle**, với ví dụ như hobby và home improvement; chọn category phát hành theo chức năng cốt lõi thực tế của app. Category là quyết định phân phối, không quyết định số tab, layout hay data view. Xem [Apple — Choosing a category](https://developer.apple.com/app-store/categories/).

Nhật ký theo dõi triệu chứng, hướng dẫn điều trị hoặc cam kết cải thiện sức khỏe cần được định nghĩa và xem xét riêng. Blueprint này không tự thêm health claim, dữ liệu sức khỏe hoặc tích hợp HealthKit vào một app Lifestyle.

Ba mức dùng xuyên suốt: **Core** để hoàn thành tác vụ đã chọn; **Conditional** chỉ bật khi feature và nhu cầu có thật; **Optional** là cải tiến có thể bỏ mà vẫn hoàn thành tác vụ. Đối chiếu [module matrix](../module-matrix.md) trước khi mở rộng scope.

## 2. Chọn archetype trước khi chọn màn

| Archetype | Việc cần hoàn thành và đơn vị dữ liệu | Data view và layout gợi ý | Screen và component gợi ý |
| --- | --- | --- | --- |
| **Collection / hobby** | Ghi lại, tìm và cập nhật một món đồ/đối tượng; mỗi record có identity bền vững | `DVP-01` list + `DVP-05` list–detail; `DVP-02` chỉ khi ảnh thật giúp nhận diện; `LP-02`, hoặc `LP-04` nếu duyệt bằng hình | `SP-01/02/03`; `CP-14` row, `CP-07` field, `CP-09` favorite toggle, `CP-01` command |
| **Journal / routine** | Ghi một entry hoặc một lần thực hiện; phân biệt ngày ghi, ngày sự kiện và trạng thái thực hiện | `DVP-06` timeline hoặc list; `DVP-07` chỉ khi chọn ngày là nhiệm vụ; `LP-01/05` | `SP-02/03`; `CP-07`, `CP-12` date/time, `CP-19` field message; trạng thái routine chỉ thêm khi có mô hình thực |
| **Planner / home** | Biết việc nào cần làm, vào lúc nào và cập nhật kết quả; mỗi task/event có identity, thời gian và trạng thái rõ | `DVP-01` grouped list; `DVP-07` khi lịch quan trọng; `DVP-08` khi chuyển trạng thái là thao tác chính; `LP-01/09` | `SP-05/03`; `CP-12`, `CP-11` picker, `CP-18` status, `CP-04` toolbar |

Các ID trỏ tới [components](../../catalog/components.md), [data views](../../catalog/data-view-patterns.md), [layouts](../../catalog/layout-patterns.md) và [screens](../../catalog/screen-patterns.md). Chúng là lựa chọn có thể kết hợp, không phải gói phải cài đủ. Chẳng hạn list–detail là cách ghép vùng; nó vẫn có thể chứa list hoặc collection ảnh.

Nếu có nhiều archetype, chọn một tác vụ làm cửa vào. Một app sưu tập không cần thêm planner chỉ để đủ tab; nhật ký không cần dashboard nếu việc chính là viết và đọc lại.

## 3. Lát cắt starter: collection CRUD + favorites

**Phạm vi starter được chọn:** tạo, xem, sửa, xóa record trong collection; đánh dấu/bỏ favorite; Settings và Help. Điều hướng dùng stack trên iPhone và split trên iPad/macOS; source widget chỉ đọc summary và mở app qua deep link, được đưa vào target khi bật `--widgets`. Các quyết định này là phạm vi cần kiểm chứng, không phải kết quả native `PASS`.

Model starter đã chọn là `LifestyleRecord(id: UUID, title, notes, isFavorite, updatedAt)`. Chốt contract dữ liệu trước khi mở rộng giao diện:

- `id` không đổi khi sửa `title`; `notes` là nội dung ghi chú. Trường nào bắt buộc, giá trị chỉ có khoảng trắng có hợp lệ không, phải được thống nhất với implementation.
- Favorite là trạng thái của record, có thể hoàn tác bằng thao tác ngược; xóa record phải xử lý tham chiếu và selection liên quan.
- Thứ tự list và favorite phải ổn định, có quy tắc khi trùng tên. `updatedAt` cần nguồn thời gian, quy tắc cập nhật và cách hiển thị theo locale rõ ràng.
- Dữ liệu local được mô tả đúng với cơ chế lưu thật. Không hứa sync, backup, mã hóa riêng hoặc draft qua lần khởi động lại khi chưa có implementation và evidence.
- Ảnh, tags, nhóm phân cấp, vị trí, giá trị tài sản và chia sẻ là **Conditional**. Không tạo trường bắt buộc chỉ vì archetype có thể dùng chúng.

### Cấu trúc màn và navigation

| Vùng/màn | Trách nhiệm | Pattern và quy tắc |
| --- | --- | --- |
| **Collection** | Tìm đối tượng và bắt đầu tạo mới | `SP-01`, `DVP-01`, `CP-14/24/01`; có thể thêm `CP-27` khi cần tìm/lọc. Favorite có thể là scope/filter thay vì một hệ navigation riêng |
| **Detail** | Hiểu record đang chọn, favorite, sửa hoặc xóa đúng đối tượng | `SP-02`, `CP-15/09/03`; `LP-02` trên vùng rộng, đích đến trong stack trên vùng hẹp |
| **Create / Edit** | Nhập dữ liệu, biết phần chưa lưu, lưu hoặc hủy có chủ đích | `SP-03`, `LP-05/10`, `CP-07/19/01`; dùng một form phù hợp độ phức tạp thật |
| **Settings / Help** | Hiểu dữ liệu lưu ở đâu, chỉnh preference có thật, xem hướng dẫn tác vụ | `SP-07/08`, `LP-01`, `CP-15/02/09`; không hiển thị switch không có tác dụng |

Khi chuyển từ split sang stack, giữ identity đang chọn và ngữ cảnh quay lại. Khi chưa chọn record trên vùng rộng, detail pane giải thích cách chọn hoặc tạo mới; không tự tạo record giả để lấp chỗ trống. Một record bị xóa không để lại detail có nút thao tác trên dữ liệu không còn tồn tại.

### Luồng hoàn chỉnh cần thiết kế

| Luồng | Kết quả quan sát được | Nhánh phục hồi |
| --- | --- | --- |
| Collection rỗng → Create → nhập → Save → Detail | Record được lưu theo contract và xuất hiện trong collection | Validation gắn đúng field; lỗi lưu giữ input; người dùng biết bản nào đã lưu |
| Chọn record → Favorite → xem scope phù hợp → mở lại | Trạng thái và count phản ánh cùng tập dữ liệu | Nếu cập nhật thất bại, UI giải thích trạng thái thật và cho thử lại |
| Detail → Edit → Save → quay lại list | Identity được giữ; nội dung mới xuất hiện đúng record | Cancel/dismiss xử lý phần thay đổi chưa lưu theo một chính sách rõ |
| Detail → Delete → quay lại collection | Record và tham chiếu liên quan biến mất đúng phạm vi | Chọn xác nhận hoặc undo dựa vào khả năng phục hồi thực; không hứa undo nếu dữ liệu đã mất |

## 4. State contract

| Trạng thái | Hành vi cần định nghĩa |
| --- | --- |
| **Empty** | Collection chưa có record: giải thích ngắn và hành động tạo. Chưa có favorite: hướng dẫn đánh dấu một record đã có; không diễn đạt thành mất dữ liệu |
| **No results** | Chỉ khi có query/filter: giữ query, cho sửa/xóa filter; tách khỏi collection thật sự rỗng |
| **Error** | Lỗi đọc/lưu/xóa có thông báo theo phạm vi; không báo thành công trước khi state thật được cập nhật; giữ phần có thể dùng tiếp |
| **Draft** | Phân biệt dữ liệu đã lưu và phần đang sửa. Nêu rõ Save/Cancel và xử lý rời màn; khôi phục draft sau khi app đóng là Conditional |
| **Privacy** | Help nêu dữ liệu nào được giữ local; tránh lộ nội dung riêng trong preview/widget khi không cần cho nhiệm vụ; không thêm analytics mặc định |
| **Permission** | Starter không có permission request. Nếu thêm ảnh/camera/location, chỉ yêu cầu quyền cho thao tác tương ứng và thiết kế deny/restricted cùng cách tiếp tục phù hợp |
| **Offline / stale** | Với thao tác local, đánh giá khả năng hoạt động không mạng. Chỉ thêm sync/loading/stale state khi nguồn dữ liệu hoặc thao tác thật tạo ra trạng thái đó |

## 5. Các biến thể mở rộng

- **Journal / routine:** Core là tạo entry hoặc ghi một lần thực hiện, đọc/sửa/xóa và tìm lại theo ngữ cảnh thật. Date grouping, draft và privacy cần được quyết định. Streak, mood scale, nhắc nhở, biểu đồ và khóa riêng là Conditional; một lần không ghi không tự có nghĩa là không thực hiện. Không dùng streak để suy ra sức khỏe hay chất lượng sống.
- **Planner / home:** Core là tạo và hoàn tất task/event theo mô hình đã chọn. Calendar cần ngày/giờ có nghĩa; board cần các trạng thái và quy tắc chuyển. Recurrence, nhiều thành viên, phân công, sync và notifications là Conditional. Múi giờ, task cả ngày, task chưa có hạn và thay đổi lịch cần contract nếu feature dùng chúng.
- **Collection có hình:** Dùng ảnh để nhận diện khi nội dung thật phù hợp; có label/fallback cho ảnh thiếu. Media input và permission chỉ được đưa vào khi implementation có nguồn ảnh cụ thể. Grid phải vẫn phân biệt các record có hình tương tự.

## 6. Widget theo nhiệm vụ

**Khi bật `--widgets`:** snapshot chỉ chứa số record và số favorite, cùng trạng thái cần thiết; không chuyển title/notes sang widget. Widget chỉ đọc summary và deep link mở app; không chỉnh sửa, xóa hay đánh favorite tại đó. Phân biệt snapshot chưa tồn tại, lỗi đọc và số đếm thực sự bằng 0; thiếu dữ liệu không được giả thành collection rỗng. Quyết định thiết kế này không bảo đảm widget đã refresh hoặc route đúng trên mọi target; cần quan sát refresh thực, không hứa thời điểm cập nhật chính xác.

Các use case Conditional ngoài starter: một record người dùng chọn để mở nhanh, một entry được phép hiển thị, task sắp tới khi planner thật có hạn. Với nội dung riêng tư, ưu tiên summary tối thiểu và lựa chọn hiển thị có chủ đích. Nếu deep link gắn với record đã xóa, mở trạng thái phục hồi hữu ích trong app. Không đồng nhất widget, notification và Live Activity; mỗi loại cần nhu cầu riêng.

## 7. Acceptance mẫu để đưa vào dự án

Các mã `LCASE-*` dưới đây là case mẫu, cần map sang criterion hiện có của dự án, chẳng hạn `C-001`. Chưa chạy thì giữ `not-tested` trong C2O (`NOT_RUN` chỉ trong profile JSON tùy chọn); không biến checklist hoặc screenshot minh họa thành bằng chứng thao tác.

| Case | Input và thao tác | Kết quả cần quan sát |
| --- | --- | --- |
| `LCASE-01` CRUD | Tạo hai record trùng tên; sửa một; xóa một | Đúng identity được thay đổi; record còn lại giữ nguyên; list/detail không tham chiếu record đã xóa |
| `LCASE-02` Favorite | Đánh dấu, bỏ đánh dấu, mở lại app theo persistence contract | State và scope favorite nhất quán; count không lấy từ dữ liệu giả hoặc list bị lọc ngoài ý muốn |
| `LCASE-03` Draft / error | Sửa dữ liệu rồi rời màn; gây lỗi lưu có kiểm soát nếu đường lỗi tồn tại | Chính sách Save/Cancel rõ; input không mất do lỗi có thể phục hồi; không hiển thị thành công sai |
| `LCASE-04` Adaptation | Chọn record ở split; chuyển vùng hẹp; dùng tên dài và cỡ chữ trong phạm vi hỗ trợ | Giữ ngữ cảnh; đọc và thao tác được; test keyboard/VoiceOver theo từng target |
| `LCASE-05` Widget | Dữ liệu rỗng, có dữ liệu, rồi đổi dữ liệu và mở deep link | Summary có scope đúng; ghi nhận refresh thực; route mở được; xử lý đích không còn tồn tại nếu có |
| `LCASE-06` Privacy | Cài mới, thực hiện toàn bộ flow starter, đọc Help và widget | Không có permission/auth/paywall bất ngờ; mô tả lưu trữ khớp hành vi; không lộ nội dung ngoài contract |

Áp dụng [nguyên tắc](../../core/principles.md), [data-view contract](../../core/data-views.md) và [quy tắc evidence](../../core/evidence.md). ID catalog và liên kết trong Markdown được review bởi người/agent; checker không tự xác nhận UI, navigation hoặc sự phù hợp của category.
