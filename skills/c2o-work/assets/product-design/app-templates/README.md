# Template ứng dụng Apple — Lifestyle và Utility

Tài nguyên tùy chọn, thích ứng từ **C2O Design v1.5.0**. Bộ này nối các catalog component/layout/data view với cấu trúc một ứng dụng. Có blueprint để chọn module và SwiftUI starter source khi nhiệm vụ yêu cầu scaffolding. C2O hiện có vẫn giữ scope, quyền quyết định và acceptance. Chưa build hoặc chạy UI native trong lần tích hợp này.

## Chọn một điểm khởi đầu

| Bạn đang xây | Template | Source starter đi kèm |
| --- | --- | --- |
| Quản lý sở thích, bộ sưu tập, nhật ký hoặc việc trong đời sống | [Lifestyle](categories/lifestyle.md) | Collection: tạo/sửa/xóa bản ghi, tìm kiếm, yêu thích, lưu cục bộ |
| Hoàn thành một thao tác rõ, tra cứu hoặc xử lý dữ liệu | [Utility](categories/utility.md) | Text workbench: nhập → normalize/count → kết quả → copy/share; lịch sử tùy chọn |

Tên category giúp chọn nhu cầu xuất phát. Task, dữ liệu và nền tảng quyết định UI. Các nhánh planner/journal/file utility là blueprint có điều kiện; source hiện thực hóa hai flow nhỏ trong bảng, không chứa mọi tính năng của mọi app.

## Các phần ghép thành template

1. **Category blueprint** xác định tác vụ, màn và dữ liệu của dòng app.
2. **[Module matrix](module-matrix.md)** chọn phần cốt lõi, phần cần khi có tính năng tương ứng và phần có thể hoãn.
3. **Platform recipe** cho [iPhone](platforms/iphone.md), [iPad](platforms/ipad.md), [macOS](platforms/macos.md) và [widget](platforms/widgets.md).
4. **Catalog hiện có** chọn [component](../catalog/components.md), [data view](../catalog/data-view-patterns.md), [layout](../catalog/layout-patterns.md) và [screen composition](../core/ui-composition.md).
5. **[SwiftUI starter](../starters/apple/README.md)** cùng generator và scaffold JSON tùy chọn để tham khảo acceptance.

Không cần nạp tất cả tài liệu trong mỗi tác vụ. Khi sửa một field, đọc contract của field và màn liên quan. Khi khởi tạo app, đọc category, module matrix và các nền tảng thực sự hỗ trợ.

## Những phần đã có trong source

| Phạm vi | Đã viết trong starter | Cần kiểm chứng trên Mac/thiết bị |
| --- | --- | --- |
| Shell | Entry theo category; navigation theo platform; Settings/help | Launch, resize, back, focus và menu |
| Lifestyle | Model ID ổn định, collection, editor/draft, local save, favorite và delete | Persistence, lỗi ghi/đọc, cancel và selection |
| Utility | Text transform/count, input/result, copy/share; history opt-in | Unicode, clipboard/share, lưu/xóa history, giữ input khi lỗi |
| Storage | JSON trong Application Support của app; atomic file write; lỗi decode được giữ | Sandbox, lifecycle, sự cố storage và nhu cầu migration của sản phẩm |
| Widget | Snapshot count/status riêng, các cỡ small/medium/large, deep link | Signing/App Group, timeline thực, các state và mở đúng app |
| Project | Generator tạo hai app target và hai widget extension target khi bật | XcodeGen generation, Xcode compilation và signing |

Auth, cloud sync, purchases, notifications, interactive widget App Intents, Live Activities và các capability khác có điều kiện trong blueprint; chưa được implement trong source này.

## Hồ sơ sản phẩm đi cùng template

Dùng [hệ thống tài liệu](../documentation/README.md) để chọn business design, product blueprint, PRD, domain, feature/technical specs và kế hoạch kiểm chứng/phát hành. App nhỏ có thể gộp vào một [product pack](../templates/product/product-pack.md). Hai bản điền [Lifestyle](../examples/lifestyle-docs/product-pack.md) và [Utility](../examples/utility-docs/product-pack.md) khớp scope source starter; business vẫn là giả thuyết và native evidence chưa có.

Generator bên dưới không tự chép/điền toàn bộ bộ tài liệu sản phẩm. Tái sử dụng tài liệu và acceptance hiện có; chỉ thêm đoạn hoặc template đang thiếu. Các file `.design/` do generator tạo là scaffold của profile JSON tùy chọn. Chúng không tự trở thành nguồn chuẩn hay thay `.context/acceptance.md`, spec hoặc tracker. Nếu chọn dùng JSON cho scope mới, ghi rõ quyền sở hữu; nếu dùng làm bản xuất để kiểm tra, giữ nó phụ thuộc nguồn chuẩn. Không chép đè hồ sơ thật bằng ví dụ.

## Tạo dự án mới

Chỉ chạy khi đã yêu cầu tạo source. Từ root của repo C2O, chọn một lệnh và thay `/path/to/projects/...` bằng **thư mục mới được chọn cho ứng dụng**, ngoài checkout C2O:

```bash
python3 skills/c2o-work/assets/product-design/starters/apple/create_project.py --category lifestyle --name MyCollection --bundle-id com.example.mycollection --output /path/to/projects/MyCollection --widgets
python3 skills/c2o-work/assets/product-design/starters/apple/create_project.py --category utility --name MyTool --bundle-id com.example.mytool --output /path/to/projects/MyTool --widgets
```

Thay tên và bundle ID bằng dự án của bạn. Bỏ `--widgets` nếu app không có một công việc hữu ích ngoài màn chính. Generator chỉ tạo thư mục mới; từ chối ghi lên thư mục đã tồn tại. Nó không cài tool, đăng ký identifier, cấp quyền, build hoặc publish.

Sau đó làm theo `GETTING_STARTED.md` trong dự án được tạo. iOS/iPadOS 17 và macOS 14 là deployment floor của starter này, không phải tuyên bố đó là OS/SDK mới nhất. Khi phát hành, chọn toolchain/SDK và yêu cầu hiện hành phù hợp.

## Nhất quán khi tùy biến

Dùng chung nghĩa của dữ liệu, token và kết quả hành động. Chọn control/navigation theo mỗi nền tảng; iPad không phải iPhone phóng to và macOS cần keyboard/menu/window behavior. Widget dùng snapshot đã giảm thông tin và mở đúng ngữ cảnh, không sao toàn màn app vào một khung nhỏ.

Ghi baseline dự án khi cần và cập nhật nguồn hiện có khi thay luật dùng chung. Chọn contract liên quan làm đầu vào cho review theo acceptance C2O. Source là implementation khởi đầu cần xác minh, không chứng minh mọi pattern trong catalog đã được code.
