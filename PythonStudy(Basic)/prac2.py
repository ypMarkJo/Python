#1
a=int(input('Insert a second: '))
b=a%60
c=a//60

print(c,'분',b,'초')
#2
a=int(input('Insert a min: '))
b=a//(24*60)
c=(a-(b*24*60))//60
d=a-(b*24*60)-c*60
print(b,'일',c,'시간',d,'분')
#3
a=5000000
b=(((((a*1.05)*1.05)*1.05)*1.05)*1.05)
print(b,' 원')
#4
a=(100*101)/2
print(a)

#5
a=int(input('포도: '))
b=int(input('딸기: '))

c=75*a+113.5*b

print('총 무게는 ',c,'g')



