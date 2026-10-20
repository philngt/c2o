# Domain model — [tên miền / phạm vi]

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-DOMAIN-MODEL` |
| Phiên bản template | `1.1.0` |
| Mục đích | Thống nhất thuật ngữ, đối tượng, identity, quy tắc nghiệp vụ, quan hệ và vòng đời mà sản phẩm phải giữ. |
| Dùng khi | Các flow cùng dùng dữ liệu, trạng thái/quy tắc dễ hiểu khác nhau hoặc thay model có thể ảnh hưởng nhiều feature. |
| Đầu vào | [Business design](business-design.md), [product blueprint](product-blueprint.md), [PRD](prd.md), sản phẩm/dữ liệu và bằng chứng hiện có. |
| Đầu ra / bàn giao | Glossary, ENT/BR, lifecycle/relationships và tác động thay đổi để bàn giao sang [feature](feature-spec.md), [technical](technical-spec.md) và [validation](validation-plan.md). |
| Nguồn chuẩn | Khi được đăng ký, tài liệu/section này giữ glossary, ENT, BR, quan hệ và lifecycle trong scope. Nếu dự án đã có nguồn chuẩn khác, giữ tham chiếu ở đây; technical spec giữ DB/schema và cơ chế lưu. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Miền / phiên bản / OUT-01 / F-01 / REQ-01 và phần ngoài scope] |

[Chuẩn template](../../documentation/template-standard.md). Placeholder là chỗ cần điền, không phải bằng chứng. Phiên bản template theo dõi mẫu dùng chung; revision tài liệu theo dõi bản được điền cho dự án.

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, tách khỏi trạng thái quyết định và kết quả kiểm chứng. `accepted` nghĩa là chọn dùng tài liệu trong phạm vi quyền hạn hiện có; không chứng minh người dùng đã phê duyệt, test đã đạt hoặc có quyền phát hành.

Giữ nguồn chuẩn đã đăng ký trong [document index](document-index.md); không tự thay owner của thông tin chỉ vì sao chép template. Đọc [hướng dẫn bộ tài liệu](../../documentation/README.md) và cập nhật đường dẫn/ID mẫu thành tham chiếu thật của dự án.

## 1. Ranh giới domain và điều chưa biết

- Việc domain này giúp người dùng hoàn thành:
- Actor và vai trò liên quan; chỉ thêm account/organization khi sản phẩm có:
- Dữ liệu/sự kiện đi vào, kết quả đi ra; hệ thống hoặc miền bên ngoài:
- Thuật ngữ/quy tắc đã quan sát từ sản phẩm, nghiên cứu hoặc tài liệu nào:
- Giả định còn mở: [ASM-01 → nơi quản lý giả định, ảnh hưởng và điều kiện xác minh].

Domain model mô tả ý nghĩa và luật của sản phẩm. Tên bảng, index, file JSON, API payload và chiến lược lưu thuộc [technical spec](technical-spec.md). Một entity có thể được lưu qua nhiều cấu trúc; một màn hình có thể ghép nhiều entity. Không dùng cấu trúc UI hoặc DB làm định nghĩa nghiệp vụ mặc định.

## 2. Glossary

| Thuật ngữ chuẩn | Ý nghĩa trong scope | Ví dụ / trường hợp dễ nhầm | Từ đồng nghĩa hoặc từ tránh dùng | Nguồn |
| --- | --- | --- | --- | --- |
| […] | […] | […] | […] | [tài liệu / quan sát] |

Định nghĩa rõ các cặp có ảnh hưởng như “đã lưu/đang soạn”, “xóa/ẩn/lưu trữ”, “không có/không biết/không được xem”. Chỉ giữ những thuật ngữ cần thống nhất cho scope này.

## 3. Entity, identity và giá trị

| Entity ref | Đại diện cho gì / một instance là gì | Identity trong runtime | Thuộc tính có ý nghĩa | Nguồn sự thật / owner |
| --- | --- | --- | --- | --- |
| `ENT-01` [tên] | […] | [ai cấp, duy nhất trong scope nào, khi nào đổi/không đổi] | [nghĩa, đơn vị, null/unknown; link nếu dài] | […] |

`ENT-01` là mã tham chiếu **loại đối tượng** trong tài liệu; nó không phải ID của một record người dùng. Phân biệt identity với tên hiển thị, khóa tra cứu và vị trí trong list. Nếu một giá trị không có identity riêng, ghi rõ nó được so sánh bằng giá trị nào.

| Thuộc tính / giá trị cần làm rõ | Quy tắc ý nghĩa | Thiếu / rỗng / 0 / unknown | Nguồn thời gian, đơn vị hoặc phạm vi |
| --- | --- | --- | --- |
| […] | […] | […] | […] |

Các field chỉ phục vụ storage không cần được liệt kê ở đây. Trường tính toán phải chỉ rõ đầu vào, phạm vi và trường hợp chưa tính được; nhãn status phải có nghĩa ngoài màu sắc hoặc cách render.

## 4. Business invariants — nguồn chuẩn `BR-*`

Khi section/tài liệu này được đăng ký làm nguồn chuẩn, giữ phát biểu quy tắc nghiệp vụ trong scope tại đây. Nếu BR đã có nguồn canonical khác, bảng này chỉ giữ tham chiếu tới ID và revision đó. Feature/technical/UI docs không tạo bản luật khác. Phân biệt invariant luôn phải giữ với policy chỉ áp dụng trong một hoàn cảnh.

| Rule | Phát biểu có thể kiểm tra | Phạm vi / điều kiện / ngoại lệ | Ví dụ hợp lệ và vi phạm | Căn cứ / giả định | Requirement và feature dùng |
| --- | --- | --- | --- | --- | --- |
| `BR-01` | [điều gì phải đúng] | [ENT-01, thời điểm áp dụng] | [mỗi loại một ví dụ có ý nghĩa] | [nguồn hoặc ASM-01] | [REQ-01, F-01] |

- Khi vi phạm, sản phẩm phải ngăn commit, phục hồi hay ghi nhận trạng thái nào: [tham chiếu rule và feature behavior].
- Ai được thay đổi policy; dữ liệu cũ được hiểu theo rule nào: […].
- Rule bị thay thế: [ID/revision cũ → rule mới, lý do và tác động]. Không đổi nghĩa ID âm thầm.

Điểm thực thi và transaction nằm trong technical spec; thông báo, hành động tiếp theo nằm trong feature/UI contract. Việc UI khóa nút không tự chứng minh invariant đã được giữ ở mọi đường ghi.

## 5. Vòng đời và transition

| Entity / trạng thái nguồn | Trigger / ý định | Điều kiện và rule | Trạng thái đích / thay đổi domain | Hủy / thất bại / phục hồi |
| --- | --- | --- | --- | --- |
| [ENT-01 / …] | […] | [BR-01] | […] | […] |

- Điểm tạo identity, thời điểm kết quả có hiệu lực và trạng thái kết thúc:
- Khả năng đảo ngược; xóa, phục hồi, lưu trữ và tác động lên dữ liệu liên quan:
- Ngày sự kiện khác ngày ghi nhận/cập nhật thế nào, nếu có:

Loading, focus, selection và draft của một màn không tự là trạng thái domain. Dẫn chiếu [feature spec](feature-spec.md) và [experience](../experience.md) cho trạng thái tác vụ. Chỉ vẽ state diagram khi nhánh hoặc thứ tự khó hiểu bằng bảng.

## 6. Quan hệ và phạm vi sở hữu

| Quan hệ | Hai đầu và vai trò / hướng | Cardinality / optionality | Ownership / quy tắc khi đổi hoặc xóa | Rule |
| --- | --- | --- | --- | --- |
| […] | [ENT-01 → ENT-02 nếu thực sự có] | [0/1/n có nghĩa gì] | [cascade, ngăn xóa, giữ tham chiếu lịch sử… nếu chọn] | [BR-…] |

Nếu có tree/graph: định nghĩa loại edge, nhiều cha, chu trình, node rời và quan hệ chưa biết. Không coi thiếu edge là bằng chứng không có quan hệ. Nếu có quyền theo workspace/owner, định nghĩa ranh giới domain tại đây; cơ chế kiểm soát truy cập ở technical spec.

## 7. Thay đổi và bàn giao

| Thay đổi model/rule | Feature / dữ liệu bị ảnh hưởng | Có cần migration hoặc compatibility? | Owner / quyết định còn mở |
| --- | --- | --- | --- |
| […] | […] | [link technical spec / ADR-01] | […] |

**Exit condition:** thuật ngữ và identity của lát cắt đã thống nhất; mỗi rule có scope cùng ví dụ kiểm tra; transition/quan hệ có đường xử lý lỗi hoặc phần chưa biết được ghi rõ; feature và technical spec trỏ đúng revision. Không cần hoàn thiện domain ngoài scope để bàn giao.

- Bàn giao cho: [F-01 → feature spec], [technical spec], [validation plan](validation-plan.md).
- Câu hỏi chặn lát cắt: [vấn đề, owner, điều kiện giải quyết]; câu hỏi có thể hoãn: […].
- Criteria thực của dự án dùng để kiểm chứng: [C-001 hoặc APP-/LIF-/UTL-/WID-/PL-…]. ID `BR/ENT` phục vụ traceability bằng tài liệu; checker không tự xác minh các quan hệ này.

## Kiểm tra trước bàn giao

- [ ] Thuật ngữ và ENT phân biệt identity runtime với tên, vị trí list và ID tài liệu; đơn vị/null/unknown có nghĩa rõ.
- [ ] BR có phạm vi, ngoại lệ và ví dụ hợp lệ/vi phạm; chỉ định nghĩa tại nguồn đã đăng ký, không sao luật sang nhiều file.
- [ ] Lifecycle và quan hệ đã nêu điều kiện chuyển, tác động khi xóa/đổi và recovery phù hợp scope.
- [ ] Domain semantics được tách khỏi DB schema và UI state; thay model/rule đã dẫn tới feature/technical/migration liên quan.
- [ ] Đã đối chiếu exit condition, revision và criteria refs; câu hỏi còn mở có owner và chỉ chặn lát cắt phụ thuộc.
