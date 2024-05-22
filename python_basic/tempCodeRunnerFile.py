import py_fun as pf

count = pf.order()
array_val = pf.input_val(count)
if pf.operation()=="+":
    pf.account_plus(array_val)
else:
    pf.account_minus(array_val)


# def fnprint(str):
#     print(str)

# def account(num1, num2):
#     return num1+num2

# def inputval():
#     num1 = int(input('첫번째 숫자를 입력하세요'))
#     num2 = int(input('두번째 숫자를 입력하세요'))
#     num3 = int(input('세번째 숫자를 입력하세요'))
#     return num1, num2, num3

# pnum1, pnum2, = inputval()
# fnprint(account(pnum1, pnum2))



