# Bản định hướng chung của dự án

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-BASELINE` |
| Phiên bản template | `1.1.0` |
| Mục đích | Ghi hướng thiết kế xuyên màn đang được chọn, revision áp dụng và các nguồn hợp đồng cần giữ nhất quán. |
| Dùng khi | Cần chốt hoặc cập nhật hướng chung cho nhiều màn, platform, component hay asset trong cùng scope. |
| Đầu vào | Brief, quyết định và phương án nguồn, hợp đồng domain/experience, design system và reference có căn cứ. |
| Đầu ra / bàn giao | Baseline có trạng thái lựa chọn riêng, nguồn canonical theo chủ đề và danh sách phần bị ảnh hưởng khi thay đổi. |
| Nguồn chuẩn | Chỉ giữ các lựa chọn xuyên màn được đăng ký cho baseline; domain, feature, UI contract và acceptance giữ nguồn riêng đã chọn. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Màn, flow, platform và revision baseline được áp dụng] |

[Chuẩn template](../documentation/template-standard.md).

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

Placeholder chỉ là chỗ điền, không phải bằng chứng hay sự kiện đã xảy ra. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu theo dõi bản đã điền của dự án. Nếu cần lifecycle tài liệu, có thể dùng `draft`, `reviewed`, `accepted`, `superseded` hoặc quy ước hiện hữu, độc lập với trạng thái quyết định, verdict review và verification; `accepted` không tự ghi nhận phê duyệt của người dùng, kết quả kiểm chứng hoặc quyền phát hành.

- Baseline ID / revision: B-01 / 1
- Trạng thái baseline: proposed / selected / superseded
- Decision ID và phương án nguồn:
- Outcome / criterion IDs:
- Ngày và vai trò quyết định:

`selected` là hướng đang dùng, không phải kết quả kiểm chứng. Các ID là tham chiếu để review; checker hiện không tự kiểm tra chúng.

## Tài liệu canonical

| Chủ đề | File/vị trí đang giữ quyết định |
| --- | --- |
| Domain, thuật ngữ, scope | |
| Flow, state, navigation, hành vi | |
| Layout theo màn và không gian | |
| Token, component, copy, motion | |
| Asset manifest và brief | |

## Reference

| Reference / revision | Vai trò và điều giữ | Điều chuyển đổi hoặc không kế thừa | Nguồn / provenance |
| --- | --- | --- | --- |
| | | | |

Có thể dùng artifact, design system hoặc mô tả contract hiện có. Nêu đâu là concept, đâu là render của implementation thật.

## Quy ước xuyên màn

Quy tắc đã có nguồn chuẩn trong domain, feature hoặc UI contract chỉ được dẫn chiếu cùng revision. Chỉ định nghĩa tại đây phần được đăng ký cho baseline; không tạo lại rule nghiệp vụ để làm đầy bảng.

| Nhóm | Quy tắc | Lý do / criterion | Ngoại lệ có phạm vi |
| --- | --- | --- | --- |
| Domain và thuật ngữ | | | |
| Navigation và selection | | | |
| Lưu/hủy/error/draft | | | |
| Hierarchy, type, color roles | | | |
| Component, imagery, icon family | | | |
| Accessibility, motion, platform | | | |

## Thay đổi revision

- Điều thay đổi và lý do:
- Màn, layout, component, asset và evidence cần xem lại:
- Điều kiện cần mở lại quyết định:
- Kiểm chứng còn `partial` hoặc `not-tested`, cùng lý do/coverage còn thiếu:

## Kiểm tra trước bàn giao

- [ ] Baseline/decision refs, revision và thông tin thời điểm có ích được giữ rõ; không dùng metadata tài liệu làm bằng chứng quyết định đã được chấp nhận.
- [ ] Mỗi chủ đề trỏ tới nguồn đang áp dụng; rule domain/feature đã có không được định nghĩa lại trong baseline.
- [ ] Quy ước xuyên màn phục vụ task và có ngoại lệ rõ phạm vi khi cần.
- [ ] Reference có provenance; concept và render từ implementation thật được phân biệt.
- [ ] Thay đổi revision nêu phần UI, asset và evidence cần xem lại, cùng giới hạn chưa kiểm chứng.
