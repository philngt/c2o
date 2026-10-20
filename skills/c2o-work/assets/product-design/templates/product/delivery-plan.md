# Kế hoạch giao hàng theo phần việc xuyên suốt — [sản phẩm / phạm vi]

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-DELIVERY-PLAN` |
| Phiên bản template | `1.1.0` |
| Mục đích | Chia scope thành các slice có kết quả đầu-cuối, dependency, owner và definition of done để giao phần việc có thể sử dụng và kiểm chứng. |
| Dùng khi | Cần sắp thứ tự, phối hợp công việc hoặc làm rõ bước tiếp theo; một thay đổi nhỏ có thể chỉ cần một slice trong plan hiện hữu. |
| Đầu vào | Scope/requirements đã chọn, domain và feature contracts liên quan, artifact hiện có, capacity/dependency và criterion IDs của dự án. |
| Đầu ra / bàn giao | Danh sách slice và quan hệ phụ thuộc, milestone/estimate có căn cứ nếu cần, definition of done/evidence refs và bước xử lý rủi ro còn mở. |
| Nguồn chuẩn | Chỉ giữ slice, dependency, milestone và estimate nếu được đăng ký cho vai trò đó; scope/requirements, domain rules, criteria và kết quả vẫn ở các nguồn hiện hữu được dẫn chiếu. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Sản phẩm/phiên bản/task, các slice và deliverable trong phạm vi kế hoạch] |

[Chuẩn template](../../documentation/template-standard.md): placeholder là chỗ cần xác định, không phải evidence. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu ghi lần thay đổi của bản dùng trong dự án, không phải cùng một số phiên bản.

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

## Mục đích, khi dùng và cách dùng

Với thay đổi nhỏ, một slice và vài dependency có thể đủ; không lập cả roadmap chỉ vì có mẫu. Dùng hoạt động phù hợp trong [vòng C2O hiện có](../../core/workflow.md), không thêm workflow hay vòng phê duyệt riêng.

Đọc [hướng dẫn tài liệu](../../documentation/README.md); tái sử dụng backlog/plan hiện có nếu nó giữ được outcome, dependency và evidence. Giữ nguồn chuẩn trong context/backlog hiện có; chỉ dùng [document index](document-index.md) khi hữu ích. Mẫu này lập kế hoạch, không xác nhận code, test hoặc giao hàng đã hoàn tất.

- Commit/baseline tham chiếu:
- Thời hạn thực sự đã được giao, nếu có:

`accepted` nghĩa là kế hoạch được chọn dùng trong quyền hiện có; không tạo authorization cho publish/deploy và không có nghĩa các slice đã pass.

## 1. Điểm xuất phát và giới hạn

| Nội dung | Tham chiếu nguồn chuẩn / điều cần biết |
| --- | --- |
| Outcome `OUT-…`, actor và context | |
| Scope được nhận, phần hoãn lại | |
| Feature `F-…`, requirement `REQ-…` liên quan | |
| Luật/data contract `BR-…`, `ENT-…` có ảnh hưởng | |
| Flow theo tên + anchor; màn `SCR-…` nếu có | |
| Quyết định `ADR-…` hoặc ID quyết định đang dùng | |
| Giả định `ASM-…` chưa xác minh | |
| Artifact hiện có và khoảng trống thật | |
| Capacity/khả năng truy cập tool, thiết bị, dữ liệu, môi trường | |

Phạm vi phiên bản và yêu cầu nằm ở [PRD](prd.md) hoặc scope section của pack đã đăng ký; brief giữ phạm vi task cụ thể, còn [blueprint](product-blueprint.md) lập bản đồ sản phẩm. Luật domain ở [domain model](domain-model.md); expected behavior chi tiết ở [feature spec](feature-spec.md). Kế hoạch chỉ tham chiếu các nguồn đó. Một trở ngại về lịch hoặc tool không tự làm yêu cầu bắt buộc thành optional.

## 2. Cắt scope thành slice

Ghi slice là experiment hay delivery theo C2O. Một slice hoàn thành không hoàn thành commitment lớn hơn; giữ mọi deliverable đã nhận và slice cam kết làm sau cho đến khi hoàn tất, được thay đổi rõ trong quyền hiện có, hoặc báo blocked.

Mỗi `SL-…` nên có điểm bắt đầu, thao tác/kết quả quan sát được, dữ liệu/state cần thiết và cách kiểm chứng. Với scope implementation, ưu tiên một đường đi xuyên UI → logic → persistence/service → feedback phù hợp tác vụ, thay vì giao “xong toàn bộ database”, “xong toàn bộ màn” rồi chưa có flow chạy được.

Công việc nền tảng, nghiên cứu hoặc migration có thể là dependency thật. Nêu artifact hoặc câu hỏi nó giải quyết, giới hạn thời gian/công sức nếu có, và slice được mở khóa; không gọi nó là outcome người dùng đã đạt. Với nhiệm vụ chỉ thiết kế, slice hoàn thành ở flow/contract/prototype và review đúng mức, không tự kéo thêm Build hoặc release.

| Slice ID | Kết quả xuyên suốt và flow liên quan | `F-…` / `REQ-…` / criterion IDs hiện có | Dependency bắt buộc | Owner | Ước lượng khoảng và căn cứ |
| --- | --- | --- | --- | --- | --- |
| `SL-…` | | | | | |

Giữ ID ổn định khi đổi thứ tự. Không đánh lại số theo tuần hoặc tạo bộ acceptance ID riêng trong kế hoạch. Nếu slice chỉ đáp ứng một phần criterion lớn, ghi đúng phần đó; chưa đủ coverage thì không kết luận criterion đã đạt. Khi cần tách criterion, cập nhật nguồn chuẩn và verification records có giải thích về scope.

### Hợp đồng cho từng slice

Lặp section này cho các slice cần chi tiết, hoặc link thẳng tới backlog/feature section hiện có:

- **Slice ID và owner:**
- **Điểm bắt đầu / actor / dữ liệu trước thao tác:**
- **Kết quả cuối quan sát được:**
- **Flow và expected behavior nguồn chuẩn:** [tên flow + section anchor, `REQ-…`, `BR-…`, `SCR-…` liên quan].
- **Đường chính và lỗi/phục hồi cần đi cùng:**
- **Thay đổi tối thiểu ở các phần liên quan:** [UI, logic, dữ liệu, dịch vụ, nội dung; chỉ phần có thật].
- **Ngoài slice này:**
- **Dependency cần trước khi bắt đầu; giả định đang dùng:**
- **Cách quan sát hoặc demo đầu-cuối:**
- **Definition of done:** [criterion IDs hiện có, artifact, tập biến thể bắt buộc, phương pháp và nơi ghi evidence].
- **Báo cáo kết quả và evidence:** [link record trong verification report; để trống hoặc ghi chưa tạo khi chưa thực hiện].

Các subtasks kỹ thuật thuộc slice có thể chia theo file/module hoặc người thực hiện, nhưng owner slice giữ việc ghép và kiểm chứng kết quả cuối. Chỉ tách công việc song song khi boundaries, ownership và dependency cho phép.

## 3. Dependency và thứ tự thực hiện

| Dependency / đầu ra cần có | Slice bị ảnh hưởng | Điều kiện hoàn thành dependency | Owner / bên cung cấp | Cách xử lý nếu chưa có |
| --- | --- | --- | --- | --- |
| | | | | |

Phân biệt dependency bắt buộc với việc “làm trước sẽ thuận tiện”. Ghi lý do: thiếu schema khiến không thể lưu đúng, thiếu quyền khiến không kiểm tra được target, hoặc chưa chọn business rule khiến hai cách triển khai cho kết quả khác nhau. Đừng biến sở thích thứ tự thành điều kiện chặn.

Đối với bất định lớn, chọn một thử nghiệm đủ hẹp để quyết định nhánh tiếp theo. Ghi câu hỏi, quan sát cần có và hành động khi giả định sai. Không chờ toàn bộ tài liệu tương lai hoàn thành trước khi bắt đầu một slice đã đủ rõ.

## 4. Mốc và ước lượng

| Mốc | Kết quả/artifact phải có | Slice/dependency | Criterion và evidence dùng để đánh giá | Khoảng thời gian / giả định / owner |
| --- | --- | --- | --- | --- |
| | | | | |

Mốc cần mô tả kết quả, chẳng hạn một flow có thể chạy và khôi phục lỗi đã chọn; tỷ lệ “UI hoàn thành” không thay cho kết quả này. Có thể có mốc design-only hoặc research nếu đó là deliverable được giao. Mốc phát hành chỉ thêm khi release nằm trong scope, cùng [hồ sơ release/operations](release-operations.md).

- Đơn vị ước lượng: [giờ/ngày công hoặc thời gian lịch; ghi rõ].
- Khoảng ước lượng và căn cứ: [việc tương tự, spike, phần đã đọc; không tự tạo số liệu].
- Capacity và giả định về người/tool/runtime:
- Thời gian chờ dependency bên ngoài:
- Hạng mục chưa đủ dữ kiện để ước lượng và cách làm rõ:
- Điều kiện cần cập nhật estimate/milestone:

Dùng khoảng và giả định thay cho ngày chắc chắn khi còn bất định. Phân biệt effort với elapsed time; hai ngày công không mặc nhiên là hai ngày lịch. Nếu chưa có căn cứ thì ghi “chưa ước lượng”; không tự điền tốc độ, capacity, buffer hoặc lịch phát hành. Một deadline thực là constraint cần xử lý qua scope/nguồn lực, không làm bằng chứng cần thiết tự biến mất.

## 5. Rủi ro và phương án điều chỉnh

| Rủi ro / `ASM-…` / quyết định còn mở | Slice/outcome bị ảnh hưởng | Dấu hiệu kích hoạt | Cách giảm bất định hoặc giảm tác động | Owner / điểm cần quyết định |
| --- | --- | --- | --- | --- |
| | | | | |

Chỉ ghi rủi ro có thể thay đổi hành động: ví dụ chưa có migration path, native tool đang thiếu hoặc dịch vụ ngoài chưa trả dữ liệu cần thiết. Nếu đánh giá xác suất/tác động, ghi căn cứ hoặc mức chưa biết; không thêm phần trăm giả. Phương án cắt scope phải chỉ rõ requirement nào thay đổi và đi qua nguồn chuẩn theo quyền hiện có.

Khi một slice bị chặn, ghi điều kiện mở chặn và phần độc lập còn làm được. `not-tested` cùng lý do thiếu môi trường chỉ mô tả tình trạng kiểm chứng criterion, không tự quyết định trạng thái task/project. Giữ `partial` khi có evidence một phần. Không dùng N/A để bỏ kiểm tra đã cam kết.

## 6. Definition of done và handoff

| Phần cần bàn giao | Nơi giữ thông tin chuẩn | Điều cần đối chiếu |
| --- | --- | --- |
| Yêu cầu / expected behavior | PRD, domain model và feature spec đã đăng ký | ID và semantics nhất quán với scope slice |
| Artifact | Source/design/prototype/data migration hoặc deliverable thật | Đúng revision và đúng deliverable được giao |
| Criteria contract | Nguồn acceptance đã chọn | ID, nghĩa, nguồn/rationale, tính bắt buộc, applicability và cách kiểm tra hiện hành |
| Kết quả đã kiểm tra | nguồn kết quả/evidence đã chọn và evidence files | Status/rationale/input/evidence khớp artifact và scope |
| Khoảng trống / việc tiếp theo | Nguồn issue/plan hiện hữu | Có owner, tác động và dependency cụ thể |

Chọn phương pháp từ [validation plan](validation-plan.md), không mặc định tạo tests cho mọi thay đổi. Native build, UI render, thao tác, dữ liệu và accessibility chứng minh các điều khác nhau. Với Apple source, dùng [NATIVE_CHECKS](../../starters/apple/NATIVE_CHECKS.md) để chọn coverage liên quan; danh sách đó chưa phải evidence.

Không tạo bảng kết quả criterion thứ hai cho slice; đọc nguồn verification/evidence đã chọn. Giữ riêng task progress, artifact verdict và external delivery. Review-only có thể hoàn thành khi subject fail; không sửa artifact trong review. Implementation slice chỉ verified khi artifact đúng scope và evidence bắt buộc đủ; thiếu môi trường giữ `not-tested` cùng lý do, evidence một phần giữ `partial`. Một slice đạt không kết thúc commitment lớn hơn và prepared không có nghĩa released.

## 7. Cập nhật kế hoạch và kết thúc

- Thay đổi so với revision trước và lý do:
- `OUT-…`, `ASM-…`, `F-…`, `REQ-…`, `BR-…`, `ENT-…`, `SCR-…`, `ADR-…`, `SL-…` bị ảnh hưởng:
- Nguồn chuẩn nào đã cập nhật, phần nào còn đề xuất:
- Slice/evidence/milestone cần xem lại và owner:
- Bài học cần giữ để lần sau không lặp lại:

Điều kiện hoàn thành **kế hoạch**: có slice tiếp theo làm được hoặc dependency cụ thể cần giải quyết; owner và output rõ; estimate được gắn căn cứ hoặc ghi chưa biết; definition of done trỏ tới acceptance/evidence hiện hành; phần hoãn lại không mâu thuẫn scope. Điều kiện hoàn thành **công việc** vẫn theo [workflow](../../core/workflow.md) và [evidence contract](../../core/evidence.md), không theo số hàng đã điền.

## Kiểm tra trước bàn giao

- [ ] Mỗi slice được chọn có kết quả quan sát được và nguồn scope/requirements rõ; công việc nền tảng không bị mô tả thành outcome người dùng đã đạt.
- [ ] Dependency bắt buộc, owner và điều kiện mở chặn đủ rõ cho bước tiếp theo; phần độc lập còn có thể làm được đã được nhận diện.
- [ ] Estimate/milestone có khoảng, căn cứ và giả định phù hợp, hoặc ghi chưa ước lượng; effort và elapsed time không bị đồng nhất.
- [ ] Definition of done dẫn đúng criterion IDs, coverage, phương pháp và nơi ghi evidence; kế hoạch không tạo một bảng pass/fail riêng.
- [ ] Các thay đổi scope/rule/decision và giới hạn hiện tại đã nối về nguồn chuẩn; việc hoàn thành kế hoạch không bị dùng như kết luận implementation đã verified hoặc được phép phát hành.
