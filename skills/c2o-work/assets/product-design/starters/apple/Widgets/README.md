# Widget đọc bản tóm tắt

`C2OSummaryWidget.swift` là source cho WidgetKit extension iOS/iPadOS 17+ và macOS 14+. Cùng source được gắn vào **hai extension target riêng**, không gắn vào host app target. Chưa build bằng Xcode hoặc chạy trên Apple runtime trong môi trường soạn bộ starter.

## Hợp đồng tích hợp

Target link package `StarterCore`; module cung cấp static `AppProfile.category`, `displayName`, `urlScheme`, `widgetsEnabled`, `widgetKind` và `WidgetSnapshotStore.read() throws -> WidgetSnapshot?`. `WidgetSnapshot` có `category`, `title`, `subtitle`, `updatedAt`, `route`. Widget không mở kho record, nội dung text workbench hoặc lịch sử riêng của app.

Host công bố snapshot đã lược dữ liệu riêng tư vào App Group sau khi lưu thành công. Sau đó host gọi `WidgetCenter.shared.reloadTimelines(ofKind: AppProfile.widgetKind)`. Lỗi công bố widget phải được xử lý riêng với lỗi lưu domain: không báo record lưu thất bại khi record thực tế đã được lưu. Nếu cần thử lại, host thử lại xuất bản snapshot hiện hành; không tạo bản sao record.

Provider trả một entry với policy `.never` vì nội dung này chỉ đổi khi host thay snapshot; không lên lịch polling. Yêu cầu reload là yêu cầu tới WidgetKit, không phải cam kết cập nhật tức thời. Nếu một sản phẩm có dữ liệu dự báo theo thời gian, thay timeline/policy theo hợp đồng sản phẩm và giữ semantics thời điểm dữ liệu. Xem [platform contract](../../../app-templates/platforms/widgets.md).

| Trường hợp | UI nguồn này |
| --- | --- |
| Đọc được snapshot đúng category và route | Title/subtitle tóm tắt, ngày cập nhật; medium/large có thêm giờ |
| `read()` trả `nil` | “Chưa có bản tóm tắt”; mở app để bắt đầu |
| `read()` throw, category/route sai hoặc title rỗng | “Chưa đọc được bản tóm tắt”; mở app để kiểm tra và thử lại |
| `context.isPreview` hoặc placeholder | Nội dung trung tính ghi rõ minh họa; không đọc disk/network |

`systemSmall`, `systemMedium`, `systemLarge` có bố cục riêng. Nội dung không phải bảng hoặc danh sách cuộn. Widget chỉ có một deep link: `<scheme>://collection` cho Lifestyle hoặc `<scheme>://utility` cho Utility. Không có button/toggle thay đổi domain data; thêm App Intent là thay đổi phạm vi riêng.

Generator bật extension bằng `--widgets`: iOS app `<base>.ios`, extension `<base>.ios.widgets`; macOS app `<base>.macos`, extension `<base>.macos.widgets`. Các target liên quan dùng đúng cùng App Group trên thiết bị đó: mặc định `group.<base>`, hoặc ID đã đăng ký truyền qua `--app-group`. App Group không đồng bộ dữ liệu giữa iPhone/iPad/Mac. Cấu hình signing, provisioning và truy cập container thực tế phải được kiểm tra trên Apple platform; tạo entitlement file chưa chứng minh container đọc được.

## Kiểm tra còn phải thực hiện

Build từng extension và host bằng Xcode với deployment target đã ghi; chạy từng family trên iPhone, iPad và Mac; thử empty/read error/real snapshot, đường mở app khi app đang đóng hoặc đang mở, publish → reload, widget vẫn hiện dữ liệu cũ trước reload, light/dark và các rendering mode được OS hỗ trợ, cỡ chữ và VoiceOver. Kiểm tra cả font/spacing riêng trên macOS. Thử khi thiết bị bị khóa nếu sản phẩm cung cấp dữ liệu nhạy cảm hơn snapshot mẫu.

Nguồn, matrix platform và các lựa chọn mở rộng nằm trong [widgets.md](../../../app-templates/platforms/widgets.md). Đây là source starter, chưa có bằng chứng build/runtime hay chứng nhận sẵn sàng App Store.
