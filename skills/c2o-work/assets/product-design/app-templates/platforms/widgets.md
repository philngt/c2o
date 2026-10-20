# Widgets — tóm tắt chỉ đọc và đường trở về app

**Baseline source: iOS/iPadOS 17+, macOS 14+.** Starter có WidgetKit extension tùy chọn bằng `--widgets`: đọc bản tóm tắt local, hiển thị vài thông tin và mở app. Source tại [Widgets](../../starters/apple/Widgets/README.md). Đây chưa phải widget đã build/chạy hoặc một chứng nhận sẵn sàng App Store.

## Chọn đúng trải nghiệm

Widget hữu ích khi một ánh nhìn ngắn trả lời được câu hỏi trước khi mở app. Extension chạy riêng với host; timeline cung cấp dữ liệu để hệ thống render. `widgetURL` liên kết nội dung widget với destination trong app. [W1]

| Khả năng | Khi có ích | Trong starter |
| --- | --- | --- |
| Summary WidgetKit | Xem số lượng/trạng thái đã lưu và mở collection/workbench | Có source read-only, `StaticConfiguration` |
| Widget có cấu hình | Chọn danh mục/đối tượng cho từng instance | Blueprint; cần `AppIntentConfiguration`, provider và mặc định hợp lý |
| Widget tương tác | Một hành động nhỏ, đủ nghĩa ngay trên widget | Blueprint; `Button`/`Toggle` dùng App Intent và quyền ghi phải được thiết kế lại |
| Live Activity | Phiên/sự kiện đang diễn ra, có thời điểm bắt đầu/kết thúc | Ngoài starter; ActivityKit, lifecycle và availability/capability riêng |
| Control Center control | Một lệnh hoặc bật/tắt tại bề mặt hệ thống hỗ trợ | Ngoài starter; ControlWidget/API theo OS, không thuộc baseline 17/14 |
| Shortcuts/App Shortcuts | Hành động người dùng kết hợp hoặc gọi từ hệ thống | Ngoài starter; App Intents schema, parameter, output và discovery riêng |

Cấu hình widget và tương tác widget là hai khả năng khác nhau. App Intent có thể phục vụ nhiều nơi, nhưng có một intent không có nghĩa app đã triển khai tất cả widget, Shortcuts, Control Center hoặc Live Activities. Apple tách các điểm tích hợp này; chọn theo tác vụ rồi kiểm tra API và platform availability. [W1][W2][W3]

## Matrix family và bố cục

Matrix dưới đây mô tả **phạm vi của starter ở baseline**, không phải toàn bộ các family Apple hiện có. Ba system family dùng được trên Home Screen/Today View của iPhone/iPad và desktop/Notification Center trên Mac theo nền tảng hỗ trợ. [W4][W5][W6]

| Family | iPhone | iPad | macOS native | Nội dung trong source |
| --- | --- | --- | --- | --- |
| `.systemSmall` | Có | Có | Có | Tên app, title ưu tiên, subtitle ngắn, ngày snapshot |
| `.systemMedium` | Có | Có | Có | Hai vùng: title và ngữ cảnh; thêm ngày/giờ cập nhật |
| `.systemLarge` | Có | Có | Có | Summary có khoảng đọc rộng hơn; freshness và lối mở app |
| Accessory circular/rectangular/inline | Ngoài starter; có thể thiết kế cho Lock Screen hỗ trợ | Ngoài starter; kiểm tra Lock Screen và OS hỗ trợ | Không khai báo trong target Mac này | Cần view nhỏ riêng, kiểm chứng rendering và availability |
| Extra large, extra large portrait, watch complication | Ngoài starter | Ngoài starter | Ngoài starter | Chỉ thêm khi có nội dung/tác vụ và target tương ứng |

Apple mô tả accessory circular xuất hiện ở Lock Screen iOS/iPadOS và watch complication; widget trên iPad Lock Screen cần OS hỗ trợ. [W7] Khi bổ sung accessory cho source dùng chung, cô lập trong `#if os(iOS)` và loại Catalyst nếu target đó được thêm; `#if os(macOS)` vẫn khai báo các family Mac đã kiểm chứng. Không thêm `.accessoryCorner` vào app không có watchOS target. Mỗi family mới cần nhánh nội dung riêng trước khi đưa vào `supportedFamilies`.

Source hiện dùng `.containerBackground(for: .widget)`, content margins của WidgetKit và layout theo `widgetFamily`. Nền có thể bị hệ thống xử lý khác trong các context; kiểm tra full color và các appearance mode được OS đó hỗ trợ. Trên Mac cần xem lại font/spacing thực, không suy ra kết quả từ preview iPhone. [W1][W8] Widget không có danh sách cuộn hoặc một form đầy đủ chỉ vì chọn size lớn.

## Ranh giới dữ liệu

Host sở hữu domain store. Sau commit, host tạo một **snapshot bất biến** chỉ chứa `category`, `title`, `subtitle`, `updatedAt`, `route`, rồi công bố vào App Group bằng cơ chế của `StarterCore`. Snapshot mẫu chỉ gồm count/status; không copy tên record riêng tư, notes, input utility hoặc history text vào các chuỗi title/subtitle.

Extension chỉ gọi `WidgetSnapshotStore.read()`. App Group là container chia sẻ giữa các target được cấu hình quyền phù hợp; nó không phải dịch vụ sync giữa thiết bị. [W9] Widget không mở trực tiếp kho record, tự tính lại domain state từ dữ liệu riêng, hoặc ghi vào đó.

| Kết quả đọc | Ý nghĩa | Cách hiển thị |
| --- | --- | --- |
| Snapshot hợp lệ | Bản tóm tắt app đã công bố, tại `updatedAt` | Hiện nội dung và thời điểm của bản dữ liệu đó |
| `nil` | Chưa có snapshot | “Chưa có bản tóm tắt”; mở app để bắt đầu |
| Throw/cấu hình group lỗi/decode lỗi | Không đọc được bản tóm tắt | “Chưa đọc được bản tóm tắt”; mở app để kiểm tra và thử lại |
| Category/route không thuộc profile hoặc title rỗng | Dữ liệu không phù hợp với widget này | Fallback lỗi; không giả làm nội dung đúng |
| Preview/placeholder | Minh họa gallery hoặc stand-in của hệ thống | Text trung tính có nhãn minh họa; không đưa vào timeline thật khi lỗi |

Không biến lỗi đọc thành “0 mục”. Không thay `updatedAt` bằng thời điểm render rồi làm dữ liệu cũ trông mới. Snapshot cũ vẫn là bản cũ cho đến khi được app thay; nhu cầu hết hạn/hạn chế dữ liệu theo thời gian cần criterion và xử lý riêng.

## Cập nhật và deep link

Source trả một timeline entry với `.never` vì bản tóm tắt này chỉ đổi khi app công bố dữ liệu. Host gọi `WidgetCenter.shared.reloadTimelines(ofKind: AppProfile.widgetKind)` sau khi công bố thành công. Nếu công bố thất bại, host giữ kết quả domain save đúng thực tế và thử lại phần widget theo cách có thể quan sát. `kind` phải khớp giữa app và extension.

Không hứa widget đổi ngay khi bấm Lưu. WidgetKit quyết định lịch thực thi và có ngân sách reload; các policy như `.after(date)` cũng không là timer chính xác. [W10] Khi sản phẩm có nội dung dự báo theo thời gian, thiết kế nhiều timeline entries và chọn policy phù hợp; không dùng reload liên tục để giả widget là app đang chạy nền.

Một lần chạm mở `<AppProfile.urlScheme>://collection` hoặc `://utility` theo category. Source tạo URL từ scheme cấu hình và route cho phép. Không có query chứa input riêng tư, lệnh xóa, thao tác chạy utility hoặc ghi record. Host phải giữ chính sách draft khi nhận route. Widget mở app không phải App Intent thay đổi dữ liệu.

## Cấu hình target và mở rộng quyền ghi

Generator dùng iOS host `<base>.ios`, widget `<base>.ios.widgets`; macOS host `<base>.macos`, widget `<base>.macos.widgets`. Khi bật widget, các target liên quan mặc định dùng App Group `group.<base>`; `--app-group` cho phép chọn ID đã đăng ký khác. Signing team, đăng ký group, entitlements và container access thực tế cần khớp trên mỗi Apple platform. Tạo các file cấu hình chưa xác nhận các quyền đó hoạt động. [W9]

macOS target ở đây là extension native đọc snapshot của app Mac. Khả năng hệ thống hiển thị iPhone widget từ xa trên Mac là một context khác, không chứng minh dữ liệu iPhone đã có trong kho Mac. [W1]

Nếu thêm App Intent có ghi, phải chốt command idempotent, validation, authorization nếu có, lỗi và nơi serialize writes giữa process. Intent không được sửa file bằng một quy tắc khác host. Sau action thành công, xuất bản lại summary và yêu cầu reload. Đây là thay đổi architecture/scope; starter chỉ đọc chưa giải quyết bài toán nhiều writer.

## Evidence còn cần ở Apple runtime

Build host + extension ở từng platform; thử ba family, snapshot thật/thiếu/lỗi, publish → reload, hiển thị bản cũ khi reload chưa xảy ra, deep link khi app đóng/đang mở, accessibility và appearance được hỗ trợ. Kiểm tra App Group trên signed targets và không rò nội dung riêng. App icon, signing, provisioning và review phát hành là việc theo app thực. Các native check này hiện chưa chạy trong môi trường Linux.

## Nguồn Apple

Đối chiếu ngày 2026-10-20. Có nguồn mới hơn baseline; khả năng ngoài baseline cần availability riêng.

- [W1 — WWDC26: WidgetKit foundations](https://developer.apple.com/videos/play/wwdc2026/277/)
- [W2 — Adding interactivity to widgets and Live Activities](https://developer.apple.com/documentation/widgetkit/adding-interactivity-to-widgets-and-live-activities)
- [W3 — Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy)
- [W4 — WidgetFamily.systemSmall](https://developer.apple.com/documentation/widgetkit/widgetfamily/systemsmall)
- [W5 — WidgetFamily.systemMedium](https://developer.apple.com/documentation/widgetkit/widgetfamily/systemmedium)
- [W6 — WidgetFamily.systemLarge](https://developer.apple.com/documentation/widgetkit/widgetfamily/systemlarge)
- [W7 — WidgetFamily.accessoryCircular](https://developer.apple.com/documentation/widgetkit/widgetfamily/accessorycircular)
- [W8 — Preparing widgets for additional platforms, contexts, and appearances](https://developer.apple.com/documentation/widgetkit/preparing-widgets-for-additional-contexts-and-appearances)
- [W9 — Configuring app groups](https://developer.apple.com/documentation/xcode/configuring-app-groups)
- [W10 — Keeping a widget up to date](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date)
