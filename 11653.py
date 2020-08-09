def ftrz(n1):
    for i in range(2,n1+1):
        if n1%i==0:
            while n1%i==0:
                print(f"{i}")
                n1/=i
num=eval(input())
ftrz(num)
