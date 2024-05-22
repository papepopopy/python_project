# 함수 사용
# 입력 수만큼 for문 돌리기
# 입력한 수만큼 숫자 받기
# 입력 숫자를 리스트 변수 입력
# for문 이용 값 도출
# 모두 더하기

# 함수 목록
# 1. 입력한 숫자갯수를 받는 함수 
def order():
    num  = int(input("숫자 입력"))
    return count
def operation():
    run = True
    while run:
        op = input("어떤 계산을 하시겠습니다? + or -")
        if op == "+" or op == "-":
            run = False
        else:
            print("잘못 씀")
            return op
            
    # return count

# count = 입력갯수

# 2. 입력 숫자만큼 숫자를 받아 리스트 형 변수에 담고 리턴하는 함수
def input_val(count):
    # 리스트 형 변수
    array_val = []
    
    for i in range(count): #count 수만큼 반복
        
        num = int(input("숫자를 입력하세요"))
        array_val.append(num) #array_val에 더하기
    return array_val #외부 함수로 전달

# 3. 계산하는 함수
def acount (array_val):
    result = 0
    cnt = 0
    
    for num in array_val:
        if(cnt==0):
            result =num
        result +=num
        cnt+=1
        
    print (result)
    # return result
        
count = order()
array_val = input_val(count)
# print(acount(array_val))
if operation() == "+":