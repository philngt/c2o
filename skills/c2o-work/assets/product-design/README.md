# Tài nguyên thiết kế sản phẩm cho C2O

Bộ tài nguyên tùy chọn để dùng lại cho ý tưởng ứng dụng, khám phá phương án, thiết kế UI, đặc tả và triển khai. Đây là bản tích hợp từ **C2O Design 1.5.0**; C2O hiện có vẫn điều phối công việc. Bắt đầu ở [router product design](../../references/product-design.md), rồi chỉ mở phần giải quyết câu hỏi đang có.

`VERSION` và `framework_version` trong ví dụ giữ phiên bản nguồn để truy xuất xuất xứ; chúng không phải phiên bản plugin C2O. Bản tích hợp này chưa phát hành riêng. Tài liệu hướng dẫn chi tiết và UI starter chủ yếu bằng tiếng Việt.

## Chọn tài nguyên theo nhu cầu

| Nhu cầu hiện tại | Tài nguyên nên mở |
| --- | --- |
| Ý tưởng ứng dụng mới, chưa rõ hướng | [Use case ứng dụng mới](use-cases/new-app.md), [khám phá phương án](core/exploration.md) |
| Business design, product/service blueprint, PRD, specs | [Hướng dẫn tài liệu](documentation/README.md), [product pack gộp](templates/product/product-pack.md) |
| Dùng template có định danh, input/output và trách nhiệm rõ | [Chuẩn template 1.0](documentation/template-standard.md), [registry 24 mẫu](documentation/template-registry.json) |
| Giữ nhất quán giữa các màn | [Baseline](core/baseline.md), [nguyên tắc](core/principles.md) |
| Chọn và đặc tả component | [Hợp đồng component](core/components.md), [catalog 28 nhóm](catalog/components.md) |
| Chọn list, table, chart, graph hoặc kiểu dữ liệu khác | [Hợp đồng data view](core/data-views.md), [catalog 14 pattern](catalog/data-view-patterns.md) |
| Đề xuất bố cục và cách thích ứng | [Hợp đồng layout](core/layout.md), [catalog 10 pattern](catalog/layout-patterns.md) |
| Ghép thành màn với state và action rõ | [UI composition](core/ui-composition.md), [catalog 8 pattern màn](catalog/screen-patterns.md) |
| Reference, icon, artwork, ảnh dữ kiện và export | [Tài nguyên hình ảnh](core/assets.md), [mẫu asset brief](templates/asset-brief.md) |
| Triển khai hoặc kiểm tra giao diện | [SwiftUI profile](profiles/swiftui.md), [web profile](profiles/web.md) |
| App Lifestyle/Utility cho iPhone, iPad, macOS, widget | [Category/platform recipes](app-templates/README.md), [module matrix](app-templates/module-matrix.md) |
| Source SwiftUI ban đầu khi đã yêu cầu scaffolding | [Apple starter](starters/apple/README.md) |
| Tham khảo một bộ tài liệu đã điền | [Plantline](examples/plantline/brief.md), [Lifestyle](examples/lifestyle-docs/product-pack.md), [Utility](examples/utility-docs/product-pack.md) |
| Cần định dạng JSON để kiểm tra hồ sơ evidence | [Hợp đồng evidence tùy chọn](core/evidence.md), [công cụ](tools/README.md) |
| Đối chiếu nguồn và phạm vi chưng cất | [Sources](SOURCES.md), [ghi chú gpt-ui-assets](notes/gpt-ui-assets-distillation.md) |

Catalog là hướng dẫn lựa chọn và hợp đồng thiết kế, chưa phải thư viện đầy đủ các component SwiftUI/React. Source starter hiện thực hóa hai flow cụ thể; không hiện thực hóa mọi pattern trong catalog. Các số lượng mô tả phạm vi tài nguyên, không bảo đảm chất lượng hoặc độ bao phủ mọi ứng dụng.

## Cách dùng trong dự án

1. Đọc outcome, phạm vi đã cam kết, quyền quyết định, design system và tài liệu acceptance hiện có. Dùng `c2o-work` hoặc skill chuyên biệt đang phù hợp.
2. Chọn một tài nguyên có ích cho phần còn thiếu. Dùng trực tiếp đoạn cần thiết hoặc cập nhật tài liệu tương đương đang có; không phải tạo đủ bộ tài liệu.
3. Giữ một nguồn chuẩn cho mỗi quyết định, requirement và kết quả. `.context/acceptance.md`, tracker hoặc spec hiện có vẫn hợp lệ. Không tự chuyển sang `.design/`.
4. Dùng C2O để tạo, triển khai hoặc review đúng quyền hạn đã giao. Review-only chỉ trả phát hiện; chỉ sửa khi nhiệm vụ cho phép. Một lát cắt hoàn thành không làm mất phần còn lại của yêu cầu lớn hơn.
5. Ghi evidence cho artifact và phạm vi thực đã kiểm tra. Đừng suy native behavior từ wireframe, screenshot giả lập, JSON hợp lệ hoặc generator chạy được.

Chuẩn 12 trường metadata áp dụng cho **24 template được phân phối trong pack**. Tài liệu dự án có thể chỉ mượn cấu trúc/đoạn cần thiết và giữ định dạng, ID, revision, owner sẵn có. Không yêu cầu migration hoặc bổ sung metadata hàng loạt. Template đã thích ứng cho C2O có version `1.1.0`; schema chuẩn template vẫn là `1.0.0`.

## Acceptance và JSON là hai lựa chọn có phạm vi rõ

C2O giữ trạng thái native `pass`, `partial`, `fail`, `not-tested` và quy tắc tổng hợp verdict của chính nó. Việc dùng các mẫu thiết kế không thay hệ trạng thái đó.

Các file `project.json`/`verification.json`, schema và `design_check.py` hỗ trợ **profile JSON kế thừa, chỉ dùng khi dự án chủ động chọn**. Nếu sử dụng, ghi rõ scope và nơi giữ nguồn chuẩn; không duy trì hai bảng acceptance hoặc kết quả có thể sửa độc lập. Report có thể là bản xuất theo phiên bản từ nguồn chuẩn. Các ví dụ đi kèm minh họa profile này, không tự áp đặt nó lên dự án thật.

Profile JSON dùng `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, `NOT_APPLICABLE`; nó không có ánh xạ đầy đủ cho `partial`. Giữ phần đạt, phần thiếu và verdict `partial` tại nguồn native khi cần; không ép thành `PASS`. `RECORDS_READY` chỉ nói về hồ sơ được kiểm tra, không có nghĩa sản phẩm đạt, công việc C2O đã `DONE`, hoặc được quyền phát hành.

## Apple source starter

Starter có Lifestyle collection và Utility text workbench, shell iPhone/iPad/macOS và nguồn widget summary chỉ đọc. Generator dùng thư viện chuẩn Python và chỉ tạo vào **thư mục mới do người dùng chọn**. Chỉ chạy khi nhiệm vụ có yêu cầu scaffolding; không cần generator để dùng catalog hoặc template.

Root `project.json` trong ứng dụng được sinh là **XcodeGen specification**. `.design/project.json` là scaffold JSON minh họa riêng, không ghi đè acceptance C2O hiện có. Generator không cài Xcode/XcodeGen, không ký, build hay phát hành ứng dụng. Các bước native được mô tả trong [GETTING_STARTED](starters/apple/GETTING_STARTED.md) và [NATIVE_CHECKS](starters/apple/NATIVE_CHECKS.md); chưa chạy chúng trong lần tích hợp này.

## Kiểm tra bộ tài nguyên

Chạy từ thư mục pack này:

```bash
python3 tools/template_check.py --root .
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s starters/apple/tests -v
```

`TEMPLATES_VALID` kiểm tra cấu trúc catalog, metadata và liên kết được tool hỗ trợ. Unit tests kiểm tra hành vi checker và generator. Chúng không chấm chất lượng thiết kế, kiểm thử ứng dụng native hay xác nhận model làm việc tốt hơn. Các scenario ở cấp repo được công bố riêng với trạng thái chưa chạy.

## Xuất xứ và giới hạn

Tài nguyên được viết và chưng cất từ các nguyên tắc đã đối chiếu trong [SOURCES](SOURCES.md), gồm hai repo tham khảo được pin theo commit. Không đóng gói lại mã nguồn, asset hoặc runtime của hai repo đó. Lịch sử phát hành, PDF, checksum và báo cáo validation của bản độc lập không được nhập vào đây để tránh nhầm kết quả lịch sử với kết quả của PR.

Nếu một tài nguyên hoặc công cụ tùy chọn không có, tiếp tục phần công việc an toàn bằng nguồn dự án hiện có và ghi đúng khoảng trống. Chỉ ghi blocker cho kết quả thực sự phụ thuộc phần thiếu.
