#1.
#enumerate() 내장 함수를 이용하여 사용자가 입력한 문자열에서 
#'a' 문자의 위치를 모두 찾아 출력하는 프로그램을 작성하라. 
# 'a'가 없으면 "a가 없습니다'라는 메시지를 출력하라.

# a=input("문자열을 입력하세요.")
# find=0
# for index in enumerate(a,start=1):
#     if index[1]=='a':
#         find+=1
#         print(index)
# if find==0:
#     print("a가 없습니다.")

#2.
#두 수의 합(sum), 차(sub), 곱(mul), 나누기(div)를 수행하는 함수를 각각 정의하라. 
#딕셔너리를 이용하여 사용자가 '1'을 입력하면 sum()을 호출하고, 
#'2'를 입력하면 sub(), '3'을 입력하면 mul(), '4'를 입력하면 div() 함수를 
#호출하여 두 수의 연산을 수행하는 프로그램을 작성하라.

# def sum(a,b):
#     return a+b
# def sub(a,b):
#     return abs(a-b)
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return float(a/b)

# a=int(input("첫번째 수 입력: "))
# b=int(input("첫번째 수 입력: "))
# c=int(input("1:합 ,2:차 ,3:곱 ,4:분 >> "))
# cal={1:sum(a,b),2:sub(a,b),3:mul(a,b),4:div(a,b)}
# print(cal[c])

#3.
#다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는 함수 작성
# 예: 문자열 'led=on&motor=off&switch=off'이고 구분 문자가 
# '&', '='일 때 {'led':'on', 'motor':'off', 'switch':off'} 반환.
# Hint: dict([['a','b'], ['c', 'd']]) -> {'a': 'b', 'c': 'd'}
# def makedict(a):
#     d=0
#     key=''
#     value=''
#     kl=[]
#     vl=[]
#     for i in range(0,len(a)):
#         if a[i]=='=':
#             key=a[d:i]
#             kl.append(key)
#             d=i+1  
#         elif a[i]=='&':
#             value=a[d:i]
#             vl.append(value)
#             d=i+1   
#         elif i==len(a)-1:  
#             value=a[d:i+1]
#             vl.append(value)   
#     return {key:value for key,value in zip(kl,vl)}

# print(makedict("led=on&motor=off&switch=off&wheel=ok"))#--------------내 코드(폐기:빈칸을 인식못함.)

#--------------------------------------------------------------교수님 코드.split이용
def makedict(a):
    kl=[]
    vl=[]
    aand=a.split('&')
    for i in aand:  
        kl.append(i.split('=')[0])
        vl.append(i.split('=')[1])
    return {key:value for key,value in zip(kl,vl)}

print(makedict("led=on&motor=off&switch=off&wheel=ok"))

#-----------------------------------------------------------진주코드
# def makedict(string):
#     List1=[]
   
#     new_str1=string.split('&')
#     for i in new_str1:
#         List1.append(i.split('='))
    
#     print(dict(List1))
    
# makedict('led=on&motor=off&switch=off')