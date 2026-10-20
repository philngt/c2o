# Hồ sơ phát hành và vận hành — [sản phẩm / bản phát hành]

## Hợp đồng tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Template ID | `TPL-RELEASE-OPERATIONS` |
| Phiên bản template | `1.1.0` |
| Mục đích | Nối một artifact phát hành với scope, evidence, nội dung phân phối, quyền thực hiện và cách hỗ trợ/phục hồi phiên bản đó. |
| Dùng khi | Phạm vi được giao có chuẩn bị phân phối, phát hành hoặc vận hành một phiên bản cụ thể; không tự thêm release cho nhiệm vụ chỉ thiết kế hoặc tạo starter. |
| Đầu vào | Scope/requirements đã chọn, artifact/version/targets, verification records, asset/metadata thực, cấu hình capability và quyền thực hiện hiện có. |
| Đầu ra / bàn giao | Hồ sơ release có tham chiếu evidence, phần nội dung/cấu hình/recovery còn thiếu và owner, quyết định phân phối cùng receipt nếu hành động đã thực sự xảy ra. |
| Nguồn chuẩn | Chỉ giữ thông tin release và vận hành khi được đăng ký cho vai trò đó; PRD/brief, technical contracts, nguồn acceptance đã chọn và nguồn kết quả/evidence đã chọn tiếp tục giữ các chủ đề tương ứng. |
| Owner | [Vai trò/người chịu trách nhiệm] |
| Revision tài liệu | [revision của tài liệu dự án] |
| Ngày cập nhật | [YYYY-MM-DD] |
| Trạng thái tài liệu | `draft` |
| Phạm vi áp dụng | [Sản phẩm/bản phát hành, artifact, targets và phần vận hành được giao] |

[Chuẩn template](../../documentation/template-standard.md): placeholder là chỗ cần xác định, không phải evidence. Phiên bản template mô tả cấu trúc mẫu; revision tài liệu ghi lần thay đổi của bản dùng trong dự án, không phải cùng một số phiên bản.

Dùng tùy chọn trong C2O: có thể lấy một section hoặc dùng artifact hiện hữu mà không sao metadata, tạo index, `.design` hay JSON. Giữ scope và nguồn acceptance/evidence đã chọn; chỉ profile JSON được chọn rõ mới dùng schema/record của gói cũ. Báo cáo C2O giữ `pass / partial / fail / not-tested`, không đổi bằng chứng một phần thành pass.

## Mục đích, khi dùng và cách dùng

Nếu chỉ thiết kế hoặc tạo starter, chỉ ghi phần liên quan và điều còn thiếu; không biến nhiệm vụ thành một đợt phát hành.

Đọc [hướng dẫn tài liệu](../../documentation/README.md). Tái sử dụng hồ sơ release/runbook đang có; có thể đặt các section cần thiết trong một tài liệu hiện hữu và đăng ký chúng ở [document index](document-index.md). Các ô trống là nội dung cần xác định, không phải xác nhận đã hoàn thành. Bỏ mục không áp dụng kèm lý do theo phạm vi thật.

- Tài liệu thay thế hoặc được thay thế:

`accepted` nghĩa là hồ sơ được chọn dùng trong quyền hạn hiện có. Nó không xác nhận native pass, không ghi nhận một người đã phê duyệt khi chưa có bằng chứng, và không tự cấp quyền publish/deploy.

## 1. Bản phát hành đang được chuẩn bị

| Trường | Giá trị và nguồn chuẩn |
| --- | --- |
| Sản phẩm, phiên bản hiển thị, build/release identifier | |
| Commit/tag và artifact dự kiến phát hành | |
| Outcome `OUT-…` và phạm vi được nhận | [Tham chiếu PRD/scope section của pack; brief cho phạm vi task cụ thể] |
| Feature `F-…`, requirement `REQ-…`, slice `SL-…` trong release | |
| Thay đổi dữ liệu/luật `ENT-…`, `BR-…` | |
| Platform, deployment target và cấu hình phân phối | |
| Device/window, theme, locale thực sự được hỗ trợ | |
| Phần hoãn lại và giới hạn công bố cho người dùng | |
| Thay đổi kể từ bản đã phân phối gần nhất | |

Trỏ tới [PRD](prd.md), [feature spec](feature-spec.md), [technical spec](technical-spec.md) và [delivery plan](delivery-plan.md) của dự án; các link trong mẫu là mẫu tham khảo. PRD/scope section đã đăng ký giữ phạm vi phiên bản, brief giữ phạm vi task; hồ sơ này nhận diện phần đã chọn cho artifact phân phối. Không viết một scope mới trong release notes để thay scope đã chọn. Nếu scope hoặc tiêu chí thay đổi, xử lý ở nguồn chuẩn và xem lại evidence trước.

## 2. Bằng chứng cho artifact hiện tại

- Nguồn acceptance đã chọn của dự án và revision/observed state áp dụng:
- Báo cáo nguồn kết quả/evidence đã chọn và bản artifact được đánh giá:
- Review có phạm vi rõ và các giới hạn còn mở:
- Môi trường native/web, dữ liệu và cấu hình đã kiểm tra được ghi ở:

| Phần cần đánh giá | Criterion IDs hiện có | Report và vị trí record/evidence | Artifact/cấu hình được bao phủ | Việc còn phải giải quyết / owner |
| --- | --- | --- | --- | --- |
| Tác vụ và dữ liệu trong release | | | | |
| Platform, accessibility, locale có liên quan | | | | |
| Persistence, migration, recovery có liên quan | | | | |
| Extension, capability hoặc dịch vụ thực sự có | | | | |

Nguồn acceptance đã chọn giữ ID, nghĩa, nguồn/rationale, tính bắt buộc, applicability và phương pháp; nguồn kết quả/evidence đã chọn giữ kết quả, artifact/revision, quan sát và giới hạn thực. Bảng này chỉ dẫn tới chúng, không tạo bảng kết quả cạnh tranh có thể cũ. Chi tiết expected behavior thuộc feature spec; phương pháp/coverage thuộc [validation plan](validation-plan.md). Áp dụng [hợp đồng evidence](../../core/evidence.md).

Đọc bằng chứng gắn với đúng build/configuration. Build thành công chưa chứng minh interaction; screenshot chưa chứng minh persistence; nếu dùng profile JSON, `RECORDS_READY` chưa chứng minh chất lượng toàn app hoặc quyền phát hành. Với Apple starter, [NATIVE_CHECKS](../../starters/apple/NATIVE_CHECKS.md) là kế hoạch để chọn phép kiểm tra phù hợp, không phải kết quả đã chạy.

## 3. Catalog nội dung phân phối

Chỉ chọn những mục kênh phân phối và sản phẩm thực sự cần. Ghi nguồn yêu cầu chính thức cùng ngày đối chiếu khi có ràng buộc thay đổi theo kênh; không dùng một danh sách chung như chứng nhận tuân thủ store/pháp lý.

| Mục | File/URL hoặc vị trí quản lý thật | Locale/target/phiên bản áp dụng | Nguồn nội dung và giới hạn tuyên bố | Việc còn thiếu / owner |
| --- | --- | --- | --- | --- |
| Tên, mô tả ngắn/dài, phân loại và metadata khác nếu kênh yêu cầu | | | | |
| Release notes và thông tin tương thích | | | | |
| App icon và biến thể cần xuất | | | | |
| Screenshots / preview của app thực | | | | |
| Chuỗi dịch, nội dung địa phương hóa và người review nếu có | | | | |
| Support URL, kênh liên hệ và nội dung trợ giúp | | | | |
| Privacy URL và mô tả xử lý dữ liệu | | | | |
| Khai báo capability, quyền truy cập hoặc nội dung khác theo kênh | | | | |

Screenshot cần khớp app/build, màn/state, locale và cấu hình đang công bố. Dữ liệu minh họa phải được nhận diện phù hợp, không đại diện cho kết quả người dùng thật. Source artwork, file export và file đã tích hợp là các artifact khác nhau; nối với asset manifest/baseline hiện có nếu chúng ảnh hưởng kết luận.

Privacy/support copy phải phản ánh tính năng, dữ liệu, dịch vụ và cách hỗ trợ đang có. Không hứa sync, backup, mã hóa, lưu trữ, hỗ trợ hoặc analytics chỉ vì template có một dòng tương ứng. Không mặc định đưa notes, input/output, screenshot người dùng hoặc định danh cá nhân vào log/metadata. Khai báo pháp lý hoặc store cụ thể cần được đánh giá theo dữ kiện, thị trường và yêu cầu thực tế của dự án.

## 4. Signing, capability và cấu hình môi trường

| Target/dịch vụ | Identity và cấu hình cần khớp | Capability/entitlement thực sự dùng | Nơi giữ cấu hình an toàn / owner | Bằng chứng kiểm tra và vấn đề còn mở |
| --- | --- | --- | --- | --- |
| Host app / client | | | | |
| Extension nếu có | | | | |
| Backend hoặc dịch vụ ngoài nếu có | | | | |

Ghi team/account/role và vị trí quản lý credential theo quy ước dự án; không chép secret, private key hoặc token vào tài liệu. Đối chiếu signed artifact, endpoint, bundle/application ID và capability trên môi trường phát hành thực. File entitlement/config được sinh ra chưa chứng minh provisioning hoặc runtime access hoạt động.

Với widget Apple, chỉ đánh giá khi đã đưa widget vào scope: host/extension/group/kind khớp, snapshot đúng dữ liệu được phép, fallback trung thực và route hợp lệ. Không mô tả App Group là sync giữa thiết bị hoặc snapshot widget là backup của app.

## 5. Migration, restore và phục hồi

- Phiên bản schema/dữ liệu đầu vào được hỗ trợ và `ENT-…`/`BR-…` liên quan:
- Dữ liệu giữ nguyên, chuyển đổi, loại bỏ hoặc cần người dùng quyết định:
- Hành vi khi đọc lỗi, write thất bại hoặc migration bị gián đoạn:
- Backup/export/restore đang thực sự có; nếu chưa có, giới hạn cần công bố:
- Điều kiện kích hoạt recovery, owner và đường liên lạc:

| Tình huống | Cách bảo vệ/khôi phục dữ liệu đã chọn | Điều kiện và giới hạn | Evidence/criterion liên quan | Bước thực hiện hoặc runbook |
| --- | --- | --- | --- | --- |
| Nâng cấp từ phiên bản được hỗ trợ | | | | |
| Migration/load/write bị lỗi | | | | |
| Restore từ nguồn backup/export hợp lệ, nếu đã hỗ trợ | | | | |
| Phát hiện lỗi nghiêm trọng sau phát hành | | | | |

Chốt riêng khả năng đưa binary cũ trở lại và khả năng binary đó đọc dữ liệu sau migration. Không ghi “rollback được” chỉ vì còn file build cũ. Khi rollback dữ liệu không được hỗ trợ hoặc chưa kiểm chứng, chọn một chiến lược có thể thực hiện như dừng rollout, giữ dữ liệu và phát hành bản sửa; nêu điều còn chưa biết. Tránh thao tác khôi phục làm ghi đè dữ liệu gốc trước khi xác định đường phục hồi.

## 6. Phân phối, readiness và quyền thực hiện

| Quyết định | Nội dung / tham chiếu |
| --- | --- |
| Kênh: nội bộ, thử nghiệm, store, trực tiếp hoặc kênh dự án chọn | |
| Nhóm người dùng, vùng/locale, phạm vi rollout | |
| Thời điểm hoặc cửa sổ phát hành, nếu đã quyết định | [Không tự đặt ngày khi chưa có căn cứ] |
| Artifact đã đóng gói và cách nhận diện đúng bản | |
| Điều kiện bắt đầu, dừng hoặc thu hẹp rollout | |
| Review readiness theo scope | [Trỏ tới review và evidence đã đọc; ghi khoảng trống cần giải quyết] |
| Quyền thực hiện đang có | [Yêu cầu người dùng/quy ước dự án/người có thẩm quyền; hành động và giới hạn cụ thể] |
| Người/agent thực hiện và nơi ghi receipt phát hành | |

Readiness và authorization là hai câu hỏi riêng. `ready`, `accepted` hoặc checker exit 0 không tự cấp quyền gửi build, publish, deploy hay thông báo cho người khác. Dùng quyền đã có trong nhiệm vụ/quy ước dự án; không xin lại quyền hợp lệ và không đặt một vòng phê duyệt mới chỉ vì có template. Nếu hành động còn ngoài quyền hiện có, chuẩn bị artifact cùng phạm vi cụ thể để quyết định cuối cùng có thể review được.

Sau khi thực hiện, ghi receipt có thật: kênh, phiên bản/build, artifact, thời gian, phạm vi rollout và người thực hiện. Không điền các giá trị này như sự kiện đã xảy ra khi mới lên kế hoạch.

## 7. Hỗ trợ, sự cố và đo lường sau phát hành

| Trách nhiệm | Kênh/owner hiện có | Tín hiệu hoặc điều kiện hành động | Cách xử lý và giới hạn |
| --- | --- | --- | --- |
| Hỗ trợ người dùng | | | |
| Triage lỗi và phản hồi | | | |
| Sự cố ảnh hưởng task/dữ liệu | | | |
| Quyết định hotfix/dừng rollout | | | |

Với sự cố, ghi phiên bản/configuration bị ảnh hưởng, quan sát có thể tái hiện, tác động, biện pháp ngăn ảnh hưởng lan rộng, cách giữ dữ liệu và bước xác nhận phục hồi. Thu thập dữ liệu chẩn đoán vừa đủ theo cơ chế hiện có; không yêu cầu gửi toàn bộ nội dung riêng tư để thay cho việc xác định lỗi. Khi cần liên hệ bên ngoài, quyền gửi thông điệp vẫn theo nhiệm vụ thực.

| Câu hỏi gắn `OUT-…`/`ASM-…` | Chỉ số/phản hồi và nguồn dữ liệu thực | Dữ liệu thu thập, quyền/notice nếu áp dụng | Lưu giữ, truy cập, owner | Khi nào xem lại quyết định |
| --- | --- | --- | --- | --- |
| | | | | |

Không có telemetry thì ghi nguồn phản hồi thủ công hoặc “chưa có dữ liệu”; không bịa baseline, mục tiêu số, tỷ lệ thành công hay độ phủ crash reporting. Thêm analytics là một quyết định sản phẩm/dữ liệu riêng. Chỉ đo thứ cần để giải quyết câu hỏi đã nêu và không suy số lượng mở app thành outcome người dùng đã đạt.

## Điều kiện hoàn thành hồ sơ

- Release scope, version, targets và artifact được nhận diện; có link tới nguồn chuẩn đang áp dụng.
- Các câu hỏi readiness liên quan dẫn tới evidence hiện hành hoặc khoảng trống có owner; không có bản sao kết quả mâu thuẫn với verification report.
- Nội dung phân phối, cấu hình/capability, migration/recovery và hỗ trợ được xử lý trong phạm vi thực; phần thiếu ghi rõ.
- Quyền thực hiện đã được xác định theo context, hoặc hành động ngoài quyền được ghi cụ thể; chưa thực hiện thì chưa có receipt giả.
- Những thay đổi sau phát hành được đưa về nguồn chuẩn và các slice/criterion bị ảnh hưởng qua [document index](document-index.md) và [delivery plan](delivery-plan.md).

Hoàn thành hồ sơ không đồng nghĩa đã phát hành hoặc đã kiểm thử. Hướng dẫn workflow và cách kết luận theo scope nằm ở [core/workflow.md](../../core/workflow.md).

## Kiểm tra trước bàn giao

- [ ] Scope, version/build, targets và artifact của release đã được nhận diện hoặc ghi rõ phần còn thiếu; chúng dẫn tới đúng nguồn chuẩn/revision.
- [ ] Readiness dẫn tới verification record/evidence hiện hành và khoảng trống có owner; không có bảng pass/fail cạnh tranh hoặc receipt phát hành giả.
- [ ] Catalog nội dung phản ánh app/build/locale/kênh thực; các tuyên bố privacy/support/capability không vượt dữ kiện đã có.
- [ ] Signing/cấu hình và migration/recovery có owner, giới hạn và cách kiểm chứng liên quan; khả năng rollback binary không bị dùng thay cho recovery dữ liệu.
- [ ] Quyền thực hiện và giới hạn rollout được ghi riêng với readiness, dùng authorization hiện có; không suy quyền publish hoặc gửi thông điệp từ `accepted` hay checker exit 0.
- [ ] Support/incident và metric/feedback có nguồn thực, dữ liệu cần thu rõ hoặc ghi chưa có; việc thiếu telemetry không bị che bằng số liệu giả.
