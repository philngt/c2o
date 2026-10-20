# Product pack — [Tên ứng dụng / phạm vi]

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-PRODUCT-PACK` |
| Phiên bản template | `1.1.0` |
| Mục đích | Gộp context sản phẩm, scope, domain, behavior, thiết kế, kỹ thuật và cách kiểm chứng cần cho một app nhỏ hoặc slice đầu-cuối. |
| Dùng khi | Cần một hồ sơ làm việc gọn, các section chưa cần owner/lifecycle riêng và tài liệu hiện có chưa bao phủ đủ việc được giao. |
| Đầu vào | Ý tưởng hoặc brief, bằng chứng nhu cầu, scope/quyền hiện có, source và hợp đồng đang dùng, nguồn acceptance/evidence đã chọn nếu đã có. |
| Đầu ra / bàn giao | Các section cần thiết cho bước tiếp theo, mapping nguồn chuẩn, slice/coverage và câu hỏi còn mở; không yêu cầu điền toàn bộ pack trước khi làm việc. |
| Nguồn chuẩn | Mỗi section chỉ giữ chủ đề được chọn rõ trong context hiện hữu hoặc index khi cần; giữ nguồn hiện hữu nếu đã có. Nguồn acceptance đã chọn giữ criterion ID/nghĩa/tính bắt buộc; nguồn kết quả/evidence đã chọn giữ kết quả và evidence. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Sản phẩm/phiên bản/task, platform và các section dùng trong pack] |

[Chuẩn template](../../documentation/template-standard.md): placeholder là chỗ cần xác định, không phải evidence. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu ghi lần thay đổi của bản dùng trong dự án, không phải cùng một số phiên bản.

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Dùng section còn thiếu trong dự án; không chép đè tài liệu canonical hoặc report thật. Không cần metadata cho bản dùng trong dự án; nếu dùng, một block hữu ích cho pack là đủ, không lặp trên từng section. Khi một section cần owner/lifecycle riêng, chuyển nó sang template chuyên biệt trong [hệ thống tài liệu](../../documentation/README.md), giữ anchor/ref trỏ tới nguồn mới.

- Baseline liên quan nếu có:
- Quyền quyết định đang có:
- Nguồn acceptance đã chọn / nguồn kết quả/evidence đã chọn thực của dự án:
- Source commit/build nếu có; phần mới là ý tưởng, source hoặc đã chạy:

`accepted` không đồng nghĩa implementation pass, nghiên cứu đã xác thực hoặc được phép publish. Thay tất cả placeholder có ảnh hưởng trước khi giao phần việc phụ thuộc. Mục chưa cần có thể ghi ngoài scope với lý do; không đổi một yêu cầu đã cam kết thành N/A để né kiểm tra.

## 1. Index và business

Chỉ xác định các chủ đề cần cho việc tiếp theo ở section dưới hoặc context/tài liệu hiện có; khi dùng external source, dẫn path/anchor/version. Cùng một rule chỉ có một nguồn chuẩn.

| Chủ đề | Canonical path/anchor | Owner / revision |
| --- | --- | --- |
| Business/outcome | | |
| Scope/requirements | | |
| Domain/behavior | | |
| UX/UI | | |
| Technical | | |
| Acceptance fields/results | Nguồn acceptance đã chọn / nguồn kết quả/evidence đã chọn | |

- User / customer / payer (có thể cùng người):
- Tác vụ và cách họ đang giải quyết; nguồn quan sát:
- Giá trị dự kiến, chi phí chuyển đổi, giới hạn lời hứa:
- Cách tiếp cận/phân phối, vận hành, hỗ trợ:
- Mô hình thu phí/tài trợ và chi phí nếu liên quan; số chưa biết ghi giả thuyết:

| ASM | Giả thuyết | Evidence đang có | Thử nghiệm/quan sát tiếp theo | Điều kiện quyết định |
| --- | --- | --- | --- | --- |
| ASM-01 | | | | |

## 2. Outcome và product blueprint

`OUT-01`: [actor] thực hiện [task] trong [context], đạt [kết quả quan sát được].

| Actor | Feature/capability | Flow tên | Domain refs | Màn/điểm tiếp xúc | Platform | Ngoài ranh giới |
| --- | --- | --- | --- | --- | --- | --- |
| | F-01 | | ENT-01 | SCR-01 | | |

Ghi hệ thống/người/dịch vụ bên ngoài và việc app không chịu trách nhiệm. Khi có service/handoff thật, dùng [service blueprint](service-blueprint.md); không tạo hậu trường giả cho một app local.

## 3. PRD của phạm vi này

- Included / deferred / excluded và lý do:
- Deployment targets, locale và biến thể hỗ trợ:
- Chỉ số thành công: định nghĩa, baseline đã biết/chưa biết, target đề xuất, thời gian/cách đo, dữ liệu tối thiểu cần thu:

| Feature | Requirement | Mức ưu tiên và lý do | Acceptance ID thật | Quyết định/assumption còn mở |
| --- | --- | --- | --- | --- |
| F-01 | REQ-01: | | | |

Yêu cầu chất lượng cần điều kiện đo được: môi trường, dữ liệu, thao tác, ngân sách/giới hạn và cách quan sát. Không điền “nhanh”, “premium”, “bảo mật tốt” như tiêu chí đã đủ.

## 4. Domain và business rules

| Entity | Nghĩa / identity | Quan hệ và lifecycle | Quy tắc canonical |
| --- | --- | --- | --- |
| ENT-01 | | | BR-01 |

| BR | Điều kiện | Rule/invariant | Nhánh lỗi và dữ liệu được giữ | Acceptance refs |
| --- | --- | --- | --- | --- |
| BR-01 | | | | |

Phân biệt user data, draft, derived result và persisted data. Ghi đơn vị, timezone, giá trị thiếu/rỗng/0 nếu liên quan. Domain model không bắt buộc là database schema.

## 5. Feature và UX/UI

### F-01 — [Tên feature]

- Actor, entry point, preconditions và kết quả cuối:
- Happy path và thời điểm commit:
- Alternative/error/cancel/retry và phục hồi:
- Rules tham chiếu; không chép lại BR:
- Input/output/event và nơi sở hữu query/selection/draft/commit:
- Screen/experience, baseline, layout, component/data-view refs thực:
- Native/platform adaptation, copy và accessibility cần kiểm tra:

| Acceptance ID thật | Given / tiền điều kiện | When / hành động | Then / kết quả quan sát được |
| --- | --- | --- | --- |
| | | | |

Giữ ID, nghĩa, nguồn, tính bắt buộc và applicability ở nguồn acceptance đã chọn; bảng này là scenario detail theo ref. Không tự ghi pass trong spec. Khi nhiều feature độc lập, tách [feature spec](feature-spec.md).

## 6. Technical spec và quyết định

- Boundaries: app/process/storage/service/extension; mức sơ đồ đủ để giải thích:
- Data/state ownership; interface và failure semantics:
- Persistence, atomicity/concurrency, sync/conflict nếu có:
- Payload/retention/delete/export/backup; dữ liệu ra khỏi thiết bị hoặc chia sẻ qua extension:
- Migration và recovery nếu schema/format thay đổi:
- Ngân sách performance/khả năng truy cập, môi trường đo và dependency/capability:

| ADR | Quyết định | Lý do / tradeoff / source | Khi nào xem lại |
| --- | --- | --- | --- |
| ADR-01 | | | |

Không thêm backend hoặc tài khoản chỉ vì template có mục đó. Nếu dùng source starter, ghi chính xác phần đã có và phần mới cần code; source chưa chạy không được mô tả là native pass.

## 7. Delivery và validation

Phân biệt experiment slice và delivery slice. Giữ toàn bộ deliverable đã nhận, các slice cam kết làm sau và non-goals; một slice đạt không hoàn thành commitment lớn hơn.

| Slice | Outcome nhìn thấy | Scope/các phần cần nối | Dependency/owner | Criterion và evidence cần |
| --- | --- | --- | --- | --- |
| SL-01 | | | | |

| Criterion ID | Fixture/config/môi trường | Phương pháp và input dependencies | Evidence destination | Điều đang chặn |
| --- | --- | --- | --- | --- |
| | | | | |

Chỉ ghi kế hoạch vào bảng trên. Results có nguồn chuẩn ở nguồn kết quả/evidence đã chọn. Phân biệt source review, unit test, build, thao tác native và nghiên cứu người dùng. Một phương pháp không thay thế tự động các phương pháp khác.

## 8. Release, vận hành và học

- Build/version/targets và phạm vi release dự kiến:
- Criteria/evidence cần trước khi đưa cho người dùng; finding còn mở:
- Assets/metadata/locales/icon/screenshots/support/privacy phù hợp app thực:
- Signing/capability/configuration theo platform; secrets giữ ngoài tài liệu:
- Migration/data recovery và phương án xử lý bản lỗi; không giả rollback luôn khả thi:
- Kênh hỗ trợ, triage, người chịu trách nhiệm, thông tin chẩn đoán tối thiểu:
- Câu hỏi học sau release, metric/feedback và giới hạn dữ liệu thu thập:
- Quyền phân phối/phát hành đã được giao hoặc điểm cần xác nhận thực sự:

## 9. Handoff và câu hỏi còn mở

Ghi phần đã đủ để thực hiện tiếp, quyết định nào đang chặn phần việc nào, bước tiếp theo nhỏ nhất và owner. Trước handoff: kiểm tra refs tồn tại, source chuẩn không mâu thuẫn, mọi requirement trong scope có cách quan sát, không có nghiên cứu/test/approval giả. Một câu hỏi chưa giải quyết chỉ chặn phần phụ thuộc; không cần dừng phần độc lập đã được giao.

## Kiểm tra trước bàn giao

- [ ] Chỉ giữ các section cần cho scope; mỗi chủ đề đã đăng ký nguồn chuẩn hoặc dẫn tới tài liệu hiện hữu, không tạo bản sao cạnh tranh.
- [ ] Facts, giả định, quyết định, phần đã viết và phần đã kiểm chứng được phân biệt; số liệu chưa biết không được trình bày như đã đo.
- [ ] Outcome/requirements, domain rules và flow/UI refs đủ rõ cho slice tiếp theo; các ràng buộc hoặc câu hỏi còn mở có tác động và owner cụ thể.
- [ ] Acceptance dùng ID thật trong nguồn acceptance đã chọn; chi tiết semantics nhất quán với criterion và kết quả chỉ dẫn về verification report/evidence thật.
- [ ] Slice, dependency, cách kiểm chứng và handoff phù hợp deliverable được giao; không tự mở rộng nhiệm vụ design-only thành implementation hoặc release.
- [ ] Nếu release thuộc scope, artifact, giới hạn readiness và quyền thực hiện được ghi riêng; `accepted` không được dùng như bằng chứng pass hoặc permission publish.
