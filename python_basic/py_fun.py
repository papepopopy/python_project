def order():
    count = int(input('몇개의 숫자를 입력하시겠어요?'))
    return count

def operation():
    run = True
    while run:
        op = input('어떤계산을 하시겠습니까 +, -')
        if op=='+' or op=='-':
            run = False
        else:
            print('잘못 입력하셨습니다.')
            return op

def input_val(count):
    array_val=[]
    for i in range(count):
        num =  int(input('숫자를 입력하세요'))
        array_val.append(num)
    return array_val

def account_plus (array_val):
    result = 0
    for num in array_val:
        result +=num
    print (result)

def account_minus (array_val):
    result = 0
    cnt = 0
    for num in array_val:
        if(cnt==0):
            result =num
        else:
            result -=num
        cnt+=1
    print (result)
count = order()
array_val = input_val(count)
if operation()=='+':
    account_plus(array_val)
else:
    account_minus(array_val)