# Hoạt động thiết kế trong vòng làm việc C2O

Các heading Inspect, Frame, Design, Build, Verify, Learn bên dưới giữ tên hoạt động của gói thiết kế cũ để tra cứu. Chúng không tạo workflow, state, skill hoặc gate bắt buộc mới. Dùng [C2O framework](../../../references/framework.md) và [outcome contract](../../../references/outcome-contract.md) hiện có, bỏ qua phần đã đủ và chỉ mở phần giải quyết việc đang làm.

| Hoạt động tham khảo | Dùng trong skill hiện có khi phù hợp |
| --- | --- |
| Inspect / Frame | `c2o-work`, `c2o-shape`, `c2o-grill`, `c2o-decide`, `c2o-spec` |
| Design | `c2o-create`, `c2o-spec` |
| Build | `c2o-slice`, `c2o-execute`, `c2o-deliver` trong phạm vi được giao |
| Verify / Learn | `c2o-verify`, `c2o-learn` |

Tác vụ nhỏ có thể giữ outcome và vài kiểm tra trong hội thoại. Không cần thư mục `.design`, project/report JSON, bộ metadata hoặc bộ tài liệu mới. Nguồn acceptance/evidence đã chọn trong dự án tiếp tục giữ thẩm quyền.

## Đầu vào và đầu ra

Đầu vào có thể là ý tưởng, brief đã rõ, spec, ảnh chụp UI, code đang có, lỗi UX hoặc yêu cầu review. Đầu ra là phần việc người dùng đã yêu cầu cùng bằng chứng tương ứng. Một nhiệm vụ chỉ yêu cầu thiết kế kết thúc ở đặc tả/prototype đã được review; không tự mở rộng thành implementation hoặc phát hành.

## Inspect

Đọc lượng context cần để hiểu phạm vi: brief/spec, người dùng, model dữ liệu, flow hiện tại, component/token, platform/deployment target, yêu cầu nội dung, quyền hạn và bằng chứng có sẵn. Quan sát UI thật khi nhiệm vụ liên quan UI đang hoạt động.

Kết quả: ghi điều đã biết, giả định tạm dùng và câu hỏi/thử nghiệm có thể làm thay đổi quyết định. Tái sử dụng tài liệu hiện hữu. Không yêu cầu người dùng cung cấp lại thông tin có thể đọc từ dự án.

Khi phạm vi là app mới hoặc tài liệu sản phẩm, dùng [hệ thống tài liệu](../documentation/README.md) để nhận diện business/blueprint/PRD/domain/specs đã có và phần thiếu. Index ghi nguồn chuẩn theo chủ đề; một product-pack gộp cũng đủ cho app nhỏ. Không yêu cầu tất cả mẫu trước khi tiếp tục phần việc đã rõ.

## Frame

Viết một câu outcome theo dạng: actor thực hiện task trong context và có kết quả quan sát được. Giữ rõ toàn bộ deliverable đã nhận, phần trong slice hiện tại, phần cam kết làm sau, non-goals, tiêu chí hoàn thành và nền tảng.

Tiêu chí tốt có hành động, điều kiện và kết quả. Ví dụ: “Khi mất mạng, người dùng sửa vị trí của cây, lưu rồi mở lại chi tiết; giá trị vừa lưu vẫn có và các trường khác không đổi.” Tránh “UI mượt”, “premium” hoặc “đạt chuẩn” mà không có cách đánh giá.

Nếu brief đã giải quyết các vấn đề này, chỉ tham chiếu nó. Với nhiệm vụ nhỏ, một đoạn ngắn và vài tiêu chí bị ảnh hưởng là đủ. Khi có bất định quan trọng, so sánh tối đa vài phương án thực sự khác nhau hoặc làm một thử nghiệm nhỏ.

## Design

Khi chưa có hướng đủ rõ, chọn hoạt động [Explore → Compare → Decide](exploration.md) trong `c2o-decide`/`c2o-create` khi phù hợp. Kết quả được ghi thành [baseline](baseline.md). [UI composition](ui-composition.md) nối tác vụ/dữ liệu với màn hình; [data view](data-views.md) chọn cách biểu diễn; [component](components.md) quy định trách nhiệm thành phần; [layout](layout.md) cụ thể hóa vùng nội dung và thích ứng; [asset workflow](assets.md) xử lý hình ảnh cần thiết. Các module này bổ sung công việc đang làm, không tạo vòng phê duyệt hoặc chuỗi bước bắt buộc mới cho mọi nhiệm vụ.

### Thiết kế experience

1. Model các đối tượng và hành động của domain ở mức phục vụ flow.
2. Viết đường đi chính và các nhánh lỗi/phục hồi.
3. Giao một trách nhiệm rõ cho từng màn hình; nêu nơi dữ liệu được đọc và được ghi.
4. Lập bảng state với trigger, nội dung, hành động hợp lệ, phản hồi và cách thoát/phục hồi.
5. Chọn navigation và interaction theo conventions nền tảng, rồi kiểm tra các chuyển tiếp có làm mất ngữ cảnh hay dữ liệu không.
6. Chọn data view theo câu hỏi cần trả lời và cấu trúc dữ liệu; ghi identity, scope, đơn vị, nguồn và phần chưa biết. Quy định chủ sở hữu query, selection, draft, dữ liệu đã commit và trạng thái tác vụ.

### Thiết kế visual

1. Nêu hierarchy và density phục vụ nhiệm vụ nào.
2. Chọn hướng hình ảnh đủ cụ thể: tone, palette role, type, imagery, spacing, shape và motion.
3. Chọn layout pattern theo tác vụ; nối từng vùng với data view và component. Tái sử dụng component/token hiện có theo hợp đồng; dùng variant hoặc composition khi trách nhiệm phù hợp, chỉ tạo mới khi phần còn thiếu có lý do rõ.
4. Dùng nội dung thực tế và các trường hợp dài/rỗng để kiểm tra bố cục.
5. Ghi điều chỉnh theo platform, form factor, theme và text size, cùng context và hành vi cần giữ khi cấu trúc đổi.
6. Ghi reference, quyết định layout và asset slots cần thiết. Chỉ tạo asset sau khi vai trò của nó đủ rõ; text, control, state và dữ liệu vẫn thuộc implementation. Dùng ảnh tham chiếu cùng token/hành vi đã chọn để giữ nhất quán giữa các màn.

Không cần ba mockup cho mọi việc. Khi hướng hình ảnh còn bất định đáng kể, so sánh vài phương án bằng cùng dữ liệu và cùng nhiệm vụ; nêu điều mỗi phương án đánh đổi.

### Điều kiện chuyển sang Build

Chỉ áp dụng khi implementation thuộc nhiệm vụ đã giao: flow và state của slice đã rõ; quyết định đang cản thực hiện đã có lựa chọn hoặc thử nghiệm trong quyền hiện có; tiêu chí quan sát được và guidance nền tảng phù hợp đã xác định. Đây là kiểm tra readiness trong gate C2O hiện tại, không phải gate Design/Build mới. Không cần đợi mọi màn hình tương lai được thiết kế.

## Build

Trong production được giao, triển khai slice xuyên suốt đủ để sử dụng hoặc trả lời câu hỏi thử nghiệm đã chọn. Phân biệt experiment slice với delivery slice. Hoàn thành một slice không hoàn thành toàn bộ commitment; giữ mọi deliverable còn lại cho đến khi hoàn tất, được thay đổi rõ bởi quyết định hợp lệ, hoặc báo blocked. Thay đổi cùng lúc model, UI và trạng thái khi chúng thuộc cùng nhiệm vụ; tránh một tập hợp màn hình tĩnh không nối được hành vi.

Reuse component và API nền tảng. Giữ data/state ownership rõ. Đưa data fixture có trạng thái rỗng, đủ dữ liệu và dữ liệu biên vào preview/harness phù hợp. Chỉ thêm loading, offline hoặc permission state khi implementation thực tế có chúng.

Với asset, ghi file nguồn/biến thể, export, destination và fallback; kiểm tra trong màn thật. Một ảnh concept hoặc file đã export không chứng minh native rendering hay animation playback. Giữ những khác biệt có chủ đích so với mockup khi platform, nội dung hoặc accessibility yêu cầu.

Khi evidence bác bỏ spec hoặc premise, xem lại Shape/Decide/Spec và thiết kế liên quan trong vòng C2O hiện có, ghi thay đổi có ảnh hưởng. Không tiếp tục dựng UI trên một giả định đã bị bác bỏ.

## Verify

### Chọn phương pháp theo tiêu chí

| Nhóm | Cách kiểm tra | Giới hạn cần ghi |
| --- | --- | --- |
| Hành vi và dữ liệu | Thao tác đầu-cuối, test state transition, persistence, failure/recovery | Một happy path không bao phủ toàn bộ state |
| Render và layout | Chạy implementation thật; snapshot/screenshot theo các biến thể đã chọn | Ảnh tĩnh không chứng minh thao tác hay accessibility hoàn chỉnh |
| Accessibility | Công cụ của nền tảng và kiểm tra thủ công theo task | Công cụ tự động chỉ phát hiện nhóm lỗi mà nó hỗ trợ |
| Nội dung và locale | Tên dài, số/ngày, chuỗi dịch, text expansion, ngôn ngữ phù hợp | Bản dịch giả lập chỉ kiểm tra layout, chưa đánh giá chất lượng ngôn ngữ |
| Chất lượng experience | Critique có bằng chứng, task walkthrough hoặc thử với người dùng | Đánh giá chuyên môn không được trình bày thành kết quả nghiên cứu người dùng |

### Kết quả review

- `Critical`: người dùng không thể hoàn thành việc bắt buộc, có sai lệch dữ liệu nghiêm trọng hoặc rào cản accessibility chặn flow.
- `Major`: nhiệm vụ vẫn có thể làm nhưng dễ thất bại, khó phục hồi hoặc có hiểu nhầm đáng kể.
- `Minor`: vấn đề không chặn nhiệm vụ và có tác động hạn chế trong scope.
- `Suggestion`: phương án cải thiện chưa được chứng minh là cần thiết.

Nếu dùng nhãn critique cũ `ready`, `rework`, `blocked`, coi chúng là khuyến nghị có phạm vi của lần review, không phải trạng thái task hoặc verdict C2O. Kết quả tiêu chí và aggregate vẫn theo outcome contract: `pass / partial / fail / not-tested`, cùng `insufficient-evidence` khi phù hợp ở mức tổng hợp. Không bù Critical bằng điểm visual cao. Review-only báo lỗi mà không sửa; production chỉ sửa trong scope/quyền đã có. Không sửa mọi Suggestion nếu nhiệm vụ đã được đáp ứng.

### Hoàn thành phạm vi

Giữ riêng tiến độ nhiệm vụ, kết quả kiểm chứng artifact và trạng thái giao/phát hành. Một review có thể hoàn thành dù artifact bị đánh giá `fail`; một implementation có yêu cầu bắt buộc chưa kiểm chứng vẫn partial hoặc blocked, không phải verified completion. Chỉ kết luận implementation đã đạt khi toàn bộ deliverable đã nhận và mọi tiêu chí bắt buộc áp dụng có evidence hiện hành, bao gồm outcome-fit cần thiết. Khi tool/platform chưa chạy được, bàn giao phần đã có, ghi `not-tested` cùng lý do và phần commitment còn lại. Prepared không có nghĩa đã gửi hoặc phát hành.

Khi traceability có ích, đối chiếu các liên hệ liên quan theo [hướng dẫn](../documentation/traceability.md): requirement → domain/feature → UX/UI/technical → criterion → evidence. Dùng nguồn acceptance và kết quả đã chọn, như `.context/acceptance.md` hoặc hệ thống native của dự án; không tạo nguồn cạnh tranh. Project/report JSON chỉ dùng khi profile [evidence](evidence.md) được chọn rõ. Plan, spec hoặc source chưa chạy không trở thành evidence runtime.

## Learn

Lưu điều có khả năng ảnh hưởng lần sau: quyết định domain, token/component dùng lại, lỗi lặp lại, giới hạn công cụ hoặc giả định đã bị bác bỏ. Cập nhật context liên quan khi được phép, tránh nhân bản lịch sử qua nhiều file. Thay đổi shared resources là đề xuất có phạm vi cho owner; không tự sửa skill/pack chung từ một kết quả cục bộ.

Một đề xuất thêm rule nên trả lời: lỗi nào lặp lại; rule áp dụng ở đâu; kiểm tra bằng gì; trường hợp nào không áp dụng; chi phí thêm vào workflow là gì. Chưa biến kết quả từ một màn hình thành luật cho mọi dự án.

## Phân chia việc cho agent

Một agent chính giữ outcome, scope, quyết định và tổng hợp evidence. Chỉ tách công việc độc lập, ví dụ rà soát native accessibility song song với review nội dung. Giao rõ input, ownership file, đầu ra, tiêu chí và điều chưa được quyền kết luận.

Critic cần brief/criteria và artifact. Khi có thể, tránh truyền toàn bộ lý do của người tạo để giảm xu hướng bảo vệ quyết định cũ. Critic vẫn phải hiểu ràng buộc sản phẩm; context riêng không đồng nghĩa với bỏ brief.

## Ba mẫu áp dụng ngắn

Các nhãn `quick / standard / deep` sau chỉ giải thích ví dụ lịch sử, không cần chọn hoặc lưu mode mới.

| Nhiệm vụ | Nhãn lịch sử | Hoạt động phù hợp trong C2O |
| --- | --- | --- |
| Sửa nhãn và lỗi wrap của một nút | quick | Đọc component, chỉnh copy/layout, render với chuỗi dài và text size liên quan |
| Tạo flow thêm và sửa một item | standard | Brief ngắn, state contract, visual mapping, implementation, persistence/error/appearance checks |
| Thiết kế lại cách tìm và phân loại dữ liệu | deep | Kiểm tra domain và hành vi hiện tại, giả thuyết IA, prototype/task test, chốt flow rồi triển khai |
