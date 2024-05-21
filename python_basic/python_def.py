def fnprint(str):
    print(str)
    
def account(num1, num2):
    return num1 + num2

def inputval():
    num1 = int(input("첫번째 숫자를 입력하세요"))
    num2 = int(input("두번째 숫자를 입력하세요"))
    return num1, num2

# num1, num2 return 값이 각각 들어가짐
pnum1, pnum2 = inputval()
fnprint(account(pnum1, pnum2)) #입력 값 

# fnprint(account(10, 20)) #30
