# Chuẩn template C2O — 1.0.0

Chuẩn cấu trúc 1.0.0 này quy định cách **author và kiểm tra source của 24 mẫu catalog Markdown** trong `templates/` và `templates/product/`. Hợp đồng 12 trường metadata giữ nguyên; bản tích hợp C2O nâng từng template lên 1.1.0 để làm rõ ngữ nghĩa tùy chọn. Khi làm dự án, có thể dùng section hữu ích hoặc artifact hiện có mà không sao metadata, tạo index, `.design`, JSON, lifecycle hay migration format. Chỉ giữ thông tin thay đổi hành động/kiểm chứng. Chất lượng sản phẩm vẫn cần kiểm tra theo hợp đồng C2O và nguồn acceptance/evidence đã chọn.

[Registry](template-registry.json) giữ ID, đường dẫn, nhóm và phiên bản của từng mẫu. [Traceability](traceability.md) giữ nghĩa của ID sản phẩm và ownership theo chủ đề. [Hệ thống tài liệu](README.md) giúp chọn mẫu cần dùng. Khi có tài liệu tương đương trong dự án, dùng tài liệu đó và bổ sung phần còn thiếu.

## 1. Phạm vi chuẩn

| Artifact | Hợp đồng áp dụng |
| --- | --- |
| 24 Markdown template trong registry | Metadata chung, nội dung chuyên biệt, kiểm tra trước bàn giao theo tài liệu này |
| Nội dung dùng trong dự án | Tùy chọn dùng toàn mẫu, một section hoặc artifact tương đương; giữ provenance/scope hữu ích, không bắt metadata đủ 12 hàng hay format migration |
| Hai example product pack Lifestyle/Utility | Minh họa metadata đã điền và nội dung khớp source; vẫn là `draft`, không có native test hoặc nghiên cứu khách hàng |
| Ví dụ Plantline cũ | Ví dụ lịch sử; giữ IDs và ý nghĩa hiện có, không yêu cầu đổi hình thức chỉ để nâng framework |
| `project.json`, verification JSON | Chỉ profile JSON được chọn rõ: giữ schema version `1.0` và [evidence profile](../core/evidence.md); không thêm metadata Markdown hoặc thay authority C2O |
| Catalog, category/platform recipe, SwiftUI starter | Giữ hợp đồng riêng cho pattern, nền tảng và source; ngoài phạm vi validator Markdown |

Chuẩn hóa ở đây không có nghĩa mọi tài liệu có cùng nội dung, mọi app dùng cùng bố cục, hay toàn bộ pattern đã được code. Mẫu component phải nói rõ events/state owner; mẫu business phải nói rõ giả thuyết/giá trị; mẫu release phải nói rõ artifact và vận hành.

## 2. Cấu trúc chung

Mỗi source template trong catalog có một H1, sau đó là H2 đầu tiên **Hợp đồng tài liệu**, phần thân chuyên biệt, và H2 cuối **Kiểm tra trước bàn giao**. Giữ heading/anchor của phần thân khi sửa mẫu để hạn chế làm gãy liên kết.

Metadata của source template catalog dùng một block bảng liên tục `Thuộc tính | Giá trị`, đủ 12 hàng theo thứ tự sau. Sau bảng đặt liên kết inline Markdown có nhãn tới chuẩn này; giữ liên kết thật, không đặt trong code:

| Trường | Cách điền |
| --- | --- |
| Template ID | ID ổn định của mẫu trong registry, ví dụ `TPL-COMPONENT`; nhiều component dự án có thể dùng cùng template ID |
| Phiên bản template | Phiên bản của mẫu, hiện `1.1.0` trong catalog tích hợp; bản cũ `1.0.0` vẫn có provenance riêng |
| Mục đích | Câu hỏi hoặc quyết định tài liệu giúp giải quyết |
| Dùng khi | Tình huống thực sự cần tài liệu; sự tồn tại của mẫu không làm nó bắt buộc |
| Đầu vào | Nguồn đang có cần đọc; phân biệt nguồn dự án với catalog, ví dụ hoặc template tham khảo |
| Đầu ra / bàn giao | Người hoặc bước tiếp theo nhận được gì và dùng để làm gì |
| Nguồn chuẩn | Chủ đề/section tài liệu có thể sở hữu và những nguồn phải tham chiếu; chỉ có hiệu lực khi được đăng ký cho scope |
| Owner | Người/vai trò chịu trách nhiệm cập nhật; nếu chưa gán, ghi rõ và nêu tác động tới việc tiếp theo |
| Revision tài liệu | Revision của bản tài liệu trong dự án, hoặc commit/tag theo quy ước dự án |
| Ngày cập nhật | Ngày thay đổi revision thực, dạng `YYYY-MM-DD`; không tự đổi ngày chỉ vì mở file |
| Trạng thái tài liệu | `draft`, `reviewed`, `accepted` hoặc `superseded`, phản ánh điều đã xảy ra |
| Phạm vi áp dụng | Dự án/task/release, feature/screen/platform hoặc giới hạn cần thiết; dẫn IDs thật khi đã có |

Ví dụ `TPL-COMPONENT / 1.1.0` mô tả nguồn mẫu; `CMP-03 / revision 4` mô tả component của dự án; C2O Design `1.5.0` mô tả gói framework. Ba phiên bản này thay đổi độc lập. Template ID không thay `CMP`, `SCR`, `BR`, `REQ` hoặc acceptance ID.

Trong template nguyên bản, owner/revision/ngày/scope là placeholder và document status là `draft`. Nội dung gợi ý không được coi là dữ kiện. Khi dùng nội dung trong dự án, chỉ giữ section và metadata hữu ích; thay placeholder ảnh hưởng đến phần việc tiếp theo, ghi giả định hoặc điều kiện giải quyết khi cần. Có thể ghi ngoài scope kèm lý do, nhưng không dùng cách này để bỏ yêu cầu đã cam kết.

## 3. Phần thân chuyên biệt

Phần thân phải đủ để người nhận thực hiện bước tiếp theo mà không phải đoán quyết định quan trọng. Không ép cùng một bộ tiêu đề cho mọi loại tài liệu.

| Nhóm | Thông tin cần giữ |
| --- | --- |
| Business/blueprint/PRD | Người dùng và outcome, căn cứ/giả định, phạm vi và ưu tiên; blueprint dẫn scope, không định nghĩa scope cạnh tranh |
| Domain/feature/technical | Nghĩa dữ liệu và invariant; hành vi/nhánh lỗi; interface, persistence và ownership, mỗi chủ đề có nguồn riêng |
| Experience/layout/screen | Tác vụ, thứ tự thông tin, vùng nội dung/hành động/cuộn, UI state và adaptation theo không gian/nền tảng |
| Component/data view/asset | Dữ liệu/content, semantics, state/event/owner, nguồn và biến thể, fallback và cách kiểm chứng |
| Options/decision/baseline/direction | Các lựa chọn thực, căn cứ/đánh đổi, lựa chọn hiện hành, quy ước dùng lại và điều kiện xem lại |
| Validation/review | Kế hoạch khác với quan sát đã có; criteria/results dẫn đúng nguồn acceptance/evidence đã chọn, evidence nêu inputs và giới hạn |
| Delivery/release/service | Slice và dependency; build/artifact/vận hành; touchpoint/handoff thật khi có con người/dịch vụ phía sau |

Với behavior/UI, xét happy path và trạng thái lỗi/rỗng/loading/cancel/retry/permission/offline khi thực sự áp dụng. Với dữ liệu, phân biệt thiếu, chưa biết và 0. Với business, không tạo market size, doanh thu hoặc nghiên cứu giả để lấp bảng. Với source starter, chỉ ghi đúng phần source đã có và phần runtime chưa kiểm chứng.

## 4. Một nguồn chuẩn cho mỗi chủ đề

`Nguồn chuẩn` trong metadata mô tả trách nhiệm của mẫu; nó không tự chuyển ownership khi được sao chép. Xác định file/section/revision đang áp dụng ở context hoặc nguồn hiện hữu; chỉ dùng document index/bảng index nếu việc tìm và handoff cần nó. Một tài liệu có thể là canonical cho một chủ đề và chỉ là summary cho chủ đề khác.

- PRD giữ scope phiên bản và `REQ`; brief giữ phạm vi task trong phiên bản đó.
- Domain giữ `ENT` và `BR`; feature dẫn rule, giữ behavior; experience/screen giữ UI state và owner.
- Baseline/contract giữ quy tắc UI; decision/ADR giữ lý do lựa chọn; delivery/backlog giữ scope của `SL`.
- Acceptance và kết quả nằm ở nguồn đã chọn của C2O/dự án, như hội thoại, `.context/acceptance.md` hoặc hệ thống native. Chỉ profile JSON tùy chọn dùng các trường `id/title/required/allow_not_applicable` và report JSON theo [evidence](../core/evidence.md); không tự chuyển ownership khi sao mẫu.
- Validation plan giữ cách kiểm tra; review có thể giữ quan sát chi tiết làm evidence, nhưng bảng status tóm tắt phải dẫn record gốc.

Khi tách một section của pack thành tài liệu riêng, đăng ký nguồn mới và thay phần cũ bằng link có revision phù hợp. Không để cả hai bản tiếp tục tự định nghĩa cùng rule. Khi có mâu thuẫn, giải quyết tại owner/nguồn đang áp dụng; không dùng quy tắc “file mới nhất thắng”.

## 5. Trạng thái và mức hoàn thành

| Hệ trạng thái | Ý nghĩa |
| --- | --- |
| Lifecycle tài liệu, nếu cần: `draft / reviewed / accepted / superseded` | Đang soạn; đã có review thực; đã chọn dùng trong quyền hiện có; đã bị thay thế; có thể giữ quy ước dự án |
| Nhãn lựa chọn cũ: `proposed / selected / superseded` | Mô tả lựa chọn cục bộ nếu dùng; giữ trạng thái và căn cứ chấp nhận/delegation của quyết định C2O hiện hữu |
| Nhãn critique cũ: `ready / rework / blocked` | Khuyến nghị có phạm vi nếu dùng, không thay task progress hoặc verdict C2O |
| Verification C2O: `pass / partial / fail / not-tested` | Kết quả theo criterion tại nguồn acceptance/evidence hiện hữu |
| Profile JSON tùy chọn: `NOT_RUN / BLOCKED / PASS / FAIL / NOT_APPLICABLE` | Chỉ có nghĩa trong profile đã chọn; không mã hóa `partial` và không được đổi partial thành PASS |

Không có chuyển trạng thái tự động giữa các loại thông tin; không phải tác vụ nào cũng cần các trường lifecycle hoặc nhãn cũ. Giữ riêng task progress, artifact verification và external delivery. Một review có thể hoàn thành với subject fail; một slice đạt không hoàn thành commitment lớn hơn. `reviewed` cần ghi ai/vai trò nào đã review phần nào, khi nào, với nhận xét/giới hạn ở đâu. `accepted` cần chỉ rõ scope/revision được dùng và căn cứ lựa chọn trong quyền đang có. Có thể giữ `draft` cho phần đang thử nghiệm và đánh dấu phần phụ thuộc còn mở; không cần tạo một vòng phê duyệt mới. `superseded` dẫn tới nguồn/revision thay thế.

## 6. Kiểm tra trước bàn giao

Mỗi source template catalog kết thúc bằng checklist từ bốn tới sáu mục, chưa tick. Nội dung dùng trong dự án không bắt buộc giữ checklist; nếu dùng, chỉ tick điều đã đối chiếu thật. Điều kiện chuyên biệt có thể được viết trong body và tham chiếu từ checklist, không cần chép hai lần. Một pack gộp có thể dùng một metadata block nếu hữu ích; không bắt metadata ở dự án, và không lặp bảng 12 trường cho từng section.

Một tài liệu đủ để bàn giao **phần việc cụ thể** khi scope và owner rõ; nguồn chuẩn/refs có thể tìm được; người nhận có đủ quyết định/đầu vào để thực hiện; giả định hoặc blocker có owner và bước xử lý; kết luận không vượt bằng chứng. Phần chưa rõ chỉ chặn phần việc phụ thuộc nó. Checklist hoàn thành không tự chuyển document status, không tạo app pass hoặc quyền publish.

## 7. Dùng nhẹ hoặc tách sâu

| Nhu cầu | Cách áp dụng |
| --- | --- |
| `quick`: sửa hẹp trong dự án đang có | Bổ sung section còn thiếu vào brief/spec thật; giữ quy ước hiện hữu, không ép reformat toàn repo |
| App nhỏ, flow đầu tiên | Context/brief hiện có hoặc section cần thiết của [product pack](../templates/product/product-pack.md); không bắt index, metadata hay JSON |
| `standard`: nhiều feature hoặc nhiều owner | Tách tài liệu theo ownership/lifecycle khi hữu ích; chỉ dùng index nếu cần nối nhiều nguồn |
| `deep`: bất định hoặc thay đổi khó đảo ngược | Thêm giả thuyết, phương án, thử nghiệm và evidence phù hợp; không thêm tài liệu chỉ vì có mẫu |

`quick / standard / deep` trong bảng là nhãn độ sâu lịch sử, không phải mode phải chọn/lưu hoặc thay mức can thiệp C2O. Chọn một mẫu không chọn sẵn thương hiệu, layout hay database. Lifestyle/Utility cung cấp hướng app; iPhone/iPad/macOS/widget có recipe riêng. Cùng outcome và rules có thể dẫn tới bố cục khác nhau theo tác vụ, dữ liệu và khả năng nền tảng.

## 8. Sao chép và nâng cấp

1. Đọc tài liệu/code đang có, xác định topic còn thiếu. Chọn đúng mẫu từ registry hoặc dùng section tương đương.
2. Tái sử dụng artifact hiện hữu hoặc sao section/mẫu cần thiết nếu việc lưu có ích. Giữ provenance, scope và IDs có ích; không bắt metadata đủ 12 hàng và không thay IDs sản phẩm đang dùng.
3. Sửa link template thành nguồn dự án hoặc đường dẫn framework thật. Link tới một template chỉ là reference, không phải spec đã được chọn.
4. Điền phần cần cho scope; ghi ngoài scope/chưa biết có lý do. Xác định nguồn đang có hiệu lực và các view tham chiếu trong context hiện hữu; không bắt index mới.
5. Review nội dung và links theo phạm vi; chỉ dùng lifecycle/checklist khi hữu ích, không tạo gate mới. Kết quả đi vào nguồn acceptance/evidence hiện hữu. Review-only báo finding mà không sửa artifact; production sửa trong quyền đã có.

Nâng từ v1.4 không cần thay nội dung đúng, renumber IDs, reset report hoặc viết lại lịch sử. Thêm thông tin handoff có ích khi sửa tài liệu liên quan; metadata vẫn tùy chọn cho dự án; hai example packs trong bản này minh họa migration. Giữ các heading cũ được người khác liên kết. Nếu đổi vị trí/heading, cập nhật inbound refs cùng thay đổi.

Phiên bản template tăng patch khi sửa câu chữ không đổi nghĩa; minor khi thêm hướng dẫn/field tùy chọn; major khi thay field bắt buộc hoặc đổi trách nhiệm làm bản cũ không còn đáp ứng hợp đồng. Chuẩn chung có version riêng. Chỉ nâng revision tài liệu dự án khi thực sự sửa nó; không coi việc nâng framework là đã review lại mọi tài liệu.

## 9. Kiểm tra cấu trúc tự động

Từ thư mục framework:

```bash
python3 tools/template_check.py --root .
```

Tool đọc registry và 24 source mẫu catalog, kiểm tra coverage, ID/đường dẫn/phiên bản không trùng hoặc lệch, một H1, vị trí hai H2 chung, đúng 12 metadata fields có giá trị, `draft` mặc định, liên kết chuẩn và checklist bàn giao chưa tick. Đây là hợp đồng authoring catalog, không áp đặt format lên artifact/section của dự án. Exit `0` / `TEMPLATES_VALID` chỉ kết luận **cấu trúc template** đạt; exit `2` / `TEMPLATES_INVALID` ghi lỗi cần sửa. Tool chỉ đọc, không thay file hoặc status.

Tool không kiểm chứng chất lượng business/design, nghĩa của mọi liên kết/ID, tính đầy đủ của body, tài liệu đã điền của dự án, hoặc native runtime. Các link nội bộ và nội dung vẫn cần review theo phạm vi. [Evidence checker](../tools/README.md) là công cụ riêng, không được đổi kết luận thành app pass từ kết quả template check.
