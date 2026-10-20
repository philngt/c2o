# Chỉ mục tài liệu và nguồn chuẩn — [dự án / phạm vi]

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-DOCUMENT-INDEX` |
| Phiên bản template | `1.1.0` |
| Mục đích | Giúp người và agent tìm đúng nguồn chuẩn, owner và revision cho một chủ đề; làm rõ các tham chiếu còn thiếu hoặc mâu thuẫn. |
| Dùng khi | Có nhiều tài liệu, cần bàn giao công việc hoặc cần đăng ký các section của một product pack mà không tạo nguồn chuẩn cạnh tranh. |
| Đầu vào | Tài liệu/section đang dùng, scope nhiệm vụ, quyết định ownership hiện có và nguồn acceptance/evidence hiện hữu của dự án. |
| Đầu ra / bàn giao | Sổ đăng ký tài liệu và mapping chủ đề đến file/anchor/revision/owner, cùng khoảng trống có tác động tới bước tiếp theo. |
| Nguồn chuẩn | Chỉ mục chỉ giữ registry khi được dự án đăng ký cho vai trò đó; nội dung từng chủ đề vẫn thuộc nguồn đã đăng ký, criteria thuộc nguồn acceptance đã chọn và kết quả thuộc nguồn kết quả/evidence đã chọn. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Dự án/task, nhóm tài liệu và revision thuộc phạm vi chỉ mục] |

[Chuẩn template](../../documentation/template-standard.md): placeholder là chỗ cần xác định, không phải evidence. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu ghi lần thay đổi của bản dùng trong dự án, không phải cùng một số phiên bản.

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

## Mục đích, khi dùng và cách dùng

Chỉ dùng index này khi số nguồn/handoff cần nó; ghi tài liệu/section đang dùng và owner/revision/vai trò hữu ích cho scope. Không cần tạo đủ mọi mẫu; số lượng tài liệu không xác nhận implementation/testing.

Đọc [hướng dẫn tài liệu](../../documentation/README.md) và [traceability](../../documentation/traceability.md). Giữ tài liệu hiện hữu khi vẫn làm tốt công việc; một file có thể chứa nhiều chủ đề nếu mỗi chủ đề có section anchor rõ. Các đường dẫn tới sibling dưới đây là mẫu tham khảo của framework, không tự trở thành tài liệu canonical của dự án.

- Project/context root và nơi giữ nguồn tham chiếu hiện hữu:
- nguồn acceptance đã chọn đang áp dụng:
- nguồn kết quả/evidence đã chọn ghi kết quả hiện tại:

`accepted` nghĩa là tài liệu được chọn dùng trong quyền hạn hiện có. `reviewed` cần có một lần review thực với phạm vi/người hoặc vai trò ghi nhận; không suy ra đã được một người phê duyệt. Cả hai trạng thái đều không phải native pass, readiness phát hành hoặc quyền deploy/publish.

## 1. Sổ đăng ký đang áp dụng

Chỉ thêm tài liệu/section có thật hoặc ghi rõ là **còn thiếu**, owner và tác động của việc thiếu. Đường dẫn section dùng dạng `path/to/file.md#anchor`; không chỉ trỏ tới đầu một tài liệu tổng hợp dài. Một file có nhiều owner/chủ đề có thể có nhiều hàng với anchor khác nhau.

| Tài liệu/section và link | Vai trò | Owner | Revision/commit áp dụng | Trạng thái | Scope/use case được phục vụ | Cần cho scope |
| --- | --- | --- | --- | --- | --- | --- |
| [Điền link thật hoặc ghi còn thiếu] | canonical / summary / reference / evidence | | | | | required / optional |

`required`/`optional` ở đây nói về tài liệu cần cho công việc hiện tại, không thay đổi cờ `required` của criterion trong nguồn acceptance đã chọn. Ghi lý do khi cần một tài liệu; không chọn required chỉ vì template tồn tại. Một section tương đương trong tài liệu đang có có thể đáp ứng nhu cầu mà không tạo file mới.

| Vai trò | Cách sử dụng |
| --- | --- |
| `canonical` | Nguồn chuẩn của một chủ đề/ID trong scope và revision đã đăng ký; sửa quyết định tại đây |
| `summary` | Tóm tắt hoặc view dẫn xuất; trỏ về canonical, không tự thay nghĩa hoặc kết quả |
| `reference` | Nguồn tham khảo, catalog, ví dụ, nghiên cứu hoặc template; chưa mặc nhiên được chọn cho dự án |
| `evidence` | Quan sát/log/render/review có scope và inputs; dùng cùng verification record, không thay yêu cầu mong đợi |

Vai trò áp dụng theo chủ đề, không theo tên file. Một PRD có thể canonical cho requirements và chỉ summary cho domain rules. Đăng ký section tương ứng để người đọc không xem cả file như nguồn chuẩn cho mọi thứ.

## 2. Nguồn chuẩn theo chủ đề

Điền link tới **một nguồn đang áp dụng cho mỗi chủ đề hoặc mỗi ID có owner riêng**. Nếu đang có brief/spec giải quyết chủ đề, giữ nó; nhận một template mới không chuyển ownership ngầm.

| Chủ đề / ID | Canonical file + section + revision thực tế | Quy tắc về phạm vi nguồn chuẩn |
| --- | --- | --- |
| Vấn đề, giá trị, actor và giả thuyết kinh doanh | | Business design nếu cần; giả định chưa kiểm chứng vẫn là giả định |
| Outcome `OUT-…` | | Nguồn định nghĩa outcome đã đăng ký trong brief/business/pack; các bản tóm tắt giữ cùng ý nghĩa |
| Phạm vi phiên bản, ưu tiên và ràng buộc sản phẩm | | PRD hoặc scope section của pack đã đăng ký; blueprint lập bản đồ và dẫn chiếu |
| Outcome/scope của task cụ thể | | Brief/task spec hiện có, chỉ rõ subset và liên kết về scope phiên bản |
| Giả định `ASM-…` | | Mỗi giả định có nơi giữ phát biểu, căn cứ, owner và điều kiện kiểm chứng; không chép thành “sự thật” ở tài liệu khác |
| Feature/capability `F-…` | | Catalog sản phẩm đã đăng ký, thường trong PRD/pack; blueprint và feature spec tái sử dụng ID, không đặt một nghĩa khác |
| Yêu cầu `REQ-…` và ưu tiên/phạm vi của yêu cầu | | PRD giữ danh mục và phát biểu yêu cầu; chi tiết behavior liên kết tới feature spec |
| Business rule `BR-…`, entity `ENT-…`, thuật ngữ và ý nghĩa dữ liệu | | Domain model giữ rule, identity, field meaning và invariants; spec/code tham chiếu cùng ID |
| Hành vi feature, flow tác vụ theo tên + anchor và expected behavior chi tiết | | Feature spec; dẫn domain rules và các hợp đồng UI, không định nghĩa lại chúng |
| Screen flow, UI state, query/selection/draft owner và màn `SCR-…` | | Experience/screen contract; feature spec dẫn đúng section, blueprint chỉ lập bản đồ |
| Layout, token, component, data view và adaptation | | Baseline và contract chuyên biệt đã chọn; chỉ rõ nơi giữ từng quy tắc |
| Architecture/interface/persistence/concurrency/migration | | Technical spec cùng code/interface schema tương ứng; domain model giữ nghĩa dữ liệu |
| Lý do quyết định `ADR-…` hoặc decision ID hiện có | | Decision/ADR record; spec dẫn lựa chọn và lý do, không copy lịch sử; giữ namespace cũ nếu đã có |
| Slice `SL-…`, dependency, milestone và estimate | | Delivery plan hoặc backlog đã đăng ký |
| Phương pháp, dataset, environment và coverage cần kiểm chứng | | Validation plan; đây là kế hoạch kiểm tra |
| Criterion ID/nghĩa/tính bắt buộc | Nguồn acceptance đã chọn: | Giữ criteria, nguồn/rationale, applicability và phương pháp; các view khác chỉ tham chiếu |
| Kết quả xác minh đã ghi | Nguồn kết quả/evidence đã chọn: | Giữ trạng thái C2O, artifact/revision, quan sát và evidence theo ID criterion |
| Phiên bản/artifact phân phối, release content và vận hành | | Release/operations record; readiness và quyền thực hiện được ghi riêng |

`F-…` là feature/capability, không dùng làm flow ID. Flow dùng tên có nghĩa và anchor tới section. Dùng lại các acceptance ID đang có trong dự án, kể cả ID native do generator tạo; không đổi sang bộ số mới chỉ để phù hợp mẫu. `OUT-`, `ASM-`, `F-`, `REQ-`, `BR-`, `ENT-`, `SCR-`, `ADR-`, `SL-` là quy ước traceability bằng tài liệu, không là đối tượng được checker tự xác minh.

Nguồn acceptance có thể dẫn outcome/scope và tài liệu tham chiếu. Giữ các phần mô tả đó nhất quán với nguồn chuẩn đã đăng ký; không dùng chúng làm bản định nghĩa scope cạnh tranh. Khi thay criterion semantics trong feature spec, đối chiếu nghĩa/tính bắt buộc/coverage và evidence có liên quan; không chỉ sửa câu chi tiết để một kết quả cũ trông đạt.

## 3. Chọn tài liệu theo việc đang làm

Bảng này là menu chọn mẫu, không phải danh sách phải tạo. Đăng ký các mục thực sự dùng ở sổ phía trên; việc còn cần nhưng chưa có được ghi như khoảng trống.

| Việc cần giải quyết | Mẫu để dùng hoặc đối chiếu | Đầu ra cần tìm |
| --- | --- | --- |
| Khởi đầu app nhỏ hoặc một slice với tài liệu gộp | [Product pack](product-pack.md) | Các section cần thiết, owner và anchor rõ; không cần tách file nếu chưa có ích |
| Làm rõ vấn đề, giá trị và cách sản phẩm có thể vận hành về kinh doanh | [Business design](business-design.md) | Dữ kiện, giả định và lựa chọn kinh doanh có căn cứ |
| Hình dung một ứng dụng mới và cấu trúc tổng thể | [Product blueprint](product-blueprint.md) | Actor/outcome, feature, phạm vi và trải nghiệm ở mức toàn sản phẩm |
| Chốt điều sản phẩm cần làm và lý do ưu tiên | [PRD](prd.md) | `REQ-…`, nguồn nhu cầu, ràng buộc và phạm vi |
| Nối trải nghiệm với con người/quy trình/dịch vụ phía sau | [Service blueprint](service-blueprint.md) | Frontstage/backstage, handoff, owner và phục hồi |
| Giữ cùng một nghĩa dữ liệu và luật nghiệp vụ | [Domain model](domain-model.md) | `ENT-…`, `BR-…`, identity, semantics và invariants |
| Thiết kế/triển khai một capability hoặc flow cụ thể | [Feature spec](feature-spec.md) | Flow, state, hành động, expected behavior và criterion refs |
| Quyết định cách triển khai và interface | [Technical spec](technical-spec.md) | Architecture, ownership, interfaces, persistence và quyết định liên quan |
| Chọn cách kiểm chứng mà không bịa kết quả | [Validation plan](validation-plan.md) | Method, coverage, fixtures, environment và nơi lưu evidence |
| Cắt và sắp thứ tự công việc | [Delivery plan](delivery-plan.md) | `SL-…`, dependencies, owner và definition of done |
| Chuẩn bị phân phối và chăm sóc phiên bản đã phát hành | [Release/operations](release-operations.md) | Artifact, evidence, nội dung, recovery, quyền thực hiện và support |
| Giữ nguồn chuẩn dễ tìm và không mâu thuẫn | Chỉ mục này | Chủ đề → file/section/revision/owner đang áp dụng |

Các hợp đồng chuyên sâu đang có vẫn dùng được: [brief](../brief.md), [experience](../experience.md), [baseline](../baseline.md), [screen](../screen.md), [component](../component.md), [data view](../data-view.md), [layout](../layout.md), [asset brief](../asset-brief.md), [decision](../decision.md). Chỉ thêm chúng khi cần giữ thông tin mà tài liệu hiện tại chưa phục vụ; không tạo bản sao requirements/rules/results để điền đủ bộ.

## 4. Chuỗi tham chiếu và kiểm tra xung đột

| Câu hỏi | Tham chiếu cần theo được |
| --- | --- |
| Vì sao làm feature này? | `F-…` → `REQ-…` / `OUT-…` và `ASM-…` có liên quan |
| Hành động này sửa dữ liệu theo luật nào? | Flow/feature → `ENT-…` / `BR-…` ở domain model |
| Màn và implementation phục vụ việc gì? | `SCR-…` / source → feature/flow/requirements và quyết định liên quan |
| Slice được giao đủ để kết luận điều gì? | `SL-…` → phạm vi và criterion IDs hiện có |
| Kết quả hiện tại dựa vào đâu? | Criterion ở project contract → record trong verification report → inputs/evidence thật |
| Release lấy bản nào và còn thiếu gì? | Release record → artifact/revision → scope/criteria/evidence tương ứng |

Nếu hai tài liệu khác nhau về cùng một chủ đề, xác định canonical và revision trước. Chủ đề vượt scope/revision của nguồn chuẩn phải được làm rõ, không tự chọn câu dễ triển khai hoặc kết quả tốt hơn. Ghi decision/thay đổi theo quyền hiện có, cập nhật nơi giữ ý nghĩa và sửa các summary bị lệch. Nếu chưa giải quyết được, ghi câu hỏi/owner/tác động vào công việc; không để hai nguồn cùng mang nghĩa “đang áp dụng”.

## 5. Lifecycle và thay đổi

Giữ lifecycle dự án nếu đã có; bảng nhãn sau chỉ là lựa chọn khi index cần lifecycle riêng, không yêu cầu thêm trường vào context.

| Trạng thái tài liệu | Ý nghĩa và cách dùng |
| --- | --- |
| `draft` | Đang định hình/chỉnh sửa; chỉ rõ giả định và phần chưa được chọn dùng |
| `reviewed` | Có review thực đã ghi scope/quan sát/giới hạn; chưa mặc nhiên thành quyết định áp dụng |
| `accepted` | Được chọn dùng trong quyền của công việc hiện có, với scope/revision cụ thể |
| `superseded` | Đã có nguồn/revision thay thế; giữ liên kết để hiểu lịch sử |

Không yêu cầu đủ mọi trạng thái cho một sửa đổi đơn giản và không tạo human approval gate mới. Ghi đúng điều đã xảy ra. Có thể giữ revision đang áp dụng và revision đề xuất riêng; chỉ mục phải cho biết rõ cái nào dùng để build/verify hiện tại.

| Thay đổi | Nơi cập nhật trước | Phần cần rà lại |
| --- | --- | --- |
| Outcome/scope/feature | Nguồn chuẩn tương ứng | PRD, slices, project contract, release scope và evidence bị ảnh hưởng |
| Requirement hoặc business rule | PRD hoặc domain model | Feature semantics, technical implementation, fixtures và acceptance coverage |
| Behavior/UI/architecture | Feature/UI/technical contract liên quan | Code, tests, input dependencies và bằng chứng render/hành vi |
| Criteria contract | Nguồn acceptance đã chọn | Mapping kết quả, artifact/revision và evidence bị ảnh hưởng cần kiểm lại |
| Artifact hoặc evidence inputs đổi | Source/config/fixture thực tế | Kết luận cũ còn áp dụng không; recheck có phạm vi và ghi report thật |
| Tài liệu chuyển chỗ/thay thế | Canonical link và chỉ mục | Anchor, inbound refs, summary; revision cũ trỏ tới nguồn thay thế |

Không đổi tính bắt buộc/applicability hoặc expectation để che lỗi hay scope thay đổi. C2O giữ `pass / partial / fail / not-tested` tại nguồn kết quả hiện có, độc lập với lifecycle tài liệu. Chỉ profile JSON được chọn rõ cần hash/binding; không cập nhật hash để giữ kết luận cũ hoặc đổi `partial` thành `PASS`. Xem [evidence](../../core/evidence.md).

## 6. Khoảng trống và điều kiện hoàn thành chỉ mục

| Chủ đề/link còn thiếu hoặc xung đột | Tác động tới nhiệm vụ | Owner | Bước xử lý / điều kiện đóng |
| --- | --- | --- | --- |
| | | | |

Chỉ mục đủ dùng khi người nhận tìm được nguồn chuẩn, owner, revision và phần áp dụng cho nhiệm vụ; các section được tham chiếu truy cập được; bản tóm tắt không cạnh tranh với nguồn chuẩn; criteria/results trỏ đúng hai JSON; khoảng trống có tác động được ghi rõ. Không cần lấp đầy catalog bằng tài liệu ngoài scope.

Chỉ khi profile JSON được chọn rõ, evidence checker `design_check.py` kiểm tra project/report JSON và file/hash đã khai báo; nó không đọc hay xác minh các nguồn C2O/native tùy ý; nó không chứng minh mọi link ở đây đúng, các ID mô tả nối đủ, hoặc nội dung tài liệu nhất quán. Đối chiếu những phần liên quan bằng review thực theo [workflow](../../core/workflow.md). Hoàn thành chỉ mục chỉ chứng minh việc tổ chức nguồn thông tin đã được xử lý trong phạm vi review, không chứng minh app đã triển khai hay kiểm thử.

## Kiểm tra trước bàn giao

- [ ] Mỗi chủ đề cần cho task đã trỏ tới nguồn được đăng ký rõ, với owner/revision áp dụng; không tự chuyển ownership vì tạo một file mới.
- [ ] Link và section anchor liên quan dùng được, hoặc khoảng trống có owner và tác động cụ thể; mục tham khảo không bị trình bày như canonical.
- [ ] Vai trò, trạng thái và mức required/optional của tài liệu được phân biệt với quyền quyết định và cờ bắt buộc của criterion.
- [ ] Criterion ID/nghĩa/tính bắt buộc trỏ về nguồn acceptance đã chọn; status/inputs/evidence trỏ về nguồn kết quả/evidence đã chọn, không có bảng kết quả cạnh tranh.
- [ ] Các xung đột ảnh hưởng bước tiếp theo được xử lý hoặc ghi rõ; các template ngoài scope không trở thành việc bắt buộc phải điền.
