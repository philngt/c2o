# iPhone — hợp đồng giao diện và tác vụ

**Baseline source: iOS 17+.** Đây là phần Platform của template Lifestyle/Utility, dùng cùng [SwiftUI profile](../../profiles/swiftui.md) và [UI composition](../../core/ui-composition.md). Các lựa chọn dưới đây là hợp đồng thiết kế để thích ứng theo sản phẩm; có source chưa đồng nghĩa đã build, chạy trên iPhone hoặc sẵn sàng App Store.

## Chọn cấu trúc theo tác vụ

| Nhu cầu | Điểm bắt đầu | Khi nên đổi |
| --- | --- | --- |
| Lifestyle: tìm một mục rồi xem/sửa | `NavigationStack` → collection `List` → detail; editor là sheet có Lưu/Hủy | Gallery khi hình ảnh thực sự giúp nhận diện; timeline khi thứ tự sự kiện là câu hỏi chính |
| Utility: nhập → xử lý → lấy kết quả | Một workbench có input, action xử lý, kết quả và Copy; history là sheet tùy chọn | Thêm tham số khi tác vụ cần; tách nhiều bước khi mỗi bước có quyết định/validation riêng |
| Nhiều mục đích cấp cao, dùng lặp lại | `TabView`, mỗi destination có state/navigation riêng | Gộp hoặc đổi tên khi các tab thực chất chỉ là action hoặc cùng một tập dữ liệu đổi filter |
| Tác vụ ngắn cần quyết định trước khi quay lại | Sheet với điểm kết thúc và chính sách bản nháp rõ | Dùng navigation khi người dùng cần đi sâu và quay lại nhiều cấp |

Starter hiện bắt đầu từ một collection hoặc một workbench, không áp số lượng tab cố định. Tab phục vụ destination cấp cao; thao tác Thêm, Lưu, Chạy thuộc control/toolbar của tác vụ. Apple cũng phân biệt tab bar dùng để điều hướng và toolbar chứa hành động theo ngữ cảnh. [I1][I2]

Không đặt onboarding, tài khoản, paywall hoặc thông báo như điều kiện mặc định trước thao tác đầu tiên. Chỉ thêm khi outcome, mô hình kinh doanh hoặc capability thực sự cần; đó là thay đổi scope của dự án.

## Components, data view và layout

| Vùng | Thành phần phù hợp | Hợp đồng cần giữ |
| --- | --- | --- |
| Collection | `List`, row với tên và metadata cần nhận diện; `.searchable` | Row chọn bằng ID; query không sửa dữ liệu; không trộn “chưa có mục” với “không khớp tìm kiếm” |
| Detail | Các trường có label; section theo câu hỏi người dùng | Giá trị chưa biết khác giá trị rỗng; action ghi rõ đang tác động mục nào |
| Editor | `Form`, `TextField`, lựa chọn native | Draft gắn record ID; Lưu commit một lần; Hủy không đổi record; lỗi giữ input |
| Workbench | Input có label, action, kết quả có thể sao chép; tham số nếu tác vụ cần | Đổi input làm kết quả cũ cần được nhận diện đúng; Copy không báo thành công khi chưa có kết quả hợp lệ |
| Feedback | Empty/error inline theo vùng; alert cho quyết định cần phản hồi | Không dùng spinner vô thời hạn cho xử lý local tức thời; không báo “đã lưu” trước commit |
| Settings | Sheet có lối đóng rõ | Cài đặt thay đổi hành vi; không biến thành kho chứa mọi tính năng ít dùng |

`List` là biểu diễn tập dữ liệu; detail/editor là composition theo tác vụ. Card là một cách nhóm nội dung, không phải mặc định cho mỗi section. Khi đổi `List` sang gallery, giữ search, identity, selection, semantics và phép thao tác cần thiết; không suy hành vi từ hình dạng container.

## Không gian, input và state

Thiết kế theo vùng nội dung thực sau safe area và bàn phím. Để form cuộn đến trường đang nhập và tới Lưu/Hủy; tránh đặt hành động thiết yếu dưới bàn phím hoặc home indicator. Text styles ngữ nghĩa, label dài và chữ accessibility có thể làm một hàng thành nhiều hàng. Quy tắc hit region, VoiceOver và màu động dùng từ [SwiftUI profile](../../profiles/swiftui.md), rồi kiểm chứng trong màn thực.

Giữ độc lập `query`, `selectedID`, `draft`, kết quả utility và trạng thái persistence. Một row không tự lưu record khi đồng thời phát event chọn. Khi rời editor, đóng sheet hoặc nhận deep link, áp dụng chính sách draft đã ghi: giữ lại, hỏi bỏ thay đổi, hoặc commit theo thiết kế; không tự bỏ input chỉ vì navigation đổi.

Widget mở `<scheme>://collection` hoặc `<scheme>://utility`. Host xử lý route thành destination được hỗ trợ, giữ chính sách draft và không biến URL thành hành động ghi dữ liệu. Mở app khi đã chạy và mở từ trạng thái đóng đều cần thử riêng. Xem [widget contract](widgets.md).

## Khi dùng OS/SDK mới hơn baseline

Giữ source baseline dùng các API đã có ở iOS 17. Một thiết kế lấy từ HIG hiện tại có thể phản ánh OS mới hơn; syntax `Tab`, `.sidebarAdaptable` và các API presentation mới cần kiểm tra availability, không sao chép vào nhánh baseline. Những thay đổi tab/sidebar của iOS 18 được Apple giới thiệu riêng trong WWDC24. [I3] Khi nâng SDK, ưu tiên để native controls thích ứng theo hệ thống và kiểm tra lại; không dựng một lớp chrome giả để khóa vẻ ngoài của một phiên bản OS.

## Chọn bằng chứng cho dự án

Đưa các trường hợp liên quan vào acceptance hiện có; bảng này không tự thêm tất cả thành gate bắt buộc cho mọi sửa đổi.

| Câu hỏi | Quan sát cần có |
| --- | --- |
| Người dùng hoàn thành thao tác chính? | Collection → detail → edit → save/reopen hoặc input → process → copy |
| Draft có sống qua hủy/lỗi/chuyển màn? | Input không mất khi write thất bại; hủy không tạo record; deep link xử lý đúng chính sách |
| Màn còn dùng được ở vùng hẹp? | iPhone hẹp, bàn phím mở, nội dung dài và chữ lớn; action không bị che |
| Trạng thái dữ liệu có trung thực? | First use, search no results, load error, empty value, populated; không lấy dữ liệu minh họa làm dữ liệu thật |
| Các cách truy cập có hoạt động? | VoiceOver, focus trường nhập và accessible names; widget route nếu đã bật |

Source review, Xcode build, simulator/device và accessibility check là các bằng chứng khác nhau. Chưa chạy thì giữ `not-tested` trong nguồn C2O hiện có, kèm lý do nếu thiếu runtime. Chỉ profile JSON tùy chọn mới dùng `NOT_RUN` hoặc `BLOCKED`; xem [Evidence](../../core/evidence.md). Phần đã đạt và phần thiếu vẫn phải được giữ nếu verdict là `partial`.

## Nguồn Apple

Đối chiếu ngày 2026-10-20; deployment baseline do bộ starter chọn, không phải tuyên bố mọi API trong tài liệu hiện tại dùng được ở baseline.

- [I1 — HIG: Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)
- [I2 — HIG: Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)
- [I3 — WWDC24: What’s new in SwiftUI](https://developer.apple.com/videos/play/wwdc2024/10144/)
