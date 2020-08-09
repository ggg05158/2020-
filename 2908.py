num1,num2=input().split( )
num1=eval(num1)
num2=eval(num2)
def reverse(n):
    a=n//100
    n=n%100
    b=n//10
    c=n%10
    return c*100+b*10+a
if reverse(num1)>reverse(num2):
    print(f"{reverse(num1)}")
else:
    print(f"{reverse(num2)}")