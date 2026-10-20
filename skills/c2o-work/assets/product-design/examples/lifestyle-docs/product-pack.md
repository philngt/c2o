# Product pack minh họa — Lifestyle Collection

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-PRODUCT-PACK` |
| Phiên bản template | `1.1.0` |
| Mục đích | Minh họa pack cho flow tạo, tìm, sửa và lưu bộ sưu tập cá nhân |
| Dùng khi | Cần xem một bản điền để khởi đầu app nhỏ từ source starter tương ứng |
| Đầu vào | Source và category refs trong [index](#1-index-và-bằng-chứng-đầu-vào); chưa có dữ liệu nghiên cứu khách hàng |
| Đầu ra / bàn giao | Phạm vi, behavior và kế hoạch tích hợp/kiểm chứng minh họa cho bước tiếp theo |
| Nguồn chuẩn | Sections đăng ký trong index chỉ có authority trong ví dụ này; khi áp dụng cho dự án thật giữ nguồn acceptance/evidence hiện có |
| Owner | Chưa gán owner sản phẩm thật; cần gán khi áp dụng ví dụ |
| Revision tài liệu | 3 — tương thích template 1.1.0, làm rõ profile JSON tùy chọn; giữ criteria, behavior và source refs của revision 2 |
| Ngày cập nhật | 2026-10-20 |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | Ví dụ Lifestyle Collection, iPhone/iPad/macOS và summary widget; C2O Design 1.5.0 |

Áp dụng [chuẩn template 1.0](../../documentation/template-standard.md). Phiên bản template khác revision của pack. Đây là bản minh họa, chưa được chọn làm spec của một sản phẩm thật.

Đây là ví dụ điền cho source Lifestyle starter; không phải app đã phát hành hoặc nghiên cứu khách hàng đã thực hiện. Source được tham chiếu trực tiếp; native build/runtime chưa chạy. Business hypotheses bên dưới là giả định minh họa, không là dữ kiện về thị trường.

Ví dụ giả định này đã chọn **profile JSON cũ, tùy chọn** cho acceptance và evidence trong index. Sao chép một section không làm JSON trở thành nguồn chuẩn thay acceptance/evidence C2O hiện có. Dự án thật giữ nguồn và các trạng thái C2O `pass / partial / fail / not-tested`; profile JSON không có nhãn `partial`, nên giữ bằng chứng một phần và giới hạn tại nguồn C2O, không đổi thành `PASS`. Chỉ dùng JSON khi đã chọn rõ trách nhiệm của nó theo [hướng dẫn evidence](../../core/evidence.md); không tạo hai nguồn acceptance độc lập.

## 1. Index và bằng chứng đầu vào

| Chủ đề | Nguồn chuẩn trong ví dụ |
| --- | --- |
| Business assumptions và outcome | [Business](#2-business-và-outcome) |
| Cấu trúc / scope / requirements | [Blueprint và PRD](#3-blueprint-và-prd) |
| Domain rules | [Domain](#4-domain-và-rules) |
| Feature behavior và UI | [Feature và UX/UI](#5-feature-và-uxui) |
| Implementation choices | [Technical](#6-technical-spec) |
| Acceptance ID/title/flags theo profile JSON của ví dụ | [project.json](project.json) |
| Recorded results/input/evidence theo profile JSON của ví dụ | [verification.json](verification.json) |
| Kế hoạch giao hàng, kiểm tra và phát hành | [Delivery](#7-delivery-và-validation), [Release](#8-release-và-learning) |

Đầu vào đã đọc: [category blueprint](../../app-templates/categories/lifestyle.md), [app model](../../starters/apple/App/StarterAppModel.swift), [collection UI](../../starters/apple/App/LifestyleCollectionRoot.swift), [editor](../../starters/apple/App/RecordEditorView.swift), [models](../../starters/apple/StarterCore/Sources/StarterCore/Models.swift). Đây là evidence về nội dung source, chưa là evidence về chạy app. [Quy ước traceability](../../documentation/traceability.md) giải thích các ID.

## 2. Business và outcome

User minh họa: một người giữ bộ sưu tập cá nhân và cần tìm lại ghi chú của từng mục. Customer/payer: chưa xác định; có thể là cùng người nhưng chưa có evidence trả tiền. Cách thay thế cần tìm hiểu: ghi chú văn bản hoặc bảng tính người đó đang dùng. Chưa có phỏng vấn hoặc dữ liệu so sánh trong ví dụ.

**OUT-01:** người dùng tạo một mục, tìm lại đúng mục, sửa ghi chú và mở lại thấy giá trị đã lưu; dữ liệu của các mục khác không đổi.

| ASM | Giả thuyết | Cách kiểm tra đề xuất | Kết quả hiện có |
| --- | --- | --- | --- |
| ASM-01 | Danh sách + search + favorite giúp nhóm người dùng dự kiến tìm mục thuận tiện | Quan sát tác vụ với bộ sưu tập do người tham gia tự cung cấp hoặc fixture đã đồng ý; so khó khăn với cách hiện tại | Chưa thực hiện |
| ASM-02 | Một flow local đơn giản đủ cho lần sử dụng đầu | Task walkthrough và hỏi lúc nào họ thực sự cần nhiều thiết bị, ảnh hoặc export | Chưa thực hiện |
| ASM-03 | Giá trị tạo ra đủ để duy trì/thu phí | Kiểm tra nhu cầu trả tiền sau khi chứng minh task value; so mô hình mua một lần/thu phí định kỳ theo chi phí phục vụ thật | Chưa nghiên cứu; chưa chọn giá hay mô hình |

Chi phí cần ước tính khi có sản phẩm cụ thể: phát triển, nội dung/asset, thiết bị kiểm tra, phân phối và hỗ trợ. Không có server trong source hiện tại không có nghĩa chi phí vận hành bằng 0. Metrics đề xuất: completion/error/recovery của task đầu và lý do quay lại; chưa có baseline, target hoặc đo lường. Chọn cách quan sát tối thiểu trước, không tự cài analytics.

## 3. Blueprint và PRD

| Actor | Feature | Flow | Domain | Screen | Platform |
| --- | --- | --- | --- | --- | --- |
| Người sở hữu bộ sưu tập | F-01 Quản lý bộ sưu tập | Tạo → tìm → xem → sửa/yêu thích/xóa | ENT-01, BR-01…04 | SCR-01 collection, SCR-02 detail, SCR-03 editor | iPhone/iPad/Mac |
| Người dùng muốn nhìn nhanh | F-02 Summary widget, đã chọn trong ví dụ | App commit → snapshot → widget → mở collection | ENT-02, BR-05 | Widget surface | iPhone/iPad/Mac |
| Người dùng cần hiểu dữ liệu | F-03 Help/settings | Mở Help và đọc giới hạn lưu | BR-04/05 | SCR-04 settings | iPhone/iPad/Mac |

Deployment baseline: iOS/iPadOS 17+, macOS 14+; UI tiếng Việt. Source dùng native appearance; coverage light/dark, chữ lớn, hẹp/rộng và input thực vẫn cần kiểm tra. Một app writer/cửa sổ chính; không có account hoặc sync.

| Requirement | Scope / ưu tiên | Criterion refs |
| --- | --- | --- |
| REQ-01: tạo, tìm, xem, sửa, favorite đúng identity và mở lại đúng dữ liệu | Core F-01 | LIF-01, APP-03 |
| REQ-02: hủy/xóa/lỗi lưu có outcome rõ; giữ draft khi write fail | Core F-01 | LIF-02, APP-03 |
| REQ-03: navigation và các biến thể nền tảng còn dùng được; links không làm mất draft | Core shell | APP-01…05 |
| REQ-04: widget chỉ đọc summary, có trạng thái thiếu/lỗi và mở đúng nơi | Conditional đã chọn F-02 | WID-01/02, APP-05 |

Deferred: ảnh, tags, export/restore, migration qua schema mới, reminders, journal, cloud, IAP và multiwindow editing. Chưa có service vận hành nhiều bên nên không tạo service blueprint. Blueprint này không đại diện mọi app Lifestyle.

## 4. Domain và rules

| Entity | Nghĩa / identity | Lifecycle |
| --- | --- | --- |
| ENT-01 LifestyleRecord | UUID; title, notes, isFavorite, updatedAt | Draft trong phiên → persisted → edited/favorited → deleted |
| ENT-02 WidgetSnapshot | Một projection theo category/route của app; count/status, updatedAt | Published sau khi đọc/commit thành công → được thay bằng snapshot mới |

| Rule | Định nghĩa chuẩn trong ví dụ | Criterion refs |
| --- | --- | --- |
| BR-01 | Title sau trim không rỗng; title có thể trùng giữa hai UUID; sửa tác động đúng UUID | LIF-01 |
| BR-02 | Commit file thành công trước khi thay dữ liệu trong model. Write fail giữ bản cũ và editor draft | APP-03, LIF-02 |
| BR-03 | Search xét title/notes không phân biệt hoa thường theo API đang dùng; list sắp updatedAt giảm dần, tie theo UUID. Favorite cập nhật cùng record, không tạo bản sao | LIF-01 |
| BR-04 | Cancel không commit. Delete có xác nhận và không có Undo. Draft chưa lưu không được khôi phục sau khi app thoát. Decode/read error chặn ghi thay kho chưa đọc được | LIF-02, APP-03 |
| BR-05 | Widget projection chỉ có count/favorite count và ngữ cảnh, không title/notes. Snapshot write lỗi không đảo ngược domain commit. Timestamp biểu thị lúc công bố snapshot | WID-01/02 |

BR-02 bảo vệ draft trong phiên khi save lỗi; nó không hứa phục hồi draft sau crash/quit. Missing file ở lần đầu khác file tồn tại nhưng không đọc được. Đổi JSON format trong tương lai cần migration riêng.

## 5. Feature và UX/UI

### F-01 — collection và editor

Entry: collection hoặc record deep link hợp lệ. Chọn một UUID để xem detail; mở editor tạo draft riêng; Save áp dụng BR-01/02, Cancel áp dụng BR-04. Search/selection thuộc app model, field draft thuộc editor; row không tự commit. Empty collection, search no results và load error là các trạng thái khác nhau.

| Platform | Composition | Điều cần quan sát |
| --- | --- | --- |
| iPhone | NavigationStack list/detail + editor sheet | Back/dismiss/keyboard không làm mất action hoặc draft |
| iPad | NavigationSplitView list/detail | Thu/mở cột giữ record selection và draft |
| Mac | Main Window + split; Settings scene; command thêm mục | Menu/toolbar cùng action; focus/window lifecycle hợp lý |

Component/data-view/layout chi tiết theo [category](../../app-templates/categories/lifestyle.md) và [catalog](../../catalog/screen-patterns.md); ví dụ chưa tạo một bộ token thương hiệu hoặc mockup đã render. Khi chọn hướng visual riêng, ghi baseline và deviation trước khi nhân ra nhiều màn.

| Criterion | Scenario detail cần chạy |
| --- | --- |
| LIF-01 | Given hai record trùng tên nhưng UUID khác, When sửa/favorite một record rồi mở lại, Then đúng record đổi, record kia giữ nguyên; search tìm được dữ liệu tương ứng |
| LIF-02 | Given draft đang sửa, When Cancel hoặc lỗi Save, Then áp BR-02/04; xác nhận Delete cho đúng record và không báo còn Undo |
| APP-03 | Given store decode lỗi, When mở app và thử sửa, Then có lỗi/retry và dữ liệu chưa đọc được không bị thay bằng array rỗng |
| APP-05 | Given editor có draft, When nhận deep link hợp lệ, Then đợi hoàn tất Save/Cancel; invalid route không ghi/xóa dữ liệu |

### F-02 — summary widget

Read-only snapshot; ba family small/medium/large; missing/error không được trình bày thành count 0. Publish → yêu cầu reload; không hứa thời điểm refresh chính xác. Chạm mở collection theo route của profile. Ranh giới và trạng thái chi tiết tại [widget contract](../../app-templates/platforms/widgets.md).

## 6. Technical spec

App SwiftUI → `StarterAppModel` trên MainActor → `LocalFileStore` ghi JSON atomic vào Application Support riêng. Các thao tác file đồng bộ phù hợp scope nhỏ đã chọn; chưa có ngân sách dữ liệu/latency được đo, cần chốt trước khi cam kết dữ liệu lớn. Domain store do app ghi; extension đọc snapshot riêng trong App Group.

| ADR | Lựa chọn trong source | Tradeoff / trigger xem lại |
| --- | --- | --- |
| ADR-01 | Một app writer, local JSON, iPad một scene/Mac một main Window | Đơn giản nhưng chưa giải concurrency nhiều writer; xem lại khi có sync/multiwindow/dữ liệu lớn |
| ADR-02 | App-private records; projection riêng cho widget | Giảm payload chia sẻ; cần signing/group và chấp nhận widget có thể cũ |

Không có backend/network/analytics/account trong scope này. Data giữ cục bộ không tự là backup hay end-to-end encryption. Backup/export, migration, privacy policy và support URL của sản phẩm phát hành chưa được triển khai/điền. App Group không đồng bộ dữ liệu giữa thiết bị.

## 7. Delivery và validation

Source đã có cho scope trên; các slice sau là trình tự tích hợp/kiểm chứng đề xuất cho app mới, không giả làm lịch sử công việc hoặc ngày cam kết.

| Slice | Kết quả đầu-cuối | Dependencies | Criterion refs |
| --- | --- | --- | --- |
| SL-01 | Tạo → lưu → đóng/mở lại → thấy đúng record | Xcode/toolchain/signing phù hợp; chốt model | APP-01/02, LIF-01 |
| SL-02 | Tìm/sửa/favorite/hủy/xóa và phục hồi khi storage lỗi | SL-01; fixtures kiểm lỗi an toàn | APP-03/04/05, LIF-01/02 |
| SL-03 | App công bố summary → widget hiển thị → mở đúng app | App Groups/extension và SL-01 | WID-01/02, APP-05 |

Validation fixtures: empty store, hai record trùng tên, Unicode/title dài, corrupt JSON, write failure mô phỏng và snapshot missing/invalid. Dùng thư mục/test app tách biệt, không làm hỏng kho cá nhân. Chọn các cấu hình phone hẹp, iPad resize và Mac keyboard/VoiceOver theo scope. Input evidence gồm source/model/spec/rules thật và configuration ảnh hưởng; chưa điền input/evidence giả chỉ để checker ready.

Trong profile JSON đã chọn cho ví dụ này, title/flags nằm ở project JSON và results ở verification JSON. Khi áp dụng cho dự án thật, tra cứu và cập nhật nguồn acceptance/evidence hiện có; không thay nó chỉ vì sao chép pack. `APP-01/02` cần build/launch, `APP-04` cần interaction/accessibility, `WID-01/02` cần signed runtime. Đọc [NATIVE_CHECKS](../../starters/apple/NATIVE_CHECKS.md). Toàn bộ native evidence còn chưa có.

## 8. Release và learning

Release candidate, icon/screenshots, listing metadata, support/privacy URLs và người chịu trách nhiệm: chưa có. Trước một bản phát hành thật, chọn đúng [release template](../../templates/product/release-operations.md), giữ scope/evidence/actual data practices khớp source; quyết định publish theo quyền được giao, không theo việc pack đã điền.

Rủi ro chưa giải: giá trị với user cụ thể, giới hạn kích thước kho, native usability, backup/migration. Bước tiếp theo nhỏ nhất: tạo source project Lifestyle, chốt một đối tượng bộ sưu tập thật, chạy SL-01 trên Mac/thiết bị, rồi quyết định phần mở rộng bằng evidence. Business hypotheses giữ trạng thái giả định cho đến khi có quan sát tương ứng.

## Kiểm tra trước bàn giao

- [x] Đã ghi metadata, scope minh họa và ranh giới giữa giả thuyết, source đã viết và runtime chưa chạy.
- [x] Index dẫn nguồn theo chủ đề trong ví dụ đã chọn profile JSON; acceptance fields/results giữ tại project/verification JSON của ví dụ, mọi native criterion vẫn `NOT_RUN`.
- [ ] Khi dùng cho sản phẩm thật: gán owner, xác định người dùng/outcome và xử lý giả định ảnh hưởng tới lát cắt đầu.
- [ ] Chọn source/targets/configuration thực, kiểm tra native theo criteria và ghi evidence thật tại nguồn kết quả của dự án; giữ mọi kết quả `partial`, giới hạn và kiểm tra chưa chạy.
- [ ] Chốt phần việc bàn giao, câu hỏi còn mở và owner bước tiếp theo trong phạm vi quyền đã giao.
