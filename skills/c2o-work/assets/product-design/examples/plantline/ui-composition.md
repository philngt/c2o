# Plantline — Ghép màn SCR-01 và SCR-02

**C2O Design v1.2.0.** Làm rõ các trách nhiệm đã chọn trong O-01 → DEC-01 → B-01 revision 1 → L-01/L-02. Không thay phạm vi, baseline hoặc tám criterion. Đây là tài liệu thiết kế, chưa là UI/code đã thực thi.

## Composition map

| Màn / vùng | Nhiệm vụ | Data view / component | Owner và hành động |
| --- | --- | --- | --- |
| SCR-01, L1-R1/R2 | Biết đang ở bộ sưu tập; tìm cây | Search/navigation của nền tảng điều khiển DV-01 | Màn danh sách giữ query; thao tác tìm không sửa domain record. |
| SCR-01, L1-R3 | Nhận diện và chọn đúng cá thể | DV-01 + CMP-01 PlantRecordRow | Chọn theo plant ID; screen xử lý chuyển selection/navigation. |
| SCR-01, L1-R4 | Hiểu vì sao chưa có kết quả | State content của DV-01 | Empty collection khác no-results; xóa query chỉ đổi view state. |
| SCR-02/read, L2-R1/R2/R3/R4 | Hiểu đúng đối tượng và hồ sơ | DV-02, các nhóm label–value | Screen đọc ID đang chọn; Sửa hồ sơ tạo draft riêng. |
| SCR-02/read, L2-R5 | Xem ảnh thật nếu có | A-01 và fallback đã định nghĩa | Lỗi ảnh giữ nguyên dữ liệu chữ và action. |
| SCR-02/edit | Sửa vị trí/ghi chú rồi lưu/hủy | CMP-02 + CMP-03; draft của cùng record | Screen/logic tác vụ giữ draft, commit, error và xử lý ý định rời form. |

[Data views](data-views.md) giữ identity/projection/biến đổi; [components](components.md) giữ trách nhiệm đơn vị; [layout](layout.md) giữ các vùng/scroll/adaptation. Không viết một bản microcopy khác tại đây; [experience](experience.md) và [asset brief](asset-brief.md) là nguồn đã chọn.

## Hợp đồng chuyển tiếp

**Tìm → mở:** query không đổi khi mở detail; selection dùng ID. **Đọc → sửa:** draft tách dữ liệu đã lưu; mã đang sửa nhìn thấy được. **Sửa → lưu:** logic tác vụ mới xác nhận commit, cập nhật cả hai view và thông báo lưu cục bộ. **Lỗi → thử lại:** giữ draft. **Rời form/đổi cây:** PL-04 giải quyết trước khi đổi selection. **Đổi cửa sổ/cỡ chữ:** đổi cấu trúc vùng theo layout, giữ selection và draft.

LP-02 là pattern tham khảo cho list–detail; khi hẹp có thể dùng navigation tuần tự theo L-01/L-02. SP-01/02/03 là những nhiệm vụ đang được ghép. Các pattern không thêm bước tạo cây, quản lý ảnh, sync hoặc editor phả hệ.

## Bằng chứng cần tạo

PL-01…PL-08 tiếp tục là acceptance duy nhất của ví dụ. Khi có build, chạy flow với fixture đủ rõ, kiểm dữ liệu trước/sau và xem component trong cả screen. Kiểm tra standalone row không tự chứng minh draft xuyên màn; kiểm tra save handler không tự chứng minh layout/focus dùng được.

Các tài liệu composition/component/data view trở thành declared inputs khi chúng có ảnh hưởng đến kết luận. Checker không tự hiểu CMP/DV/SCR/LP/SP hoặc xác minh mapping; review nội dung và kết quả thực vẫn cần thiết. [Verification](verification.json) hiện giữ mọi kết quả **NOT_RUN**.
