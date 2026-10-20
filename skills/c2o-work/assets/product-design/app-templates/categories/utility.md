# Utility — blueprint theo tác vụ

**C2O Design v1.3.** Mục tiêu là đưa người dùng từ đầu vào đến kết quả sử dụng được, với quy tắc rõ và đường phục hồi ngắn. Blueprint cung cấp lựa chọn thiết kế; feature Conditional không được xem là đã triển khai.

## 1. Utility trong framework và Utilities trên App Store

Tên nhóm nội bộ là **Utility**; category chính thức của Apple là **Utilities**, dành cho app giúp giải một vấn đề hoặc hoàn thành một tác vụ cụ thể. Khi phát hành, một app tra cứu, quản lý tài liệu hoặc xử lý văn bản cũng có thể cần cân nhắc category khác tùy chức năng cốt lõi. Xem [Apple — Choosing a category](https://developer.apple.com/app-store/categories/). Không suy ra rằng mọi utility cần calculator UI, timer, dashboard hoặc hàng loạt công cụ trên một màn.

Chọn **một đầu ra có giá trị** trước: văn bản đã xử lý, thông tin tra cứu đúng, tài liệu đã lưu, hoặc thời gian đã đo. Xác định người dùng làm gì với đầu ra đó rồi mới chọn navigation và module. Mức **Core / Conditional / Optional** theo [module matrix](../module-matrix.md), không theo số feature muốn trưng bày.

## 2. Archetype và pattern phù hợp

| Archetype | Tác vụ và dữ liệu | Data view / layout | Screen / component |
| --- | --- | --- | --- |
| **Input → process → result** | Nhập giá trị, chạy phép biến đổi, hiểu và dùng kết quả; input và output có contract riêng | `DVP-11` cho số đo có nghĩa; text result dùng label–value/text; `LP-01/10`, `LP-08` nếu cần đối chiếu trước/sau | `SP-03/02`; `CP-07/12` input, `CP-01` command, `CP-15` result, `CP-19/24` recovery |
| **Reference / search** | Đặt query, chọn đúng entry, xem nguồn và phạm vi câu trả lời | `DVP-01/05`; `DVP-09` nếu taxonomy thật là cây; `LP-02` | `SP-01/02`; `CP-27`, `CP-14`, `CP-15/17`; không mặc định có tài khoản hoặc lịch sử |
| **File / document workbench** | Mở/import file, xem/sửa, lưu/export đúng phiên bản | `DVP-01/05`; preview theo loại nội dung; `LP-02/03` | `SP-01/02/03`; `CP-04/13/19/22/25`; tiến độ chỉ khi có tiến trình thật |
| **Timer / time tracking** | Đo một khoảng thời gian hoặc ghi session khi thời gian là tác vụ chính | `DVP-11` elapsed/remaining; `DVP-06` session history nếu cần; `LP-01` | `SP-02/03`; `CP-01/12/18`; các state idle/running/paused/completed phải được định nghĩa |

Tham chiếu [components](../../catalog/components.md), [data views](../../catalog/data-view-patterns.md), [layouts](../../catalog/layout-patterns.md) và [screens](../../catalog/screen-patterns.md). Một ô hiển thị word count là metric có scope; nó không khiến cả app trở thành dashboard. Không dùng chart chỉ để trang trí kết quả của một phép biến đổi.

## 3. Lát cắt starter: normalize / count text

**Phạm vi starter được chọn:** nhập văn bản, normalize/count, xem kết quả; local history chỉ lưu khi người dùng opt in; Settings và Help. iPhone dùng stack, iPad/macOS dùng split; source widget chỉ đọc summary và deep link, được đưa vào target khi bật `--widgets`. Auth, cloud, IAP và permission request không nằm trong starter. Các mục này là scope để kiểm chứng, chưa phải native `PASS`.

### Contract xử lý văn bản

Trước khi dùng kết quả làm thông tin đáng tin, ghi rõ trong dự án:

1. **Normalize thay đổi gì?** Ví dụ trim đầu/cuối, đổi kiểu xuống dòng hoặc gộp khoảng trắng là những phép khác nhau. Unicode normalization, đổi hoa/thường và bỏ dấu là những lựa chọn riêng; không tự gộp dưới một nút mà không giải thích.
2. **Count đếm đơn vị nào?** Ký tự người dùng nhìn thấy, Unicode scalar, byte, token và word không đồng nghĩa. Chốt quy tắc word boundary, newline, dấu câu và input chỉ có khoảng trắng; nhãn kết quả khớp thuật toán thật.
3. **Kết quả dựa vào input nào?** Input gốc, normalized output hay cả hai phải được ghi rõ. Sửa input sau khi chạy cần làm kết quả cũ dễ nhận biết, hoặc tính lại theo hành vi đã chọn.
4. **Dữ liệu giữ ở đâu?** Input đang soạn, output hiện tại và history là ba vòng đời khác nhau. Opt in history phải nói rõ lưu từ lúc nào, giữ phần nào và cách xóa. Không suy ra “local” nghĩa là có backup, đồng bộ hoặc không bao giờ xuất hiện trong bản sao lưu thiết bị.
5. **Giới hạn và thất bại?** Nếu có giới hạn độ dài, định nghĩa theo đơn vị thật và giải thích trước khi mất input. Việc xử lý đồng bộ không cần spinner giả; tác vụ tốn thời gian mới cần progress/cancel phù hợp.

**Quy tắc cụ thể được chọn trong starter:** `TextTools.normalizedWhitespace` tách theo `Character.isWhitespace`, rồi nối bằng một dấu cách; vì thế khoảng trắng đầu/cuối bị bỏ, khoảng trắng liên tiếp và xuống dòng đều bị gộp. Statistics dùng Swift `String.count` cho extended grapheme clusters; words là các đoạn phân cách bằng whitespace, không phải tokenizer ngôn ngữ. Lines đổi CRLF/CR thành LF rồi tách dòng: input rỗng có 0 dòng, newline ở cuối tạo thêm một dòng rỗng. Nhãn UI phải ghi rõ số đếm đang áp dụng cho input hay normalized output.

Local history mặc định tắt. Khi bật, preset starter giữ tối đa **50 lần xử lý gần nhất** và cần nói rõ giới hạn trong UI; đây là lựa chọn của starter, không phải ngưỡng chung cho Utility. Việc giữ/xóa bản cũ khi đạt giới hạn thuộc acceptance của retention. Các quy tắc source này vẫn cần test và native evidence cho flow sử dụng chúng.

### Cấu trúc màn

| Vùng/màn | Trách nhiệm | Pattern và quy tắc |
| --- | --- | --- |
| **Text tool** | Nhập và xử lý một đoạn văn bản | `SP-03`, `LP-01`, `CP-07/01/19`; label input rõ, không tự đọc clipboard |
| **Result** | Hiểu output và count đúng scope | `SP-02`, `CP-15`, `DVP-11`; cùng flow trên vùng hẹp, có thể đối chiếu input/output trên vùng rộng bằng `LP-08` |
| **History** | Mở lại những kết quả đã được phép lưu | `SP-01/02`, `DVP-01/05`, `CP-14/24`; chỉ có record khi opt in và thao tác lưu theo contract thật |
| **Settings / Help** | Đổi history preference, giải thích phép xử lý và dữ liệu lưu | `SP-07/08`, `CP-09/15/02`; phân biệt ngừng lưu tương lai và xóa lịch sử đã có |

Trên iPad/macOS, split phục vụ lựa chọn công cụ/mục hoặc history và nội dung đang làm. Không chia thành nhiều pane chỉ để dùng hết chiều rộng. Trên iPhone, quay lại không được vô tình thay input bằng history khác; khi có draft đang sửa phải định nghĩa hành vi mở một record cũ.

### Flow đầu đến cuối

| Luồng | Kết quả mong đợi | Điều cần giữ đúng |
| --- | --- | --- |
| Nhập → normalize/count → đọc output | Kết quả và nhãn count khớp contract | Input gốc không bị mất ngoài ý muốn; người dùng phân biệt nguồn và kết quả |
| Đổi input → xử lý lại | Kết quả thuộc phiên input hiện tại | Không hiển thị output cũ như thể vừa tính cho input mới |
| Opt in history → xử lý → mở lại record | Lưu và mở đúng dữ liệu đã được cho phép | Dùng identity ổn định; thứ tự và thời gian có nghĩa; không ghi dữ liệu trước opt in trái mô tả |
| Tắt history hoặc xóa history | Tác động đúng phạm vi được mô tả | “Tắt lưu tiếp” và “xóa đã lưu” là hai ý định riêng; cần chọn chính sách rõ |

Copy/share có trong scope source starter và cần xác minh dùng đúng output hiện tại. Export file, xử lý batch hoặc thêm công cụ là **Conditional**; chỉ thêm vào acceptance khi được chọn cho nhiệm vụ. Thao tác Copy không tự thay đổi history preference.

## 4. State contract

| Trạng thái | Hành vi cần định nghĩa |
| --- | --- |
| **Input empty** | Cho biết cần nhập gì; xác định output/count cho chuỗi rỗng hoặc khi nào action chưa khả dụng. `0` hợp lệ không bị thay bằng “unknown” |
| **History empty / disabled** | Tách “chưa lưu record” khỏi “đang tắt history”; hành động opt in có mô tả phạm vi, không bật âm thầm |
| **Invalid / error** | Thông báo lỗi theo field hoặc thao tác; giữ input để sửa; output cũ không bị nhận là kết quả thành công mới |
| **Draft** | Input đang soạn có vòng đời rõ khi chuyển màn, mở history hoặc đóng app; persistence của draft là quyết định riêng với history |
| **Privacy** | Không lưu history trước lựa chọn của người dùng; mô tả local retention thật. Không tự thêm analytics, network upload hoặc hiển thị raw text trên widget |
| **Permission** | Starter không yêu cầu quyền. File picker, camera, microphone, notification hoặc tài nguyên khác chỉ xuất hiện khi feature thực sự sử dụng chúng, với flow deny/cancel phù hợp |
| **Loading / long-running** | Chỉ thêm khi có khoảng chờ thật; công bố scope xử lý, cancel/retry nếu khả thi; không để progress đánh lạc hướng về thao tác đã hoàn tất |

## 5. Blueprint Conditional cho archetype khác

- **Reference / search:** xác định corpus, ngôn ngữ, nguồn, freshness, query và thứ tự kết quả. Core là query → results → entry → quay lại query; phân biệt no results, lỗi nguồn và dữ liệu chưa tải. Favorites/history/offline download chỉ thêm khi cần. Kết quả tra cứu không trở thành sự thật đã kiểm chứng chỉ vì có layout đẹp.
- **File / document workbench:** xác định loại file, quyền sửa, bản gốc/bản đang sửa và đích lưu. Core là chọn → mở → thao tác → lưu/export → mở lại đúng kết quả. Định nghĩa cancel import, unsupported/corrupt file, thiếu quyền, lưu thất bại và unsaved changes. Không dùng tên file làm identity duy nhất hoặc báo export thành công khi file chưa được tạo.
- **Timer / time tracking:** chỉ chọn khi đo thời gian là mục tiêu thật. Chốt count up/count down, pause/resume/reset, tác động khi app không ở foreground, thay đổi đồng hồ và khôi phục state. Notifications, Live Activities, session history và App Intents là Conditional; mỗi tính năng cần behavior và target cụ thể, không được suy ra từ việc có số đếm trên màn.

## 6. Widget theo nhiệm vụ

**Khi bật `--widgets`:** read-only summary và deep link mở app. Snapshot chỉ chứa count/status phù hợp với history preference; không chứa raw input/output hoặc draft. Quyết định cuối về status hay số history phải khớp implementation. Phân biệt snapshot chưa tồn tại, lỗi đọc, history đang tắt và số record thực sự bằng 0; không khuyến khích bật lưu chỉ để lấp chỗ trống. Cần quan sát refresh thực, không hứa thời điểm cập nhật chính xác.

Với archetype khác, widget có thể mở một reference đã chọn, tài liệu gần đây được phép hiển thị hoặc summary của timer. Đây là biến thể Conditional. Tác vụ đang diễn ra, cập nhật theo thời gian và thao tác trực tiếp cần contract riêng; read-only widget hiện tại không chứng minh app có Live Activity, timer nền hay shortcut action.

## 7. Acceptance mẫu để đưa vào dự án

Các mã `UCASE-*` là case mẫu, map sang criterion hiện có của dự án như `C-001`. Chưa chạy thì giữ `not-tested` trong C2O (`NOT_RUN` chỉ trong profile JSON tùy chọn); chốt expected output theo thuật toán thật trước khi chạy.

| Case | Input và thao tác | Kết quả cần quan sát |
| --- | --- | --- |
| `UCASE-01` Text contract | Chuỗi rỗng, khoảng trắng, tiếng Việt có dấu, emoji, nhiều dòng | Normalize và count đúng định nghĩa; không suy expected từ chính hàm đang được test |
| `UCASE-02` Result identity | Xử lý A, đổi thành B, xử lý lại | Output/count gắn với input đúng; draft và output cũ không bị đánh tráo |
| `UCASE-03` Opt in / retention | Cài mới → xử lý → kiểm tra history → bật history → xử lý tiếp và qua giới hạn đã chọn | Không lưu trước opt in; lưu đúng payload/thứ tự/thời điểm; giữ tối đa 50 recent runs đúng preset và mô tả UI |
| `UCASE-04` History lifecycle | Mở record cũ khi có input đang soạn; tắt lưu; xóa history | Hành vi draft rõ; tắt/xóa có phạm vi đúng; app và summary không tham chiếu record đã xóa |
| `UCASE-05` Adaptation | Input dài, chữ lớn, keyboard và VoiceOver trên target đã chọn | Input/output đọc và thao tác được; split/stack giữ ngữ cảnh; error được nhận biết |
| `UCASE-06` Widget / privacy | History tắt, rỗng, có dữ liệu; mở widget link | Summary đúng scope, không lộ raw text ngoài contract; route mở được; ghi nhận refresh thực |

Áp dụng [nguyên tắc](../../core/principles.md), [data-view contract](../../core/data-views.md) và [quy tắc evidence](../../core/evidence.md). ID catalog được review bởi người/agent; checker không tự xác nhận thuật toán, native behavior hay tính phù hợp của category.
