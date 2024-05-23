#  OpenAI API와 상호작용
import os # os모듈 불러오기
import openai as oi # openai 라이브러리를 oi이름으로 불러오기

# 키 설정
oi.api_key="sk-proj-WzIygSxDJhkABeWaXY0ZT3BlbkFJJ2bYIBf6gN0RlXolWKia"

# complation 변수 설정
complation = oi.ChatCompletion.create( #메서드 호출 / ChatCompletion 객체 생성 / 
    model = "gpt-3.5-turbo",
    messages = [
        {"role":"user", "comtent": "니 이름이 뭐야?"}
    ]
)
print(complation.choices[0].message.content)