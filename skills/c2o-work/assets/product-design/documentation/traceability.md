# Nguồn chuẩn, ID và cập nhật theo thay đổi

Dùng phần cần thiết cùng [hệ thống tài liệu](README.md) và [chuẩn template](template-standard.md). Nguồn C2O/native đã chọn giữ thẩm quyền; các bảng và ID sau là trợ giúp tùy chọn, không yêu cầu index, `.design`, metadata hoặc migration. Các quy ước sau được đưa vào từ v1.4 và tiếp tục trong v1.5. Đây là quan hệ do người/agent review; evidence checker không tự parse các ID này hoặc chứng minh quan hệ business–code. Template checker chỉ đối chiếu cấu trúc catalog; `TPL-*` là ID của mẫu trong registry, không là ID requirement/entity/screen của dự án.

## 1. Một nguồn chuẩn cho một chủ đề

| Chủ đề | Nơi định nghĩa chuẩn | Các tài liệu khác làm gì? |
| --- | --- | --- |
| Phân khúc, giá trị, giả thuyết kinh doanh, giả thuyết metric | Business design hoặc section tương ứng của pack | Dẫn chiếu ASM/OUT và ghi tác động; không tự biến giả thuyết thành bằng chứng |
| Phạm vi phiên bản, ưu tiên, requirements | PRD hoặc scope section đã đăng ký | Brief của một task lấy subset; blueprint lập bản đồ các requirement |
| Outcome/scope của task cụ thể | Brief/task spec hiện có, liên kết về scope phiên bản | Không tự mở rộng yêu cầu cấp sản phẩm khi chỉ sửa UI |
| Entity, identity, business rule, lifecycle | Domain model | Feature/technical dùng ENT/BR ref; không viết lại retention ở ba nơi |
| Hành vi cụ thể của feature | Feature spec | UX ghi biểu hiện và navigation, technical ghi cơ chế hiện thực hóa |
| Screen flow, UI state, query/selection/draft owner | Experience/screen contract | Blueprint chỉ chỉ ra nơi cần đọc |
| Token, visual rules, component reuse và adaptation | Baseline + contract chuyên biệt | Các màn dẫn baseline revision; deviation có lý do |
| Interface, persistence, concurrency và migration | Technical spec + code/interface schema tương ứng | Domain giữ nghĩa; technical giữ cách lưu/giao tiếp |
| Lý do quyết định quan trọng | Decision/ADR | Các spec ghi lựa chọn đang dùng và link lý do; không copy toàn lịch sử |
| Scope/dependencies/thứ tự/owner của slice | Delivery plan/backlog hoặc section slice đã đăng ký khi chưa tách file | Feature spec ghi view tham chiếu, không giữ scope slice cạnh tranh |
| Acceptance: ID/nghĩa/nguồn/tính bắt buộc/phương pháp | Nguồn acceptance đã chọn trong hội thoại, `.context/acceptance.md` hoặc hệ thống native | Mọi plan/scenario tham chiếu nguồn đó; không tạo tiêu chí cạnh tranh |
| Kết quả thực tế và evidence hiện hành | Nguồn kết quả/evidence đã chọn trong dự án | Release/delivery/index dẫn tới kết quả, không giữ bảng kết quả thứ hai |
| Phạm vi build phát hành, cấu hình phân phối và vận hành | Release/operations | Reuse source requirements/evidence; không suy quyền publish từ readiness |

Nếu PRD/brief/acceptance hoặc hệ thống hiện có đã là nguồn chuẩn thì giữ nó. Những tên file trên mô tả trách nhiệm, không buộc migration. Một anchor hoặc context hội thoại có thể đủ. Chỉ profile JSON được chọn rõ trong [evidence](../core/evidence.md) dùng `id/title/required/allow_not_applicable`, `project_sha256` và verification JSON; khi là snapshot, dẫn nguồn/revision gốc và không tạo hai authority độc lập.

## 2. Các ID được dùng khi cần

| ID | Nghĩa trong framework | Ví dụ nối tiếp |
| --- | --- | --- |
| OUT-01 | Outcome có thể quan sát | Người dùng mở lại đúng bản ghi vừa lưu |
| ASM-01 | Giả thuyết cần evidence | Nhóm người dùng này muốn lưu history |
| F-01 | Feature/capability; **không phải flow** | Quản lý bộ sưu tập |
| REQ-01 | Yêu cầu sản phẩm | Có thể sửa đúng record theo identity |
| ENT-01 | Đối tượng domain | LifestyleRecord |
| BR-01 | Quy tắc nghiệp vụ/invariant | Save lỗi không thay bản đã commit |
| SCR-01 | Màn trong dự án | Collection/detail/editor theo scope |
| ADR-01 | Quyết định architecture | Một app writer cho kho nhỏ cục bộ |
| SL-01 | Lát cắt giao hàng từ đầu đến cuối | Tạo → lưu → đóng/mở lại → xem đúng |

Các ID acceptance tiếp tục dùng ID thật của project: `C-001`, `APP-01`, `LIF-01`, `UTL-01`, `WID-01`, `PL-01`… Không đổi prefix chỉ để giống template. Catalog `CP/DVP/LP/SP` là pattern; instance `CMP/DV/L/SCR` là lựa chọn trong dự án; `O/DEC/B/AST` có các contract cũ tương ứng. ADR có thể dùng template decision với tên và trách nhiệm phù hợp.

Không cần đánh ID mọi đoạn văn. Dùng ID khi có nhiều nơi cần tham chiếu, cần kiểm tra impact hoặc giao việc độc lập. ID chỉ cần duy nhất trong namespace dự án; hai example project được phép cùng dùng F-01 hoặc APP-01. Khi tham chiếu chéo dự án, thêm project/path.

## 3. Bảng truy vết tối thiểu

| Outcome | Feature / requirement | Rule / dữ liệu | UX/UI ref | Technical ref | Criterion | Kết quả |
| --- | --- | --- | --- | --- | --- | --- |
| OUT-01 | F-01 / REQ-01 | ENT-01 / BR-01 | Anchor screen/experience | Anchor interface/store/ADR | ID thật trong acceptance đã chọn | Link nguồn kết quả/evidence, không sao status |

Một criterion có thể bao nhiều yêu cầu nếu một quan sát đầu-cuối đủ rõ. Khi các hành vi thất bại độc lập hoặc cần theo dõi riêng, tách criterion và cập nhật report tương ứng. Không dùng một tiêu chí rộng “app tốt” che tất cả requirement.

Ví dụ dự án có requirement về thành công của tác vụ nhưng chưa có criterion hoặc cách quan sát là coverage gap. Một screen không phục vụ outcome/feature nào có thể là scope thừa; chưa tự xóa chỉ vì thiếu ref, hãy xác minh intent. Một `pass` có evidence từ implementation cũ cần xem dependency, không được giữ nguyên chỉ vì ID chưa đổi.

## 4. Năm trạng thái phải phân biệt

| Loại thông tin | Cách ghi | Không được suy ra |
| --- | --- | --- |
| Fact/source observation | Nguồn, thời điểm/phạm vi và điều thực sự thấy | Nghiên cứu toàn thị trường từ một repo hoặc một người |
| Hypothesis | ASM, mức chưa chắc, cách kiểm tra, tiêu chí quyết định dự kiến | Đã xác thực vì template đã điền |
| Document/decision | Revision + status; decision có lý do/tradeoff | Runtime pass hoặc người dùng đã phê duyệt |
| Implementation | Source/commit/target và phần đã/chưa viết | Build thành công, thao tác đúng hoặc có người dùng |
| Verification | Kết quả, môi trường, input và evidence thật | Release authorization hoặc toàn sản phẩm đã đạt |

Nếu dùng lifecycle tài liệu, `accepted` cần scope và căn cứ chọn dùng trong quyền đã có; `reviewed` cần lần review thật và không giả làm phê duyệt. Giữ quy ước hiện hữu, không bắt thêm lifecycle. C2O giữ `pass / partial / fail / not-tested` ở nguồn acceptance/evidence và tách task progress, artifact verdict, external delivery. Review hoàn thành có thể kết luận subject fail; một delivery slice hoàn thành không hoàn thành commitment lớn hơn.

## 5. Ví dụ impact: thay lịch sử Utility từ 50 thành 100 lần

Đây là ví dụ thay đổi, **không áp dụng cho starter hiện tại**, vẫn giữ cap 50.

1. Tìm BR về retention trong domain; xác định lý do người dùng và tác động storage/privacy. Quyết định thay trong quyền hiện có; nếu còn chưa rõ thì chỉ chặn phần phụ thuộc.
2. Cập nhật BR và revision, PRD nếu scope/quality thay đổi. Feature spec dẫn rule mới; Help/Settings và thông báo liên quan đọc cùng chính sách.
3. Xem technical limit, thứ tự loại bản ghi, dữ liệu cũ và hành vi clear/off. Tăng cap không tự đồng nghĩa migrate được mọi dữ liệu.
4. Cập nhật code, fixtures và scenario boundary; giữ criterion ID nếu nghĩa không đổi, tách/thay nếu contract đã khác.
5. Xác định input có ảnh hưởng để vô hiệu hóa evidence cần thiết. Nếu chọn profile JSON, evidence checker chỉ phát hiện file đổi trong dependency đã khai báo; nó không tự biết BR, Swift constant hoặc Help copy phụ thuộc nhau.
6. Trong production được phép, chạy lại phép kiểm tra bị tác động và cập nhật nguồn kết quả/evidence đúng thực tế; chỉ profile JSON cần binding/hash theo contract riêng. Các phần khác không bị đổi không cần lặp kiểm tra chỉ để đủ danh sách.

Tương tự, thay local-only thành sync sẽ tác động business promise, domain identity/conflict, UX offline/error, architecture, privacy/data lifecycle và verification. Đó là thay đổi lớn hơn đổi một màn hình; blueprint giúp thấy các liên hệ này.

## 6. Quy tắc handoff

Handoff cần nêu outcome/scope, đường dẫn nguồn chuẩn, quyết định/giả thuyết còn mở, lát cắt cần làm, các ràng buộc dữ liệu/UI và criterion phải quan sát. Giao rõ quyền sửa file, quyền thực thi và phần chưa được phép kết luận. Thư mục chứa nhiều tài liệu không tự tạo đủ context; chỉ nạp phần liên quan đến tác vụ.

Chi tiết kết quả và cách chạy checker: [evidence](../core/evidence.md), [validation plan](../templates/product/validation-plan.md) và [tools](../tools/README.md).
