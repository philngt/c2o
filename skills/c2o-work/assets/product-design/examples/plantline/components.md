# Plantline — Các component contract minh họa

**C2O Design v1.2.0.** Ba contract mô tả trách nhiệm để triển khai [layout](layout.md). Không có SwiftUI component, API, preview hoặc runtime test được tạo. Giữ [baseline B-01 revision 1](baseline.md), [data views](data-views.md) và PL-01…PL-08 ở **NOT_RUN**.

## CMP-01 — PlantRecordRow

Pattern tham khảo: **CP-14 Record row**; áp dụng vào DV-01 của slice.

**Trách nhiệm:** biểu diễn một cá thể trong DV-01 và cho chọn/mở đúng hồ sơ. Nhận ID, tên gọi, vị trí và selection hiện tại. [Component core](../../core/components.md) hướng dẫn kiểm tra semantics trước khi chọn control.

Anatomy theo L1-R3: tên, mã, vị trí; không thumbnail, không nút sửa con hoặc thao tác batch trong slice. Chiều cao tăng theo nội dung/cỡ chữ; mã cần đọc đủ. Nội dung và ngữ nghĩa selection không chỉ thể hiện bằng màu.

**Event:** yêu cầu chọn/mở `plantID`. Màn danh sách/detail giữ selection bằng ID và quyết định có được rời draft hay chưa. Row không giữ bản sao domain record có thể tự lưu và không tự chọn ID theo index.

**State áp dụng:** bình thường/được chọn; focus/pressed khi control/platform có. Trạng thái thiếu ảnh không tồn tại trên row vì thiết kế không dùng thumbnail. Loading/error của toàn bộ collection thuộc DV-01; không bắt mỗi row có spinner/error riêng.

**Kiểm tra cần làm:** hai cá thể cùng giống mở đúng ID; vùng chọn, tên truy cập, thứ tự đọc và nội dung dài/chữ lớn theo profile. PL-01/02/05/08 liên quan; chưa có kết quả.

## CMP-02 — LocationAndNotesFields

Composition tham khảo: **CP-07 Text field / text area**, dùng **CP-19 Field message** khi có hướng dẫn hoặc lỗi gắn với field. Không tạo thêm validation rule chỉ để dùng catalog.

**Trách nhiệm:** thu nhận hai giá trị draft trong L-02/edit. Nhận ID/tên chỉ đọc để đối chiếu theo layout, vị trí, ghi chú, trạng thái đang lưu và lỗi field nếu implementation có. Label ở ngoài trường; cả hai trường được phép trống.

Component phát ý định thay đổi field; màn điều phối giữ draft gắn với ID. Field không tự commit dữ liệu, đổi taxonomy hoặc tự hủy khi mất focus. Trạng thái focus có thể do control/view giữ theo conventions nền tảng; dirty/saving và dữ liệu đã lưu có owner ở màn/logic tác vụ.

**State áp dụng:** editing, focused, read-only/disabled theo logic lưu đã chọn; invalid chỉ khi có rule thực sự. Không tạo lỗi “bắt buộc” cho field vốn được phép trống. Lỗi persistence của toàn bản ghi không gán sai thành lỗi của một field.

**Adaptation:** form cuộn được khi bàn phím mở, text wrap, field/focus và action còn truy cập được. Không đặt chiều cao ghi chú cố định để giữ một mockup. Giới hạn độ dài chưa có trong brief; khi triển khai phải chốt theo dữ liệu thực và phản ánh vào criterion nếu cần.

**Kiểm tra cần làm:** draft giữ qua thao tác và lỗi; nội dung không ghi sang cây khác; chữ lớn/bàn phím/focus; PL-03/04/05/08. Chưa có preview hay test.

## CMP-03 — SaveAction

Pattern tham khảo: **CP-01 Button / command**; nhận trạng thái thao tác lưu từ owner của tác vụ.

**Trách nhiệm:** thể hiện hành động “Lưu thay đổi” và phát yêu cầu lưu. Nhận trạng thái tác vụ từ màn điều phối. Dùng control nền tảng có semantics của action; glyph nếu có chỉ hỗ trợ nhãn.

Button không tự xác nhận persistence hoặc hiện thông báo thành công ngay khi bấm. Màn/logic tác vụ mới quyết định commit, ngăn ghi chồng, cập nhật DV-01/DV-02 hoặc giữ draft và báo lỗi. Chưa chốt API/callback SwiftUI; đây là phân công trách nhiệm.

**State:** idle, saving nếu quá trình có khoảng chờ cần phản hồi; điều kiện tương tác phụ thuộc tác vụ đang chạy. Không dựa chỉ vào spinner để ngăn gửi trùng. Hành động retry sau lỗi không xóa draft. Quy tắc disable khi chưa thay đổi chưa được nêu trong baseline; không tự thêm nó như yêu cầu đã thống nhất.

**Kiểm tra cần làm:** không báo thành công trước commit, không tạo ghi chồng, lỗi còn nội dung đã sửa, nhãn/focus/hit region theo profile; PL-03/04/05/08. Các kết quả đều chưa chạy.

## Reuse và variant

Hợp đồng tương tự của dự án được ưu tiên tái sử dụng. Một row có thumbnail trong O-02 chưa được chọn, nên không thêm variant đó vào implementation của ví dụ. Trường đọc và trường sửa không nên bị gộp chỉ vì cùng một giá trị nếu semantics khác; screen có thể dùng component phù hợp cho từng mode.

Các số CMP là instance trong ví dụ. Catalog CP mô tả family tham khảo, không đồng nghĩa đã có implementation dùng được. Xem [catalog](../../catalog/components.md) và [composition map](ui-composition.md).
