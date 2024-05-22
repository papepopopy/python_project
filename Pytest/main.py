from gui import start_gui
# gui에서 start_gui 함수(클래스) 찾기

if __name__ == "__main__":
    # 참이면 start_gui() 실행
    # 위와 같이 선언하면 다른 파일에서 실행할수 없음
    # __안에 넣어 변수화를 시킬수 있다.
    
    start_gui()
    
# 터미널 입력
# pip install openai==0.28.0 
# ctrl + 5
# pip list 확인 가능