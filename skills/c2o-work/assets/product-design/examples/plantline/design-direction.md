# Plantline — Visual và Platform

> Hướng thiết kế **đề xuất** cho **C2O Design v1.1**, chưa có mockup hay screenshot. Tiêu chí PL-01…PL-08: **Proposed / NOT_RUN**.

[DEC-01](decision.md) chọn O-01 trong ví dụ; [B-01 revision 1](baseline.md) là nguồn quy ước dùng chung, [L-01/L-02](layout.md) mô tả vùng và state. Tài liệu này diễn giải ý đồ visual/platform. Thay đổi quy tắc chung cần cập nhật baseline và các màn liên quan, không tạo một chuẩn song song.

## Visual phục vụ tác vụ

Chọn cảm giác **bình tĩnh, dễ tra cứu**. Ưu tiên nhận đúng cá thể và biết thay đổi đã lưu. Danh sách dùng các hàng nhất quán; không cố làm mỗi hàng khác nhau để tránh vẻ “AI”.

Tên cây là nhãn chính, mã để đối chiếu, vị trí hỗ trợ nhận diện. Trạng thái có nhãn, không chỉ màu. L-01 ưu tiên chữ, không có thumbnail. Ảnh thật A-01 tùy chọn ở L-02/read sau nhóm dữ liệu chính; thiếu ảnh vẫn nhận diện được hồ sơ.

## Vật liệu thiết kế

| Vai trò | Hướng đề xuất |
|---|---|
| Chữ | Kiểu chữ hệ thống theo vai trò; hỗ trợ co giãn theo cài đặt đọc. |
| Màu | Màu nền/chữ hệ thống; một màu nhấn cho lựa chọn/hành động. Chỉ chốt giá trị sau khi đo contrast thực. |
| Khoảng cách | Nhóm định danh, vị trí, nguồn gốc tách được; ưu tiên nội dung và khả năng đọc. |
| Thành phần | Dùng control nền tảng phù hợp; tùy biến khi nhu cầu cụ thể đòi hỏi. |
| Chuyển động | Phản hồi lưu/chuyển màn ngắn, có phương án giảm chuyển động; không cần animation vô hạn. |

## Vai trò asset

| Asset | Ràng buộc của hướng đang chọn |
|---|---|
| A-01 | Ảnh thật đúng cá thể, giữ nguồn và màu mang thông tin; không dùng cây sinh bằng AI để điền chỗ thiếu. Crop không được che đặc điểm cần nhận diện. |
| A-02 | Illustration empty-state chỉ có vai trò trang trí và đang hoãn. Empty-state bằng chữ vẫn hoàn chỉnh; không cần tạo file trong ví dụ này. |
| A-03 | Glyph hệ thống hoặc bộ đang dùng phù hợp với control; tên thao tác và semantics vẫn do UI/code cung cấp. Chọn symbol cụ thể khi biết target, không vẽ lại icon hệ thống thành raster. |

[Asset brief](asset-brief.md) là hợp đồng nội dung, crop/appearance/fallback; [assets.json](assets.json) là inventory mô tả với `planning_only: true`. Kích thước xuất, format và destination còn chưa xác định. Không suy kích thước control hoặc màu native từ một ảnh concept. Không đưa tên cây, mã, nhãn trường, nút hay thông báo lưu vào bitmap.

PL-07 kiểm tra source cùng asset đã tích hợp ở kích thước dùng thật, nền sáng/tối liên quan và trạng thái thiếu/lỗi. PL-08 đối chiếu các màn theo baseline và state; khác biệt do Dynamic Type hoặc không gian cửa sổ được giải thích bằng nhiệm vụ. Chưa có review file ảnh hay runtime evidence.

## Thích ứng nền tảng

**iPhone:** danh sách → chi tiết → sửa. Sau lưu, trở về đúng chi tiết; back về danh sách giữ truy vấn và vị trí cuộn nếu khả thi.

**iPad:** đề xuất danh sách bên trái, chi tiết bên phải khi đủ rộng; cửa sổ hẹp chuyển thành điều hướng tuần tự. Mã cá thể đang sửa vẫn hiện để tránh nhầm khi đổi lựa chọn. Khi có bản nháp, chọn cây khác dùng cùng quy tắc PL-04.

**Tiếp cận:** kiểm tra tên control, thứ tự đọc, chữ lớn, bàn phím, focus và giảm chuyển động theo [profile SwiftUI](../../profiles/swiftui.md). A-01 nếu mang thông tin cần mô tả phù hợp; glyph lặp nhãn không tạo lượt đọc thừa; A-02 trang trí không thêm thông tin domain. Đây là danh sách cần xác minh, chưa phải tuyên bố hỗ trợ.

## Câu hỏi cần quan sát

X-01: đưa hai cây cùng giống, yêu cầu tìm cây tại “Kệ đông”; ghi lựa chọn và nhầm lẫn. X-02: sau lưu offline, hỏi dữ liệu đang nằm ở đâu. Chưa tuyển người tham gia; chưa có kết quả.
