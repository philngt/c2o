# C2O Design v1.5 — SwiftUI profile

Áp dụng cho iOS, iPadOS và macOS native. Profile chuyển quyết định sản phẩm thành UI và bằng chứng trên Apple platforms; không phải thư viện component. Chỉ chọn mục liên quan đến thay đổi.

Áp dụng qua [hướng dẫn tích hợp C2O](../../../references/product-design.md) trong skill và mức can thiệp đang dùng. Brief/spec, acceptance và báo cáo hiện hữu giữ vai trò nguồn chuẩn; profile cung cấp lựa chọn kiểm tra, không tạo lifecycle, mode hay hồ sơ bắt buộc mới.

Khi khởi tạo app Lifestyle/Utility, dùng [Apple app templates](../app-templates/README.md) và [SwiftUI starter](../starters/apple/README.md) nếu cần source. Starter có deployment floor và phạm vi nhỏ riêng; nó chưa hiện thực hóa mọi pattern của profile hoặc thay thế kiểm chứng native.

## 1. Chốt phạm vi trước khi thiết kế

Ghi ngắn: `outcome`, flow bị ảnh hưởng, deployment targets, thiết bị/cửa sổ hỗ trợ, dữ liệu, locale, component hiện có và điều chưa biết. Outcome phải quan sát được, ví dụ: “người dùng tìm đúng vật dụng và sửa vị trí lưu, kể cả khi offline”.

Đọc màn tương tự, navigation, asset catalog và test hiện có trước. Tái sử dụng pattern đang phù hợp. Khi thay pattern, giải thích lợi ích cho thao tác, khả năng đọc hoặc phục hồi lỗi. Màu sắc, mật độ và độ trang trí là lựa chọn theo sản phẩm; không đặt tỷ lệ “đẹp” hay giới hạn card/gradient chung.

| Tình huống | Skill C2O liên quan khi cần | Bằng chứng theo phạm vi |
|---|---|---|
| Sửa hẹp, pattern đã rõ | `c2o-execute`; `c2o-verify` cho kiểm tra | Render vùng đổi và kiểm tra hành vi bị ảnh hưởng |
| Flow/component có state mới | `c2o-spec` hoặc `c2o-create` cho phần còn thiếu; `c2o-execute` khi đã yêu cầu code | Chạy flow và chọn các biến thể dễ gây lỗi |
| Navigation mới, nhiều platform hoặc giả định lớn | `c2o-shape` / `c2o-decide` cho quyết định còn mở; `c2o-create` cho prototype được giao | Prototype câu hỏi khó trước; mở rộng kiểm tra theo rủi ro còn lại |

Bảng chỉ gợi ý hoạt động và coverage trong C2O hiện có; bỏ qua phần đã rõ hoặc ngoài nhiệm vụ. Một sửa label không bắt buộc dựng lại bộ design system. Chọn một flow đại diện để kiểm tra quyết định chung khi hữu ích, rồi tiếp tục mọi flow, platform và deliverable đã cam kết.

## 2. Quy tắc triển khai

**System controls trước.** Dùng `Button`, `Toggle`, `TextField`, `List`, `Form` và navigation phù hợp khi đáp ứng outcome. Custom control cần lý do và phải có semantics, input, focus, states tương đương. Kiểm tra API theo SDK/deployment target của dự án.

**Typography và layout.** Ánh xạ token ngữ nghĩa sang text styles như `.body`, `.headline`, `.title`; font custom phải có scaling phù hợp. Dùng `@ScaledMetric` cho kích thước cần đi cùng text. Cho nội dung wrap, tăng chiều cao và đổi bố cục khi cần. Chỉ dùng fixed dimensions cho nội dung thực sự cố định; `minHeight` là mức sàn, không phải bảo đảm layout tốt. Xem chữ lớn trong UI thật, đặc biệt button, row, sheet và toolbar. [S1]

**Hit region.** Đo vùng tương tác, không suy ra từ kích thước icon. Apple nêu hướng dẫn chung vùng bấm 44×44 pt; đối chiếu control, platform và ngữ cảnh cụ thể. Control nhỏ phải dễ chọn, có khoảng cách hợp lý và không tạo vùng bấm chồng nhau. Không áp 44 pt như kích thước hình vẽ bắt buộc cho mọi control macOS. [S2]

**Semantic tokens.** Dùng vai trò như `text.primary`, `surface.grouped`, `action.destructive`. Ưu tiên semantic styles/colors của hệ thống; brand colors có asset appearances phù hợp. UIKit và AppKit cần mapping riêng ở nơi API khác nhau. Không chuyển nguyên bảng hex hoặc pixel của website sang native. Kiểm tra foreground trên nền thực, cả khi dùng material/transparency. [S3]

**State và hành động.** Chỉ xây state có nghĩa với control. Disabled phải ngăn hành động và giúp người dùng hiểu điều kiện khi cần. Loading phải quyết định chặn gửi trùng, giữ input, cho hủy hay cho tiếp tục; spinner không thay logic này. Dùng destructive role khi phù hợp, mô tả hậu quả và thiết kế undo/confirmation theo khả năng phục hồi. Không báo “đã lưu” trước khi đạt điều kiện lưu đã cam kết.

**Motion và VoiceOver.** Tôn trọng `accessibilityReduceMotion`; vẫn giữ phản hồi trạng thái. Tên accessible cần đủ nghĩa, giá trị/selection phải phản ánh dữ liệu. Group khi giúp đọc, tránh lặp label hoặc thêm trait vốn có. Hint mô tả kết quả khi cần. Thử thứ tự đọc, hành động và thay đổi focus trong flow, không chỉ kiểm tra sự tồn tại của modifier.

**Platform và localization.** Xác định navigation theo tác vụ và không gian hiện có. Kiểm tra iPad khi thu cửa sổ, macOS khi resize, keyboard/focus và safe area nơi liên quan. Dùng chuỗi có thể dịch, plural và format theo locale; thử tên dài và nội dung người dùng nhập. Thiết kế empty, error, stale và offline theo mô hình dữ liệu thật, giữ được công việc chưa lưu.

## 3. Chọn coverage có lý do

Chọn trường hợp đại diện; không nhân toàn bộ thiết bị × theme × locale × state nếu chưa có rủi ro cần giải quyết.

Chốt các biến thể bắt buộc cho từng criterion và ghi kết quả từng biến thể trong evidence hiện hữu. Chỉ gán `pass` khi tất cả phần bắt buộc đã có bằng chứng đạt; giữ `partial`, lỗi và phần chưa kiểm tra khi coverage chưa đủ. Tách criterion nếu cần theo dõi độc lập, giữ nguyên phạm vi đã cam kết.

| Nhóm | Quan sát cần thực hiện |
|---|---|
| Flow | Entry → thao tác chính → kết quả; quay lại/hủy và phục hồi lỗi liên quan |
| Text/layout | Cỡ mặc định và cỡ accessibility lớn; tên dài; nội dung không bị cắt hoặc che |
| Không gian/input | iPhone nhỏ hoặc cửa sổ hẹp; iPad/macOS nếu hỗ trợ; bàn phím mở và navigation vẫn dùng được |
| Appearance | Themes được hỗ trợ; contrast trên nền thật; Reduce Motion khi có chuyển động |
| Data | Empty, populated, loading/error; stale khi có nguồn dữ liệu từ xa; offline khi outcome cam kết dùng offline, kể cả kho hoàn toàn local; dữ liệu đã nhập sau retry |
| Language/accessibility | Locale gây expansion; RTL nếu hỗ trợ; VoiceOver và keyboard cho control thay đổi |

Các trường hợp có thể xác định ngoài phạm vi: macOS ngoài phạm vi sản phẩm; stale-network với màn hoàn toàn local không có nguồn dữ liệu từ xa; RTL ngoài danh sách locale hỗ trợ. Ghi lý do theo contract hiện hữu. Không miễn kiểm tra cỡ chữ lớn chỉ vì chưa thiết kế, hay offline chỉ vì chưa biết app sẽ phản ứng thế nào; kiểm tra bắt buộc chưa làm vẫn là `not-tested`.

## 4. Deliverable và xác minh

Giao thay đổi SwiftUI/asset thực tế khi nhiệm vụ yêu cầu code, kèm quyết định cần biết, coverage đã chọn và báo cáo kết quả. Nếu chỉ thiết kế, giao flow, state, token mapping và kết luận đúng artifact đã xem; nêu điều còn phải kiểm chứng khi triển khai, không suy ra bằng chứng runtime. Một flow đại diện không hoàn tất các deliverable khác đã cam kết.

Với review-only, dùng `c2o-verify` để đọc contract và artifact hiện tại, ghi findings và giới hạn; không sửa code/asset, thay acceptance hoặc thay đổi trạng thái của đối tượng đang review. Chỉ sửa lỗi trong vòng production đã được giao quyền, rồi kiểm tra lại phần bị ảnh hưởng.

Xcode previews giúp kiểm tra bố cục; build xác minh compilation; simulator/device xác minh thao tác. Chụp đúng UI của build đang đánh giá. HTML mockup hoặc ảnh sinh ra chỉ minh họa định hướng. Có thể dùng Accessibility Inspector và `performAccessibilityAudit()` trong UI tests theo môi trường hỗ trợ; audit chỉ kiểm tra màn đang mở và không thay VoiceOver. [S4]

Trong acceptance/báo cáo và evidence hiện hữu, ghi criterion, artifact/revision, check, scope, phương pháp, quan sát và giới hạn. Giữ `pass`, `partial`, `fail`, `not-tested` theo C2O:

- `pass`: bằng chứng hiện tại bao phủ đầy đủ tiêu chí bắt buộc trong phạm vi.
- `partial`: đã có một phần bằng chứng nhưng coverage hoặc kết quả cần thiết còn chưa đủ; giữ chi tiết từng phần.
- `fail`: có bằng chứng không đạt; chỉ rõ bước tái hiện và phần chưa kiểm tra nếu còn.
- `not-tested`: chưa thực hiện hoặc đang bị chặn; nêu lý do như thiếu Xcode/runtime hay fixture, không chuyển thành miễn áp dụng.

Chỉ khi đã chọn rõ profile JSON legacy cho phạm vi này mới dùng `verification.json` với `criterion_id`, `status`, `rationale`, `inputs`, `evidence`, path và SHA-256 theo [hợp đồng bằng chứng](../core/evidence.md). `PASS` / `FAIL` ghi kết quả đã quan sát; `NOT_RUN` / `BLOCKED` giữ kiểm tra chưa chạy và lý do; `NOT_APPLICABLE` cần contract cho phép cùng lý do đúng phạm vi. Profile này không có trạng thái tương đương đầy đủ cho C2O `partial`: giữ chi tiết trong evidence và báo cáo C2O, không ép thành `PASS`, bỏ lỗi hoặc tạo nguồn acceptance cạnh tranh.

Không chuyển build thành công thành `pass` cho UX, hoặc kiểm tra token thành `pass` cho VoiceOver. Cài đặt công cụ cũng chưa phải bằng chứng đã chạy. Tài liệu profile này không chứng nhận bất kỳ native test nào đã được thực hiện.

## 5. Asset trong native UI

Giữ thông tin asset, baseline và layout cần cho nhiệm vụ tại nguồn hiện có theo [hợp đồng asset](../core/assets.md); manifest riêng là tùy chọn. Tách artwork khỏi native controls, text và đồ thị dữ liệu. Mockup chọn hướng thị giác; screenshot từ app thật mới chứng minh asset đã tích hợp.

Ưu tiên SF Symbols hoặc icon family hiện có cho hành động quen thuộc. Custom icon cần lý do về ý nghĩa/brand, cùng kiểm tra kích thước sử dụng và accessible label. Giữ artwork tương tác bên trong control đúng semantics. [S5]

Ảnh specimen/sản phẩm thật phải giữ nguồn và đặc điểm nhận diện. Không redraw hoặc đổi màu để khớp palette nếu làm sai dữ kiện. Illustration sinh ra được phân loại riêng, không đóng vai ảnh record hay bằng chứng thuộc tính. Giữ text và quan hệ dữ liệu dưới dạng nội dung có thể cập nhật.

Trước export, ghi kích thước nguồn, kích thước hiển thị dự kiến, crop/focal area, alpha, appearance và fallback. Xem asset trên nền thật ở cỡ sử dụng; kiểm tra viền alpha, crop mất chi tiết, upscale và light/dark. Sau import, xác nhận target tham chiếu đúng file, rồi render build thật. Export hợp lệ và compile thành công là hai bằng chứng khác với runtime.

Phân biệt format, khả năng decoder đọc file và player phát animation. Ghi runtime/player được chọn; thử loop, timing và lifecycle trong app. Với Reduce Motion, cung cấp frame tĩnh hoặc phản hồi giảm chuyển động mà vẫn giữ ý nghĩa trạng thái. Thiếu player hoặc môi trường native phải được ghi `not-tested` cùng lý do bị chặn hoặc chưa chạy; giữ phần bằng chứng đã có.

App icon theo target/toolchain hiện tại: dùng Asset Catalog hoặc [Icon Composer](https://developer.apple.com/icon-composer/) phù hợp; kiểm tra appearance và mask thực. Không áp một bảng kích thước hoặc safe zone chung cho mọi platform. Đây là yêu cầu kiểm chứng, không xác nhận đã chạy các phép kiểm tra.

## 6. Component, data view và composition

Áp dụng [hợp đồng component](../core/components.md), [data view](../core/data-views.md) và [composition](../core/ui-composition.md) vào model/state/navigation thực của dự án. Catalog chưa phải package SwiftUI có thể import. Chọn control/container hệ thống theo task và API của deployment target; thuật ngữ hay keyboard rule của ARIA web không được chuyển nguyên sang native.

Ghi selection bằng ID ổn định, query thuộc tập nào, draft thuộc record nào và nơi commit dữ liệu. Row phát ý định chọn record; field thay đổi draft; screen/logic tác vụ xử lý đổi selection, rời form, lưu/hủy và lỗi. Đây là phân chia trách nhiệm thiết kế, không áp đặt một kiến trúc persistence hay property wrapper chung.

Chọn list, collection, table, chart hoặc canvas vì câu hỏi người dùng cần trả lời. Với list–detail, thích ứng theo không gian thực và giữ selection/draft; native split navigation có cơ chế thích ứng số cột, nhưng hành vi cụ thể phải đối chiếu target và kiểm tra trong app. [S6] Không suy native readiness từ wireframe, HTML preview hoặc hợp đồng đã điền.

## Nguồn nền tảng

- [S1 — Apple: Dynamic Type, layout và Xcode previews](https://developer.apple.com/videos/play/wwdc2024/10074/)
- [S2 — Apple HIG: Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
- [S3 — Apple: SwiftUI Color](https://developer.apple.com/documentation/swiftui/color)
- [S4 — Apple: Performing accessibility audits](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app)
- [S5 — Apple HIG: Image views và interface icons](https://developer.apple.com/design/human-interface-guidelines/image-views)
- [S6 — Apple WWDC25: What’s new in SwiftUI](https://developer.apple.com/videos/play/wwdc2025/256/)
