#1
cm=int(input("길이 입력: "))
if cm<0:
    print("잘못 입력하였습니다.")
else:
    b=float(cm/2.54)
    print("인치로 변환",b,"inch")

#2
s=int(input("학점 입력: "))
if s<40:
    print("1학년이네?")
elif 40<=s<80:
    print("2학년이네?")
elif 80<=s:
    print("졸업반이네?")

#3
tm=int(input("현재시간 입력: "))
apm=str(input("am or pm?: "))
kt=int(input("몇 시간 후?: "))
a=(kt+tm)//12
b=kt+tm
if a%2==1:
    if apm=='pm':
        print("최종 시간은 am",(b)%12,"시 입니다.")
    else :
        print("최종 시간은 pm",(b)%12,"시 입니다.")
else:
    if apm=='pm':
        print("최종 시간은 pm",(b)%12,"시 입니다.")
    else :
        print("최종 시간은 am",(b)%12,"시 입니다.")



