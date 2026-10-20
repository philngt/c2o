# SwiftUI Apple starter

Source starter tùy chọn từ **C2O Design v1.5.0**, dùng chung cho Lifestyle collection và Utility text workbench. SwiftPM tools version 5.9, Swift language mode 5; deployment floor iOS/iPadOS 17, macOS 14. Có nguồn widget cho cả hai nền tảng; generator đưa extension vào project khi bật `--widgets`. Chỉ chạy generator khi tạo source thuộc phạm vi nhiệm vụ C2O hiện có.

## Tạo một bản độc lập

Chạy từ thư mục này, chọn một category. Thay đường dẫn ví dụ bằng thư mục mới đã chọn cho ứng dụng, ngoài checkout C2O:

```bash
python3 create_project.py --category lifestyle --name MyCollection --bundle-id com.example.mycollection --display-name "Bộ sưu tập" --output /path/to/projects/MyCollection --widgets
```

Hoặc:

```bash
python3 create_project.py --category utility --name MyTool --bundle-id com.example.mytool --display-name "Công cụ" --output /path/to/projects/MyTool
```

Đường `--output` phải chưa tồn tại. Dùng một vị trí bên ngoài thư mục starter. Có thể thêm `--team` với team ID thật và `--app-group` với App Group đã đăng ký; không đặt credential trong file. Nếu không truyền group, preset dùng `group.<bundle-id>` khi có widget; bạn vẫn cần đăng ký/cấu hình signing phù hợp.

## Các phần trong gói

| Đường dẫn | Trách nhiệm |
| --- | --- |
| App/ | SwiftUI app, hai root flow, state/draft, Settings/help, navigation theo platform |
| StarterCore/ | Package Foundation cho model, local store, text logic, route và widget snapshot; có XCTest source |
| Widgets/ | WidgetKit provider và view theo family; đọc snapshot, mở app |
| create_project.py | Tạo bản source mới và XcodeGen `project.json`, hai app target, widget target tùy chọn |
| tests/ | Kiểm tra generator không ghi đè, identifier, target/dependency, profile và hồ sơ evidence |
| [GETTING_STARTED.md](GETTING_STARTED.md) | Cách sinh Xcode project, signing, test/build và các giới hạn |
| [NATIVE_CHECKS.md](NATIVE_CHECKS.md) | Các trường hợp kiểm tra trước khi dùng starter trong sản phẩm |

Generator không chỉnh code bằng thay chuỗi tùy tiện: `AppProfile` đọc category, tên hiển thị, URL scheme và App Group từ Info.plist từng target. Cùng source được build cho từng category. App bundle iOS và macOS có suffix riêng; không tự tạo universal purchase hoặc một App Store listing chung.

## Phạm vi source

Lifestyle giữ title/notes/favorite theo UUID, có tìm kiếm, thêm/sửa và xóa. Utility chuẩn hóa toàn bộ whitespace thành một khoảng trắng; đếm Swift grapheme clusters, token ngăn bởi whitespace và số dòng theo quy ước trong `TextTools.swift`. Word count này không là phân tích ngôn ngữ. Mỗi chức năng có output thật từ input hiện tại.

Dữ liệu app ở Application Support, widget chỉ nhận snapshot count/status riêng. History Utility mặc định tắt; khi bật giữ tối đa 50 kết quả gần đây theo preset. Không có mạng, telemetry, login, cloud hoặc paywall được thêm sẵn. Lưu local không đồng nghĩa backup hoặc sync. File JSON không cung cấp mã hóa bổ sung ngoài cơ chế của hệ điều hành; với dữ liệu nhạy cảm cần chọn storage phù hợp.

Thiết kế persistence cố ý nhỏ: một main window/scene, một app writer, widget chỉ đọc snapshot. Khi cần nhiều cửa sổ chỉnh cùng dữ liệu, background writers, tập dữ liệu lớn, migration hoặc sync, thay repository và kiểm tra xung đột theo nghiệp vụ. Không tăng scope chỉ bằng việc đổi Window thành WindowGroup.

## Trạng thái kiểm chứng

Nguồn Swift, XCTest và cấu hình đã được viết; lần tích hợp này chưa chạy Swift/Xcode/XcodeGen hoặc UI native. Các kiểm tra native giữ `not-tested` cùng lý do trong nguồn acceptance/evidence C2O hiện có. Không suy native `pass` từ generator chạy thành công. Dùng [NATIVE_CHECKS](NATIVE_CHECKS.md) để chọn kiểm tra phù hợp với scope ứng dụng thật.

Generator luôn kèm `.design/project.json` và `.design/verification.json` như scaffold của **profile JSON tùy chọn**, khởi đầu `NOT_RUN`. Chúng không ghi đè hoặc tự thay nguồn acceptance hiện có. Chỉ chủ động chọn profile này khi có ích; xem [hợp đồng evidence](../../core/evidence.md). C2O giữ `partial` và các phần chưa kiểm tra ngay cả khi JSON checker trả `RECORDS_READY`. Root `project.json` khác hai file trên: đó là XcodeGen specification phục vụ tạo project.

## Nguồn triển khai

- [XcodeGen Project Spec](https://github.com/yonaskolb/XcodeGen/blob/master/Docs/ProjectSpec.md): JSON/YAML, local package, target, info và entitlement configuration.
- [Apple: Configuring app groups](https://developer.apple.com/documentation/xcode/configuring-app-groups): group và signing cho app/extension.
- [Apple: WidgetKit](https://developer.apple.com/documentation/widgetkit): provider, timeline, family và widget navigation.

Source trong starter được viết cho bộ framework này, không kèm source của XcodeGen hoặc repo tham khảo.

## Tài liệu sản phẩm đi cùng source

Starter tạo source/configuration và scaffold hồ sơ JSON. Để thiết kế sản phẩm, dùng tài liệu hiện có; chọn đoạn còn thiếu từ [product pack gộp](../../templates/product/product-pack.md) hoặc các [mẫu business/blueprint/PRD/specs](../../documentation/README.md). Xem bản điền minh họa cho [Lifestyle](../../examples/lifestyle-docs/product-pack.md) và [Utility](../../examples/utility-docs/product-pack.md). Mỗi trách nhiệm giữ một nguồn chuẩn; không bắt tạo đủ bộ, gắn metadata vào mọi tài liệu hoặc đổi acceptance chỉ vì dùng starter. Generator không tự xác thực nhu cầu hoặc chọn business model.
