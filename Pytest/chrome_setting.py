import subprocess as sp #새로운 프로세스 실행 및 관리를 위한 내부 모듈 
import winreg as wr #윈도우 레지스트 편집 및  엑세스를 위한 내부 모듈

def get_chrome_path():
    try:
        reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe" #파일경로
        #경로 실행
        with wr.OpenKey(wr.HKEY_LOCAL_MACHINE, reg_path) as key:
            return wr.QueryValue(key, None)
    except Exception as e:
        #경로 찾지 못할때
        print(f"Error finding Chrome path: {e}")
        return None

def open_url_in_chrome(url):
    chrome_path = get_chrome_path()
    if not chrome_path: #에러시 return 값 실행
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" 
    sp.Popen([chrome_path, url], shell=True)
