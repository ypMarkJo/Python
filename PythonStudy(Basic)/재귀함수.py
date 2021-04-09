def fact(n):
    if n==0: #재귀 함수 종료 조건. n=0이면 종료
        return 1
    else:
        return n*fact(n-1) #n! = n x (n-1)! 
def factchs(n):
    result=''
    count=1
    while n !=0:
        if count==1:
            
            result=str(n)+result+'='+str(fact(n))
            n=n-1
            count+=1
        else:
            result=str(n)+'x'+result
            n=n-1
            
    return result

print(factchs(10))
