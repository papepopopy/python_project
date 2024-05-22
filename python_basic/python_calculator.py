# 계산기 만들기

# 함수사용
# if문을 이용하여 + - 구현
# 입력값은 최대 3개

def op():
    run = True
    while(run):
        str = input("기호를 입력하세요 +-x/")
        if str == "+" or str=="-" or str=="x":
            run = False
            return str
        else :
            print("잘못 입력하셨습니다.")

str=op()


# ///////////////////////////////////////////////////////////////////////////

# num1 = int(input("1번째 숫자 입력"))
# com = input("+ -")


# if com == "+":
#     num2 = int(input("2번째 숫자 입력"))
#     if com == "+":
#         com = input("+ -")
#         num3 = int(input("3번째 숫자 입력"))
#         print (num1+num2-num3)
#         print("잘못 입력하셨습니다.")
#     elif com == "-":
#         com = input("+ -")
#         num3 = int(input("3번째 숫자 입력"))
#         print (num1+num2+num3)
#         print("잘못 입력하셨습니다.")
# elif com == "-":
#     num2 = int(input("2번째 숫자 입력"))
#     if com == "+":
#         com = input("+ -")
#         num3 = int(input("3번째 숫자 입력"))
#         print(num1-num2+num3)
#         print("잘못 입력하셨습니다.")
#     elif com == "-":
#         com = input("+ -")
#         num3 = int(input("3번째 숫자 입력"))
#         print(num1-num2-num3)
#         print("잘못 입력하셨습니다.")