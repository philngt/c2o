# Plantline — Asset brief v1.1

> Kế hoạch minh họa, chưa có source/derived image, lần gọi tạo ảnh, export hay runtime check. **PL-07/PL-08: Proposed / NOT_RUN**. [assets.json](assets.json) là inventory mô tả, `planning_only: true`; `outputs` rỗng, không phải job queue.

[DEC-01](decision.md) chọn O-01 cho ví dụ; [B-01 revision 1](baseline.md) là baseline. [Layout](layout.md) gồm L-01 danh sách ưu tiên chữ và L-02 chi tiết với read/edit states. Nội dung tác vụ và các tiêu chí nằm trong [experience](experience.md). Áp dụng quy trình [core/assets](../../core/assets.md) khi triển khai thật.

## Phân chia UI và asset

Tên cây, mã cá thể, nhãn loài/giống, provenance, vị trí, ghi chú, nút, form, navigation và phản hồi đều thuộc UI/code. Giữ text có thể đọc, dịch và phóng to. Không dựng một bitmap cả màn hình để thay thế UI. Chưa có kích thước đo, destination, format hay glyph mapping; các trường tương ứng trong manifest giữ `null` hoặc rỗng.

## Asset A-01

**Vai trò:** ảnh thật tùy chọn của đúng cá thể, ở L-02/read sau nhóm dữ liệu chính. L-01 không có thumbnail. Read/edit/save vẫn hoàn thành khi không có ảnh; slice không thêm bước chụp/import/chỉnh ảnh. Liên quan PL-02, PL-07 và PL-08.

**Nguồn:** `real_capture`; chưa cung cấp. `PLT-014` và `PLT-027` là fixture giả định, không đại diện cây thật. Khi kiểm tra nhánh có ảnh, dùng ảnh thật có nguồn và mapping rõ tới hồ sơ thử nghiệm; không dùng ảnh đó để khẳng định dữ liệu fixture là thật. Giữ original, nguồn/quyền sử dụng đã biết và mọi biến đổi.

| Thuộc tính | Hợp đồng / phần còn mở |
|---|---|
| Nội dung | Đúng cá thể; không sinh thêm lá, đặc điểm nhận diện hoặc màu để hợp palette. Ảnh minh họa không thay ảnh hồ sơ. |
| Kích thước và aspect | Chưa đo. Chọn theo vùng L-02, kích thước source thật, không gian và cỡ chữ; ghi logical size và export pixels khi có triển khai. |
| Crop và màu | Giữ focal point/đặc điểm cần nhận diện; cho orientation/crop/resizing có ghi lại, giữ original. Không recolor ảnh dữ liệu theo theme. |
| Alpha / nền | Chưa có source để xác định. Ảnh opaque có thể đúng brief; nếu source/export có alpha, xem cạnh trên nền sáng/tối liên quan. |
| Appearance | Ưu tiên cùng ảnh thật ở các appearance; kiểm tra nền/viền và khả năng đọc UI xung quanh, không thêm biến thể màu cây. |
| Thiếu / lỗi | “Chưa có ảnh cá thể” hoặc “Không đọc được ảnh cá thể” tại vùng tương ứng; không che định danh hay chặn sửa/lưu. |
| Semantics | Mô tả phù hợp nội dung ảnh; không tự thêm nhận định taxonomy. Hạn chế lượt đọc lặp với nhãn hồ sơ. |
| Export / runtime | Format, destination, color handling và cách fit cần chốt theo target thật; chưa có file xuất hay kết quả tích hợp. |

## Asset A-02

**Vai trò:** illustration trang trí cho bộ sưu tập rỗng ở L-01. **Deferred**; chưa chọn reference, viết prompt, gọi model hoặc tạo ứng viên. `generated_raster` chỉ mô tả một route có thể dùng sau này. Không cần artwork để hoàn thành slice.

Fallback hiện tại là UI text **“Chưa có cây nào.”**; không có nút thêm cây ngoài scope. Nếu đưa A-02 vào sau, artwork không chứa text/control hoặc thông tin về một cá thể; không được hiểu như ảnh `PLT-014`. Ghi style/crop, vùng trống, alpha/nền, appearance, source và output thật; giữ semantics trang trí. Mọi quyết định kích thước/format còn mở, không có số đo ước lượng được trình bày như đã xác minh.

## Asset A-03

**Vai trò:** glyph hệ thống cho control phù hợp ở L-01/L-02, cùng family theo B-01. Ưu tiên control sẵn có và SF Symbols phù hợp target; chưa chọn tên symbol/API hay xác minh availability. Liên quan PL-05, PL-07 và PL-08.

Glyph hỗ trợ nhãn thao tác thật; không thay tên nút bằng artwork hoặc chỉ dựa vào màu. Khi symbol không khả dụng, dùng control có nhãn chữ rõ hoặc symbol đã xác minh. Không có raster export bắt buộc cho route này. Khi triển khai, ghi mapping/code và kiểm tra kích thước thực, disabled state, focus, VoiceOver và appearance; icon lặp nhãn không tạo lượt đọc thừa.

## Kiểm chứng phải làm khi có implementation

1. Đối chiếu B-01 revision 1, L-01/L-02 và manifest với asset/code thực dùng. Kiểm nguồn và mapping của A-01 nếu có; ghi phạm vi vắng mặt của A-01 và A-02 deferred. A-01 thiếu hợp lệ, nhưng fallback và A-03 vẫn cần kiểm tra nên PL-07 không tự thành `NOT_APPLICABLE`.
2. Review file source/derived thật ở kích thước hiển thị: crop, nét, color handling, alpha nếu có và appearance liên quan. Sau đó xem trong app và thao tác; file export hoặc ảnh concept không thay bằng chứng runtime.
3. Chạy các state liên quan của L-01/L-02: không ảnh/lỗi ảnh, có ảnh nếu build cung cấp, read/edit/save/error. Ghi build, device/window, theme, text size, locale và data/state theo coverage PL-05/07/08 đã chốt.
4. Slice không yêu cầu animated asset. Nếu bổ sung motion, phân biệt format, decoder và player thực dùng; kiểm playback cùng fallback tĩnh khi Reduce Motion bật hoặc tải/phát thất bại. Không suy khả năng phát chỉ từ đuôi file.

Kết quả thật mới được đưa vào [verification.json](verification.json) cùng input/evidence có hash theo [evidence contract](../../core/evidence.md). Hiện mọi criterion PL-01…PL-08 vẫn `NOT_RUN`; không có ảnh ứng viên hay screenshot để đánh giá.
