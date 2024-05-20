import re

pid = input("ID를 입력하세요")
# ppass = input("password를 입력하세요")

pattern1 = "[0-9]"

if re.match(pattern1, pid):
    print("입력 값은 숫자입니다.")
else:
    print("입력 값은 문자입니다.")