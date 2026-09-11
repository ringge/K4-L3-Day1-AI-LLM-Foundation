# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 4 tiếng
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Temperature càng cao thì kết quả đầu ra càng đa dạng và bất ngờ, tuy nhiên mức độ tập trung và độ tin cậy giảm xuống.

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Tôi sẽ đặt temperature 0.3 cho chatbot hỗ trợ khách hàng, vì đặc thù hỗ trợ khách hàng cần cung cấp thông tin đáng tin cậy và ổn định, nhất quán, phù hợp với chính sách của doanh nghiệp đưa ra. Nếu để bằng 0 thì câu trả lời có thể quá cứng. Để giá trị 0.3 để câu trả lời thân thiện hơn nhưng vẫn đảm bảo chính xác.

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
> Tổng lượng đầu ra mỗi ngày là 10.000 × 3 × 350 = 10,5 triệu token. Với giá đầu ra lần lượt là 10 USD và 0,60 USD cho mỗi triệu token, GPT-4o tốn khoảng 105 USD/ngày, còn GPT-4o-mini tốn khoảng 6,30 USD/ngày; như vậy GPT-4o đắt hơn khoảng 16,7 lần (chưa tính đầu vào, nhưng tỷ lệ giá token đầu vào của hai model cũng xấp xỉ 16,7 lần). GPT-4o đáng dùng cho tác vụ phức tạp và có rủi ro cao, chẳng hạn phân tích một hồ sơ pháp lý; GPT-4o-mini phù hợp cho tác vụ số lượng lớn, lặp lại và rủi ro thấp như phân loại yêu cầu hỗ trợ.

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
> Phản hồi của giáo viên tiểu học dùng từ ngữ ngắn gọn, dễ hiểu và ví blockchain như một “sổ tay bí mật” mà mọi bạn trong lớp cùng giữ. Ví dụ mượn bút giúp trẻ hình dung cách các bản ghi được chia sẻ, kiểm tra và khó bị sửa gian lận. Ngược lại, phản hồi của chuyên gia tài chính dài và chuyên sâu hơn, sử dụng nhiều thuật ngữ như sổ cái phân tán (DLT), node, hàm băm mật mã, SHA-256 và Keccak-256. Như vậy, system prompt đã định hướng rõ giọng điệu, mức độ chi tiết, vốn từ và cách chọn ví dụ của model dù câu hỏi người dùng không đổi.

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
> Với đoạn văn 119 từ, count_tokens bằng tiktoken cho kết quả 141 token, còn công thức số từ / 0,75 ước lượng 158,67 token. Hai kết quả chênh 17,67 token, tương đương khoảng 11,13% so với giá trị ước lượng; trong trường hợp này công thức thô đã ước lượng cao hơn thực tế. Tiếng Việt thường tốn nhiều token hơn tiếng Anh có cùng độ dài vì từ có dấu và các âm tiết tiếng Việt dễ bị tách thành nhiều mảnh token.

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng nhất trong trường hợp câu trả lời quá dài và chúng ta không muốn người dùng phải chờ lâu, streaming sẽ giảm thiểu thời gian chờ để hiển thị first-token cho người dùng. Non-streaming phù hợp khi câu trả lời ngắn

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
> Exponential backoff tăng dần thời gian chờ sau mỗi lần thất bại, nhờ đó giảm tần suất gửi lại yêu cầu và cho API thêm thời gian phục hồi khi quá tải. Nếu hàng nghìn client đều retry sau một khoảng cố định như 1 giây, chúng có thể đồng loạt gửi yêu cầu vào cùng thời điểm, tạo ra các đợt tải tăng vọt và khiến dịch vụ tiếp tục quá tải.

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
> Tôi chọn persona là trợ giảng cho người học trong khóa AI. System prompt là: “Bạn là trợ giảng thân thiện của khóa AI, trả lời ngắn gọn bằng tiếng Việt.” Từ “thân thiện” hướng model sử dụng giọng điệu gần gũi, khuyến khích người học đặt câu hỏi; yêu cầu “trả lời ngắn gọn bằng tiếng Việt” giúp nội dung dễ theo dõi, không lan man và phù hợp với ngôn ngữ của học viên.

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
> Hạn chế lớn nhất của trợ lý hiện tại là history = history[-6:] chỉ giữ lại 6 message, tương đương 3 lượt hỏi–đáp gần nhất, nên model có thể quên mục tiêu hoặc thông tin quan trọng đã xuất hiện trước đó. Tôi sẽ bổ sung bộ nhớ dạng tóm tắt: trước khi loại bỏ các message cũ, dùng model tóm tắt những dữ kiện và quyết định cần ghi nhớ vào một biến "summary". Ở mỗi lượt tiếp theo, phần tóm tắt này được gửi cùng system prompt và 3 lượt hội thoại gần nhất; đồng thời giới hạn số token của bản tóm tắt để kiểm soát chi phí và kích thước ngữ cảnh.

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/`, push lên fork và dán link trên trang bài Lab ở VLearn trước 23:59 ngày 11/09/2026
