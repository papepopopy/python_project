# a=[1,2,3]
# print(a[0])
# b=0

# 1
# for i in a:
#     print(i)

# 2
# for i in range(len(a)):
#     print(a[i])

# 3
# for i in a:
#     print(a[b])
#     b+=1

# b=["가", "나", "다"]
# c="디언"
# e="라"
# f="람쥐"

# 1
# g=[c,e,f]
# for i in range(len(b)):
#     for i in range(len(g)):
#         print(b[i]+g[i])
        
# 2
# for i in b: 
#     if(i=='가'):{
#         print(i+c)
#     }
#     if(i=='나'):{
#         print(i+e)
#     }
#     if(i=='다'):{
#         print(i+f)
#     }


# b=["가", "나", "다"]
b=["나", "마", "다"]
b.remove("마") #텍스트만 가능
# b.append("라") #텍스트 추가
# b.sort() #한칸 앞으로 변경
# b.insert(0,"가")

for str in b:
    print(str)
    