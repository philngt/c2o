# C2O Design v1.2 — Web profile

Áp dụng cho website và web app, gồm dashboard. Profile nối outcome với component, tương tác trình duyệt và bằng chứng kiểm chứng. Điều chỉnh theo sản phẩm, framework và mức hỗ trợ thực tế.

Áp dụng qua [hướng dẫn tích hợp C2O](../../../references/product-design.md) trong skill và mức can thiệp đang dùng. Brief/spec, acceptance và báo cáo hiện hữu giữ vai trò nguồn chuẩn; chỉ đọc hướng dẫn giúp quyết định hoặc kiểm tra tiếp theo, không tạo lifecycle, mode hay hồ sơ bắt buộc mới.

## 1. Bắt đầu từ flow và hệ thống hiện có

Ghi `outcome`, route/flow, người dùng, browser/input hỗ trợ, dữ liệu, locale và tiêu chí hoàn thành. Với dashboard, nêu quyết định người dùng cần đưa ra; chọn hierarchy theo quyết định đó. Không bắt buộc mọi dashboard có một KPI khổng lồ hoặc mọi trang có cùng hero.

Đọc component library, tokens, routing và màn tương tự trước khi sửa. Tái sử dụng component có behavior phù hợp. Không thêm thư viện, font hoặc design system mới chỉ để đổi diện mạo. Style preference có thể thay đổi theo thương hiệu, mật độ và nội dung; nhận xét taste cần dẫn tới một vấn đề quan sát được, không có điểm phần trăm làm gate.

| Tình huống | Skill C2O liên quan khi cần | Kiểm chứng theo phạm vi |
|---|---|---|
| Chỉnh nhỏ trong pattern đã có | `c2o-execute`; `c2o-verify` cho kiểm tra | Render vùng đổi; thử hành vi và responsive liên quan |
| Component hoặc flow mới | `c2o-spec` hoặc `c2o-create` cho phần còn thiếu; `c2o-execute` khi đã yêu cầu code | Chạy flow; keyboard; state, viewport và theme đại diện |
| Tương tác mới, nhiều route/browser hoặc giả định lớn | `c2o-shape` / `c2o-decide` cho quyết định còn mở; `c2o-create` cho prototype được giao | Prototype câu hỏi khó; thêm kiểm tra interoperability/usability theo rủi ro |

Bảng là gợi ý hoạt động và coverage trong C2O hiện có, không yêu cầu chọn mode hay số tài liệu. Dùng bằng chứng để quyết định cần làm thêm gì. Flow đại diện giúp kiểm tra quyết định chung khi hữu ích; vẫn hoàn thành mọi route, flow, browser và deliverable đã cam kết.

## 2. Chuyển ý đồ thành implementation

**HTML semantics trước.** Dùng link cho navigation, button cho action, label cho field, table cho dữ liệu có quan hệ hàng/cột. Tận dụng component library đang có. Custom select, dialog hay grid cần lý do từ tác vụ và phải triển khai keyboard, focus, accessible name/state. ARIA mô tả semantics, không tự tạo hành vi bàn phím. [W1]

**Tokens có vai trò.** Component dùng semantic/component tokens của dự án. Kiểm tra theme thực, không chỉ JSON hợp lệ. Theo dõi một giá trị từ token tới computed style khi có mismatch. Không token hóa mọi con số cơ học: tỷ lệ ảnh, số cột hoặc offset gắn với một thuật toán cần được giải thích tại nơi sử dụng.

**State theo ngữ cảnh.** Field có thể có invalid/read-only; button có pressed/loading; tab có selected. Không ép mọi component có tám state. Disabled và `aria-disabled` cần behavior tương ứng. Loading xác định retry/cancel, giữ dữ liệu và ngăn gửi trùng theo nghiệp vụ. Error cho biết cách phục hồi. Empty phân biệt “chưa có dữ liệu” với “bộ lọc không có kết quả”. Hiển thị stale/offline khi mô hình dữ liệu cần; không giả báo success.

**Content và layout.** Dùng nhãn có nghĩa, cho chuỗi dịch/nội dung dài wrap. Tránh fixed height cho vùng chứa text chưa biết trước. Navigation phải giữ được context khi back/forward. Chart cần đơn vị, nhãn và cách đọc giá trị quan trọng; chọn mật độ theo tác vụ. Desktop-only có thể là phạm vi sản phẩm, nhưng zoom và accessibility vẫn phải được xét.

## 3. Kiểm tra trên browser thật

Chạy UI implementation đang giao. HTML dựng lại, SSR output hoặc screenshot tĩnh không chứng minh event handler, hydration, focus hay dữ liệu được lưu. Automation cần điều khiển luồng tương tác và kiểm tra kết quả, không chỉ tìm thấy một selector.

| Check | Bằng chứng cần quan sát |
|---|---|
| Core flow | Click/submit → trạng thái xử lý → kết quả; dữ liệu giữ đúng sau back, retry hoặc reload khi có yêu cầu |
| Keyboard | Tab/Shift+Tab, Enter/Space phù hợp; focus nhìn thấy; Escape/arrow keys theo pattern; focus trả về nơi hợp lý khi đóng overlay |
| Accessibility | Name/role/value/state đúng; lỗi gắn với field; thông báo thay đổi có ý nghĩa; thử screen reader khi control/flow yêu cầu |
| Contrast | Text và control trên nền thực, gồm theme, overlay và state liên quan; đo computed/rendered values thay vì suy từ palette |
| Layout/zoom | Viewport hẹp và rộng liên quan; text 200%; reflow ở mức tương đương 320 CSS px; sticky UI không che nội dung/focus |
| Locale/motion | Chuỗi dài, số/ngày theo locale; RTL nếu hỗ trợ; Reduce Motion khi có animation; chức năng vẫn nhận được phản hồi |
| Data | Empty/loading/error và permission/stale/offline nếu tồn tại; không mất input khi thất bại |

Nếu mục tiêu là WCAG 2.2 AA, contrast text thông thường là 4.5:1, large text là 3:1 theo định nghĩa và ngoại lệ của tiêu chí. Dùng tiêu chí phù hợp cho non-text UI; đừng áp tỷ lệ text cho mọi pixel. [W2]

Reflow có ngoại lệ cho phần nội dung cần bố cục hai chiều, như bảng hoặc bản đồ; ngoại lệ không tự áp cho cả trang. 400% zoom từ viewport rộng 1280 CSS px tương đương 320 CSS px. Kiểm tra text resize và reflow như hai nhu cầu liên quan nhưng khác nhau. [W3]

Vùng target WCAG 2.2 AA có mốc 24×24 CSS px cùng các ngoại lệ, gồm spacing/inline; không kiểm tra mỗi width rồi kết luận. Chọn target rộng hơn khi thao tác touch cần sự thoải mái. [W4]

Chọn coverage theo audience và vùng thay đổi. Một browser đã chạy chỉ chứng minh browser đó. Browser emulation không thay toàn bộ kiểm tra Safari/mobile hoặc screen reader. Mở rộng khi có API/layout khác biệt hay người dùng mục tiêu cần; tránh chạy mọi tổ hợp mà không có câu hỏi cụ thể.

## 4. Deliverable và báo cáo trung thực

Giao code/stylesheet có thể chạy trong dự án khi nhiệm vụ yêu cầu implementation, kèm quyết định, flow/state coverage và bằng chứng browser. Nếu chỉ thiết kế, giao artifact và kết luận đúng phần đã xem; nêu rõ interactive behavior còn cần implementation, không suy bằng chứng runtime từ mockup. Giữ fixture deterministic để tái hiện; đánh dấu dữ liệu mô phỏng.

Với review-only, dùng `c2o-verify` để đọc contract và artifact hiện tại, ghi findings và giới hạn; không sửa code/asset, thay acceptance hoặc thay đổi trạng thái của đối tượng đang review. Chỉ sửa lỗi trong vòng production đã được giao quyền, rồi kiểm tra lại phần bị ảnh hưởng. Một flow đại diện không hoàn tất các deliverable khác đã cam kết.

Trong acceptance/báo cáo và evidence hiện hữu, ghi criterion, artifact/revision, check, scope, phương pháp, quan sát và giới hạn. Dùng `pass` khi bằng chứng hiện tại bao phủ đầy đủ tiêu chí; `partial` khi mới có một phần coverage/kết quả cần thiết; `fail` khi đã thấy lỗi; `not-tested` khi chưa chạy hoặc bị chặn. Giữ nguyên lỗi đã thấy và coverage chưa kiểm tra, không dùng kết quả của một trường hợp để đại diện tất cả biến thể đã cam kết.

Ví dụ phạm vi có lý do: RTL ngoài locale hỗ trợ; dialog focus-return không áp dụng nếu không có overlay bị ảnh hưởng. Thiếu browser binary là `not-tested` với blocker; chưa thử NVDA là `not-tested` vì chưa thực hiện. Không đổi các trường hợp chưa kiểm tra thành `pass`. Không dùng “desktop-only” để miễn kiểm tra keyboard.

Chỉ khi đã chọn rõ profile JSON legacy cho phạm vi này mới dùng `verification.json` với `criterion_id`, `status`, `rationale`, `inputs`, `evidence`, path và SHA-256 theo [hợp đồng bằng chứng](../core/evidence.md). `PASS` / `FAIL` ghi kết quả đã quan sát; `NOT_RUN` / `BLOCKED` giữ kiểm tra chưa chạy và lý do; `NOT_APPLICABLE` cần contract cho phép cùng lý do đúng phạm vi. Profile này không có trạng thái tương đương đầy đủ cho C2O `partial`: giữ chi tiết trong evidence và báo cáo C2O, không ép thành `PASS`, bỏ lỗi hoặc tạo nguồn acceptance cạnh tranh.

Build, lint, axe và visual review cho các loại bằng chứng khác nhau. Ghi lỗi taste bằng tình huống, ảnh và tác động; dùng review để quyết định. Không tuyên bố toàn bộ app accessible chỉ vì axe không tìm lỗi, hoặc mọi tương tác đúng vì screenshot đẹp.

## 5. Asset trong web UI

Giữ thông tin asset, baseline và layout cần cho nhiệm vụ tại nguồn hiện có theo [hợp đồng asset](../core/assets.md); manifest riêng là tùy chọn. Tái sử dụng icon family của component library hoặc hệ thống hiện có. Custom artwork phục vụ mục đích rõ; không thay semantic controls, text hoặc chart có dữ liệu bằng ảnh mockup.

Giữ nguồn ảnh specimen/sản phẩm thật và phạm vi được chỉnh. Không dựng ảnh giả để đại diện record thật, sửa đặc điểm sản phẩm hay thay số liệu trong ảnh. Illustration sinh ra cần được phân loại riêng; nội dung minh họa không trở thành bằng chứng nghiệp vụ. Text quan trọng cần cập nhật, dịch và truy cập được.

Trước export, ghi kích thước nguồn, vùng crop/focal area, alpha, appearance, kích thước hiển thị dự kiến và fallback. Review trên nền thực, gồm viền trong suốt, crop responsive và chi tiết ở kích thước nhỏ. Không suy chất lượng từ độ phân giải file hoặc ảnh preview phóng lớn.

Trong browser, xác nhận asset thực được tải từ đường dẫn dự kiến, không dùng nhầm candidate cũ. Kiểm tra resize, zoom, theme liên quan, lỗi tải và trạng thái trước khi ảnh xuất hiện. Giữ thông tin hoặc thao tác cần thiết khi asset thiếu; ảnh trang trí không được chặn flow. Ghi browser, viewport, dataset và asset version trong evidence.

Format hỗ trợ, decoder đọc được và player phát đúng là ba việc khác nhau. Đừng suy playback trên mọi browser từ một preview. Animation cần kiểm tra loop, timing, crop và fallback tĩnh với Reduce Motion; phản hồi trạng thái vẫn phải rõ. Chỉ thêm player/dependency khi nhu cầu thực vượt khả năng của implementation hiện có.

Export check, browser integration và runtime review là các criterion khác nhau. Chưa chạy browser/player thì ghi `not-tested` với lý do chưa chạy hoặc bị chặn; không dùng screenshot similarity hay file xuất thành công để nâng thành `pass` toàn flow. Giữ partial coverage và lỗi đã quan sát trong bằng chứng hiện hữu.

## 6. Component, data view và composition

Áp dụng [hợp đồng component](../core/components.md), [data view](../core/data-views.md) và [composition](../core/ui-composition.md) vào library/router/state model thực của dự án. Catalog đề xuất trách nhiệm và cách chọn; không cung cấp React component hoặc CSS có sẵn. Tái sử dụng semantics/hành vi phù hợp của implementation hiện có.

Phân biệt CSS grid để xếp vùng, HTML table cho quan hệ hàng/cột và interactive grid có hợp đồng điều hướng/focus theo ô. Một table vẫn có thể chứa button, link hay input mà không phải chuyển toàn bộ thành ARIA grid. Chọn grid khi task cần hành vi đó và thực hiện đầy đủ keyboard/focus. [W5]

Ghi selection theo ID, scope của filter/sort/paging và quyền truy cập dữ liệu. Dữ liệu đầy đủ, dữ liệu đã tải và kết quả sau lọc có thể khác nhau; UI cần diễn đạt đúng tập mà count/bulk action/export áp dụng. Khi đổi layout, giữ khả năng so sánh hoặc đọc giá trị cần cho task. Nguồn dữ liệu/quy tắc nghiệp vụ có một nơi chuẩn, component phát intent thay vì tự suy nghĩa dữ liệu.

## Nguồn nền tảng

- [W1 — W3C APG: Semantics và khả năng tương tác](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)
- [W2 — W3C: Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- [W3 — W3C: Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- [W4 — W3C: Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- [W5 — W3C APG: Table](https://www.w3.org/WAI/ARIA/apg/patterns/table/) và [Grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)
