# Feature spec F-01 — [tên capability]

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-FEATURE-SPEC` |
| Phiên bản template | `1.1.0` |
| Mục đích | Chốt hành vi quan sát được, IO/events và tình huống chấp nhận của một feature để triển khai một lát cắt dùng được. |
| Dùng khi | Thêm/đổi capability có nhánh, quyền hoặc trạng thái cần thống nhất giữa product, design và engineering. |
| Đầu vào | [Product blueprint](product-blueprint.md), [PRD](prd.md), [domain model](domain-model.md), flow/UI contracts và implementation hiện có. |
| Đầu ra / bàn giao | Behavior và acceptance semantics theo actor/flow, state owner, UI/technical refs và view tham chiếu slice canonical để bàn giao triển khai/validation. |
| Nguồn chuẩn | Khi được đăng ký, file/section này giữ behavior và expected semantics của F. REQ/BR dùng nguồn đã chọn; experience/screen giữ UI state chi tiết; delivery/backlog giữ slice; nguồn acceptance đã chọn giữ criterion ID/nghĩa/tính bắt buộc và report giữ results. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [F-01 / OUT-01 / REQ-01 / phiên bản / input-output và phần ngoài scope] |

[Chuẩn template](../../documentation/template-standard.md). Placeholder là chỗ cần điền, không phải bằng chứng. Phiên bản template theo dõi mẫu dùng chung; revision tài liệu theo dõi bản được điền cho dự án.

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, tách khỏi trạng thái quyết định và kết quả kiểm chứng. `accepted` nghĩa là chọn dùng tài liệu trong phạm vi quyền hạn hiện có; không chứng minh người dùng đã phê duyệt, test đã đạt hoặc có quyền phát hành.

Giữ nguồn chuẩn đã đăng ký trong [document index](document-index.md); không tự thay owner của thông tin chỉ vì sao chép template. Đọc [hướng dẫn bộ tài liệu](../../documentation/README.md) và cập nhật đường dẫn/ID mẫu thành tham chiếu thật của dự án.

`F-01` là feature/capability; flow dùng tên và anchor. Không dùng F-ID để đánh số flow.

## 1. Kết quả và điều kiện sử dụng

- Actor, nhu cầu và hoàn cảnh sử dụng:
- Kết quả nào cho biết actor đã hoàn thành; dấu hiệu thành công quan sát được:
- Entry point và đích đến sau hoàn thành:
- Preconditions: dữ liệu, phiên tác vụ, quyền hoặc dependency thực sự cần:
- Trigger bắt đầu; trường hợp feature không khả dụng và lý do:
- Nguồn chuẩn business rules: [domain-model.md / revision / BR-01…].

Không mặc định actor phải đăng nhập, đi qua onboarding hoặc có backend. Yêu cầu nghiệp vụ nằm ở PRD/domain; file này diễn giải hành vi để thực hiện chúng, không thêm rule ngầm.

## 2. Flow chính — [tên flow]

| Bước | Actor / hành động hoặc sự kiện | Phản hồi và kết quả dữ liệu | Rule / requirement | Điểm chuyển tiếp |
| --- | --- | --- | --- | --- |
| 1 | […] | […] | [BR-01, REQ-01] | [màn / bước / kết thúc] |
| 2 | […] | […] | […] | […] |

- Điểm được coi là hoàn thành: [đã tính, đã commit, đã nhận xác nhận… đúng với feature].
- Kết quả phải còn sau back, đổi màn hoặc mở lại app: [phân biệt đã lưu và draft].
- Hủy/back/đổi đối tượng trong lúc thực hiện; dữ liệu giữ lại và thông báo:

## 3. Nhánh thay thế, lỗi và phục hồi

Giữ các hàng có thể xảy ra; không thêm state chỉ để đủ mẫu. Đặt tên/anchor ổn định để validation plan dẫn chiếu.

| Tình huống / xuất phát từ bước | Điều kiện | Hành vi và dữ liệu được giữ | Hành động phục hồi / đích đến | Rule / criterion liên quan |
| --- | --- | --- | --- | --- |
| [Input không hợp lệ] | […] | […] | […] | […] |
| [Hủy / thay đối tượng / rời màn] | […] | […] | […] | […] |
| [Thao tác thất bại] | […] | […] | […] | […] |
| [Dữ liệu/quyền thay đổi trong lúc thao tác, nếu có] | […] | […] | […] | […] |

Với nhiều bước ghi dữ liệu, nói rõ bước nào đã có hiệu lực khi bước sau lỗi. Retry không được mặc nhiên tạo thêm một lần xử lý hoặc record; yêu cầu hành vi nằm ở đây, cơ chế nằm trong technical spec.

## 4. IO và sự kiện

| Input / output | Ý nghĩa, shape hoặc schema nguồn chuẩn | Identity / đơn vị / null | Nguồn, validation và người nhận |
| --- | --- | --- | --- |
| […] | [link schema/code khi đã có] | […] | [BR-…] |

| Event / ý định | Payload và scope | Người xử lý / thời điểm có hiệu lực | Kết quả, lỗi, cancel hoặc retry |
| --- | --- | --- | --- |
| […] | […] | […] | […] |

Phân biệt hành động được yêu cầu, thao tác đang chạy và sự kiện đã hoàn thành. Event có thể chỉ là lời gọi nội bộ; không mặc định cần event bus, API mạng hoặc telemetry. Interface kỹ thuật cụ thể dẫn sang [technical spec](technical-spec.md).

## 5. Quyền và state ownership

| Actor / thao tác | Phạm vi dữ liệu | Điều kiện cho phép / nguồn rule | Khi thiếu, từ chối hoặc mất quyền | Điểm kiểm tra thực |
| --- | --- | --- | --- | --- |
| […] | […] | [BR-… / platform permission nếu thật sự cần] | […] | [link technical spec] |

Nếu không có account hoặc permission request, ghi đúng phạm vi đó. Quyền nghiệp vụ, quyền hệ điều hành và khả năng thao tác của control là các điều kiện riêng.

| State có áp dụng | Canonical owner | Ai thay đổi / trigger | Vòng đời và phần cần giữ/reset | Nơi mô tả chi tiết |
| --- | --- | --- | --- | --- |
| [Domain / committed data] | […] | […] | […] | [ENT-/BR- refs] |
| [Draft / input / result] | […] | […] | […] | […] |
| [Query / selection / focus] | […] | […] | […] | [SCR-01] |
| [Processing / lỗi / quyền] | […] | […] | […] | […] |

## 6. UI và experience được dẫn chiếu

| Hợp đồng | Tài liệu / revision đang sở hữu | Phần feature sử dụng hoặc thay đổi |
| --- | --- | --- |
| Flow và trạng thái xuyên màn | [Experience](../experience.md) → [file dự án] | […] |
| Trách nhiệm màn | [Screen](../screen.md) → [SCR-01 / file dự án] | […] |
| Component behavior | [Component](../component.md) → [CMP-… nếu cần] | […] |
| Dữ liệu và cách biểu diễn | [Data view](../data-view.md) → [DV-… nếu cần] | […] |

Tái sử dụng các contract đang có. Feature spec chỉ ghi tác động và dẫn chiếu; không sao lại anatomy, token, layout, query semantics hoặc toàn bộ state table của UI. Nếu không cần tách file, giữ một nguồn canonical trong context hiện hữu; chỉ dùng document index khi hữu ích.

## 7. Tình huống chấp nhận

Expected semantics chi tiết được định nghĩa tại đây khi section/tài liệu được đăng ký làm nguồn chuẩn; nếu đã có nguồn canonical khác, giữ tham chiếu tới tình huống và revision đó. **Criterion ID, nghĩa, tính bắt buộc và applicability lấy từ nguồn acceptance đã chọn**; không duy trì một bộ acceptance bắt buộc thứ hai trong Markdown. Dùng ID thực như `C-001`, `APP-*`, `LIF-*`, `UTL-*`, `WID-*`, `PL-*`; không đổi ID chỉ để theo mẫu.

| Tên / anchor tình huống | Given: trạng thái và fixture | When: hành động | Then: kết quả quan sát và phần phải giữ | Criterion thực |
| --- | --- | --- | --- | --- |
| [Hoàn thành flow chính] | […] | […] | […] | [C-001] |
| [Nhánh lỗi ảnh hưởng kết quả] | […] | […] | […] | […] |
| [Dữ liệu biên / adaptation liên quan] | […] | […] | […] | […] |

Tình huống phải phân biệt được đúng/sai; “dễ dùng”, “nhanh” hoặc “an toàn” cần điều kiện và cách quan sát cụ thể. Chốt tập biến thể bắt buộc trước khi chạy; một ví dụ đạt không đại diện cho mọi cấu hình. Phương pháp và evidence đặt trong [validation plan](validation-plan.md); kết quả thật trong nguồn kết quả/evidence đã chọn.

## 8. Delivery slice và điều kiện bàn giao

Bảng này là view tham chiếu tới slice canonical trong delivery plan/backlog đã đăng ký, không là scope/dependency thứ hai. Nếu dự án chưa có delivery plan, có thể đăng ký chính section này làm nguồn chuẩn của slice; khi tách file, chuyển định nghĩa sang nguồn mới và giữ link tại đây.

| Slice | Flow hoàn chỉnh nhỏ nhất | Included / deferred | Dependency / giả định chặn | Criteria và evidence cần |
| --- | --- | --- | --- | --- |
| `SL-01` | [input → tác vụ → kết quả dùng được → recovery] | […] | [ASM-/ADR- refs] | […] |

Dẫn chiếu [delivery plan](delivery-plan.md) để quản lý scope, dependency, thứ tự, owner và trạng thái triển khai của slice khi tài liệu đó đã là canonical. Không chép lại giá trị cần cập nhật ở hai nơi. Không chia lát cắt chỉ thành “vẽ UI” rồi coi kết quả người dùng đã hoàn tất.

**Exit condition:** actor/preconditions, flow và nhánh quan trọng đủ rõ; IO/state có owner; `BR/REQ` dẫn đúng nguồn; acceptance map tới criteria thật; UI/technical contract và `SL-01` xác định được. Câu hỏi còn mở có owner, ảnh hưởng và điều kiện giải quyết; chỉ chặn phần phụ thuộc. Bàn giao có thể tiếp tục theo quyền hạn hiện có, không tự tạo gate phê duyệt mới.

## Kiểm tra trước bàn giao

- [ ] Actor, preconditions, flow chính và nhánh lỗi/hủy có kết quả quan sát được; không thêm business rule ngầm.
- [ ] IO/events, quyền và state có owner; điểm commit và cách giữ/reset draft, input, result được nêu đúng scope.
- [ ] UI/experience/component/data-view dẫn đúng nguồn và revision; không sao hợp đồng chi tiết để duy trì hai nơi.
- [ ] Expected scenarios dẫn tới criterion thật trong nguồn acceptance đã chọn; nghĩa/tính bắt buộc/results không bị tái định nghĩa tại feature spec.
- [ ] Bảng SL là view tham chiếu delivery/backlog canonical, trừ khi section được đăng ký rõ; exit condition và blocker được đối chiếu trước bàn giao.
