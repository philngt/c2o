# Bằng chứng thiết kế và profile JSON tùy chọn

## Phạm vi của hợp đồng

Trong C2O, [outcome contract](../../../references/outcome-contract.md) và nguồn acceptance/evidence đã chọn trong dự án tiếp tục quyết định tiêu chí, phương pháp, kết quả và completion. Nguồn đó có thể là hội thoại cho tác vụ nhỏ, `.context/acceptance.md` khi hữu ích, hoặc hệ thống native đang dùng. Tài nguyên này bổ sung cách quan sát thiết kế; không yêu cầu `.design`, JSON, hash hay một nguồn chuẩn mới.

Các section Project contract, Verification report và Sử dụng công cụ bên dưới mô tả **profile JSON cũ, tùy chọn** của C2O Design. Chỉ áp dụng khi profile đó đã được chọn rõ cho tác vụ hoặc starter. Sự hiện diện của file mẫu, file được generator tạo hay tài liệu này không tự chuyển acceptance sang JSON. Nếu dùng JSON như snapshot phục vụ checker, dẫn nguồn acceptance/revision gốc và giữ việc cập nhật nhất quán; không duy trì hai nơi độc lập cùng định nghĩa tiêu chí hoặc kết quả. Không có parser, đồng bộ hay migration tự động được thêm vào C2O.

## Trạng thái của từng tiêu chí

Báo cáo C2O dùng trạng thái của outcome contract:

| Trạng thái C2O | Cách dùng |
| --- | --- |
| `pass` | Toàn bộ yêu cầu của tiêu chí có evidence hiện hành, phù hợp phương pháp và scope |
| `partial` | Có bằng chứng cho một phần, nhưng chưa đủ để kết luận toàn tiêu chí đạt |
| `fail` | Đã quan sát thấy yêu cầu không đạt; giữ cả lỗi và phần còn chưa kiểm tra |
| `not-tested` | Chưa có kiểm tra đủ; ghi rõ chưa thực hiện, thiếu tool/môi trường, dữ liệu hoặc reviewer |

Ghi applicability và lý do tại nguồn đã chọn. Một kiểm tra không áp dụng không trở thành `pass`, không loại bỏ requirement đã cam kết, và thiếu môi trường không phải lý do N/A. Kết quả tổng hợp vẫn theo outcome contract: yêu cầu bắt buộc fail dẫn tới fail; evidence một phần/chưa đủ giữ partial hoặc insufficient-evidence theo phạm vi. Không dùng tập tiêu chí rỗng làm pass.

Chỉ profile JSON tùy chọn dùng năm nhãn sau:

| Nhãn trong profile JSON | Nghĩa của record | Khi báo cáo qua C2O |
| --- | --- | --- |
| `PASS` | Phương pháp đã chọn được ghi nhận đạt với input/evidence theo profile | Chỉ hỗ trợ `pass` sau khi đọc evidence và kiểm tra đủ scope/currency; checker không tự quyết định verdict C2O |
| `FAIL` | Đã quan sát không đạt | Giữ `fail` và coverage còn thiếu |
| `BLOCKED` | Trở ngại khiến chưa kiểm tra đủ | `not-tested` cùng lý do; giữ `partial` nếu nguồn C2O đã có evidence một phần |
| `NOT_RUN` | Chưa thực hiện | `not-tested`, không suy thành pass |
| `NOT_APPLICABLE` | Criterion cho phép N/A và có lý do phù hợp | Giữ quyết định applicability, không chuyển thành pass |

Profile JSON không có nhãn `partial`. Không đổi C2O `partial` thành `PASS`, không che bằng chứng một phần bằng một phép đổi nhãn. Giữ kết quả và giới hạn đầy đủ tại nguồn C2O; không chọn profile nếu nó làm mất nghĩa. Chỉ tách criterion khi có nhu cầu theo dõi thực và giữ nguyên toàn bộ yêu cầu/coverage đã nhận.

Với tiêu chí gồm nhiều biến thể, chốt tập bắt buộc trước khi chạy và ghi kết quả từng trường hợp. Một lần chạy iPhone không tự đại diện cho iPad, chữ lớn hoặc VoiceOver. Nếu đã thấy lỗi, giữ lỗi cùng các trường hợp chưa chạy. Chỉ `pass` khi toàn bộ trường hợp bắt buộc có bằng chứng đạt.

## Project contract

**Chỉ khi đã chọn profile JSON:** `project.json` có `schema_version`, `project_name` và `criteria`. Mỗi criterion có ID ổn định, title, `required` và `allow_not_applicable`. File có thể chứa platform, mode lịch sử, outcome, scope, tài liệu tham chiếu và cách kiểm tra. Các trường mô tả không tạo workflow hoặc scope mới.

Profile yêu cầu ít nhất một criterion bắt buộc. Giữ ID/nghĩa/flags nhất quán với acceptance đã chọn; nếu JSON được dùng làm nguồn cho một phần thì ghi rõ trách nhiệm và tham chiếu từ nguồn C2O, không tạo bản định nghĩa song song. Thay scope/tiêu chí phải có căn cứ và quyền hiện có; không đổi một yêu cầu khó thành optional để có kết quả xanh.

## Verification report

**Chỉ khi đã chọn profile JSON:** `verification.json` có `schema_version`, `project_sha256` và `results`. Mỗi result trỏ tới đúng một `criterion_id`; scaffold khởi đầu `NOT_RUN`. `inputs` và `evidence` chứa đường dẫn tương đối từ project root và SHA-256 của byte thật.

`project_sha256` gắn report với nguyên bản project JSON. Null phù hợp với scaffold; không phải evidence hoàn thành. Khi input/contract đổi, xem lại phần bị ảnh hưởng và thu evidence cần thiết; không chỉ đổi hash để che thay đổi scope. Hash xác định file, không chứng minh nội dung đúng, dependency đầy đủ, reviewer xác thực hoặc hành động được cho phép.

## Input và evidence khác nhau thế nào

- Input: mã thực thi, token, stylesheet, config, fixture dữ liệu, locale, test/harness và môi trường liên quan đến phép kiểm tra.
- Evidence: log test/build, ảnh render, video thao tác, ghi chép accessibility, task walkthrough hoặc critique có vị trí và quan sát cụ thể.

Giữ artifact/revision hoặc observed state, phương pháp, môi trường, quan sát, evidence location và reviewer khi cần tại nguồn hiện có. Chỉ thêm trường có ích; không bắt mọi tác vụ tạo file/hash. Khi dùng profile JSON, danh sách input cần bao phủ dependency ảnh hưởng đến kết luận: hash HTML mà bỏ CSS có thể bỏ sót thay đổi UI. Với native, ghi build/OS/device, appearance, text size, locale và dataset.

Screenshot cần màn/state, kích thước hoặc thiết bị, appearance và dữ liệu. Báo cáo thủ công cần thời điểm, người/vai trò hoặc phương pháp, thao tác, kết quả và giới hạn. Với layout/asset, giữ baseline/revision và source/derived files có ảnh hưởng; với component/data view, giữ model/fixture/query logic và implementation liên quan. Tài liệu thiết kế xác định expectation; cần quan sát riêng để biết UI thực làm đúng. Phân biệt measured, estimated và unmeasured; provenance không chứa key/token.

Khi so screenshot, ghi vùng được đo, phần ngoài ảnh, masks/alignment/crop, dữ liệu/state và phép kiểm tra bị skip. Điểm cao trên vùng overlap không chứng minh cả màn đã được kiểm tra. Tách export, runtime, visual và behavior khi cần theo dõi riêng. Khác biệt adaptation có chủ đích được đánh giá theo baseline và hợp đồng dự án.

ID option/decision/baseline/layout/asset/component/data-view/screen và metadata assets do người/agent đối chiếu. ID catalog khác instance dự án. Checker JSON chỉ kiểm record và file hash đã khai báo; không tự đọc nghĩa, xác minh liên kết ID, chạy UI/asset pipeline hoặc phát hiện dependency bị bỏ quên.

## Sử dụng công cụ

**Chỉ cho profile JSON được chọn rõ.** Xem [lệnh của checker](../tools/README.md). `snapshot` tính hash file có thật; không tạo evidence render hoặc tự gán `PASS`. `validate` kiểm schema tối thiểu, mapping criteria, status, sự hiện diện file và mọi hash đã khai báo. Không cần chạy checker để sử dụng guidance hay template Markdown.

Kết quả riêng biệt của checker giữ nguyên nghĩa:

1. `record_validity`: record có hợp lệ và tham chiếu còn khớp hay không.
2. `required_coverage`: các criterion bắt buộc được ghi đạt, fail, blocked hoặc chưa chạy ở đâu.

| Exit code | Nghĩa trong profile JSON |
| --- | --- |
| 0 | `RECORDS_READY`: hồ sơ hợp lệ, còn khớp và mọi tiêu chí bắt buộc áp dụng được ghi đạt |
| 1 | Hồ sơ đầy đủ/hợp lệ nhưng có tiêu chí bắt buộc `FAIL` |
| 2 | Hồ sơ không hợp lệ, cũ, thiếu hoặc còn yêu cầu chưa thể/chưa được kiểm tra |

Không có criterion, tất cả optional hoặc tất cả bắt buộc N/A không tạo records-ready. File khai báo đổi hash làm record không đủ xác nhận phiên bản hiện tại. Kết quả checker không thay quyết định kiểm chứng C2O; không được diễn giải lại exit code thành app pass.

## Phần cần kiểm tra bằng phương pháp thật

Ghi lệnh và output thực khi dùng công cụ ngoài. Kiểm tra phép đo đã chạy, test count có nghĩa và scope đúng. Process exit 0 có thể chỉ là không tìm thấy test hoặc skip môi trường; không chuyển thành `pass`.

Review chỉ ghi điều đã quan sát. Source review không chứng minh render; screenshot không chứng minh hành vi; build không chứng minh user journey; agent walkthrough không phải usability research. Thiếu native SDK/runtime giữ kết luận native chưa kiểm chứng. Sau thay đổi, vô hiệu hóa evidence bị ảnh hưởng và giữ phần còn hợp lệ với provenance; không chạy lại mọi kiểm tra không liên quan.

## Không gộp hoàn thành hồ sơ với phát hành

`RECORDS_READY` không là chứng nhận WCAG, native/App Store readiness, toàn hệ thống đúng, C2O DONE hoặc quyền phát hành. Giữ riêng task progress, artifact verification và external delivery. Review-only có thể hoàn thành khi subject fail; không tự sửa artifact. Implementation còn required gap vẫn partial hoặc blocked. Một slice đạt không hoàn thành commitment lớn hơn; prepared không phải sent/released. Quyền deploy/publish theo yêu cầu người dùng và hợp đồng dự án.
