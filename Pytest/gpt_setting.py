import openai as oi 

# oi.api_key = "sk-proj-iTQctJvnxIETFsmbxWbRT3BlbkFJiqlmixKGjW1vBEgNdVab"
oi.api_key = "sk-proj-WzIygSxDJhkABeWaXY0ZT3BlbkFJJ2bYIBf6gN0RlXolWKia" #개인용 key 입력

def create_completion(messages):
    #try catch문 : 실패할 확률 있는 경우
    try:
        return oi.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages #gui 파일의 GPT에게 보내는 메세지
        )
    #except : 안되는 경우
    except oi.OpenAIError as e:
        print("GPT ERROR: ", str(e))
        return None #반환값 없음

class basic_condition:
    condition_text = (
        "If the user asks for a URL, provide the URL in this format: **URL**. "
        "If the user asks to open a URL, provide the URL in this format: **URL**. "
        "Here's an example: **www.openai.com**. "
        "URL is website adress. "
        "If the user asks to open a URL in Chrome, provide a direct URL."
    )