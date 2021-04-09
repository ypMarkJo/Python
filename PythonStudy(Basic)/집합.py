import random
pick = set() #빈 집합
while len(pick) < 6:
    n = random.randint(1,45) #랜덤 넘버 생성
    if n not in pick:
        pick.add(n) #집합에 요소 추가

print(sorted(pick)) #순서대로 나열된 집합 출력
