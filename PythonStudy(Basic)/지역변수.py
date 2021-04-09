# 함수 선언부
def func1() :
    v = 10 # 함수 func1()안의 지역 변수. func1 내에서만 유효
    print("func1()의 v = %d" % v)

def func2() :
    v = 20 # 함수 func2()안의 지역 변수. func2 내에서만 유효
    print("func2()의 v = %d" % v)

# 메인 코드 부분
func1()
func2()
