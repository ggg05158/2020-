max=0
index=0
for i in range(9):
    num=eval(input())
    if num>=max:
        max=num
        index=i+1
print(f"{max}")
print(f"{index}")