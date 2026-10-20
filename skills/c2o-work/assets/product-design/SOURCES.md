# Nguồn và phạm vi thiết kế lại

C2O Design là bản tổng hợp và thiết kế lại cho workflow cá nhân của Ngo Phuc. Tài liệu, mẫu và công cụ kiểm tra trong gói được viết riêng. Gói không kèm mã nguồn, bộ gate, asset hoặc thư viện design system của repo tham khảo.

## Xuất xứ bản tích hợp C2O

Bản này thích ứng từ bộ độc lập **C2O Design 1.5.0** vào tài nguyên tùy chọn của `c2o-work`. `VERSION` và `framework_version` giữ xuất xứ bộ nguồn, không thay phiên bản plugin C2O. Các template được điều chỉnh lên `1.1.0` để ghi rõ vai trò tùy chọn; chuẩn cấu trúc template vẫn là `1.0.0`. C2O hiện có giữ workflow, scope, quyền quyết định, acceptance và verdict.

Lịch sử phát hành, PDF, checksum và báo cáo validation của bộ độc lập không được đưa vào bản tích hợp. Kiểm tra hiện tại của repo/PR mới là evidence cho các file đã thích ứng; nguồn Swift vẫn chưa có build/runtime evidence đi kèm. Các giấy phép được dẫn ở dưới thuộc nguồn tham khảo tương ứng, không được suy thành giấy phép mới của toàn bộ pack.

## 1. ux-ui-agent-skills

- [plugin87/ux-ui-agent-skills, commit 62092bd83bc3df0bcb9a2b3b643305ab11c547da](https://github.com/plugin87/ux-ui-agent-skills/tree/62092bd83bc3df0bcb9a2b3b643305ab11c547da), được đánh giá ngày 19/10/2026.
- [Component specification and rendered state verification](https://github.com/plugin87/ux-ui-agent-skills/blob/62092bd83bc3df0bcb9a2b3b643305ab11c547da/.claude/skills/design-component/SKILL.md).
- [Design system role mapping](https://github.com/plugin87/ux-ui-agent-skills/blob/62092bd83bc3df0bcb9a2b3b643305ab11c547da/design-systems/interop-protocol.md).
- [Critique workflow](https://github.com/plugin87/ux-ui-agent-skills/blob/62092bd83bc3df0bcb9a2b3b643305ab11c547da/.claude/skills/critique/SKILL.md).
- [Published evaluation provenance and limitations](https://github.com/plugin87/ux-ui-agent-skills/blob/62092bd83bc3df0bcb9a2b3b643305ab11c547da/evals/RESULTS.md).

Các ý được giữ: token theo ý nghĩa, state coverage theo applicability, quan sát render/tương tác thật, critic có bằng chứng, mapping nền tảng và ghi rõ giới hạn phép đo. Các ý được thay: luật thẩm mỹ tuyệt đối, yêu cầu quy trình giống nhau cho mọi nhiệm vụ, suy ra pass từ exit code, và suy ra native readiness từ kiểm tra web.

## 2. gpt-ui-assets

- [Shakibuzzaman3104/gpt-ui-assets, commit ec246513cfc3a2f6ee368022c83bd09100169bab](https://github.com/Shakibuzzaman3104/gpt-ui-assets/tree/ec246513cfc3a2f6ee368022c83bd09100169bab), đọc ngày 20/10/2026; metadata phiên bản 5.2.0.
- [README và workflow được công bố](https://github.com/Shakibuzzaman3104/gpt-ui-assets/blob/ec246513cfc3a2f6ee368022c83bd09100169bab/README.md).
- [Skill điều phối](https://github.com/Shakibuzzaman3104/gpt-ui-assets/blob/ec246513cfc3a2f6ee368022c83bd09100169bab/skills/gpt-ui-assets/SKILL.md).
- [Design/reference](https://github.com/Shakibuzzaman3104/gpt-ui-assets/blob/ec246513cfc3a2f6ee368022c83bd09100169bab/skills/gpt-ui-assets/references/design.md), [asset production](https://github.com/Shakibuzzaman3104/gpt-ui-assets/blob/ec246513cfc3a2f6ee368022c83bd09100169bab/skills/gpt-ui-assets/references/assets.md), [build UI](https://github.com/Shakibuzzaman3104/gpt-ui-assets/blob/ec246513cfc3a2f6ee368022c83bd09100169bab/skills/gpt-ui-assets/references/build-ui.md), [hybrid routing](https://github.com/Shakibuzzaman3104/gpt-ui-assets/blob/ec246513cfc3a2f6ee368022c83bd09100169bab/skills/gpt-ui-assets/references/hybrid.md).
- [Imaging helpers](https://github.com/Shakibuzzaman3104/gpt-ui-assets/blob/ec246513cfc3a2f6ee368022c83bd09100169bab/skills/gpt-ui-assets/scripts/gptkit/imaging.py), [comparison](https://github.com/Shakibuzzaman3104/gpt-ui-assets/blob/ec246513cfc3a2f6ee368022c83bd09100169bab/skills/gpt-ui-assets/scripts/gptkit/compare.py), [plan evaluations](https://github.com/Shakibuzzaman3104/gpt-ui-assets/blob/ec246513cfc3a2f6ee368022c83bd09100169bab/evals/evals.json).
- [MIT License, copyright 2026 Shakibuzzaman](https://github.com/Shakibuzzaman3104/gpt-ui-assets/blob/ec246513cfc3a2f6ee368022c83bd09100169bab/LICENSE).

| Ý tham khảo | Cách đưa vào C2O Design |
| --- | --- |
| Anchor/reference cho các màn tiếp theo | Baseline có revision, scope, token và hành vi; ảnh là một đầu vào có mục đích rõ. |
| Inventory trước sản xuất asset | Manifest mô tả vai trò, nguồn, route, vùng đặt, fallback và evidence. Không phải hàng đợi tự chạy. |
| Kết hợp code với hình ảnh | UI có semantics/data bằng code; chọn system icon, vector chính xác, raster hoặc ảnh thật theo nhu cầu. |
| Reference tập trung và kiểm tra asset | Giữ nguồn, file dẫn xuất và thông số; xem ở cỡ sử dụng trên nền thật. Crop/redraw phụ thuộc nhiệm vụ. |
| Asset export và screenshot comparison | Tách chất lượng file, tích hợp runtime, visual và behavior; ghi coverage, skip và giới hạn phép đo. |

Phần được điều chỉnh: không dùng tuyên bố “1:1”, ngưỡng similarity hoặc kích thước ảnh sinh ra làm bảo đảm chung; không bắt custom artwork thay mọi icon; không biến hình minh họa thành ảnh dữ kiện. Không cố định provider/model, giá, tỉ lệ frame, safe zone hoặc ma trận export cho mọi nền tảng.

[Ghi chú chưng cất](notes/gpt-ui-assets-distillation.md) giải thích lựa chọn và giới hạn review. Đây là đọc tài liệu/mã nguồn, chưa chạy gptkit, model hoặc native workflow của repo nguồn. Gói không mang mã, prompt nguyên văn, asset hay dependency của repo này.

## Apple

- [Get started with Dynamic Type, WWDC24](https://developer.apple.com/videos/play/wwdc2024/10074/): text styles, layout thích ứng, Xcode previews và phạm vi accessibility audit.
- [Human Interface Guidelines: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).
- [Human Interface Guidelines: Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons).
- [Performing accessibility audits for your app](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app).
- [Human Interface Guidelines: Image views](https://developer.apple.com/design/human-interface-guidelines/image-views).
- [Icon Composer](https://developer.apple.com/icon-composer/): đối chiếu workflow icon với target/toolchain đang dùng.
- [What’s new in SwiftUI, WWDC25](https://developer.apple.com/videos/play/wwdc2025/256/): thích ứng cửa sổ và split navigation; dùng làm tham khảo, kiểm tra API/behavior trên target thực.

Profile cần đối chiếu deployment target, phiên bản công cụ và guideline đang áp dụng khi bắt đầu dự án; danh sách link là điểm truy cập, không phải snapshot mọi API.

## Web

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/).
- [WAI ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/).
- [WAI ARIA APG: Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/).
- [APG Table](https://www.w3.org/WAI/ARIA/apg/patterns/table/) và [Grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/): phân biệt quan hệ dữ liệu với composite interaction và focus.
- APG [Button](https://www.w3.org/WAI/ARIA/apg/patterns/button/), [Link](https://www.w3.org/WAI/ARIA/apg/patterns/link/), [Tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/), [Checkbox](https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/), [Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) và [Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/): đối chiếu semantics, input, focus và state của component web.
- [Understanding Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html): phạm vi thích ứng và ngoại lệ nội dung cần bố cục hai chiều.

Các tiêu chí accessibility cần được chọn theo phạm vi sản phẩm và phép kiểm tra thực. Tài liệu framework không tự tạo chứng nhận tuân thủ.

## Trình bày dữ liệu

- [ONS: Choosing a chart type](https://service-manual.ons.gov.uk/data-visualisation/chart-types/choosing-a-chart-type), [Bar charts](https://service-manual.ons.gov.uk/data-visualisation/chart-types/bar-charts) và [Line charts](https://service-manual.ons.gov.uk/data-visualisation/chart-types/line-chart): chọn biểu diễn theo dữ liệu/câu hỏi; kiểm tra scale, baseline, đơn vị và cách đọc giá trị.

Các nguồn trên được dùng để đối chiếu nguyên tắc và hành vi trong bản v1.2 ngày 20/10/2026. Catalog là tổng hợp đề xuất của C2O Design; không sao chép thư viện UI, không tuyên bố đây là phân loại chuẩn hoặc mẫu đã kiểm thử trên mọi nền tảng.

## Các quyết định riêng của framework

### Apple app templates và starter v1.3

- [Apple: Choosing a category](https://developer.apple.com/app-store/categories/): Lifestyle/Utilities là category phát hành theo chức năng cốt lõi, không quy định taxonomy UI.
- [WidgetKit foundations, WWDC26](https://developer.apple.com/videos/play/wwdc2026/277/) và [Keeping a widget up to date](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date): snapshot/placeholder/timeline, shared data và reload do hệ thống điều phối.
- [Configuring app groups](https://developer.apple.com/documentation/xcode/configuring-app-groups), [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.application-groups) và [Accessing app group containers](https://developer.apple.com/documentation/xcode/accessing-app-group-containers): identity/capability và truy cập container cần xác minh với signing thực.
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview), [Window](https://developer.apple.com/documentation/swiftui/window), [Settings](https://developer.apple.com/documentation/swiftui/settings), [SettingsLink](https://developer.apple.com/documentation/swiftui/settingslink): đối chiếu shell native của starter.
- [XcodeGen Project Spec](https://github.com/yonaskolb/XcodeGen/blob/master/Docs/ProjectSpec.md): specification JSON/YAML, local Swift package, target/dependency, Info.plist và entitlements. XcodeGen không được vendor hoặc cài trong gói.

Nguồn đối chiếu ngày 20/10/2026. Source mới được viết cho C2O Design, chưa compile/typecheck bằng Apple SDK. SwiftPM tools version 5.9, Swift language mode 5 và deployment floor 17/14 là lựa chọn starter; không là tuyên bố toolchain mới nhất hoặc yêu cầu phát hành hiện hành. Các platform docs có nguồn chi tiết theo mục.

Trong bộ độc lập, năm lớp Outcome, Experience, Visual, Platform, Evidence; các hoạt động Inspect, Frame, Design, Build, Verify, Learn; ba nhãn quick/standard/deep; hợp đồng JSON evidence và ví dụ Plantline là cách tổ chức được đề xuất cho nhu cầu tái sử dụng. Khi tích hợp, những hoạt động này nằm trong các stage C2O hiện có; nhãn chỉ gợi ý độ sâu đọc và profile JSON chỉ dùng khi được chọn. Chúng không tạo lifecycle, intervention level hoặc nguồn acceptance thứ hai. Nhánh Explore → Compare → Decide, bộ layout/baseline và chuỗi ID tài liệu hỗ trợ sáng tạo, chọn phương án và giữ nhất quán. Đây không phải nguyên gói sao từ một repo hoặc phương pháp đã được benchmark trên nhiều dự án.

v1.2 thêm 28 nhóm component, 10 layout pattern, 14 data-view pattern, 8 screen pattern và hợp đồng ghép chúng. Các khía cạnh có thể giao nhau: list–detail vừa tổ chức không gian vừa phối hợp selection; form vừa sắp xếp field vừa quản lý nhiệm vụ nhập. Số lượng catalog chỉ mô tả phạm vi gói, không là thước đo chất lượng hay bảo đảm bao phủ mọi use case.


### Hệ thống tài liệu sản phẩm v1.4

Các template và quy ước product blueprint/document ownership là tổng hợp riêng cho C2O Design; không phải một bộ tiêu chuẩn bắt buộc hoặc bản sao của template bên ngoài. Đối chiếu nguồn ngày 20/10/2026:

- [Strategyzer — Business Model Canvas](https://www.strategyzer.com/library/the-business-model-canvas): góc nhìn tạo/cung cấp/thu nhận giá trị và giữ mô hình kinh doanh ở mức giả thuyết cần evidence. Không sao chép canvas hoặc đưa dữ liệu pricing/market của ví dụ thành fact.
- [NN/g — Service Blueprints: Definition](https://www.nngroup.com/articles/service-blueprints-definition/): phân biệt service blueprint theo journey/frontstage/backstage/handoff với product map và architecture diagram.
- [C4 — Diagrams](https://c4model.com/diagrams): chọn mức sơ đồ kiến trúc phục vụ người đọc, không yêu cầu vẽ đủ bốn mức cho mọi app.
- [Cucumber — Gherkin reference](https://cucumber.io/docs/gherkin/reference/): cách diễn đạt scenario bằng context/action/observable outcome; các bảng ví dụ không phải executable automated tests.
- [Apple — Manage app privacy](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy/) và [App Review](https://developer.apple.com/distribute/app-review/): nguồn kiểm tra actual data practices, privacy/support links và thông tin phát hành. Template không tự xác nhận compliance, không tạo policy hoặc contact giả; kiểm tra yêu cầu hiện hành khi phát hành thật.

Đọc nguồn, có spec hoặc đã viết code không là bằng chứng product-market fit, native behavior hoặc quyền publish. Hai product packs mới là ví dụ cùng source starter, không chứa nghiên cứu người dùng/giá bán/benchmark giả.
