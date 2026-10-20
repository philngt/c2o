# Validation plan — [phạm vi / release / slice]

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-VALIDATION-PLAN` |
| Phiên bản template | `1.1.0` |
| Mục đích | Xác định kiểm tra gì, bằng cách nào, với input/config nào và evidence nào đủ để đánh giá từng criterion. |
| Dùng khi | Chốt cách kiểm chứng trước triển khai, chuẩn bị kiểm tra thay đổi hoặc làm rõ coverage, blocker và evidence còn thiếu. |
| Đầu vào | [PRD](prd.md), [feature spec](feature-spec.md), [technical spec](technical-spec.md), UI contracts, nguồn acceptance đã chọn và verification report hiện có. |
| Đầu ra / bàn giao | Matrix criterion–fixture/config–input–method–evidence, negative cases, blocker và index dẫn tới execution records; bàn giao kế hoạch chạy và phần cần xử lý tiếp. |
| Nguồn chuẩn | Khi được đăng ký, file này giữ phương pháp, fixtures và coverage dự kiến. Nguồn acceptance đã chọn giữ criterion ID/nghĩa/tính bắt buộc; expected semantics theo nguồn đã đăng ký; nguồn kết quả/evidence đã chọn giữ kết quả và artifact/revision; evidence/log giữ quan sát thật. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Release / SL-01 / OUT-01 / F-01 / REQ-01 / coverage và phần ngoài scope] |

[Chuẩn template](../../documentation/template-standard.md). Placeholder là chỗ cần điền, không phải bằng chứng. Phiên bản template theo dõi mẫu dùng chung; revision tài liệu theo dõi bản được điền cho dự án.

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, tách khỏi trạng thái quyết định và kết quả kiểm chứng. `accepted` nghĩa là chọn dùng tài liệu trong phạm vi quyền hạn hiện có; không chứng minh người dùng đã phê duyệt, test đã đạt hoặc có quyền phát hành.

Giữ nguồn chuẩn đã chọn trong context hiện có hoặc [document index](document-index.md) nếu hữu ích; không tự thay owner của thông tin chỉ vì sao chép template. Đọc [hướng dẫn bộ tài liệu](../../documentation/README.md) và cập nhật đường dẫn/ID mẫu thành tham chiếu thật của dự án.

Áp dụng [hợp đồng bằng chứng](../../core/evidence.md). Tài liệu accepted vẫn chỉ là kế hoạch nếu chưa thực hiện các phép kiểm tra.

## 1. Nguồn chuẩn và phạm vi kết luận

- Hồ sơ thật dùng cho scope này: [đường dẫn nguồn acceptance đã chọn] / [đường dẫn nguồn kết quả/evidence đã chọn].

- **Nguồn acceptance đã chọn:** criterion ID/nghĩa, nguồn/rationale, tính bắt buộc, applicability, phương pháp và reviewer khi cần; dùng nguồn C2O/native hiện có, không tạo bản cạnh tranh.
- **Feature spec:** expected semantics chi tiết của tình huống; dẫn chiếu tên/anchor và revision, không viết một expectation khác trong kế hoạch này.
- **Nguồn kết quả/evidence đã chọn:** status, rationale, artifact/revision hoặc observed state, input/evidence refs và giới hạn thật.
- **Evidence:** kết quả quan sát thật, cấu hình, bước/lệnh đã chạy, giới hạn và các trường hợp bị skip. Tác vụ nhỏ có thể ghi trong context hiện có.

Chỉ khi đã chọn profile JSON tùy chọn, dùng [project template](../project.json) và [report template](../verification-report.json) theo [evidence profile](../../core/evidence.md). Các field/hash và uppercase status thuộc profile đó, không thành yêu cầu của mọi validation plan; profile không mã hóa C2O `partial`.

Dùng criterion ID thực của dự án: `C-*`, `APP-*`, `LIF-*`, `UTL-*`, `WID-*`, `PL-*` hoặc bộ đã được dự án chọn. `REQ/BR/F/SL` là traceability, không tự trở thành criterion. Nếu thay phạm vi/tiêu chí, cập nhật hợp đồng và nguồn acceptance đã chọn theo quyền hiện có, có lý do trước khi đánh giá; không hạ required hoặc đổi expectation để hợp thức hóa lỗi.

## 2. Criterion → phương pháp → evidence

| Criterion thực | Expected semantics / revision | Fixture và cấu hình bắt buộc | Inputs ảnh hưởng kết luận | Phương pháp / thao tác | Evidence dự kiến |
| --- | --- | --- | --- | --- | --- |
| [C-001] | [F-01 / tên tình huống / BR-01] | [fixture + config refs] | [code, query/model, config, harness…] | [lệnh hoặc bước; oracle độc lập] | [đường dẫn file sẽ tạo] |

Mỗi hàng phải giúp reviewer biết cách phân biệt đạt/không đạt. Đường dẫn “dự kiến” không chứng minh file đã tồn tại; chỉ đưa evidence thật vào report sau khi chạy. Không suy expected output bằng chính hàm đang được kiểm tra.

### Chọn đúng loại bằng chứng

| Điều muốn kết luận | Phương pháp phù hợp | Giới hạn cần giữ |
| --- | --- | --- |
| Source/config tuân theo contract | Review, lint, static checks | Không chứng minh compile hoặc runtime |
| Source build được | Build log từ đúng target/toolchain/config | Không chứng minh launch, interaction, signing capability thực hoặc usability |
| Logic và invariant đúng trong input đã chọn | Unit/integration checks với expected result có căn cứ | Không tự đại diện cho mọi UI/environment |
| Flow/state/native hoặc web behavior hoạt động | Runtime thao tác/test đúng build, fixture và config | Screenshot riêng lẻ không chứng minh action, persistence hoặc recovery |
| Layout/nội dung/semantics trong scope | Render + quan sát; kiểm tra accessibility/input phù hợp | Một kích thước/theme/thiết bị không đại diện toàn bộ coverage |
| Người dùng hiểu và hoàn thành nhiệm vụ | Task study với người tham gia và protocol phù hợp | Agent critique hoặc walkthrough không phải nghiên cứu người dùng đã thực hiện |

Chọn mức kiểm tra giải quyết rủi ro thực của thay đổi. Không bắt mọi sửa nhỏ phải có toàn bộ các loại nghiên cứu; không dùng một loại evidence thay cho một kết luận nó không hỗ trợ.

## 3. Fixtures và coverage

| Fixture / dataset ref | Mục đích / đặc điểm | Expected facts và nguồn | Cách tạo/reset / dữ liệu nhạy cảm |
| --- | --- | --- | --- |
| […] | [identity trùng tên, biên, missing/0/unknown… có áp dụng] | [quy tắc hoặc oracle độc lập] | […] |

| Configuration ref | Runtime / target / build | Thiết bị, viewport hoặc window | Locale, theme, text/input/assistive technology | Vì sao bắt buộc / criterion |
| --- | --- | --- | --- | --- |
| […] | [version / revision / flags] | […] | [chọn các biến thể thật] | […] |

Chốt tập biến thể trước khi chạy. Không mặc định tích Descartes của mọi option; chọn coverage có căn cứ, nhưng mọi biến thể đã cam kết phải được đánh giá. Nếu cần theo dõi riêng từng cấu hình, tách criterion trong nguồn acceptance đã chọn. Nếu giữ chung một criterion, evidence phải ghi kết quả từng trường hợp; chỉ pass khi đủ các trường hợp bắt buộc đạt.

## 4. Negative cases và recovery

Giữ các tình huống thực sự có thể xảy ra. Dẫn về flow/state contract thay vì sáng tạo hành vi mới trong test.

| Rủi ro / tình huống | Fault hoặc input tạo ra | State/data phải giữ / expectation ref | Cách quan sát / phục hồi | Criterion |
| --- | --- | --- | --- | --- |
| [Invalid input / empty / missing] | […] | […] | […] | […] |
| [Read/decode/write failure nếu có storage] | […] | […] | […] | […] |
| [Cancel/back/đổi đối tượng khi có draft] | […] | […] | […] | […] |
| [Duplicate/concurrent/stale response nếu có] | […] | […] | […] | […] |
| [Permission/network/dependency failure nếu có] | […] | […] | […] | […] |

Ghi cách fault injection tránh ảnh hưởng dữ liệu thật. Test migration/restore/delete cần xác định bản dữ liệu có thể phục hồi và phạm vi xóa. Dữ liệu nhạy cảm hoặc credential không đưa vào log/artifact nếu không cần cho kết luận.

## 5. Chuẩn bị chạy và blocker

| Điều kiện / blocker | Criterion hoặc biến thể bị ảnh hưởng | Bằng chứng về trạng thái môi trường | Owner / việc cần làm để chạy được |
| --- | --- | --- | --- |
| […] | […] | [tool/SDK/device/dependency/fixture/permission…] | […] |

- Lệnh/bước chạy và working directory thật:
- Dependency, capability, signing hoặc service config thật cần có:
- Cách reset dataset, thứ tự chạy khi có state phụ thuộc và cleanup:
- Điều kiện dừng; tiêu chí cần chạy lại khi input thay đổi:

Chưa chạy hoặc thiếu môi trường giữ `not-tested` cùng lý do cụ thể; evidence một phần giữ `partial`. N/A là quyết định applicability có căn cứ trong contract, không thay kiểm tra khó chạy hoặc requirement đã cam kết. Nếu đã quan sát lỗi, giữ `fail` cùng coverage chưa chạy; không làm mất lỗi vì biến thể khác bị chặn.

## 6. Tham chiếu execution — chỉ điền sau khi thực hiện

Đây là index của lần chạy. Quan sát/lệnh/output chi tiết có một nguồn chuẩn ở evidence/log; status/rationale/input/evidence references nằm trong nguồn kết quả/evidence đã chọn. Bảng dưới chỉ dẫn tới các nguồn đó, không chép lại quan sát hoặc tạo bảng kết quả thứ hai.

| Lần chạy / ngày / người hoặc agent | Criterion + biến thể / report record | Build/input/config/fixture refs | Log/evidence ghi lệnh và quan sát | Giới hạn / skip được ghi ở đâu |
| --- | --- | --- | --- | --- |
| [chưa chạy] | […] | […] | […] | […] |

- Ghi số test/case đã thực sự chạy, các skip và output; exit code 0 không chứng minh có test hoặc đủ coverage.
- Giữ artifact/revision hoặc observed state và evidence locations tại nguồn đã chọn. Chỉ profile JSON yêu cầu đường dẫn tương đối từ **project root**, SHA-256 byte thật và project binding theo contract riêng.
- Xác định code, config, fixtures, harness và dependency ảnh hưởng kết luận; danh sách hash của profile JSON không tự chứng minh dependency đầy đủ.
- Screenshot ghi màn/state, build, thiết bị/kích thước, appearance và dataset; thao tác/persistence cần evidence bổ sung phù hợp.
- Khi input hoặc requirement đổi, đánh giá bằng chứng nào không còn dùng được và chạy lại phần bị ảnh hưởng; không chỉ cập nhật hash để giữ kết luận cũ.

Kế hoạch, source review và tài liệu `accepted` không phải execution receipt. Checker của profile JSON tùy chọn chỉ kiểm tra contract/report JSON và tham chiếu hash được khai báo; không tự chạy UI/test, xác minh traceability hoặc chứng nhận nội dung review.

## 7. Điều kiện bàn giao và kết luận

**Sẵn sàng chạy:** criteria đã canonical; expectation refs rõ; fixtures/config/method đủ cụ thể; owner và điều kiện môi trường xác định; blocker được ghi cho đúng phần bị ảnh hưởng.

**Sau khi chạy:** nguồn kết quả/evidence đã chọn giữ kết quả thật; review-only không sửa artifact, còn production chỉ sửa trong scope/quyền đã có; evidence giải thích scope và giới hạn; lỗi/blocker có owner cùng bước tiếp theo. [Delivery plan](delivery-plan.md) và [release/operations](release-operations.md) tiếp nhận phần còn lại theo nhiệm vụ đã được giao. Không gọi hồ sơ đầy đủ là quyền phát hành hay chứng nhận chất lượng toàn hệ thống.

- Criteria còn `fail / partial / not-tested`: [dẫn report, không sao chép một bảng trạng thái dễ lệch].
- Thay đổi cần thực hiện hoặc phạm vi cần quyết định lại:
- Bằng chứng đủ cho kết luận nào; kết luận nào chưa được hỗ trợ:

## Kiểm tra trước bàn giao

- [ ] Nguồn acceptance/evidence thật và expected-semantics refs đã xác định; ID/nghĩa/tính bắt buộc/applicability theo contract hiện có.
- [ ] Mỗi criterion cần kiểm tra có fixture, configuration, input dependencies, phương pháp và nơi lưu evidence dự kiến.
- [ ] Expected output có căn cứ độc lập; negative/recovery cases phù hợp rủi ro và không làm hỏng dữ liệu thật.
- [ ] Coverage bắt buộc được chốt; phần chưa chạy, bị chặn hoặc không áp dụng được phân biệt đúng evidence contract.
- [ ] Execution index chỉ dẫn tới report/evidence canonical; không sao status hoặc kết quả quan sát thành bảng thứ hai.
- [ ] Đã đối chiếu điều kiện sẵn sàng chạy/bàn giao; không dùng placeholder, checklist hoặc document status thay execution evidence.
