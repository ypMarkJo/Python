# #1두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램을 함수로 작성
# def box(n,m):
#     for i in range(0,n):
#         for j in range(0,m):
#             print('*',end=' ')
#         print('')

# box(2,4)
# #2.하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성예: 123  1+2+3 = 6
# def positsum(n):
#     slist=0
#     while n%10!=0:
#         a=n%10
#         slist+=a
#         n=n//10
#     return slist
  
# print(positsum(123))

#3.두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 두 개의 문자열이 같으면 -1을 반환
# def difposit(n,m):
#     find=0;
#     count=0;
#     if len(n)==len(m):
#         for i in range(0,len(n)):
#             if n[i]!=m[i]:
#                 find=i
#                 break
#             count+=1
#         if count==len(n):
#             return -1
#         else:
#             return find+1
#     else:
#         if len(n)>len(m):
#             for i in range(0,len(m)):
#                 if n[i]!=m[i]:
#                     find=i
#                     break
#                 count+=1
#             if count==len(m):
#                 return count+1
#             else:
#                 return find+1
#         if len(n)<len(m):
#             for i in range(0,len(n)):
#                 if n[i]!=m[i]:
#                     find=i
#                     break
#                 count+=1
#             if count==len(n):
#                 return count+1
#             else:
#                 return find+1
        
#     # def same(a,b):#-----------교수님 코드
#     #     if a==b:
#     #     return -1

#     # for i in range(0,len(a)):
#     #     if a[i:i+1] != b[i:i+1]:
#     #         return i

#     # return len(a)#----------------------


# print('처음 달라지는 자리는 ',difposit('applej','applejuice'),'번째 입니다.')

# #4.숫자를 전달받아 그 수의 약수를 리스트로 반환하는 함수를 작성
# def den(n):
#     list=[]
#     count=1
#     for i in range(1,n+1):
#         if n%i==0:
#             list.append(i)
#             count+=1
#     if count==3:
#         print("소수입니다.")
#     else:
#         print(list)

# den(16)


# #5.문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성
# def posilist(a,b):
#     list=[]
#     count=1
#     same=0
#     for i in a:
#         if i==b:
#             list.append(count)
#             same+=1
#         count+=1
#     if same==0:
#         print("문자열에 해당 문자 없음.")
#     else:
#         print(list)

# posilist("application","i")

# # #6.재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램
# def ssum(n):
#     sum=0
#     proc=''
#     for i in range(1,n+1):
#         sum+=i
#     print(sum)

# ssum(50)


