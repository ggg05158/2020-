def max(n1,n2):
    div=0
    for i in range(1,(n2 if n1>n2 else n1)+1):
        if(n1%i==0 and n2%i==0):
            div=i
    return div
def min(n1,n2):
    n1d=n1/max(n1,n2)
    n2d=n2/max(n1,n2)
    return max(n1,n2)*n1d*n2d
def main():
    num1, num2=input().split( )
    num1=eval(num1)
    num2=eval(num2)
    print(f"{max(num1,num2)}")
    print(f"{min(num1,num2):.0f}")
main()