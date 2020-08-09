best=0
num=0
for i in range(5):
    n1,n2,n3,n4=input().split()
    n1=eval(n1)
    n2=eval(n2)
    n3=eval(n3)
    n4=eval(n4)
    result=n1+n2+n3+n4
    if best<result:
        best=result
        num=i+1
print(f"{num} {best}")