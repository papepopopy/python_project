data = {
    "java" : 100,
    "python" : 80,
    "html" : 70,
    "js" : 90
}

# str1 = data[1]
str2 = data["python"]

# print(str1)
print(str2)

hashmap = {}

for key, Value in data.items():
    hashmap[key] = Value
    
item_list = list(hashmap.items())

for item in item_list:
    print(item)
    # ('java', 100)
    # ('python', 80) 
    # ('html', 70)   
    # ('js', 90)

# i = 10
# j = 20

# if i+j == 30:
#     print("안녕") 
# else:
#     print("잘가")
    
# run = Trues
# run = False

# if run:
#     print("안녕")
# else:
#     print("잘가")
    
str = input("글자를 입력하세요")

if str == "가":
    print ("나")
elif str == "나":
    print("다나마바")
else:
    print("없다.")
    
