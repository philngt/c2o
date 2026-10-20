# Từ thiết kế đến asset dùng trong giao diện

Module này đặt asset vào cùng chuỗi quyết định của sản phẩm: outcome, phương án, baseline, layout, file đầu ra, tích hợp và evidence. Chắt lọc từ gpt-ui-assets theo phạm vi ghi trong [SOURCES.md](../SOURCES.md); tài liệu và mẫu của C2O được viết riêng. Không yêu cầu cài repo, backend hoặc model cụ thể.

## 1. Chọn phần nào cần asset

Đọc baseline và bố cục trước. Mỗi hình cần một vai trò: giúp nhận diện, giải thích, tạo cảm giác, thể hiện thương hiệu hoặc chỉ trang trí. Một asset không cần thiết có thể được bỏ khỏi scope.

| Loại nội dung | Cách xử lý ưu tiên |
| --- | --- |
| Text, form, button, navigation, surface, separator, state | Triển khai bằng UI/code hoặc control nền tảng, giữ semantics và khả năng thích ứng |
| Icon thông dụng | Dùng system symbol hoặc bộ icon hiện có phù hợp; tùy biến khi có lý do |
| Logo, icon hoặc hình vector cần chính xác | Giữ source vector/code đang có; kiểm tra sửa đổi ở kích thước dùng thật |
| Illustration, texture, vật liệu, ảnh khái niệm | Dùng nguồn đã có hoặc tạo raster phù hợp; lưu vai trò, reference, prompt và giới hạn |
| Ảnh cây/sản phẩm/tài liệu thật | Dùng ảnh thực có nguồn; ảnh sinh chỉ được dùng như minh họa được phân biệt rõ |
| Motion | Code/player kiểm soát thời gian, state và input; asset cung cấp hình/frame cần thiết |

Không đưa text thao tác hoặc cả màn hình thành một bitmap thay UI hoạt động. Với preview trình bày, ảnh toàn màn vẫn có thể là artifact khám phá; gắn đúng nhãn concept.

## 2. Inventory và asset brief

Ghi phần inventory hữu ích trong context hoặc tài liệu hiện có: vai trò, vị trí dùng, reference, file đầu ra và criterion liên quan. [assets.json](../templates/assets.json) là mẫu tùy chọn khi cần quản lý nhiều asset/biến thể; không phải file bắt buộc cho một chỉnh sửa nhỏ. Nếu dùng mẫu, `ui_owned_by_code` chỉ ghi các thành phần loại khỏi danh mục hình cần tạo. Route là quyết định mô tả, không phải lệnh sẽ được thực thi.

Trước khi tạo một asset, làm rõ thông tin ảnh hưởng đầu ra: vùng sử dụng, kích thước cần thiết, background/alpha, crop, appearance và fallback khi liên quan. Giữ tại brief/context đang dùng; [asset brief](../templates/asset-brief.md) là điểm khởi đầu tùy chọn cho phần còn thiếu, không phải tài liệu mới phải điền đủ. Nêu điều phải giữ từ reference và điều được thay. Giá trị chưa quyết định ghi chưa xác định; không điền số đo giả.

Chốt sự thật của nội dung. Một hình minh họa lá cây không thay ảnh của PLT-014; việc đổi màu để hợp palette có thể làm sai ý nghĩa ảnh sản phẩm. Giữ bản gốc và ghi biến đổi. Nguồn/quyền sử dụng là provenance của asset, không phải kết luận pháp lý tự động.

## 3. Tạo hoặc thích ứng asset

Chọn công cụ theo đầu ra: UI/code cho bố cục và control; vector tooling cho hình cần chính xác; công cụ tạo ảnh cho raster khi phù hợp; renderer/native runtime cho kiểm tra. Ghi giới hạn của công cụ đang dùng. Không chuyển sang backend, cài dependency hoặc gửi dữ liệu ra dịch vụ khác ngoài quyền hạn của nhiệm vụ.

Khi tái tạo art từ mockup, một crop có trọng tâm có thể làm reference. File đem tích hợp cần đủ chất lượng cho kích thước dùng và không lẫn text, card, chrome hoặc nền ngoài ý muốn. Crop không phải lúc nào cũng sai: crop ảnh gốc có độ phân giải phù hợp hoặc dùng đúng một source được cấp phép có thể là đầu ra hợp lệ. Phân biệt crop dùng làm input với asset độc lập được bàn giao.

Tạo số ứng viên theo bất định, mức ảnh hưởng và ngân sách đã có. Nếu gọi công cụ tính phí/quota, ghi dự kiến số lần gọi và điểm dừng trước khi chạy; sử dụng quyền đã được giao, không bắt hỏi lại mỗi lần. Không ghi giá hoặc model như một hằng số của framework. Khi chỉnh sửa không còn giải quyết được lỗi đã xác định, đổi cách làm hoặc báo giới hạn thay vì lặp vô hạn.

## 4. Review asset trước khi chọn

Xem cạnh reference, ở kích thước thực và trong vùng bố cục dự kiến. Với asset trong suốt, xem trên nền sáng, tối và nền ứng dụng liên quan. Kiểm tra:

- Nội dung/nhận diện đúng vai trò; không thêm chi tiết sai sự thật.
- Silhouette, focal point, style family và màu theo baseline.
- Alpha, viền/halo, phần bị cắt, text/nền bị dính, khoảng trống dành cho UI.
- Độ rõ ở kích thước nhỏ; dung lượng và chi phí render phù hợp.
- Các appearance/state cùng một đối tượng vẫn liên tục và nhất quán.

Chỉ coi blank, opaque, clipping hoặc phần giống reference là lỗi khi chúng vi phạm asset brief. Full-bleed background có thể chạm mép; ảnh opaque có thể đúng; tái sử dụng source gốc có thể là lựa chọn mong muốn. Điểm similarity và màu hỗ trợ tìm khác biệt, không chứng minh đúng nghĩa, accessibility hay chất lượng UX. Ghi thuật toán, scope và giới hạn khi dùng số đo; không dùng ngưỡng của một repo như chuẩn chung.

Nếu sửa một state trong ảnh, so sánh cả vùng thay đổi và vùng phải giữ. Chỉ tuyên bố vùng ngoài mask không đổi khi phép đo thực đã chứng minh trên file đầu ra. Không coi lời nhắc “chỉ sửa vùng này” là bằng chứng.

## 5. Export và tích hợp

Giữ source cùng file dẫn xuất. Xác định format, kích thước, alpha, color handling, crop/resizing mode, tên tài nguyên và destination theo build target thực. Chọn vector khi hình và renderer phù hợp; raster vẫn hợp lệ cho ảnh/vật liệu hoặc hình mà chuyển vector làm mất chi tiết. Export không đồng nghĩa đã chạy trong app.

Tích hợp bằng control/code của nền tảng, giữ text có thể dịch và semantics của nội dung có nghĩa. Ghi static/loading/missing-asset fallback. Với motion, kiểm tra decoder, player và đường tích hợp thật; nêu loop/duration/input và phương án Reduce Motion/static. Hỗ trợ format của hệ điều hành không tự chứng minh một UI component sẽ phát animation.

App icon là asset riêng: chọn concept, kiểm tra hình ở kích thước/appearance liên quan rồi xác minh pipeline icon hiện hành của target. Không áp cứng một bộ kích thước hay asset-catalog path từ repo tham khảo cho mọi SDK.

## 6. Kiểm chứng trong màn thật

Ghi screenshot hoặc thao tác trên implementation thật cùng build, device/window, scale, theme, text size, locale, data và state. Nếu có diff, ghi vùng được so, phần ngoài ảnh, masks, phép đo bị bỏ qua và các khác biệt có chủ đích. Native metrics, chữ lớn và reflow có thể tạo hình học khác với concept một cách đúng đắn.

Criterion bắt buộc chỉ được `pass` khi đủ scope đã chốt. File ảnh tồn tại, review sheet đẹp hoặc điểm similarity cao không thay cho integration test. Build/test thất bại là `fail` theo criterion tương ứng; bằng chứng một phần giữ `partial`; thiếu môi trường hoặc chưa chạy giữ `not-tested` cùng lý do. Các nhãn viết hoa chỉ dùng nếu đã chọn profile JSON tùy chọn trong [evidence](evidence.md).

Tại nguồn evidence đã chọn, nhận diện baseline/layout, asset brief, manifest nếu có, source/derived asset, code/config, fixture và môi trường ảnh hưởng kết luận; evidence là quan sát kiểm tra thật. Không cần kê mọi file dự án. Chỉ khi chọn profile JSON mới cần danh sách inputs/hash theo schema; không bỏ dependency quan trọng để giữ hash ổn định.

## Giới hạn của bản v1.1

Manifest, IDs và route sản xuất là hợp đồng làm việc cho người/agent. Khi profile JSON được chọn rõ, `design_check.py` kiểm tra verification JSON và hash của file khai báo; nó không chạy image generation, kiểm tra schema assets.json, tự nối ID baseline/layout/asset hoặc đánh giá tính nhất quán hình ảnh. Đọc evidence và review nội dung vẫn là trách nhiệm của người thực hiện.
