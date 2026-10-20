# Technical spec — [hệ thống / lát cắt]

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-TECHNICAL-SPEC` |
| Phiên bản template | `1.1.0` |
| Mục đích | Chốt cách thực hiện behavior, invariant và quality requirements trong boundary kỹ thuật có thể triển khai, kiểm chứng. |
| Dùng khi | Có interface, persistence, concurrency hoặc dependency cần thống nhất; thay đổi kỹ thuật ảnh hưởng nhiều phần. |
| Đầu vào | [PRD](prd.md), [domain model](domain-model.md), [feature spec](feature-spec.md), code/config và ràng buộc môi trường hiện có. |
| Đầu ra / bàn giao | Boundary, interface/storage/consistency/privacy contract, quality budget và ADR refs để bàn giao slice, validation và operations phù hợp. |
| Nguồn chuẩn | Khi được đăng ký, tài liệu giữ hợp đồng kỹ thuật trong scope; schema/code/interface và ADR hiện có giữ phần đã canonical. Domain/PRD/feature giữ nghĩa nghiệp vụ và expected behavior; không định nghĩa lại ở đây. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Hệ thống / runtime / OUT-01 / F-01 / REQ-01 / BR-01 / SL-01 và phần ngoài scope] |

[Chuẩn template](../../documentation/template-standard.md). Placeholder là chỗ cần điền, không phải bằng chứng. Phiên bản template theo dõi mẫu dùng chung; revision tài liệu theo dõi bản được điền cho dự án.

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, tách khỏi trạng thái quyết định và kết quả kiểm chứng. `accepted` nghĩa là chọn dùng tài liệu trong phạm vi quyền hạn hiện có; không chứng minh người dùng đã phê duyệt, test đã đạt hoặc có quyền phát hành.

Giữ nguồn chuẩn đã đăng ký trong [document index](document-index.md); không tự thay owner của thông tin chỉ vì sao chép template. Đọc [hướng dẫn bộ tài liệu](../../documentation/README.md) và cập nhật đường dẫn/ID mẫu thành tham chiếu thật của dự án.

## 1. Ranh giới và runtime

- Entry points, kết quả cần cung cấp và feature liên quan:
- Nền tảng/OS/runtime/toolchain hỗ trợ; configuration/build targets cần có:
- Phần hiện có sẽ giữ, thay hoặc mở rộng; lý do gắn với requirement:
- Ràng buộc môi trường, quyền chạy, signing hoặc dịch vụ thật cần dùng:
- Giả định còn mở: [ASM-01 → nguồn chuẩn và ảnh hưởng].

| Phần / module trong scope | Trách nhiệm và dữ liệu sở hữu | Chạy ở đâu / ai gọi | Boundary / dependency |
| --- | --- | --- | --- |
| […] | […] | [app process, extension, worker, service… nếu có] | […] |

Một app cục bộ, một process và file store có thể đủ. Không mặc định backend, microservices, queue hoặc cloud. Chỉ vẽ sơ đồ khi nó làm rõ trust boundary, ownership hay luồng dữ liệu khó đọc bằng bảng.

## 2. Nguồn dữ liệu và ownership

| Domain ref / dữ liệu | Nguồn sự thật khi đã commit | Writer / reader | Cache, bản sao, dữ liệu dẫn xuất | Vòng đời / boundary |
| --- | --- | --- | --- | --- |
| [ENT-01] | […] | […] | [cách invalidation nếu có] | […] |

- Identity, version, ordering và timestamp: [tham chiếu domain; mapping kỹ thuật].
- UI draft, committed data và snapshot dùng ngoài app được tách/đồng bộ thế nào:
- File/DB/schema cụ thể: [code/schema canonical, format version, encode/decode và precision].
- Dữ liệu thiếu, corrupt, unsupported version hoặc không đọc được: [cách phân biệt; bảo toàn dữ liệu cũ; recovery].

Không coi `load` lỗi là empty thành công. Không hứa persistence, sync hoặc backup chỉ vì dữ liệu đang hiển thị trong memory. Nếu storage nhỏ hoặc synchronous là lựa chọn có chủ đích, ghi phạm vi và dấu hiệu phải thay.

## 3. Interfaces và hợp đồng thực thi

| Interface / operation | Caller → owner | Input/output và schema nguồn chuẩn | Validation / rule | Lỗi, cancellation, retry |
| --- | --- | --- | --- | --- |
| […] | […] | [link code/schema hoặc mô tả tối thiểu khi chưa có] | [BR-…] | […] |

- Auth/authorization hoặc OS permissions, **nếu có**: kiểm tra ở đâu và trường hợp quyền đổi giữa thao tác:
- Correlation/operation identity nếu cần phân biệt retry, duplicate hoặc response cũ:
- Compatibility khi caller và callee khác phiên bản:

Interface có thể là function nội bộ, file format hoặc event; chỉ ghi endpoint/network contract khi thực sự có. Khi schema đã có nguồn chuẩn trong code, dẫn chiếu và ghi ý nghĩa còn thiếu thay vì chép toàn bộ schema vào đây.

## 4. Commit, consistency và concurrency

| Thao tác quan trọng | Invariant cần giữ | Điểm commit / phạm vi atomic | Writer đồng thời / thứ tự | Thất bại trước và sau commit |
| --- | --- | --- | --- | --- |
| […] | [BR-01] | […] | [single writer, actor, transaction… lựa chọn thật] | [state thật, rollback/retry/compensation nếu có] |

- Chống ghi đè bản mới, double submit hoặc kết quả đến sai thứ tự khi có khả năng đó:
- Hủy tác vụ có dừng side effect không; khi nào không thể hủy:
- Nếu ghi nhiều file hoặc bước, failure ở giữa được trình bày/phục hồi thế nào:
- Snapshot, cache, widget hoặc notification update lỗi sau commit có ảnh hưởng kết quả chính không:

Không dùng “atomic” để chỉ một flow nhiều bước nếu chỉ một file write thực sự atomic. Nêu giới hạn consistency mà người dùng có thể quan sát, cùng criterion kiểm chứng.

## 5. Sync, migration và backup theo nhu cầu

| Khả năng | Có trong scope? / lý do | Contract nếu chọn | Recovery / criterion |
| --- | --- | --- | --- |
| Sync / nhiều writer | […] | [nguồn sự thật, offline, conflict, thứ tự, delete propagation] | […] |
| Migration / thay schema | […] | [version vào/ra, phát hiện lỗi, bảo toàn bản cũ, compatibility] | […] |
| Backup / export | […] | [payload/phạm vi, format, nơi giữ, tính đầy đủ, version] | […] |
| Restore / import | […] | [validate, merge/replace, trùng identity, phần thất bại] | […] |

“Ngoài scope” là quyết định thiết kế, không tự là `không áp dụng` trong verification. Local storage không tự tạo cam kết backup. Nếu dữ liệu có giá trị nhưng chưa có recovery, ghi giới hạn và dẫn tới [release/operations](release-operations.md); không thêm hệ thống mới khi tác vụ chưa cần.

## 6. Privacy và vòng đời dữ liệu

| Nhóm dữ liệu / mục đích | Thu thập từ đâu / phạm vi tối thiểu | Nơi lưu / bên nhận / quyền truy cập | Retention / xóa / export | Log, cache, backup và bản sao |
| --- | --- | --- | --- | --- |
| […] | […] | […] | [thời điểm và phạm vi cụ thể] | [có giữ lại gì sau xóa không] |

- Secret/credential, nếu có: nguồn cấp và cách quản lý; không ghi giá trị thật vào tài liệu.
- Dữ liệu hiển thị ngoài ngữ cảnh chính: widget, preview, clipboard, notification, log hoặc analytics nếu feature dùng:
- Đường dữ liệu khi người dùng tắt lựa chọn, xóa đối tượng hoặc rút quyền:
- Biện pháp và giới hạn: [chỉ mô tả cơ chế đã chọn; không dùng “secure/private” thay contract].

Yêu cầu privacy cần quan sát được trong phạm vi xác định, ví dụ loại dữ liệu nào bị cấm trong payload nào, dưới những flow/fixture nào và bằng phương pháp kiểm tra nào. Không biến một phiên quan sát không thấy network thành bằng chứng cho mọi hành vi của app.

## 7. Quality budget có phạm vi đo

| Requirement / property | Metric, đơn vị và ngưỡng được chọn | Workload / fixture / configuration | Cách đo và sampling | Căn cứ / criterion |
| --- | --- | --- | --- | --- |
| [REQ-…: latency, memory, reliability…] | [giá trị hoặc quy tắc; percentile nếu phù hợp] | [thiết bị, data size, trạng thái đầu, thời gian] | […] | […] |
| [REQ-…: privacy, data integrity…] | [điều kiện đúng/sai hoặc phạm vi không được xuất hiện] | […] | […] | […] |

Ghi baseline là measured/estimated/unmeasured. Không áp cùng ngưỡng tốc độ, số record hay dung lượng cho mọi app. Khi chưa có căn cứ, ghi phép đo cần làm và owner; không giả vờ đã đạt budget. Accessibility/adaptation theo contract UI và validation plan, không suy từ việc dùng native control.

## 8. Dependency risk và ADR

| Dependency / capability | Version hoặc nguồn chuẩn | Vì sao cần / điểm phụ thuộc | Rủi ro, license/quyền dùng nếu liên quan | Fallback / owner / trigger xem lại |
| --- | --- | --- | --- | --- |
| […] | […] | […] | [availability, data access, update, lock-in… thực tế] | […] |

| ADR | Quyết định / trạng thái | Lựa chọn đã xét và lý do | Đánh đổi / khả năng đảo ngược | Khi xem lại / file canonical |
| --- | --- | --- | --- | --- |
| `ADR-01` | […] | […] | […] | […] |

ADR có thể giữ ngay tại đây hoặc dẫn tới tài liệu quyết định đang có; chọn một nguồn chuẩn. Không tạo phương án giả để đủ bảng, không tạo gate phê duyệt ngoài quyền hạn nhiệm vụ.

## 9. Handoff

**Exit condition:** boundary và ownership rõ; interface/schema có nguồn; failure/commit/đồng thời được chốt cho `SL-01`; quality/privacy có scope và cách đo; dependency và giả định chặn có owner. Feature behavior và `BR-*` vẫn nhất quán sau mapping kỹ thuật.

- Implementation slice / owner / thứ tự: [delivery plan](delivery-plan.md).
- Fixtures, config, build/runtime checks và evidence dự kiến: [validation plan](validation-plan.md).
- Deployment, rollback, support hoặc recovery cần tiếp nhận nếu áp dụng: [release/operations](release-operations.md).
- Điều chưa quyết định, phần bị chặn và điều kiện tiếp tục:

Spec được chấp nhận không thay build log, runtime test hoặc criterion result. Các ID `ADR/ENT/BR` được người/agent review; checker không tự xác minh architecture hoặc chạy hệ thống.

## Kiểm tra trước bàn giao

- [ ] Boundary/runtime, nguồn dữ liệu và writer/reader có owner; interface/schema trỏ đúng nguồn đang dùng.
- [ ] Commit, failure trước/sau commit, cancellation và concurrency được chốt cho slice; không hứa atomic ngoài phạm vi thực.
- [ ] Sync/migration/backup/privacy lifecycle chỉ mô tả khả năng đã chọn; dữ liệu corrupt và recovery có contract rõ.
- [ ] Quality budget có metric, workload, config và cách đo; measured/estimated/unmeasured được phân biệt.
- [ ] Dependency/ADR có căn cứ, đánh đổi và trigger xem lại; delivery/validation/operations nhận đúng phần qua exit condition, không suy spec thành build/runtime pass.
