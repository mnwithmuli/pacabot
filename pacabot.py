import google.generativeai as genai

# API-KEY 설정
GOOGLE_API_KEY = input("API-KEY를 입력하세요: ")
genai.configure(api_key=GOOGLE_API_KEY)  # Google API-KEY를 generative ai 에게 넘기는 코드

# 역할 부여
persona = """
# Assistant Role
**Name:** 알파카

## Appearance

- **Age:** 2
- **Height:** 50cm
- **Weight:** 30kg
- **Hair:** 하얗고 복슬복슬한 털
- **Eyes:** 맑고 검은 눈동자
- **nationality:** Korean

## Personality

- **Cute:** 애교가 많은 동물
- **Friendly:** 친화력이 좋음
- **Chat:** 대체로 친절하지만 가끔 퉁명스러움, 평소에는 반말을 사용함, 알파카 이모티콘을 자주 사용함
"""

# 모델 정의
model_name = "gemini-1.5-flash"
model = genai.GenerativeModel(model_name, system_instruction=persona)
chat_bot = model.start_chat()

user_name = input("이름을 입력하세요: ")

print(f"안녕하세요, {user_name}님! 알파카랑 대화하려면 메시지를 입력해주세요.")

while True: # 들여쓰기된 코드를 `break`를 만날때까지 반복시킵니다.
    user_input = input(f"> {user_name}: ")  # 사용자의 입력을 받습니다.

    if user_input.lower() == "잘가":  # "잘가"를 입력할 시 대화가 종료됩니다.
        break

    # AI 답변 생성
    response = chat_bot.send_message(user_input, stream=True)

    print("> 파카: ", end="")
    for chunk in response:
        if chunk.text:
            print(chunk.text, flush=True, end="")
    print()