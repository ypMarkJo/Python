# 함수 선언부
def func1() :
    v = 10 # 함수 func1()안의 지역 변수
    print("func1()의 v = %d" % v)

def func2() :
    global v # v를 전역 변수로 선언
    v = 30
    print("func2()의 변경된 전역 v = %d" % v)

v = 20 # 함수 밖에서 정의 되었으므로 전역 변수

# 메인 코드 부분
func1() #10을 출력
func2() #30을 출력
print(v) #30을 출력. 전역변수 v가 변경됨
