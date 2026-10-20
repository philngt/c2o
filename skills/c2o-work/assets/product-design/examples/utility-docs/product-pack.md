# Product pack minh họa — Text Utility

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-PRODUCT-PACK` |
| Phiên bản template | `1.1.0` |
| Mục đích | Minh họa pack cho flow normalize/count/copy/share và history opt-in |
| Dùng khi | Cần xem một bản điền để khởi đầu app nhỏ từ source starter tương ứng |
| Đầu vào | Source và category refs trong [index](#1-index-và-bằng-chứng-đầu-vào); chưa có dữ liệu nghiên cứu khách hàng |
| Đầu ra / bàn giao | Phạm vi, behavior và kế hoạch tích hợp/kiểm chứng minh họa cho bước tiếp theo |
| Nguồn chuẩn | Sections đăng ký trong index chỉ có authority trong ví dụ này; khi áp dụng cho dự án thật giữ nguồn acceptance/evidence hiện có |
| Owner | Chưa gán owner sản phẩm thật; cần gán khi áp dụng ví dụ |
| Revision tài liệu | 3 — tương thích template 1.1.0, làm rõ profile JSON tùy chọn; giữ criteria, behavior và source refs của revision 2 |
| Ngày cập nhật | 2026-10-20 |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | Ví dụ Text Utility, iPhone/iPad/macOS và summary widget; C2O Design 1.5.0 |

Áp dụng [chuẩn template 1.0](../../documentation/template-standard.md). Phiên bản template khác revision của pack. Đây là bản minh họa, chưa được chọn làm spec của một sản phẩm thật.

Ví dụ điền theo source Utility starter; chưa có nghiên cứu thị trường, native build/runtime hoặc bản phát hành. Các giả định business là ví dụ để kiểm tra, không là khẳng định về người dùng thật.

Ví dụ giả định này đã chọn **profile JSON cũ, tùy chọn** cho acceptance và evidence trong index. Sao chép một section không làm JSON trở thành nguồn chuẩn thay acceptance/evidence C2O hiện có. Dự án thật giữ nguồn và các trạng thái C2O `pass / partial / fail / not-tested`; profile JSON không có nhãn `partial`, nên giữ bằng chứng một phần và giới hạn tại nguồn C2O, không đổi thành `PASS`. Chỉ dùng JSON khi đã chọn rõ trách nhiệm của nó theo [hướng dẫn evidence](../../core/evidence.md); không tạo hai nguồn acceptance độc lập.

## 1. Index và bằng chứng đầu vào

| Chủ đề | Nguồn chuẩn trong ví dụ |
| --- | --- |
| Business assumptions / outcome | [Business](#2-business-và-outcome) |
| Blueprint / scope / requirements | [Blueprint và PRD](#3-blueprint-và-prd) |
| Text/history/data rules | [Domain](#4-domain-và-rules) |
| Hành vi feature / UI | [Feature](#5-feature-và-uxui) |
| Implementation choices | [Technical](#6-technical-spec) |
| Acceptance ID/title/flags theo profile JSON của ví dụ | [project.json](project.json) |
| Recorded results/input/evidence theo profile JSON của ví dụ | [verification.json](verification.json) |
| Delivery / validation / release | [Delivery](#7-delivery-và-validation), [Release](#8-release-và-learning) |

Đầu vào đã đọc: [Utility blueprint](../../app-templates/categories/utility.md), [TextTools](../../starters/apple/StarterCore/Sources/StarterCore/TextTools.swift), [app model](../../starters/apple/App/StarterAppModel.swift), [workbench](../../starters/apple/App/UtilityWorkbenchRoot.swift), [Settings/Help](../../starters/apple/App/StarterSettingsView.swift). Đọc source chỉ chứng minh nội dung đã viết; chưa xác nhận runtime. Quy tắc ID tại [traceability](../../documentation/traceability.md).

## 2. Business và outcome

User minh họa: người thường nhận văn bản có tab/xuống dòng/dấu cách không mong muốn và muốn làm gọn để copy sang nơi khác. Customer/payer chưa xác định. Các cách thay thế cần quan sát: chỉnh tay, công cụ web hoặc editor hiện có; chưa có benchmark hoặc phỏng vấn trong ví dụ.

**OUT-01:** người dùng xử lý văn bản theo phép chuẩn hóa đã giải thích, hiểu các bộ đếm và copy/share đúng kết quả, giữ được input khi việc lưu lịch sử gặp lỗi.

| ASM | Giả thuyết | Quan sát/thử nghiệm đề xuất | Kết quả hiện có |
| --- | --- | --- | --- |
| ASM-01 | Một workbench local tiết kiệm bước cho nhóm user dự kiến | Cho làm một tác vụ thật bằng cách hiện tại rồi prototype; ghi lỗi/khó hiểu, tránh mặc định app mới luôn nhanh hơn | Chưa thực hiện |
| ASM-02 | Một số user muốn mở lại input/output cũ | Hỏi bằng tình huống đã xảy ra, sau đó thử history opt-in và hành vi clear/off | Chưa thực hiện |
| ASM-03 | Tác vụ này có giá trị đủ để phát triển thành sản phẩm duy trì được | Xác minh tần suất/độ khó và điều kiện chi trả trước khi chọn pricing | Chưa nghiên cứu; chưa có giá hoặc mô hình doanh thu |

Phép xử lý nhỏ này chỉ là nguồn khởi đầu, chưa chứng minh giá trị thương mại độc lập. Chi phí dự kiến cần ghi sau: phát triển, hỗ trợ, distribution và nội dung/bản dịch. Metrics đề xuất: task completion, copy đúng kết quả, hiểu normalization mất ngắt dòng; chưa có baseline/target. Không thêm telemetry mặc định chỉ để có dashboard.

## 3. Blueprint và PRD

| Actor | Feature | Flow | Domain | Screen/surface | Platform |
| --- | --- | --- | --- | --- | --- |
| Người xử lý văn bản | F-01 Text workbench | Nhập → xem count → normalize → copy/share | ENT-01/02, BR-01…03 | SCR-01 workbench | iPhone/iPad/Mac |
| Người muốn tái dùng kết quả | F-02 History opt-in, đã chọn | Bật history → xử lý → mở lại → clear/off | ENT-03, BR-04/05 | SCR-02 history, SCR-03 Settings | iPhone/iPad/Mac |
| Người muốn mở nhanh công cụ | F-03 Summary widget, đã chọn | App publish trạng thái → widget → mở workbench | ENT-04, BR-06 | Widget | iPhone/iPad/Mac |

Baseline iOS/iPadOS 17+, macOS 14+; UI tiếng Việt. Scope gồm phép xử lý local, thống kê, Copy/Share, opt-in history, Settings/Help và read-only widget. Deferred: NLP word tokenization, batch, file import/export, timer, account/cloud, multiwindow và App Intents có ghi. Chưa có handoff dịch vụ cần service blueprint.

| Requirement | Scope / lý do | Criterion refs |
| --- | --- | --- |
| REQ-01: normalize/count theo nghĩa đã công bố | Core F-01 | UTL-01 |
| REQ-02: copy/share kết quả hiện tại; thay input không làm output cũ thành output mới | Core F-01 | UTL-02 |
| REQ-03: history chỉ ghi khi opt in; retention/off/clear và write failure rõ | Conditional đã chọn F-02 | UTL-02, APP-03 |
| REQ-04: app/platform/deep link usable, không tự chạy hoặc xóa input qua URL | Core shell | APP-01…05 |
| REQ-05: widget tóm tắt trạng thái và mở app, không có raw text | Conditional đã chọn F-03 | WID-01/02, APP-05 |

## 4. Domain và rules

| Entity | Nghĩa / identity | Lưu giữ |
| --- | --- | --- |
| ENT-01 Workbench draft | utilityInput và processedInput, output gắn input đã chạy | Trong bộ nhớ; không phục hồi khi quit |
| ENT-02 TextStatistics | Derived characters/words/lines với scope riêng cho input hiện tại và output current | Tính lại, không là bản ghi độc lập |
| ENT-03 UtilityHistoryItem | UUID, input, output, createdAt | File local khi rule history cho phép |
| ENT-04 WidgetSnapshot | Category/route, trạng thái đã tạo kết quả hoặc sẵn sàng và thời điểm công bố | Projection riêng trong App Group |

| Rule | Định nghĩa chuẩn trong ví dụ | Criterion refs |
| --- | --- | --- |
| BR-01 | Normalize split theo whitespace rồi join một dấu cách; trim hai đầu, gộp cả tab/ngắt dòng. Không tự sửa chính tả hay nghĩa | UTL-01 |
| BR-02 | Characters = Swift String.count theo grapheme; words = tokens chia bằng whitespace, không là tách từ ngôn ngữ học. Lines chuẩn hóa CRLF/CR về LF; empty có 0 dòng, trailing newline có dòng trống cuối | UTL-01 |
| BR-03 | Output chỉ current nếu input hiện tại bằng input đã xử lý. Sửa input làm result cũ không còn được dùng như current; input/result chỉ trong phiên | UTL-02 |
| BR-04 | History mặc định off. Khi bật và một run ghi thành công, giữ tối đa 50 recent runs cùng input/output. Tắt chỉ dừng ghi thêm; clear là action riêng có xác nhận | UTL-02 |
| BR-05 | Transform thành công không phụ thuộc history save. History write fail giữ history cũ và result mới, kèm cảnh báo riêng. Read/decode fail chặn ghi đè store chưa đọc được | APP-03, UTL-02 |
| BR-06 | Widget source chỉ tóm tắt trạng thái workbench, không input/output/history text. Deep link chỉ mở context; publish lỗi không đảo ngược transform/history commit | WID-01/02, APP-05 |

BR-04 là preset đã chọn cho ví dụ, không là hạn mức phổ quát của mọi utility. Copy/Share đưa dữ liệu sang clipboard hoặc đích do người dùng chọn; local processing không có nghĩa mọi chia sẻ đều ở lại app.

## 5. Feature và UX/UI

### F-01 — workbench

Entry vào workbench; nhập/dán để xem counters của input; chọn normalize để tạo output cùng counters riêng. Input rỗng thì normalize bị vô hiệu hóa. Whitespace-only có thể tạo output rỗng; Copy/Share chỉ bật với output current không rỗng. App model giữ input/result; UI không tự ghi history khi chỉ đọc count hoặc sửa input. Settings có Help mô tả rõ BR-01/02/03.

### F-02 — history

Bật preference khi settings/history đọc được. Một lần xử lý thành công có thể có kết quả lưu history khác kết quả transform theo BR-05. Mở lại history thay input/output bằng snapshot đã lưu; nếu đang có input khác, phải xác nhận thay, Cancel giữ nguyên. Input rỗng hoặc cùng input của lần cũ có thể mở lại trực tiếp. New text cần xử lý input cũ theo chính sách xác nhận; không tự xóa do deep link. Clear không tự đổi preference off/on. User có thể tắt ghi thêm và giữ các lần cũ.

| Platform | Composition | Trạng thái cần phân biệt |
| --- | --- | --- |
| iPhone | NavigationStack workbench; history sheet | Chưa nhập / input có / result current / input đã đổi |
| iPad/Mac | History leading column, workbench detail | History off / empty / có dữ liệu / read error |
| Widget | Small/medium/large | Snapshot hợp lệ / chưa có / không đọc được / preview |

UI, component và data-view mở rộng theo [category](../../app-templates/categories/utility.md). Đây chưa có direction thương hiệu hoặc mockup đã render. Native copy/share, focus, resize, chữ lớn và VoiceOver còn cần chạy thật.

| Criterion | Scenario detail cần chạy |
| --- | --- |
| UTL-01 | Given input chứa dấu tiếng Việt, emoji ghép, tab và CRLF/trailing newline, When xem count/chạy normalize, Then kết quả đúng BR-01/02; giải thích UI khớp thuật toán |
| UTL-02 | Given history off, When xử lý, Then không lưu history; bật rồi chạy vượt cap thì BR-04 đúng. Sửa input không copy result cũ như current; output rỗng không bật Copy/Share. Mở history khi input khác phải xác nhận, Cancel giữ input hiện tại |
| APP-03 | Given history write failure được mô phỏng, When normalize, Then result mới còn, input còn, history cũ giữ và cảnh báo riêng theo BR-05 |
| APP-05 | Given đang có input, When mở utility deep link hợp lệ, Then chỉ điều hướng; URL lạ không chạy transform hoặc clear |

## 6. Technical spec

SwiftUI workbench → MainActor app model → `TextTools` cho xử lý thuần; `LocalFileStore` cho settings/history. JSON atomic file writes giữ kết quả commit. Mọi xử lý đang đồng bộ và scope nhỏ; chưa có budget input size/latency được đo. Cần đo/giới hạn hoặc chuyển công việc khi mở rộng input lớn, không tự hứa UI mượt với mọi kích thước.

| ADR | Lựa chọn hiện có | Tradeoff / trigger xem lại |
| --- | --- | --- |
| ADR-01 | Không backend, result trong bộ nhớ, history local opt-in | Đơn giản; draft không sống qua quit và chưa có sync/backup |
| ADR-02 | Transform và lưu history là hai outcome riêng | Có thể trả result dù write lỗi; UI phải nói đúng phần chưa lưu |
| ADR-03 | Extension chỉ đọc projection trạng thái | Không lộ raw text; cần App Group/signing và chấp nhận snapshot không realtime |

Source không gọi network hoặc thu analytics. Preferences lưu bằng Codable file. History chứa raw input/output nên cần giải thích retention và xóa theo BR; nếu thêm SDK, cloud, export hoặc diagnostics phải xem lại actual data practices và release policy. App Group chia sẻ local giữa targets, không sync thiết bị. Backup/migration/source update và privacy/support URLs sản phẩm vẫn chưa hoàn tất.

## 7. Delivery và validation

Source đã có; các slice sau hướng dẫn tích hợp/kiểm chứng một app mới, chưa có lịch giao hoặc bằng chứng native.

| Slice | Kết quả đầu-cuối | Dependencies | Criterion refs |
| --- | --- | --- | --- |
| SL-01 | Nhập → normalize/count → copy/share trên app chạy thật | Toolchain Apple và fixture Unicode | APP-01/02/04, UTL-01/02 |
| SL-02 | Bật history → lưu/mở lại → off/clear → xử lý lỗi | SL-01, store fixture/fault injection tách biệt | APP-03, UTL-02 |
| SL-03 | Publish trạng thái → widget → mở workbench giữ input | App Group và extensions signed | WID-01/02, APP-05 |

Fixtures đề xuất: empty/whitespace-only, emoji/Unicode, CRLF/CR/LF và trailing newline, hơn 50 successful runs, corrupted settings/history, failed writes, snapshot missing/invalid. Chốt coverage window/input/locale trước khi chạy; không giả dữ liệu người dùng thật trong fixtures. [NATIVE_CHECKS](../../starters/apple/NATIVE_CHECKS.md) có bước quan sát bổ sung.

Trong profile JSON đã chọn cho ví dụ này, title/flags nằm ở project JSON và record kết quả ở verification JSON; khai báo spec/source/rules/config ảnh hưởng trong inputs khi có evidence thật. Khi áp dụng cho dự án thật, giữ nguồn acceptance/evidence hiện có; JSON chỉ giữ trách nhiệm được chọn rõ. Không dùng test generator làm bằng chứng transform/native PASS. Ngưỡng performance và data sizes cần chốt trước nếu trở thành yêu cầu phát hành. Toàn bộ native evidence còn chưa có.

## 8. Release và learning

Chưa có release build, icon/screenshots, listing, support/privacy URLs hoặc owner phát hành. Dùng [release template](../../templates/product/release-operations.md) khi có sản phẩm thật; metadata phải phản ánh đúng thuật toán, retention, địa điểm lưu và feature chưa có. Không biến starter text utility thành lời hứa mọi loại xử lý văn bản.

Bước tiếp theo: tạo project Utility, chạy SL-01 và xác minh người dùng hiểu phép chuẩn hóa trước khi thêm công cụ mới. Nếu business evidence cho thấy task khác có giá trị hơn, đổi blueprint/PRD và specs liên quan; giữ rõ khác biệt giữa giả thuyết được thay và lỗi implementation cần sửa.

## Kiểm tra trước bàn giao

- [x] Đã ghi metadata, scope minh họa và ranh giới giữa giả thuyết, source đã viết và runtime chưa chạy.
- [x] Index dẫn nguồn theo chủ đề trong ví dụ đã chọn profile JSON; acceptance fields/results giữ tại project/verification JSON của ví dụ, mọi native criterion vẫn `NOT_RUN`.
- [ ] Khi dùng cho sản phẩm thật: gán owner, xác định người dùng/outcome và xử lý giả định ảnh hưởng tới lát cắt đầu.
- [ ] Chọn source/targets/configuration thực, kiểm tra native theo criteria và ghi evidence thật tại nguồn kết quả của dự án; giữ mọi kết quả `partial`, giới hạn và kiểm tra chưa chạy.
- [ ] Chốt phần việc bàn giao, câu hỏi còn mở và owner bước tiếp theo trong phạm vi quyền đã giao.
