# Product blueprint — [tên sản phẩm]

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-PRODUCT-BLUEPRINT` |
| Phiên bản template | `1.1.0` |
| Mục đích | Lập bản đồ actor → capability → flow → domain → screen/surface → platform và ranh giới để tìm đúng hợp đồng chi tiết. |
| Dùng khi | App mới có nhiều flow/nền tảng/kênh, nhiều người triển khai hoặc sản phẩm hiện có thiếu bản đồ chung; một flow nhỏ đã rõ có thể dùng brief và experience. |
| Đầu vào | [Brief](../brief.md), [business design](business-design.md) nếu áp dụng, [PRD](prd.md), code/tài liệu hiện có và support contract. |
| Đầu ra / bàn giao | Bản đồ năng lực, ranh giới và liên kết đặc tả để chọn một slice đầu đến cuối; câu hỏi còn mở có phần bị ảnh hưởng và owner. |
| Nguồn chuẩn | Khi được đăng ký, blueprint giữ bản đồ quan hệ. PRD giữ định nghĩa/phạm vi/ưu tiên F và REQ; [domain model](domain-model.md) giữ ENT/BR; [experience](../experience.md), [screen](../screen.md) và [technical spec](technical-spec.md) giữ hợp đồng chi tiết. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Sản phẩm / phiên bản / OUT-01 / platform-kênh và phần ngoài scope] |

[Chuẩn template](../../documentation/template-standard.md). Placeholder là chỗ cần điền, không phải bằng chứng. Phiên bản template theo dõi mẫu dùng chung; revision tài liệu theo dõi bản được điền cho dự án.

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, tách khỏi trạng thái quyết định và kết quả kiểm chứng. `accepted` nghĩa là chọn dùng tài liệu trong phạm vi quyền hạn hiện có; không chứng minh người dùng đã phê duyệt, test đã đạt hoặc có quyền phát hành.

Giữ nguồn chuẩn đã đăng ký trong [document index](document-index.md); không tự thay owner của thông tin chỉ vì sao chép template. Đọc [hướng dẫn bộ tài liệu](../../documentation/README.md) và cập nhật đường dẫn/ID mẫu thành tham chiếu thật của dự án.

## 1. Đích đến và ranh giới

- Outcome tham chiếu: [OUT-01 và nguồn chuẩn].
- Actor chính và tác vụ cần hoàn tất: [...].
- Điểm bắt đầu/kết thúc trách nhiệm của sản phẩm: [...].
- Hệ thống, người hoặc quy trình bên ngoài mà sản phẩm phụ thuộc: [...].
- Phần nằm ngoài scope: [tham chiếu PRD; chỉ ghi ranh giới cần hiểu ở bản đồ này].

## 2. Bản đồ năng lực

`F-01` là feature/capability, không phải flow. Flow dùng tên và anchor trong experience hoặc feature spec; một capability có thể có nhiều flow, một screen có thể phục vụ nhiều capability.

| Actor | Capability | Flow / anchor | Domain liên quan | Screen / surface | Platform / kênh | Ranh giới đi qua |
| --- | --- | --- | --- | --- | --- | --- |
| [vai trò] | F-01 — [tên theo PRD] | [tên; đường dẫn + anchor] | ENT-01; BR-01 | SCR-01 / [surface khác] | [trong support contract] | [local / dịch vụ / con người] |

Không buộc mỗi hành động phải có một màn hình mới. Widget, lệnh bàn phím hoặc thao tác hệ thống có thể là surface; tham chiếu hợp đồng tương ứng thay vì gọi tất cả là screen.

## 3. Tóm tắt các flow thuộc scope

| Tên flow | Entry / điều kiện vào | Kết quả và điểm commit | Nhánh cần đặc tả | Nguồn chi tiết |
| --- | --- | --- | --- | --- |
| [cùng tên/anchor ở bảng trên] | | | [hủy, lỗi, khôi phục có áp dụng] | [experience / feature spec] |

Chỉ ghi điều giúp hiểu liên kết giữa các phần. Field validation, state transition và cách giữ draft nằm trong hợp đồng chi tiết; không sao chép toàn bộ vào blueprint.

## 4. Ranh giới dữ liệu và nền tảng

| Phần/hệ thống | Trách nhiệm sản phẩm | ENT-xx và nguồn dữ liệu chuẩn | Ai được đọc/ghi, ở mức vai trò | Hợp đồng chi tiết |
| --- | --- | --- | --- | --- |
| [phần bên trong hoặc bên ngoài] | | | | [domain / technical / service blueprint] |

| Platform / form factor | Tác vụ và điểm vào hỗ trợ | Cấu trúc thích ứng | Context/dữ liệu cần giữ | Nguồn quy định |
| --- | --- | --- | --- | --- |
| [nền tảng thực trong scope] | [F-01; tên flow] | [navigation/surface ở mức tổng thể] | | [experience / screen / profile dự án] |

Đánh dấu rõ phần chưa hỗ trợ. Hợp đồng quyền truy cập, đồng bộ, giao tiếp và lỗi xuyên ranh giới cần trỏ về spec; sơ đồ tổng thể không tự chứng minh các cơ chế đó đã tồn tại.

## 5. Chỗ còn mở và phần triển khai đầu tiên

| Câu hỏi ảnh hưởng bản đồ | Nguồn theo dõi | Phần bị ảnh hưởng | Owner / bước giải quyết |
| --- | --- | --- | --- |
| [ranh giới hoặc quan hệ chưa chốt] | [ASM-01 / ADR-01 nếu phù hợp] | [F-01; ENT-01; SCR-01] | |

- Slice đang chọn: [SL-01 và bản điền của delivery plan](delivery-plan.md).
- Feature/flow/domain/screen cần nối trong slice đó: [...].
- Cách kiểm chứng quan hệ quan trọng: [validation plan](validation-plan.md); [criterion IDs trong nguồn acceptance đã chọn của dự án].

## Điều kiện kết thúc bản này

Mỗi capability trong scope có actor, flow, domain và nền tảng rõ; ghi surface cần thiết hoặc lý do không có UI. Mỗi thông tin chi tiết có nguồn chuẩn; ranh giới chưa chốt đã được nêu cùng tác động tới slice. ID và liên kết ở đây phục vụ review thủ công, không phải quan hệ ngữ nghĩa được validator tự xác minh.

## Kiểm tra trước bàn giao

- [ ] Mỗi capability trong scope trỏ tới F theo PRD và có actor, flow tên/anchor, domain và platform phù hợp.
- [ ] Screen, widget hoặc surface khác chỉ xuất hiện khi phục vụ tác vụ; phần không có UI được giải thích.
- [ ] Entry, kết quả, điểm commit và nhánh quan trọng trỏ tới nguồn chi tiết, không tạo bản behavior thứ hai.
- [ ] Ranh giới đọc/ghi và hỗ trợ nền tảng được ghi đúng scope; cơ chế chưa có không bị mô tả là đã triển khai.
- [ ] Đã dẫn tới slice canonical, câu hỏi chặn và validation; các ID/link quan trọng đã được đối chiếu thủ công.
