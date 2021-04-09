for i in range(1,4,1):#1부터 시작하여 1씩 증가하여 4가 되면 종료
    print("Number",i)

#for문을 이용하여 1부터 100까지의 합 구하기.
sum=0
for i in range(1,101,1):
    sum=sum+i
print("sum=",sum)

#X^n을 구하는 프로그램.
x=float(input('Type x: '))
n=int(input('Type n: '))

prod=1
for i in range(1,n+1):
    prod=prod*x
print(prod)