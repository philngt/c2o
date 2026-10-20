# Plantline — Đề xuất L-01 và L-02

> Bố cục bằng mô tả cho **O-01 → DEC-01 → B-01 revision 1**. Được chọn để hoàn thiện ví dụ, chưa phải wireframe đo được hay UI đã chạy. PL-01…PL-08: **Proposed / NOT_RUN**.

Nguồn chuẩn: [brief](brief.md), [fixture/flow/state](experience.md), [baseline](baseline.md), [direction](design-direction.md), [asset brief](asset-brief.md). Theo [hướng dẫn layout](../../core/layout.md), ưu tiên tác vụ và dữ liệu trước trang trí. Tên dài, trường trống, chữ lớn, bàn phím và thiếu ảnh đều phải có chỗ trong cấu trúc.

## L-01 — Danh sách

Thứ tự đọc: tên bộ sưu tập → tìm kiếm → các hàng cây. Mỗi hàng là một đích mở hồ sơ, không gom nhiều cây cùng giống thành một hồ sơ.

| Vùng | Nội dung và hành động | Cuộn/co giãn |
| --- | --- | --- |
| L1-R1: navigation | Tiêu đề “Bộ sưu tập”. Không có nút thêm cây vì chưa thuộc slice. | Theo navigation nền tảng; không tự dựng thanh cố định che nội dung. |
| L1-R2: tìm kiếm | Nhãn/gợi ý “Tìm theo tên hoặc mã cây”; giữ query khi vào rồi quay lại chi tiết; có xóa query. | Gắn với danh sách bằng cơ chế tìm kiếm nền tảng; kiểm tra khả năng truy cập khi cuộn/chữ lớn. |
| L1-R3: kết quả | Mỗi hàng: tên → mã → vị trí. `PLT-014` hiện “Monstera bàn làm việc”, `PLT-014`, “Kệ đông”. Toàn hàng mở đúng ID; selected state có ngữ nghĩa cho AT. | Vùng chính cuộn dọc. Tên/vị trí wrap; mã còn đọc đầy đủ. Không thumbnail, không cuộn ngang để đọc hàng. |
| L1-R4: thay thế kết quả | Kho rỗng: “Chưa có cây nào.” Query không khớp: “Không tìm thấy cây phù hợp.” và hành động xóa tìm kiếm. | Nằm trong vùng nội dung, không overlay che query; không cần A-02 để hiểu trạng thái. |

`PLT-027` vẫn là hàng riêng dù cùng giống; không tự bổ sung tên/vị trí chưa có trong fixture. Không có mạng không đổi bố cục và không chặn tìm dữ liệu cục bộ.

## L-02 — Chi tiết và sửa

### Trạng thái đọc

| Vùng | Nội dung và hành động | Thứ tự/co giãn |
| --- | --- | --- |
| L2-R1: định danh/hành động | Tên đầy đủ, mã cá thể; **Sửa hồ sơ**. Hẹp có đường quay lại list; rộng giữ selection ở list. | Định danh nằm đầu nội dung; hành động ở toolbar phù hợp nền tảng. Không ép toàn bộ header phải luôn nổi. |
| L2-R2: thông tin đang dùng | **Vị trí**, **Ghi chú**, hiển thị đầy đủ. Đề xuất copy khi trống: “Chưa ghi vị trí”, “Chưa có ghi chú”. | Hai mục xếp dọc, cuộn cùng nội dung. Không ép ghi chú vào ô cao cố định. |
| L2-R3: taxonomy | Loài, giống và “Theo nhãn người bán, chưa xác minh”. | Nhóm riêng, giữ nhãn dài; không biến tên giống thành tiêu đề cá thể. |
| L2-R4: nguồn gốc | Với fixture: “Giâm cắt”; “Cây nguồn: PLT-003”; “Chủ bộ sưu tập ghi nhận”. Dữ liệu chưa biết dùng copy trong experience. | Tóm tắt dạng chữ; không dựng pedigree. Mã cây nguồn chưa trở thành link nếu đích điều hướng chưa được triển khai. |
| L2-R5: ảnh tùy chọn | A-01: ảnh thật của chính cá thể nếu hồ sơ cục bộ đã có. Thiếu: “Chưa có ảnh cá thể”. Đọc lỗi: “Không đọc được ảnh cá thể”. | Sau các nhóm chính, trong luồng cuộn. Fit bảo toàn nội dung nhận diện; không kéo méo. Crop/focal point phải xem trên ảnh thật. |

L2-R5 không có ảnh minh họa thay thế và không thêm chức năng chụp/import. Không đọc được ảnh không làm mất dữ liệu chữ hoặc vô hiệu hóa **Sửa hồ sơ**.

### Trạng thái sửa

Giữ tên/mã của cây đang sửa ở đầu để đối chiếu, mã chỉ đọc. Nội dung là form cuộn dọc gồm **Vị trí** và **Ghi chú**, nhãn ngoài trường; hai trường được phép trống. Không đưa taxonomy, nguồn gốc hoặc ảnh thành trường sửa trong slice.

Toolbar có **Hủy** và **Lưu thay đổi**. Draft gắn với ID đã chọn; thao tác lưu không được tạo nhiều lần ghi chồng nhau. Nếu thời gian ghi đủ dài để cần phản hồi, hiển thị trạng thái đang lưu có ngữ nghĩa; thời điểm và cách thể hiện còn phải kiểm tra runtime.

Sau commit thành công, trở về chi tiết cùng cây, báo “Đã lưu trên thiết bị này”; vị trí tại detail và hàng list thành “Bàn làm việc”. Nếu ghi lỗi, giữ form/draft, hiện “Chưa lưu được thay đổi. Nội dung bạn sửa vẫn được giữ.” và cho thử lưu lại. `PLT-027` không đổi.

Hủy, back hoặc chọn cây khác khi draft thay đổi đều hỏi “Bỏ thay đổi chưa lưu?”. **Tiếp tục sửa** giữ cây/draft hiện tại; **Bỏ thay đổi** thực hiện ý định rời form. Không tự bỏ draft khi đổi bố cục cửa sổ. Chưa đề xuất bảo đảm khôi phục draft sau khi tiến trình bị kết thúc; đây là quyết định cần làm rõ nếu mở rộng scope.

## Thích ứng theo không gian và input

| Điều kiện | Đề xuất và điều phải giữ |
| --- | --- |
| Không đủ chỗ cho hai vùng đọc được | List → detail → edit tuần tự; quay lại giữ query và vị trí cuộn theo mục tiêu thiết kế. |
| Đủ chỗ hiển thị list và detail | List bên cạnh detail; giữ mã được chọn. Chuyển selection khi đang sửa vẫn theo PL-04. Không mặc định mọi iPad đều đủ chỗ. |
| Cửa sổ co/giãn hoặc chữ lớn | Chuyển giữa một/hai vùng theo khả năng đọc; wrap/stack nội dung, không thu nhỏ chữ. Giữ selection, query và draft. |
| Bàn phím hiện | Form dùng vùng an toàn và cuộn để trường/focus đang thao tác thấy được; hành động lưu/hủy còn truy cập được. |
| Công nghệ hỗ trợ | Thứ tự ngữ nghĩa theo vùng; đọc tên/mã trước vị trí. Glyph A-03 không là dấu hiệu duy nhất của hành động hoặc lỗi. |

A-03 dùng glyph hệ thống theo cùng vai trò; mọi chữ, field, button, selection và feedback do UI tạo, không nhúng vào bitmap. A-02 hoãn. Quy tắc asset chi tiết giữ tại manifest/brief, không tạo bản định nghĩa cạnh tranh trong layout.

## Phần chưa đo và cách xác minh

Chiều rộng cột, khoảng cách, chiều cao vùng ảnh, ngưỡng chuyển bố cục và kết quả contrast/clipping đều **chưa đo** vì chưa có implementation/ảnh thật. Các quan hệ trên là yêu cầu thiết kế, không phải số đo hoặc screenshot chứng minh.

Khi Build/Verify: PL-01/02/06 kiểm tra ID, nội dung và nguồn gốc; PL-03/04 chạy lưu offline, mở lại, lỗi/hủy; PL-05 chạy cấu hình iPhone/iPad, chữ lớn và AT đã xác định; PL-07 kiểm tra fallback thiếu/lỗi và glyph ở runtime, thêm nhánh ảnh thật nếu build cung cấp; PL-08 đối chiếu vùng, hành động, thuật ngữ và state giữa L-01/L-02 với B-01. Chưa có bước nào được thực hiện; kế hoạch này không tạo kết quả PASS.
