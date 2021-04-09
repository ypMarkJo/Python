#기본 매개변수1
def prtMesg(message, count=1): #count의 기본값이 1로 지정
    print (message * count)
prtMesg('default') #message='default'. count는 기본값 사용
prtMesg('Hi! ', 5) #message와 count 인자 전달

#기본 매개변수2
def greet(name, msg="Nothing new?"):
    print("Hi! ", name + ', ' + msg)
greet("Abe") #name 만 전달
greet("Bob", "Good morning!") #name과 msg 전달

#일반(위치) 매개변수의 값을 전달하지 않으면 오류
