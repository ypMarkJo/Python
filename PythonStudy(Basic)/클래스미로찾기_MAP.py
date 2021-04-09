class Stack:
    def __init__(self):
        self.data=[]
    def push(self,n,m):
        self.data.append([n,m])
        

    def is_empty(self):
        return self.size()==0
    def pop(self):
        if self.is_empty():
            #언더 플로우 예외 처리
            return  
        else:
            return self.data.pop()
    def size(self):
        return len(self.data)


m=[[0,0,0,0,0,0,0,1,1],
   [0,1,1,0,1,1,0,1,0],
   [0,0,0,1,0,0,0,1,0],
   [0,1,0,0,1,1,0,0,0],
   [0,1,1,1,0,0,1,1,1],
   [0,1,0,0,0,1,0,1,0],
   [0,0,0,1,0,0,0,1,0],
   [0,1,1,1,0,1,0,0,0],
   [0,1,1,1,0,1,0,1,0]]

path=[['■','■','■','■','■','■','■','■','■'],
      ['■','■','■','■','■','■','■','■','■'],
      ['■','■','■','■','■','■','■','■','■'],
      ['■','■','■','■','■','■','■','■','■'],
      ['■','■','■','■','■','■','■','■','■'],
      ['■','■','■','■','■','■','■','■','■'],
      ['■','■','■','■','■','■','■','■','■'],
      ['■','■','■','■','■','■','■','■','■'],
      ['■','■','■','■','■','■','■','■','■']]

point=Stack()
#maze size
x=9
y=9
#출구지정
exit_a=5
exit_b=8
a=0#시작점 지정a
b=0#시작점 지정b
m[0][0]=2
flag=0 #출구 막혀서 Pop할 데이터가 더이상 없을 때 기준점
while 1:
    if a==exit_a and b==exit_b:
        point.push(a,b)
        break
    if b<(y-1) and m[a][b+1]==0:#1번 경로 탐색
        point.push(a,b)
        b=b+1
        m[a][b]=2
        continue
    elif 0<a and m[a-1][b]==0:#2번 경로 탐색
        point.push(a,b)
        a=a-1
        m[a][b]=2
        continue
    elif 0<b and m[a][b-1]==0 :#3번 경로 탐색
        point.push(a,b)
        b=b-1
        m[a][b]=2
        continue
    elif a<(x-1) and m[a+1][b]==0:#4번 경로 탐색
        point.push(a,b)
        a=a+1
        m[a][b]=2
        continue
    if point.size()!=0:#Pop할 게 있을 때만 Pop
        t=point.pop()
        a=t[0]
        b=t[1]
        continue
    else:#스택이 비었을 때
        flag=1#출구막힘 플래그
        break
   
    
if flag==1:
    print('NO EXIT!')
else:
    for i in range(0,point.size()):
        t=point.pop()
        path[t[0]][t[1]]='□'
    for i in range(0,x):
        for j in range(0,y):
            print(path[i][j],' ',end='')
        print('')

   





