result=0
for i in range(5):
    a=eval(input())
    if a<40:
        a=40
    result+=a
print(f"{result/5:.0f}")