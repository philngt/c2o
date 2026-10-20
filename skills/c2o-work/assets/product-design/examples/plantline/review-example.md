# Plantline — Ví dụ review và kế hoạch bằng chứng

> **Review minh họa trên đặc tả C2O Design v1.1 này**, không phải review app đã chạy. Không có screenshot, kết quả test, hoặc verdict ship. Mọi acceptance criterion: **Proposed / NOT_RUN**.

## Inspect → Frame → Design

Outcome giới hạn vào đọc/sửa cá thể offline. Experience, Visual và Platform đã có đề xuất; Evidence vẫn chưa có thực thi.

Chuỗi tài liệu: [brief](brief.md), [options](options.md), [DEC-01](decision.md), [B-01 revision 1](baseline.md), [L-01/L-02](layout.md), [asset brief](asset-brief.md) và [manifest](assets.json). O-01 được chọn để minh họa cách giữ quyết định xuyên tài liệu, chưa phải kết luận từ nghiên cứu người dùng.

## Phản biện có thể đưa ra từ tài liệu

| ID | Phát hiện / câu hỏi | Cơ sở hiện có | Quyết định đề xuất |
|---|---|---|---|
| PL-01 | Chưa biết tên/mã/vị trí có đủ phân biệt hai cây. | H-01 và X-01 trong brief; chưa quan sát người dùng. | Thử tìm cây trước khi bổ sung ảnh bắt buộc. |
| PL-03 | “Lưu trên thiết bị” cần khác nghĩa với sao lưu. | H-03 và X-02; slice chưa có sync. | Dùng microcopy đã đề xuất, kiểm tra cách người dùng hiểu. |
| PL-04 | Đổi lựa chọn trên iPad có thể bỏ dở bản nháp. | Luồng nhiều cột trong design-direction. | Áp dụng cùng quy tắc chưa lưu cho back, đóng và đổi cây. |
| PL-06 | Tự suy ra bố mẹ từ nhãn giống sẽ tạo dữ liệu không có chứng cứ. | Ranh giới domain trong brief. | Giữ quan hệ chưa biết; không tạo pedigree tự động. |
| PL-07 | Ảnh cây đẹp có thể bị hiểu là ảnh đúng cá thể; ảnh hỏng có thể làm phần hồ sơ bị che. | A-01 chưa có source/output; A-02 chỉ là ý tưởng trang trí đang hoãn. | Chỉ dùng ảnh thật có mapping/source rõ; kiểm tra thiếu/lỗi ảnh và màu/crop trong app. |
| PL-08 | Chi tiết hoặc edit có thể đổi cách gọi, màu trạng thái hay quy tắc bản nháp khi phát triển riêng. | B-01 và L-01/L-02 hiện là hợp đồng tài liệu, chưa có implementation. | Đối chiếu cùng fixture xuyên màn/state; ghi ngoại lệ cùng lý do và criterion bị ảnh hưởng. |

Đây là **rủi ro/giả định thiết kế**, chưa phải bug quan sát được. Không gán severity Critical để làm review trông nghiêm ngặt.

## Build → Verify

Chỉ khi có implementation mới thực hiện:

- PL-01/02/06: đối chiếu fixture domain với giao diện và kết quả lưu.
- PL-03/04: kiểm tra mất mạng, đóng/mở app, ghi thất bại, thử lại và hủy; ghi rõ artifact/version.
- PL-05: chạy tác vụ trên cấu hình iPhone/iPad và accessibility thực tế đã chọn.
- PL-07: đối chiếu nguồn, mapping cá thể và biến đổi của asset thực dùng; kiểm tra vùng ảnh thật nếu có, glyph, crop, appearance, semantics và fallback thiếu/lỗi trong runtime. Nhánh tùy chọn chưa tích hợp được ghi rõ phạm vi; A-02 deferred không yêu cầu tạo artwork.
- PL-08: so L-01 và L-02/read+edit với B-01 revision 1 ở state bình thường, rỗng/không tìm thấy, thiếu ảnh, bản nháp, lưu thành công và lỗi; thử chuyển cửa sổ/selection theo coverage đã chốt.
- X-01/02: ghi quan sát người tham gia riêng với phán đoán của reviewer.

Khi tạo record thực, đưa baseline/layout, manifest/asset brief, code/config, source/derived asset và fixture có ảnh hưởng vào `inputs`; `evidence` trỏ tới kết quả đã thu được. Ghi build, thiết bị/cửa sổ, theme, cỡ chữ, locale và state. File ảnh đã xuất không tự chứng minh đã tích hợp hoặc chạy đúng. Manifest là tài liệu mô tả; checker không tự kiểm provenance hay nối IDs để chứng minh consistency.

Hiện tại **PL-01…PL-08 = Proposed / NOT_RUN** trong [verification.json](verification.json). `project_sha256` còn `null`, inputs/evidence rỗng vì chưa thực thi. Thiếu implementation và bằng chứng nên chưa đưa ra quyết định phát hành. Không lấy sự đầy đủ của bảng làm bằng chứng chức năng đúng.

## Learn

Sau xác minh, ghi: ID → quan sát → quyết định → phạm vi kiểm tra lại. Giữ danh sách đơn giản nếu mã/vị trí đủ phân biệt; nếu nhầm, thử ảnh hoặc cách đặt mã. Chỉ cập nhật giả định bằng dữ liệu thực thu được.
