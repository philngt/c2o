# Module matrix cho Apple app templates

**C2O Design v1.3.** Dùng matrix sau khi xác định tác vụ, trước khi mở rộng màn hình hoặc capabilities. Mỗi dòng trả lời “module này phục vụ việc gì?” và “điều kiện nào làm nó cần thiết?”. Không dùng matrix như danh sách phải bật đủ khi tạo app mới.

## 1. Cách đọc và áp dụng

- **Core:** cần để hoàn thành và phục hồi tác vụ đã chọn trong phạm vi đã cam kết. Tác vụ khác có thể có Core khác.
- **Conditional:** chỉ chọn khi có feature, dữ liệu, nguồn hoặc mô hình kinh doanh tạo nhu cầu thật. Khi đã chọn, các yêu cầu an toàn dữ liệu, lỗi và accessibility liên quan trở thành Core của feature đó.
- **Optional:** cải tiến có thể bỏ mà không phá kết quả chính; vẫn phải có lý do và chi phí bảo trì rõ.

Mức cần thiết, quyết định đưa vào scope và trạng thái verification là ba thông tin khác nhau. “Có trong starter scope” không có nghĩa là đã build, render hay kiểm tra native đạt. Các acceptance cần evidence thật trong nguồn hiện có của C2O; chưa chạy thì giữ `not-tested` và ghi lý do nếu bị chặn. Bảng minh họa dùng `NOT_RUN` của profile JSON tùy chọn; cách viết đó không thay hệ trạng thái native hoặc làm mất kết quả `partial`.

## 2. Phạm vi hai starter đang xây

| Phần | Lifestyle starter | Utility starter |
| --- | --- | --- |
| Tác vụ chính | Collection: tạo, xem, sửa, xóa; favorites | Normalize/count text; xem kết quả |
| Dữ liệu giữ lại | `LifestyleRecord`: UUID, title, notes, favorite, updatedAt theo persistence contract | Local history mặc định tắt, sau opt in giữ tối đa 50 recent runs theo preset; vòng đời draft/output định nghĩa riêng |
| Navigation | iPhone stack; iPad/macOS split | iPhone stack; iPad/macOS split |
| Phần dùng chung | Settings, Help, empty/error states theo chức năng thật | Settings, Help, empty/error states theo chức năng thật |
| Widget | Read-only count record/favorite + deep link; không title/notes | Read-only count/status + deep link; không raw text/draft |
| Chưa đưa vào | Auth, cloud, IAP, permission request; các archetype khác | Auth, cloud, IAP, permission request; các archetype khác |

Các blueprint mở rộng trong [Lifestyle](categories/lifestyle.md) và [Utility](categories/utility.md) là lựa chọn cho dự án tiếp theo. Journal, planner, document workbench, timer, notifications, App Intents và Live Activities không tự trở thành feature đã triển khai của hai starter.

## 3. Matrix lựa chọn module

| Module | Mức theo tác vụ | Điều kiện và contract phải chốt | Scope starter / bằng chứng cần có |
| --- | --- | --- | --- |
| **App shell / navigation** | Core | Entry point, hierarchy, back/dismiss, selection và trạng thái chưa chọn; adaptation theo target | Stack/split đã chọn; cần thao tác native chứng minh giữ ngữ cảnh, focus và draft |
| **Core task** | Core | Actor, input, output quan sát được, đường hoàn thành đầu đến cuối | Collection CRUD/favorites; normalize/count; verify kết quả theo contract, không chỉ màn mở được |
| **Create / edit data** | Core khi tác vụ tạo hoặc sửa dữ liệu | Identity, field nghĩa gì, validation, Save/Cancel, draft, xung đột nếu có | Lifestyle CRUD; Utility có input văn bản, không tự cần trình sửa history hoặc file editor |
| **Storage / persistence** | Core khi kết quả phải tồn tại sau phiên | Payload, thời điểm ghi, nguồn sự thật, read/write failure, migration khi đổi model | Collection local; Utility opt-in local history; test mở lại đúng dữ liệu theo contract |
| **Empty / errors / recovery** | Core | Tách empty, no results, invalid, lỗi thao tác; giữ input và trạng thái đã lưu | Theo từng flow thật; không thêm fake loading/offline state cho đủ checklist |
| **Accessibility** | Core | Semantics, đọc/focus, keyboard/assistive technology theo target, chữ lớn, thông tin không chỉ bằng màu | Phải kiểm tra trong môi trường đã chọn; source review không đủ để tuyên bố VoiceOver hoặc native PASS |
| **Localization / formatting** | Core cho locale đã hỗ trợ; Conditional khi thêm ngôn ngữ | Chuỗi có thể dịch; date/number/unit phù hợp; plural, text expansion, RTL khi nằm trong scope | Không tuyên bố hỗ trợ mọi locale; label count của Utility phải khớp thuật toán |
| **Settings / preferences** | Conditional; Core với preference đã chọn | Chỉ chứa lựa chọn có tác dụng, giá trị mặc định, phạm vi và thời điểm lưu | Có Settings; Utility có history opt in. Không thêm theme/account/sync switches giả |
| **Help / support** | Core tối thiểu cho tác vụ và dữ liệu cần giải thích; kênh liên hệ Conditional | Nêu cách dùng, ý nghĩa kết quả, dữ liệu giữ lại, phục hồi; contact chỉ khi có đích thực | Có Help; không tạo form gửi hỗ trợ hoặc SLA khi chưa có dịch vụ tiếp nhận |
| **Onboarding / first use** | Conditional; gợi ý ngắn Optional | Chỉ chặn entry khi có thiết lập thật cần hoàn tất; có thể dùng empty state/contextual help | Không mặc định multi-step onboarding, tạo tài khoản hoặc slide giới thiệu trước tác vụ |
| **Search / filter / sort** | Conditional | Nhu cầu tìm/chọn thật; query scope, thứ tự, reset và no results | Không bắt buộc chỉ vì có list; nếu thêm favorite filter thì phải rõ scope và count |
| **History / recent items** | Conditional | Lợi ích truy hồi, payload, retention, opt in nếu đã cam kết, xóa, tái sử dụng | Utility đã chọn opt-in local history; Lifestyle không tự có nhật ký mọi thao tác |
| **Permissions** | Conditional | Feature thật cần tài nguyên được bảo vệ; request đúng thời điểm; deny/restricted/cancel; cách tiếp tục | Không có permission request trong starter; không xin camera/location/notification trước nhu cầu |
| **Notifications / reminders** | Conditional | Sự kiện nào cần nhắc, lịch/timezone, thay đổi/hủy, quyền và tình huống không gửi được | Chưa đưa vào starter; calendar hoặc routine blueprint không tự bật reminders |
| **Widgets** | Conditional; source có sẵn, bật target bằng `--widgets` | Summary phục vụ tác vụ, payload/privacy, empty/stale/refresh, deep-link destination; tách snapshot thiếu/lỗi khỏi số đếm 0 | Chỉ đọc count/status + deep link; verify snapshot, refresh và route thật theo target; không hứa lịch refresh chính xác hoặc suy PASS từ source |
| **App Intents / Shortcuts** | Conditional | Hành động có giá trị ngoài UI, tham số, authorization/state và kết quả; target hỗ trợ cụ thể | Chưa cam kết shortcut hay action feature. Dùng framework cho cấu hình widget không tự chứng minh đã có workflow người dùng |
| **Live Activities** | Conditional | Một hoạt động đang diễn ra có thời điểm bắt đầu/kết thúc, cập nhật hữu ích và vòng đời rõ | Chưa đưa vào starter; chỉ xem xét cho tác vụ thật như timer, theo target và capabilities được chọn |
| **IAP / paywall** | Conditional | Có phần bán thật, entitlement, purchase/restore/cancel/error và dữ liệu sau hết quyền | Chưa đưa vào starter; không mặc định paywall, subscription hoặc khóa kết quả chính |
| **Backup / export / restore** | Conditional | Người dùng cần chuyển/khôi phục dữ liệu; format, phạm vi, phiên bản, xung đột, thất bại | Local persistence không tự hứa backup hay export; chọn riêng và verify file/khôi phục khi bổ sung |
| **Delete / data lifecycle** | Core với dữ liệu người dùng được app giữ | Xóa gì, ảnh hưởng references/widget, khả năng phục hồi, clear-all nếu cần; account deletion chỉ khi có account | Lifestyle xóa record; Utility cần chính sách xóa history đã lưu. Không đồng nhất tắt history với xóa lịch sử |
| **Analytics / diagnostics** | Optional, trừ nhu cầu vận hành được xác định | Câu hỏi cần trả lời, dữ liệu tối thiểu, consent/privacy nếu áp dụng, retention và cách tắt | Không analytics mặc định; local error message hoặc test log không tự là telemetry sản phẩm |
| **Authentication / accounts** | Conditional | Có identity phía dịch vụ, quyền truy cập hoặc cross-device ownership thật | Chưa đưa vào starter; local collection/text tool không tự cần login |
| **Cloud / collaboration** | Conditional | Nhu cầu nhiều thiết bị/người dùng, nguồn sự thật, offline, conflict, quyền và sync state | Chưa đưa vào starter; không hiển thị “synced” hoặc trạng thái online giả |

## 4. Quy trình chọn module cho dự án mới

1. Chọn một archetype trong category blueprint; viết một outcome, một actor và một flow hoàn chỉnh.
2. Chọn module Core cho flow đó. Với mỗi Conditional muốn thêm, ghi tác vụ nào tạo ra nhu cầu và tiêu chí nào chứng minh lợi ích.
3. Chốt data contract và các state thực sự có thể xảy ra. Chọn `SP` cho trách nhiệm màn, `DVP` cho cách hiểu dữ liệu, `LP` cho cấu trúc vùng, `CP` cho hành vi tương tác.
4. Ghi capability và target cụ thể; phân biệt UI được thiết kế, code đã có, môi trường đã build và hành vi đã kiểm chứng. Không thay “chưa chạy” bằng “không áp dụng”.
5. Dùng một lát cắt nhỏ đầu đến cuối trước khi thêm module; mỗi thay đổi phải giữ dữ liệu, recovery và acceptance nhất quán.

Ví dụ: một app ghi bộ sưu tập cá nhân có Core là CRUD, favorite nếu đã chọn, local persistence, navigation và recovery. Ảnh chỉ cần khi giúp nhận diện; permission chỉ xét khi nguồn ảnh cần nó. Một text utility có Core là phép xử lý đúng và kết quả rõ; history trở thành Core của scope khi sản phẩm đã chọn tính năng này, còn opt in và xóa dữ liệu là phần của contract history.

## 5. Hồ sơ review tối thiểu

Lưu cho từng module đã chọn: lý do, owner, trạng thái implementation, màn và data contract liên quan, criterion cần kiểm chứng, evidence và giới hạn. Một ví dụ để điền:

| Module | Quyết định scope | Ref dự án | Criterion mẫu | Verification ban đầu |
| --- | --- | --- | --- | --- |
| Utility history | Conditional đã chọn; opt in local | `DV-01`, screen history, storage contract | `C-001`: không lưu trước opt in; lưu/mở/xóa đúng dữ liệu | `NOT_RUN` |
| Collection favorite | Core của starter đã chọn | `CMP-01`, `DV-02`, collection/detail | `C-002`: cùng identity và state sau cập nhật/mở lại | `NOT_RUN` |
| Notifications | Chưa chọn; không có tác vụ nhắc | Không tạo màn xin quyền hoặc settings giả | Không tạo criterion yêu cầu feature chưa có | Ngoài scope, không dùng để che tiêu chí đã cam kết |

Ref là ví dụ minh họa; tạo instance thật khi áp dụng. Xem [components](../catalog/components.md), [data views](../catalog/data-view-patterns.md), [layouts](../catalog/layout-patterns.md), [screens](../catalog/screen-patterns.md) và [evidence](../core/evidence.md). Checker hiện không tự hiểu quan hệ module–screen–pattern hoặc tự chạy native tests; người/agent phải review mapping và evidence tương ứng.
