# Use case: ứng dụng mới từ ý tưởng đến hướng có thể triển khai

## Đầu vào và quyền hạn

Ý tưởng thô, brief hoặc spec; nền tảng, dữ liệu, ràng buộc và mục tiêu đã biết. Dùng `c2o-work` hiện có hoặc specialist phù hợp qua [hướng dẫn tích hợp C2O](../../../references/product-design.md). Đọc thông tin có sẵn trước khi hỏi; dùng giả định có nhãn cho lựa chọn nhỏ có thể đảo ngược trong quyền đã giao. Đừng biến persona, pain point hay điểm ưu tiên do model tạo thành nghiên cứu đã xác thực.

Giữ mức can thiệp và các gate C2O đang áp dụng. Khi còn câu hỏi về giá trị, cấu trúc hoặc hướng thiết kế, chỉ mở tài nguyên giúp giải quyết câu hỏi đó; khi outcome và flow đã rõ, tiếp tục công việc đã được giao. Không cần chọn mode riêng, lặp lại quyết định đã chốt hoặc sinh đủ bộ tài liệu.

Brief/spec, acceptance và báo cáo hiện hữu giữ vai trò nguồn chuẩn. Tài nguyên bổ sung phần còn thiếu; template không tự giành ownership hoặc yêu cầu thêm metadata. Phân biệt design-only, implementation và review-only theo yêu cầu thật trước khi chọn hoạt động.

## Đầu ra theo phạm vi đã yêu cầu

| Câu hỏi | Công việc / artifact hữu ích |
| --- | --- |
| Cần business design, blueprint, PRD hoặc specs nào? | [Hệ thống tài liệu](../documentation/README.md), [product-pack gộp](../templates/product/product-pack.md), và nguồn chuẩn đã có của dự án |
| Xây để làm gì? | Outcome, scope, facts/assumptions, acceptance trong brief đang có |
| Có template app Apple theo category không? | [Lifestyle/Utility templates](../app-templates/README.md), [module matrix](../app-templates/module-matrix.md) và [SwiftUI starter](../starters/apple/README.md) khi cần source |
| Có những hướng nào? | [Khám phá](../core/exploration.md), [mẫu options](../templates/options.md) |
| Vì sao chọn hướng này? | [Mẫu quyết định](../templates/decision.md), evidence và tradeoff |
| Dữ liệu nên hiện bằng list, table, graph hay kiểu khác? | [Hợp đồng data view](../core/data-views.md), [catalog](../catalog/data-view-patterns.md), [mẫu áp dụng](../templates/data-view.md) |
| Dùng lại hoặc tạo component nào? | [Hợp đồng component](../core/components.md), [catalog](../catalog/components.md), [mẫu áp dụng](../templates/component.md) |
| Màn hình được tổ chức thế nào? | [Layout](../core/layout.md), [mẫu layout](../templates/layout.md), flow/state |
| Ghép thành màn và quản lý state thế nào? | [UI composition](../core/ui-composition.md), [mẫu screen](../templates/screen.md), [catalog màn theo nhiệm vụ](../catalog/screen-patterns.md) |
| Các màn giữ cùng hướng bằng gì? | [Baseline](../core/baseline.md), [mẫu baseline](../templates/baseline.md), token/component và reference |
| Cần tạo hình ảnh nào? | [Asset workflow](../core/assets.md), asset brief/manifest khi có nhu cầu |
| Đã kiểm chứng điều gì? | Acceptance/báo cáo hiện hữu, profile nền tảng và [evidence contract](../core/evidence.md) |

## Hoạt động tùy chọn trong C2O hiện có

Chọn hoạt động theo blocker hiện tại; bảng không tạo lifecycle mới hoặc yêu cầu đi qua mọi hàng.

| Skill hiện có | Hoạt động hữu ích khi còn thiếu |
| --- | --- |
| `c2o-shape` / `c2o-spec` | Xác định actor, task, data, context và outcome; giữ nguồn/rationale của tiêu chí, điều bắt buộc và câu hỏi có thể làm đổi phương án. |
| `c2o-decide` / `c2o-create` | Khám phá và so sánh lựa chọn ở đúng cấp còn mở, cùng nhiệm vụ/dữ liệu; xem constraints và tradeoff. Prototype câu hỏi khó khi được giao thay vì luôn tạo nhiều hướng. |
| `c2o-create` | Giữ quyết định và baseline đang dùng. Chọn data view theo task/dữ liệu, component theo trách nhiệm, vùng/ưu tiên/action/scroll/adaptation; ghi owner của query/selection/draft/commit cùng criterion. Chỉ tách contract riêng khi hữu ích. |
| `c2o-create` / `c2o-execute` | Chọn asset theo vai trò và route reuse/system/code/vector/raster/real photo. Chỉ tạo, thích ứng hoặc tích hợp asset trong scope; review artifact thực và giữ nguồn. |
| `c2o-slice` / `c2o-execute` | Khi implementation được yêu cầu, làm một phần xuyên suốt có trạng thái thật; kiểm tra quyết định chung bằng flow đại diện khi hữu ích rồi tiếp tục tất cả flow và deliverable đã cam kết. |
| `c2o-verify` / `c2o-learn` | Đối chiếu artifact hiện tại với acceptance, ghi bằng chứng và giới hạn; lưu bài học có khả năng ảnh hưởng công việc sau vào nguồn hiện hữu. |

Trong production được giao quyền, kiểm tra dữ liệu, layout, accessibility và asset theo phương pháp thực, sửa lỗi thuộc scope rồi recheck phần bị ảnh hưởng. Với review-only, chỉ ghi findings và evidence; không sửa artifact, đổi acceptance hoặc chuyển review thành implementation. Với design-only, chỉ kết luận về thiết kế/prototype đã xem; không suy ra runtime, usability research hay thành công của sản phẩm từ mockup.

Báo cáo criterion bằng `pass`, `partial`, `fail`, `not-tested` theo C2O và nguồn hiện hữu. Nêu rõ kiểm tra chưa chạy/bị chặn, coverage còn thiếu và lỗi đã quan sát. Runtime ngoài phạm vi review thiết kế cần lý do đúng boundary; runtime bắt buộc chưa chạy giữ `not-tested`, không trở thành `pass` vì thiết kế đã được chọn.

Chỉ khi đã chọn rõ profile JSON legacy cho phạm vi này mới dùng `verification.json` và các trạng thái `PASS`, `FAIL`, `NOT_RUN`, `BLOCKED`, `NOT_APPLICABLE` theo [hợp đồng bằng chứng](../core/evidence.md). Không có trạng thái JSON tương đương đầy đủ cho C2O `partial`; giữ kết quả một phần trong evidence và báo cáo C2O, không ép thành `PASS` hoặc tạo ledger acceptance cạnh tranh. Ví dụ và scaffold chưa chạy không được dùng thay report thật.

## Prompt dùng lại

```text
Dùng c2o-work hiện có cho ứng dụng này; dùng specialist C2O trực tiếp nếu giai đoạn đã rõ.
Đầu vào: [ý tưởng/brief/spec và tài liệu đã có].
Phạm vi đầu ra đầy đủ: [thiết kế / prototype / implementation / review và các deliverable].
Đọc brief/spec, acceptance và nguồn chuẩn hiện hữu; giữ quyền hạn đã có.
Chỉ mở tài nguyên product-design liên quan qua c2o-work/references/product-design.md.
Làm rõ phần outcome hoặc quyết định còn thiếu; không mở lại lựa chọn đã chốt nếu không có căn cứ.
Khi cần, so sánh phương án; chọn data view, component, layout và state owner theo task/dữ liệu.
Với Apple, chỉ chọn category/platform/module hoặc source starter thuộc yêu cầu thực.
Giữ baseline đang dùng; bổ sung asset plan và tài liệu chỉ khi giúp bước tiếp theo.
Tự xử lý lựa chọn nhỏ trong quyền hạn đã giao; ghi giả định ảnh hưởng.
Giữ đủ phạm vi sau flow đại diện; design-only không chuyển thành implementation.
Nếu review-only, báo findings và evidence mà không sửa artifact hoặc acceptance.
Kết thúc bằng deliverable coverage, artifact, quyết định và bằng chứng hiện tại.
Ghi pass/partial/fail/not-tested; nêu rõ phần chưa chạy và giới hạn của kết luận.
```

## Điểm dừng

Nếu nhiệm vụ là tìm hướng hoặc thiết kế, dừng khi artifact đã yêu cầu đủ rõ cho bước tiếp theo và được review đúng scope; quyết định còn mở có owner hoặc thử nghiệm cụ thể. Nếu nhiệm vụ gồm implementation, tiếp tục toàn bộ phạm vi đã cam kết sau flow đại diện, hoặc báo rõ phần bị chặn. Review hoàn tất có thể kết luận artifact không đạt. Nghiên cứu còn thiếu giữ là bất định; không dùng hình đẹp, điểm tổng hoặc template đã điền để che thiếu bằng chứng. Đừng thiết kế màn ngoài scope chỉ để hoàn thành một chuỗi file.
