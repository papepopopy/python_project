from tkinter import Tk, Label, Entry, Button, Text #내부모듈 사용

from gpt_setting import create_completion, basic_condition
from chrome_setting import open_url_in_chrome

def link_from_response(response):
    if '**' in response: #** 다음부터 url
        start_of_link = response.find('**') + 2 
        end_of_link = response.find('**', start_of_link)
        return response[start_of_link:end_of_link].strip() #response 반환
    return None

def submit_query(entry, text_widget):
    user_input = entry.get() #entry 사용자 입력 값 가져오기

    condition_text = (
        "If the user asks for a URL, provide the URL in this format: **URL**. "
        "If the user asks to open a URL, provide the URL in this format: **URL**. "
        "Here's an example: **www.openai.com**. "
        "URL is website adress. "
        "If the user asks to open a URL in Chrome, provide a direct URL."
    )

    messages = [ #GPT에게 보내는 메세지
        {"role": "user", "content": condition_text}, #질문자 : 답변자
        {"role": "user", "content": user_input}
    ]

    completion = create_completion(messages) #답변

    if completion:
        #제이슨 형태로 나오기에 볼수있는 형태로 추출
        
        #태그를 가지고 들고옴(map과 비슷한 형태)
        response_text = completion.choices[0].get("message", {}).get("content", "").strip()
        #Text 위젯에 응답을 설정
        text_widget.delete(1.0, 'end') #첫번째지점부터 끝지점 까지 내용 삭제 (초기화)
        text_widget.insert('end', response_text) #끝지점에서부터 response_text까지 내용 삽입
        url = link_from_response(response_text) #GPT답
        if url:
            open_url_in_chrome(url)

#엔터키
def on_enter(event, entry, text_widget):
    submit_query(entry, text_widget)

#ui창
def start_gui():
    root = Tk()
    root.title("Chat with GPT")
    root.geometry("600x400")  #화면 설정
    root.resizable(True, True)  #크기 조절 가능

    Label(root, text="User:").pack()
    entry = Entry(root, width=50)
    entry.pack()
    entry.bind("<Return>", lambda event: on_enter(event, entry, response_label))  #Enter 키로도 입력

    response_label = Text(root, height=15, wrap='word')
    response_label.pack()

    Button(root, text="Submit", command=lambda: submit_query(entry, response_label)).pack()
    root.mainloop()
