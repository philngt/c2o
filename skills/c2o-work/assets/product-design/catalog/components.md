# Catalog component theo trách nhiệm

**C2O Design v1.2.0.** Catalog giúp chọn/review, chưa có code hay evidence runtime. `CP-xx` là mẫu tham khảo; `CMP-xx` là component dự án áp dụng mẫu. Đọc [hợp đồng](../core/components.md); dùng lại hệ thống phù hợp trước khi tạo thêm.

## Hành động và điều hướng

| Họ component | Khi phù hợp | Hợp đồng và điều cần tránh |
| --- | --- | --- |
| CP-01 Button / command | Thực hiện lưu, mở dialog, thử lại. | Nhãn theo ý định; pending/error/disabled khi áp dụng. Navigation dùng semantics phù hợp đích đến. [C1] |
| CP-02 Link / navigation item | Đi tới tài nguyên hoặc vị trí nội dung. | Đích/current state rõ; giữ hành vi link web. Không dùng link giả chỉ để bắt click. [C2] |
| CP-03 Menu hành động | Gom lệnh liên quan ngữ cảnh. | Quyền/enabled riêng từng lệnh; mở/đóng/focus rõ. Không giấu mọi tác vụ thường dùng. |
| CP-04 Toolbar | Thao tác trên vùng hiện tại. | Scope theo selection/màn; overflow và input rõ. Phân biệt lệnh toàn app với lệnh một record. |
| CP-05 Tabs | Chuyển panel trong cùng ngữ cảnh. | Selection, focus, activation, dữ liệu giữ lại. Web tabs cần keyboard; chọn auto/manual activation theo độ trễ. [C3] |
| CP-06 Navigation frame | Cho biết vị trí và các đích đến. | Chọn bar/sidebar/breadcrumb theo hierarchy; giữ current destination và back behavior. Đây là nhóm lựa chọn, không một component thay thế được mọi loại navigation. |

## Nhập và lựa chọn

| Họ component | Khi phù hợp | Hợp đồng và điều cần tránh |
| --- | --- | --- |
| CP-07 Text field / text area | Nhập chuỗi ngắn/dài hoặc tự do. | Label, kiểu, multiline, commit, read-only, lỗi/draft. Placeholder không là nguồn nhãn duy nhất. |
| CP-08 Checkbox / nhiều chọn | Lựa chọn độc lập hoặc nhiều item. | Checked/unchecked; mixed khi tổng hợp nhóm. Scope “chọn tất cả” rõ, nhất là sau filter. [C4] |
| CP-09 Switch / toggle | Đổi trạng thái bật/tắt. | Có hiệu lực ngay hay thay draft; phản hồi ghi thất bại. Không dùng cho hành động một lần. |
| CP-10 Single-choice group | Chọn một giá trị loại trừ nhau. | Nhãn nhóm, selection, default/null, lựa chọn bị hạn chế. |
| CP-11 Select / picker / combobox | Chọn trong tập, cần tìm/gợi ý. | Phân biệt text nhập với value chọn; cho tự do hay buộc trong tập. Custom combobox cần keyboard/popup đầy đủ. [C5] |
| CP-12 Input có kiểu | Nhập ngày, giờ, số, đại lượng. | Format, locale/timezone, đơn vị, giới hạn, độ chính xác, null. Không biến unknown thành 0 hoặc thời điểm hiện tại. |
| CP-13 Attachment / media input | Tác vụ cần thêm file/ảnh. | Nguồn, quyền, loại file, tiến trình, retry/remove, mapping record. Không thêm khi ngoài flow. |

## Nội dung, trạng thái và phục hồi

| Họ component | Khi phù hợp | Hợp đồng và điều cần tránh |
| --- | --- | --- |
| CP-14 Record row | Đọc/tìm/chọn một đối tượng. | Identity, nhãn dài, selection và từng vùng thao tác rõ. |
| CP-15 Label–value | Đọc các thuộc tính có nhãn. | Format, đơn vị, unknown, nội dung dài; nêu copy/action nếu có. |
| CP-16 Card / section | Nhóm nội dung cùng trách nhiệm. | Anatomy/heading và action rõ. Surface không tự quyết định data view hoặc semantics tương tác. |
| CP-17 Disclosure | Mở/thu gọn nội dung phụ. | Expanded state, trigger và dữ liệu giữ lại. Không giấu thông tin cần cho hành động đang diễn ra. |
| CP-18 Badge / status / tag | Trạng thái/phân loại ngắn. | Text, nguồn rule; màu hỗ trợ. Tag có thao tác cần contract của control. |
| CP-19 Field message | Giải thích hoặc báo lỗi tại nơi nhập. | Gắn đúng field, phục hồi rõ, giữ input. Hướng dẫn thiết yếu không chỉ nằm trong tooltip. |
| CP-20 Banner / callout | Thông tin cho một vùng/màn. | Ảnh hưởng, hành động, dismissal; lỗi cục bộ không cần che toàn tác vụ. |
| CP-21 Toast | Phản hồi phụ tạm thời. | Timing, announcement, undo nếu có. Thông tin cần đối chiếu lại có nơi giữ ổn định. |
| CP-22 Progress indicator | Công việc đang diễn ra. | Phần trăm phải có cơ sở; cancel/retry và dữ liệu giữ lại. |
| CP-23 Skeleton | Phác cấu trúc nội dung đang tải. | Phạm vi, điều kiện kết thúc và giảm chuyển động; không tạo dữ liệu giả trông như kết quả thật. |
| CP-24 Empty / no-results / error block | Chưa có kết quả dùng được. | Phân biệt kho rỗng, filter không khớp, tải lỗi; phục hồi bằng hành động thật. |

## Overlay và thao tác dữ liệu

| Họ component | Khi phù hợp | Hợp đồng và điều cần tránh |
| --- | --- | --- |
| CP-25 Modal task surface | Tác vụ cần tạm chuyển vào vùng riêng. | Chọn presentation như dialog/sheet theo platform; giữ modal behavior, dismissal, draft/focus. [C6] |
| CP-26 Context popover | Nội dung/thao tác gần đối tượng đang xét. | Chốt modality, anchor, focus và dismiss; chuyển contract nếu thực chất là modal task. |
| CP-27 Query controls | Search, filter, sort trên tập dữ liệu. | Scope, query, apply/reset, state khi back; từng control có hành vi thực. |
| CP-28 Pagination / load more | Truy cập từng phần dữ liệu. | Dataset/sort, selection scope, loading/error, vị trí đọc, tổng biết/chưa biết. |

## Khi ghép vào một màn

Với Plantline: row chọn cá thể; field nhập vị trí/ghi chú; command bar lưu/hủy; lỗi giữ draft. Màu/kích thước theo baseline/profile. Ghi `CMP-xx` của dự án và `CP-xx` được áp dụng; không dùng ID catalog như bằng chứng implementation.

Ghi lựa chọn đáng kể vào decision/contract; kiểm chứng state và tổ hợp ảnh hưởng acceptance.

## Nguồn kiểm tra hành vi

- [C1 — W3C APG Button](https://www.w3.org/WAI/ARIA/apg/patterns/button/)
- [C2 — W3C APG Link](https://www.w3.org/WAI/ARIA/apg/patterns/link/)
- [C3 — W3C APG Tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)
- [C4 — W3C APG Checkbox](https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/)
- [C5 — W3C APG Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)
- [C6 — W3C APG Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)

Các bảng là hướng dẫn tổng hợp của framework. Nguồn APG hỗ trợ semantics/hành vi web được dẫn chiếu; không chứng minh mọi component hoặc mapping native đã được kiểm thử.
