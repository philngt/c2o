# Plantline — Experience

> Ví dụ **C2O Design v1.1**; nội dung và dữ liệu minh họa. Tất cả tiêu chí: **Proposed / NOT_RUN**. Không có kết quả quan sát người dùng.

## Dữ liệu mẫu

`PLT-014` — “Monstera bàn làm việc”; vị trí “Kệ đông”; nhãn loài `Monstera deliciosa`, giống `Thai Constellation`, ghi rõ “Theo nhãn người bán, chưa xác minh”. Nguồn gốc: giâm cắt từ `PLT-003`, do chủ bộ sưu tập tự ghi nhận. Một cá thể khác `PLT-027` dùng cùng nhãn giống để kiểm tra khả năng phân biệt. Đây không phải dữ liệu cây thật.

## Luồng chính

Luồng bắt đầu khi kho cục bộ đã có hồ sơ cây. Fixture ở trên chỉ giúp kiểm tra slice đọc/sửa; sản phẩm mới cần xác định riêng đường tạo hoặc import dữ liệu.

1. **Danh sách L-01:** nhập `PLT-014`; hàng kết quả có tên, mã và vị trí, không có thumbnail theo O-01. Chọn hàng mở đúng cá thể.
2. **Chi tiết L-02/read:** tên/mã dẫn đầu; vị trí và ghi chú dễ đọc. Loài/giống nằm trong nhóm định danh; nguồn gốc là nhóm riêng. A-01, nếu có ảnh thật của cá thể, nằm sau nhóm dữ liệu chính; thiếu ảnh vẫn đọc đầy đủ hồ sơ. Chọn **Sửa hồ sơ**.
3. **Sửa:** mã chỉ đọc; hai trường sửa được là **Vị trí** và **Ghi chú**. Nhãn hiện ngoài ô nhập. Bản nháp chưa ghi đè dữ liệu đã lưu.
4. **Lưu:** đổi “Kệ đông” thành “Bàn làm việc”, chọn **Lưu thay đổi**. Chỉ báo thành công sau khi ghi cục bộ thành công: **Đã lưu trên thiết bị này**. Chi tiết và danh sách cập nhật cùng bản ghi.

Read và edit là hai state của L-02, cùng giữ mã cá thể và quy tắc bản nháp. Liên kết thiết kế: [DEC-01](decision.md) → [B-01 revision 1](baseline.md) → [L-01/L-02](layout.md); nội dung ảnh theo [asset brief](asset-brief.md), inventory theo [assets.json](assets.json).

## Tiêu chí chấp nhận

| ID | Tiêu chí đề xuất | Bằng chứng cần tạo khi Build/Verify |
|---|---|---|
| PL-01 | Tìm bằng mã mở đúng cá thể dù trùng tên/giống. | Chạy luồng với hai cá thể trùng nhãn. |
| PL-02 | Tên gọi, mã cá thể và loài/giống phân biệt được; không biến nhãn chưa xác minh thành kết luận. | Kiểm tra nội dung và thử tác vụ nhận diện cây. |
| PL-03 | Lưu offline cập nhật đúng cá thể, còn nguyên sau khi đóng/mở app. | Kiểm tra persistence và đối chiếu hồ sơ còn lại. |
| PL-04 | Lỗi lưu giữ bản nháp; hủy có thay đổi cần lựa chọn rõ. | Mô phỏng ghi thất bại và thử các đường hủy. |
| PL-05 | Chọn cây, sửa, lưu dùng được trên iPhone/iPad với chữ lớn và công nghệ hỗ trợ đã chọn. | Chạy luồng theo profile nền tảng; ghi thiết bị/cấu hình thực. |
| PL-06 | Nguồn gốc giữ đúng cách nhân giống, quan hệ biết được và phần chưa biết. | Đối chiếu giâm/tách/hạt; có, không hoặc chưa rõ quan hệ lai. |
| PL-07 | Asset thực dùng có provenance và đúng vai trò; ảnh cá thể không bị thay bằng ảnh sinh. Thiếu/lỗi ảnh có fallback, hiển thị và semantics đúng trong runtime đã chọn. | Đối chiếu manifest với source/derived file thực có; xem crop, màu, alpha nếu có, appearance và fallback trong app. |
| PL-08 | L-01 và L-02/read+edit giữ B-01 revision 1 về định danh, token/component, thuật ngữ, selection, bản nháp và phản hồi qua các state thuộc scope. | Chạy cùng fixture qua danh sách, chi tiết, sửa, lưu/hủy/lỗi và thay đổi không gian; ghi khác biệt có chủ đích cùng lý do. |

Trạng thái cho **từng hàng PL-01…PL-08: Proposed / NOT_RUN**; bảng mô tả kế hoạch bằng chứng. PL-01…PL-06 giữ nguyên nội dung tiêu chí của ví dụ v1.0.

Trước khi chạy PL-05, chọn và ghi thiết bị/OS, cỡ chữ, công nghệ hỗ trợ và các trường hợp bắt buộc. Evidence phải có kết quả từng trường hợp; PL-05 chỉ được `PASS` khi tất cả trường hợp bắt buộc đã đạt. Có thể tách thành các criterion nhỏ nếu cần theo dõi độc lập.

PL-07/08 dùng cùng coverage phù hợp đã chốt: iPhone hẹp, iPad rộng/cửa sổ hẹp, appearance và cỡ chữ có ảnh hưởng. Ghi build, data/state và cấu hình thực cho từng bằng chứng. Nhánh A-01 có ảnh chỉ bắt buộc nếu build cung cấp ảnh; nhánh thiếu ảnh và glyph/control vẫn cần kiểm tra. A-02 đang hoãn, không tạo yêu cầu sinh artwork để hoàn thành slice. Việc một asset tùy chọn vắng mặt không làm toàn bộ PL-07 thành `NOT_APPLICABLE`.

## Trạng thái và microcopy

| Tình huống | Phản hồi đề xuất |
|---|---|
| Bộ sưu tập rỗng | “Chưa có cây nào.” Hành động thêm cây thuộc slice tiếp theo; không tạo nút giả. |
| Tìm không thấy | “Không tìm thấy cây phù hợp.” Cho xóa tìm kiếm. |
| Chưa rõ nguồn gốc | “Chưa ghi nhận nguồn gốc.” Khác với “Gieo hạt — chưa biết cây bố mẹ”. |
| Chưa lưu | “Bỏ thay đổi chưa lưu?” Hai lựa chọn: “Tiếp tục sửa”, “Bỏ thay đổi”. |
| Ghi thất bại | “Chưa lưu được thay đổi. Nội dung bạn sửa vẫn được giữ.” Cho thử lưu lại. |
| Không có mạng | Vẫn đọc/sửa/lưu cục bộ; không che nội dung bằng thông báo mất kết nối. |
| Không có ảnh cá thể | “Chưa có ảnh cá thể” tại detail; không thêm nút tải ảnh ngoài scope. Danh sách giữ hàng chữ. |
| Không đọc được ảnh đã liên kết | Thông báo cục bộ “Không đọc được ảnh cá thể”; giữ dữ liệu hồ sơ và khả năng sửa/lưu. |

Vị trí và ghi chú được phép để trống. Tên dài phải xem đầy đủ trong chi tiết; không dùng dữ liệu giả để lấp khoảng trống.
