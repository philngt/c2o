# Plantline — Hợp đồng DV-01 và DV-02

**C2O Design v1.2.0.** Phần làm rõ cách biểu diễn dữ liệu cho [DEC-01](decision.md), [B-01 revision 1](baseline.md), [L-01/L-02](layout.md). Không đổi slice hoặc PL-01…PL-08. Chưa có model, repository, query hoặc UI thực thi; mọi criterion vẫn **NOT_RUN**.

## Dữ liệu chung

Một item là một cá thể cây, có ID ổn định. Hai cây cùng giống không được gom thành một item hoặc dùng tên giống làm key. Tên, vị trí và ghi chú thuộc hồ sơ; label loài/giống giữ nguồn và mức chắc chắn. Tên field trong tài liệu chỉ là vai trò mô tả, không cam kết một schema lưu trữ đã tồn tại.

Fixture trong [experience](experience.md): PLT-014 có tên, vị trí “Kệ đông”, nhãn giống chưa xác minh và nguồn giâm từ PLT-003. PLT-027 chỉ được mô tả là cá thể khác có cùng nhãn giống. Các trường PLT-027 chưa cung cấp là khoảng trống fixture, không tự chứng minh record thực có giá trị null. Trước Build/Verify, điền đủ fixture cho test case mà không giả làm dữ liệu cây thật.

| Ý nghĩa | Quy tắc trình bày |
| --- | --- |
| Mã cá thể | Hiện đủ để đối chiếu; selection và save gắn ID, không gắn vị trí hàng. |
| Tên gọi | Hỗ trợ nhận diện; không thay ID. Nội dung dài cần đọc đầy đủ ở detail. |
| Vị trí / ghi chú | Được phép trống; dùng microcopy theo layout. Trống không phải số 0 hoặc lỗi đọc. |
| Loài / giống | Hiển thị cùng câu “Theo nhãn người bán, chưa xác minh” khi đúng fixture. |
| Nguồn gốc | Giữ cách nhân giống, quan hệ đã biết, nguồn ghi nhận và phần chưa biết. Không suy thêm bố mẹ. |
| Ảnh | A-01 thật, tùy chọn; không phải trường bắt buộc để nhận diện hoặc chỉnh sửa. |

## DV-01 — Bộ sưu tập để tìm đúng cá thể

**Câu hỏi:** “Đâu là cây tôi cần mở?” **Representation:** list ưu tiên chữ theo O-01, tham khảo **DVP-01**. **Nơi dùng:** L1-R3, với search ở L1-R2 và state ở L1-R4. [CMP-01](components.md) trình bày từng item.

Projection hiển thị tên → mã → vị trí. Thuộc tính taxonomy, nguồn gốc và ghi chú vẫn có trong DV-02; chúng không biến mất khỏi model chỉ vì không nằm trong hàng. Không thêm thumbnail, chart tổng hợp hoặc thao tác sửa trực tiếp trên hàng.

Query thuộc màn danh sách và được giữ khi quay lại. PL-01 yêu cầu tìm bằng mã và mở đúng ID; phần tìm theo tên đã được đề xuất nhưng quy tắc chuẩn hóa, đối sánh và thứ tự kết quả chưa được chốt bằng implementation. Ghi quyết định đó khi Build, giữ nhất quán với copy tìm kiếm; không gọi đây là fuzzy search đã có. Sort/filter nâng cao, paging và batch actions chưa nằm trong slice.

Chọn hàng phát ý định mở/chọn ID. View không tự ghi dữ liệu và không đổi selection sang cây khác chỉ vì thứ tự kết quả đổi. Nếu có draft tại detail, screen xử lý PL-04 trước khi hoàn tất ý định đổi cây.

**Trạng thái:** kho rỗng khác query không khớp. Không có mạng không làm hỏng dữ liệu cục bộ. Nếu implementation có lỗi đọc repository, cần mô tả lỗi và retry đúng scope; hiện chưa có bằng chứng đường đó. Nếu sau này chia trang/tải từng phần, phải ghi tổng phạm vi và cách giữ selection; không lấy số hàng đang tải làm tổng số cây.

## DV-02 — Hồ sơ một cá thể

**Câu hỏi:** “Đây có đúng cây không, hồ sơ nói gì và phần nào có thể sửa?” **Representation:** các nhóm label–value theo L2-R1…R5, tham khảo **CP-15** trong màn chi tiết **SP-02**; không dùng table nhiều cá thể hoặc graph phả hệ trong slice này. Catalog data view chưa có entry riêng cho mọi kiểu detail; chọn representation phù hợp thay vì ép DV-02 vào một DVP không khớp.

Thứ tự: định danh → vị trí/ghi chú → taxonomy → nguồn gốc → ảnh thật tùy chọn. Chỉ đọc hồ sơ của ID đang chọn; nguồn gốc giữ từng loại quan hệ và phần chưa biết. Mã cây nguồn được trình bày dạng chữ khi navigation đích chưa có.

Không tạo phần trăm, số thế hệ hoặc xác suất từ dữ liệu chưa có. Lịch sử/timeline và graph có thể phục vụ một nhiệm vụ sau này, nhưng chưa được thêm vào scope vì catalog hỗ trợ chúng.

Trạng thái sửa dùng draft riêng do màn điều phối, qua CMP-02/CMP-03. Commit thành công cập nhật dữ liệu đã lưu và cả DV-01/DV-02 của cùng ID; lỗi giữ draft. “Đã lưu trên thiết bị này” không hàm ý sao lưu hoặc sync.

## Kiểm chứng

- PL-01/02/06: đối chiếu identity, projection, label chắc chắn và quan hệ với fixture thật dùng trong lần kiểm tra.
- PL-03/04: kiểm tra draft/commit/lỗi/hủy và cây còn lại không đổi; đóng/mở lại xác nhận dữ liệu đã lưu.
- PL-05/08: đổi không gian/chữ lớn, quay lại và đổi selection; vẫn tìm/đọc/sửa đúng đối tượng.
- PL-07: kiểm tra fallback/glyph và ảnh thật nếu được tích hợp.

Chốt coverage và policy tìm kiếm trước khi chạy; phần chưa làm không trở thành PASS qua việc viết contract. Xem [data view core](../../core/data-views.md), [composition](ui-composition.md) và [verification](verification.json).
