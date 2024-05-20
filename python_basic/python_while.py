count = 0

while count < 5:
    num1 = int(input("첫번째 숫자를 입력하세요"))
    num2 = int(input("두번째 숫자를 입력하세요"))
    op = input("어떤 연산을 하시겠습니다? +-*/")

    result = 0

    if op == "+":
        # print (num1+num2)
        result = num1 + num2
    elif op == "-":
        # print (num1-num2)
        result = num1 - num2
    elif op == "*":
        # print (num1*num2)
        result = num1 * num2
    elif op == "/":
        # print (num1/num2)
        # result = num1 / num2
        if num1 == 0 | num2 ==0:
            print("0으로 나눌 수 없습니다.")
        else:
            result = num1/num2
        
    else:
        print("잘못 입력하셨습니다.")
        # result = "잘못 입력하셨습니다."
        
    print(result)
    count += 1
        
