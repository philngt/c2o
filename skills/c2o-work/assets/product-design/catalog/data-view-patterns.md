# Catalog data view

**C2O Design v1.2.0.** Xét các pattern theo [hợp đồng data view](../core/data-views.md). Đây chưa phải component code hay benchmark. `DVP-*` chỉ mẫu; dự án tạo instance `DV-01`, liên kết decision/baseline/layout.

## Chọn theo việc người dùng cần làm

| Pattern | Phù hợp khi | Cần giữ / khi nên xét lựa chọn khác |
| --- | --- | --- |
| **DVP-01 — Danh sách đối tượng** | Tìm, quét, chọn một đối tượng bằng vài dấu hiệu chính. | ID, nhãn, thông tin phân biệt và thứ tự có nghĩa. Nếu cần so nhiều trường giữa các đối tượng, xét table. Đừng giấu toàn bộ dấu hiệu nhận diện sau thao tác mở detail. |
| **DVP-02 — Bộ sưu tập card/media** | Hình, preview hoặc nội dung ngắn giúp nhận biết và chọn item. | Tên/ID, fallback, aspect/crop và thứ tự đọc. Card có thể xếp một hay nhiều cột; ảnh thiếu vẫn có nghĩa. Xét list/table khi ảnh chỉ trang trí hoặc cần quét giá trị chính xác. |
| **DVP-03 — Bảng so sánh** | Các đối tượng chia sẻ thuộc tính và người dùng cần so hàng/cột. | Header, đơn vị, ô thiếu, sort và hàng định danh. Control bên trong có hành vi riêng. Có thể giữ scroll có phạm vi; không bỏ cột cần cho task chỉ để vừa một frame. |
| **DVP-04 — Grid tương tác** | Task cần điều hướng ô, nhập/sửa nhiều ô, selection hoặc thao tác kiểu bảng tính. | Focus, chế độ điều hướng/sửa, validation, commit/undo và selection scope. Chi phí hành vi lớn hơn bảng đọc; không chọn chỉ vì có đường kẻ hoặc nhiều cột. |
| **DVP-05 — List–detail** | Người dùng cần chuyển giữa tập đối tượng và thông tin của đối tượng đang chọn. | Đây là composition: list/table có thể là vùng chọn. Đồng bộ ID, focus, draft và back; hẹp chuyển tuần tự khi phù hợp. Không coi click item mới là quyền bỏ draft. |
| **DVP-06 — Timeline/sự kiện** | Cần biết điều gì xảy ra trước/sau và nguồn của thay đổi. | Event identity, timestamp/múi giờ, loại sự kiện, người/nguồn ghi và thứ tự khi cùng thời điểm. Nếu cần đo xu hướng số, xét chart; khoảng cách thị giác không tự biểu thị thời lượng. |
| **DVP-07 — Calendar/agenda** | Quyết định phụ thuộc ngày, giờ, khoảng trống hoặc trùng lịch. | All-day/timezone/duration, quyền chỉnh, conflict và trạng thái lịch. Agenda là biến thể hữu ích khi cần đọc tuần tự; một log lịch sử không mặc nhiên cần ô lịch. |
| **DVP-08 — Board theo trạng thái** | Tác vụ là nhìn hoặc thay trạng thái của các item trong workflow. | Ý nghĩa cột, transition hợp lệ, quyền và kết quả lưu. Reorder khác đổi trạng thái; có thao tác thay thế kéo-thả. Xét list nếu cần quét xuyên nhiều cột hoặc trạng thái không có thứ tự. |
| **DVP-09 — Tree/outline** | Dữ liệu thực có quan hệ phân cấp dùng để tìm hoặc quản lý nhánh. | Parent/child, expand, selection, node lá và tải nhánh. Nếu một đối tượng có nhiều quan hệ hoặc nhiều cha, quyết định cách tham chiếu và chống trùng; đừng ép mô hình thành cây giả. |
| **DVP-10 — Network graph** | Câu hỏi cần thấy kết nối, đường đi hoặc nhiều loại quan hệ. | Node/edge có ID, type, hướng, confidence và nguồn; search/filter/focus/detail. Phân biệt không nối với chưa biết/đang lọc. Xét bảng quan hệ khi task chỉ cần tra vài liên kết cụ thể. |
| **DVP-11 — Metric/tóm tắt** | Một số hoặc tập nhỏ chỉ số giúp quyết định có hành động tiếp theo. | Định nghĩa, đơn vị, phạm vi, kỳ đo, mẫu số và so sánh. Cho đường tới dữ liệu giải thích khi cần. Không thêm KPI chỉ vì còn khoảng trống trên màn. |
| **DVP-12 — Biểu đồ** | Cần hiểu phân bố, độ lớn, thay đổi, thành phần hoặc tương quan. | Mark/scale/aggregation khớp câu hỏi; nhãn, nguồn, thiếu dữ liệu và cách đọc giá trị. Nếu task là tìm số chính xác hoặc sửa bản ghi, bổ sung hoặc chọn table/detail. |
| **DVP-13 — Bản đồ** | Vị trí, khoảng cách, vùng hoặc tuyến đường làm thay đổi quyết định. | Tọa độ/độ chính xác, loại địa lý, đơn vị, zoom/filter và đối tượng trùng vị trí. Có đường tìm/đọc nội dung ngoài thao tác với map. Xét danh sách theo địa chỉ khi vị trí không tạo giá trị. |
| **DVP-14 — Ma trận/heatmap** | Cần so giao điểm của hai chiều, như item × yêu cầu hoặc thời gian × nhóm. | Hai trục có nghĩa, ô không có quan hệ khác ô chưa biết, legend/đơn vị và đọc giá trị cụ thể. Màu chỉ hỗ trợ mã hóa; xét table thường nếu quan hệ hai chiều không cần thiết. |

Có thể phối hợp search + list–detail, table + summary, graph + detail, calendar + agenda. Giữ nguồn dữ liệu và quy tắc đồng bộ filter/selection; đổi view vẫn giữ thông tin cần cho task.

## Khi chọn chart

ONS đề nghị bắt đầu từ dữ liệu và quan hệ cần truyền đạt [nguồn](https://service-manual.ons.gov.uk/data-visualisation/chart-types/choosing-a-chart-type). Các câu hỏi sau giúp kiểm tra đề xuất của dự án:

| Câu hỏi | Lựa chọn có thể xét | Điều cần kiểm tra |
| --- | --- | --- |
| Nhóm nào lớn hơn? | [Bar](https://service-manual.ons.gov.uk/data-visualisation/chart-types/bar-charts) hoặc dot trên cùng scale | Đơn vị, sort, baseline và giá trị âm nếu có. |
| Đại lượng thay đổi thế nào? | [Line](https://service-manual.ons.gov.uk/data-visualisation/chart-types/line-chart) cho diễn tiến có ý nghĩa; column cho lượng theo kỳ | Khoảng thời gian, missing, đổi định nghĩa và cách tổng hợp. |
| Các phần đóng góp gì vào tổng? | Stacked hoặc một biểu diễn parts-of-whole phù hợp | Tổng/mẫu số, phần chưa phân loại, khả năng so phần cần quyết định. |
| Dữ liệu phân bố hoặc hai biến liên hệ thế nào? | Histogram hoặc scatter theo câu hỏi | Độ hạt/bin, outlier, missing và giới hạn suy luận. |

Đây là ứng viên, không phải mapping bắt buộc. Câu hỏi phải biện minh cho độ phức tạp; table hoặc lời giải thích có thể đủ dùng.

## Phân biệt hình thức và hành vi

Một bộ card xếp lưới không tự cần `role="grid"`. [APG Table](https://www.w3.org/WAI/ARIA/apg/patterns/table/) và [APG Grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/) mô tả các hợp đồng khác nhau; chọn sau khi biết cách người dùng di chuyển và thao tác. Native mapping theo profile của dự án, không chuyển nguyên ARIA role sang API native.

Không có ngưỡng số item/cột chung buộc phải dùng table, pagination hoặc virtualization. Chọn theo task, lượng dữ liệu thực, khả năng đọc, hiệu năng và công nghệ hỗ trợ; đo implementation khi quyết định phụ thuộc hiệu năng.
