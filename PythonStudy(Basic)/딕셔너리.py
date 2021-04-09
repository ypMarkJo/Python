days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June':30, 'July':31, 'August':31,'September':30, 'October':31, 'November':30, 'December':31}
#1
# a=str(input('월을 입력: '))
# print(days[a])
# #2
# print(sorted(days.keys())
#3
# for i in days:
#     if days[i]==31:
#         print(i)
#4
#print(sorted(days.items(),key=lambda x:x[1]))
#4.교수님 풀이
# II=days.items()
# tt=[]
# for (k,v) in II:
#   tt.append((v,k))
# ttt=sorted(tt)
# for i in ttt:#1
#   print(i[1],i[0])

#5.사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
# a=str(input('세글자를 입력하세요'))
# for i in days:
#     if i[0:3]==a:
#         print(days[i])
#     else:
#         continue

#연습문제2
d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
#1
# for i in d:
#    for j in i:
#        if j=='phone' and i[j][-1:]=='8':
#            print(i['name'])
#2
# for i in d:
#     for j in i:
#         if j=='email' and i[j]=='':
#             print(i['name'])
#3
usn=input("이름을 입력: ")
find=False#플래그
for i in d:
    if i['name']==usn:
        print(i['phone'],i['email'])
        find=True#발견하면 플래그 트루로 전환
        break
   
# if find==False:
#     print('이름이 없습니다.')-----------방법1

#if usn not in i['name']:
#   print('이름이 없습니다.')#-----------방법2
        
    
    
    
    


