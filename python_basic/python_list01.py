# i = [1, 2, 3, 4, 5]
# j = [6, 7, 8, 9, 10]

# # int [] num = new int[5]
# print (i+j) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# i=[]#[1, 2, 3]
i = [0, 3, 8] #[0, 3, 8, 1, 2, 3] 순서가 차례로 들어감

i.append(1)
i.append(2)
i.append(3)

print(i) #[0, 3, 8, 1, 2, 3]
i.sort() # 크기로 나열

# j = len(i) #6
j = i.count(8) #1 / i 배열의 8의 갯수 
j = i.remove(8) #none
print(i) #[0, 1, 2, 3, 3, 8]
print(j)