num1=eval(input())
num2=eval(input())
num3=eval(input())
result=str(num1*num2*num3)
r_len=len(result)
list=[]
for i in range(10):
    list.append(0)
for j in range(r_len):
    list[eval(result[j])]+=1
for k in range(10):
    print(f"{list[k]}")