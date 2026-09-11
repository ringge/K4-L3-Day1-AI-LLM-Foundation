from template import call_openai
from template import call_openai_mini
from template import compare_models
from template import chat_with_system_prompt
from template import count_tokens
from template import streaming_chatbot

# call_openai(prompt="Hãy kể cho tôi một sự thật thú vị về Việt Nam", temperature=1.5)
# call_openai_mini("hello world")
# compare_models(prompt="hello how are you")
# chat_with_system_prompt(
#     system_prompt="Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi.",
#     user_prompt="Giải thích blockchain là gì?"
# )
# chat_with_system_prompt(
#     system_prompt="Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật.",
#     user_prompt="Giải thích blockchain là gì?"
# )
vietnamese_text = (
    "Trí tuệ nhân tạo đang thay đổi cách con người học tập và làm việc mỗi ngày. "
    "Một trợ lý thông minh có thể tóm tắt tài liệu, giải thích khái niệm khó, dịch "
    "ngôn ngữ và gợi ý ý tưởng mới. Tuy nhiên, người dùng vẫn cần kiểm tra thông tin "
    "vì mô hình đôi khi tạo ra câu trả lời nghe hợp lý nhưng không chính xác. Khi sử "
    "dụng công nghệ này, chúng ta cũng phải chú ý đến quyền riêng tư, bản quyền và sự "
    "công bằng. Trí tuệ nhân tạo phát huy giá trị tốt nhất khi hỗ trợ con người suy "
    "nghĩ, thay vì thay thế hoàn toàn trách nhiệm của con người."
)
word_count = len(vietnamese_text.split())
token_count = count_tokens(text=vietnamese_text, model="gpt-4o")
estimated_tokens = word_count / 0.75
percentage_difference = abs(token_count - estimated_tokens) / estimated_tokens * 100
print(f"Số từ: {word_count}")
print(f"Số token ước lượng: {estimated_tokens:.2f}")
print(f"Chênh lệch: {percentage_difference:.2f}%")
# streaming_chatbot()
