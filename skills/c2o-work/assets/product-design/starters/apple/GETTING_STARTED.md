# Khởi động dự án Apple được tạo

## 1. Những gì đã tạo

Root `project.json` là **XcodeGen specification**, không phải Xcode project đã generate. `App/`, `StarterCore/` và `Widgets/` nếu bật là source thật. `.design/project.json` và `.design/verification.json` là **scaffold của profile JSON tùy chọn**, report khởi đầu `NOT_RUN`; chúng khác XcodeGen spec và không tự trở thành acceptance của dự án. Giữ nguồn C2O/spec/tracker hiện có; chỉ chọn JSON làm nguồn chuẩn cho scope mới hoặc bản xuất phụ thuộc nguồn chuẩn khi thực sự hữu ích.

Hai app target dùng cùng SwiftUI source: `<Name>_iOS` cho iPhone/iPad và `<Name>_macOS` cho native Mac. Target widget riêng được nhúng vào app tương ứng khi bật. Preset category lấy từ Info.plist; không cần sửa thủ công nhiều chuỗi trong source.

## 2. Mở trên Mac

Cần Xcode với SDK hỗ trợ deployment floor iOS/iPadOS 17 và macOS 14, command line tools được chọn đúng, Python 3.9+ nếu chạy generator, và XcodeGen hỗ trợ specification (gói đặt mức tối thiểu 2.44.0). Chọn phiên bản tool hiện hành phù hợp dự án; starter chưa có kết quả build trên một bản Xcode cụ thể.

XcodeGen là dependency của bước tạo project, không là package runtime. Cài theo [hướng dẫn chính thức](https://github.com/yonaskolb/XcodeGen). Trong thư mục dự án mới:

```bash
xcodegen generate --spec project.json
```

Mở `<Name>.xcodeproj`, chọn scheme `<Name>_iOS` hoặc `<Name>_macOS`. Trước khi chạy trên thiết bị hoặc widget, chọn Development Team và kiểm tra Signing & Capabilities cho từng target.

## 3. Widget và App Group

Nếu có widget, cả app và extension tương ứng cần cùng App Group đã được cấp cho team. Group trong Info.plist `C2OAppGroupID` phải khớp entitlement. Nếu bạn đổi group, sửa specification và generate lại; tránh để sửa tay trong project bị mất ở lần generate sau.

Đọc [Apple App Groups](https://developer.apple.com/documentation/xcode/configuring-app-groups) và cấu hình theo môi trường thật. Generator không đăng ký group hoặc sửa tài khoản Apple Developer. App dùng kho riêng; chỉ snapshot count/status được đưa sang group. Lỗi cập nhật snapshot không biến một lần lưu record thành thất bại sau khi record đã commit.

Chạy app, tạo dữ liệu/thực hiện tác vụ, thêm widget rồi kiểm tra small/medium/large và deep link. Timeline reload là yêu cầu gửi cho hệ thống; không cam kết cập nhật đúng một thời điểm. Chưa cấu hình group thì widget phải phản hồi absence/error, không hiện dữ liệu ví dụ như dữ liệu thật.

## 4. Test và build

Các lệnh sau cần chạy trên Mac. Thay `MyCollection` bằng tên project thật:

```bash
swift test --package-path StarterCore
xcodebuild -project MyCollection.xcodeproj -scheme MyCollection_iOS -destination 'generic/platform=iOS Simulator' CODE_SIGNING_ALLOWED=NO build
xcodebuild -project MyCollection.xcodeproj -scheme MyCollection_macOS -destination 'platform=macOS' CODE_SIGNING_ALLOWED=NO build
```

Hai lệnh build không signing kiểm tra compilation; chúng không chứng minh widget group, entitlement, runtime, accessibility hoặc phát hành. Chạy scheme có signing phù hợp trong Xcode để kiểm tra các phần đó. [NATIVE_CHECKS.md](NATIVE_CHECKS.md) nêu các phép kiểm tra flow cần làm.

Ghi kết quả trong nguồn acceptance/evidence hiện có, dùng `pass`, `partial`, `fail`, `not-tested` nếu theo C2O. Các lệnh native ở trên chưa được chạy bởi generator. Chỉ khi đã chủ động chọn profile JSON, có thể kiểm tra hồ sơ bằng lệnh sau từ root ứng dụng; thay `/path/to/c2o` bằng checkout C2O thực:

```bash
python3 /path/to/c2o/skills/c2o-work/assets/product-design/tools/design_check.py validate --root . --project .design/project.json --report .design/verification.json
```

Exit 2 là kết quả mong đợi khi các tiêu chí JSON còn `NOT_RUN`. CLI kiểm tra hồ sơ; không chạy Xcode thay bạn. `RECORDS_READY` không phải verdict sản phẩm, trạng thái C2O `DONE` hoặc quyền phát hành. Profile JSON không có trạng thái biểu diễn đầy đủ `partial`; giữ phần đạt/phần thiếu và verdict thật trong C2O, không đổi thành `PASS` hoặc tạo hai nguồn kết quả độc lập.

## 5. Tùy biến trước khi thành sản phẩm

Bộ tài nguyên ở `skills/c2o-work/assets/product-design` trong repo C2O có `documentation/README.md` và `templates/product/product-pack.md` cho business assumptions, blueprint, PRD, domain, UX/UI, technical và release plan. Dùng tài liệu dự án hiện có trước; chỉ bổ sung đoạn hoặc mẫu cần thiết và sửa refs theo vị trí thật. Không cần metadata retrofit hoặc bộ tài liệu mới. Giữ criterion/report thật ở nguồn đã chọn, không chép đè bằng scaffold hoặc ví dụ. Những file product templates này không được generator tự chép/điền.

Chốt outcome và archetype; thay tên/microcopy/domain; chọn locale thực; tạo app icon/brand assets và kiểm tra render; xác định chiến lược backup/export/migration nếu app lưu dữ liệu có giá trị. Starter có UI tiếng Việt; chưa có bộ bản dịch nhiều ngôn ngữ đã review.

Settings/help hiện giải thích chức năng local của starter. Khi sản phẩm có hỗ trợ người dùng, thêm địa chỉ/kênh hỗ trợ thật. Khi có permissions, thông báo, purchase, account, analytics hoặc cloud, bổ sung module tương ứng và acceptance riêng.

Privacy manifest và App Store privacy labels phải dựa trên code/dependency thực khi phát hành. Starter không tự tuyên bố compliance hoặc điền các lý do API chưa dùng. Source hiện dùng file store thay UserDefaults; kiểm tra lại khi thêm SDK/API. Không coi template privacy trống hoặc build thành công là kết quả review.

Tên category mặc định của macOS là Lifestyle hoặc Utilities theo preset. Cần đánh giá lại category/listing theo chức năng cốt lõi thật của sản phẩm; template không quyết định thay bạn.
