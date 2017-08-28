#날개달기_내장함수
#외부 모듈과는 달리 import를 할 필요 없다.

#abs : 절대값
print(abs(3))
print(abs(-3))
print((1+2j))
#복소수의 절대값 : abs(a+bj) = sqrt(a^2 + b^2)

#all : 반복가능한 x가 모두 참인경우 True, 하나라도 거짓이 있는경우 False. 반복가능한 x라는 의미는 for문으로 x값을 출력할수 있는 형태의 자료형을 의미한다.
print(all([1, 2, 3])) #True
print(all([1, 2, 3, 0])) #False

#any : 반복가능한 x중 하나라도 참인경우 True, 모두 거짓인 경우 False 출력.
print(any([1, 2, 3, 0])) #True
print(any([0, ""])) #False

#chr : 아스키코드값을 입력으로 받아서 해당하는 문자를 출력하는 함수.
print(chr(97)) #'a'
print(chr(48)) #0

#dir : 객체가 가지고있는 변수나 함수를 리스트 형태로 보여준다.
#리스트 객체 관련 함수(메소드)를 보여준다.
print(dir([1, 2, 3])) #[1, 2, 3]. 으로 해도 보인다.
#딕셔너리 객체 관련 함수(메소드)를 보여준다.
print(dir({'1':'a'}))

#divmod(a, b) : 두 숫자를 입력으로 받았을 때, 몫과 나머지를 튜플의 형태로 반환
print(divmod(7, 3)) #(2, 1)
print(divmod(1.3, 0.2)) #(6.0, 0.099999999999978)

#enumerate : 시퀀스자료형(리스트, 튜플, 문자열)을 입력으로 받아 enumerate 객체를 리턴한다.
#enumerate는 첫번째로 그 순서값, 두번째로 그 순서값에 해당되는 시퀀스 자료형의 실제값을 갖는다.
#뭔가... dictionary의 key값을 integer를 주고, value값을 시퀀스자료형(리스트, 튜플, 문자열)의 값을 주는 느낌이다.
for i, name in enumerate(['boby', 'foo', 'bar']):
	print(i, name)
#0 boby
#1 foo
#2 bar
#반복구간에서 시퀀스 자료형의 값 뿐만 아니라 현재 어떤 위치에 있는지에 대한 인덱스 값이 필요한 경우에 enumerate 함수는 유용하다.

#eval : 입력값으로 실행가능한 문자열을 받아서 문자열을 실행한 결과값을 반환한다.
#R에서 eval(parse(text=~~~))와 같은 역할
eval('1+2') #3
eval("'hi' + 'a'") #hia
eval('divmod(4, 3)') #(1, 1)

#filter(function, iterable) : 함수와 반복가능한 자료형(리스트, 튜플, 문자열)을 입력으로 받아서 반복자료형의 값이 하나씩 함수에 인수로 전달될 때, 
#참을 반환시키는 값만을 따로 모아서 리턴하는 함수이다. for문의 역할을 할 수 있는 듯 하다.
#positive.py
def positive(l):
	result = []
	for i in l:
		if l>0:
			result.append(i)
	return result
print(positive([1, -3, 2, 0, -5, 6])) #[1, 2, 6]이 출력된다. 양수만 출력되는 효과
#filter를 이용하면,
def positive(x):
	return x>0
print(list(filter(positive, [1, -3, 2, 0, -5, 6]))) 
#positive라는 함수에 해당 리스트를 통째로 넣고 이 리스트를 for문 돌리듯이 하나씩 탐색해가며 함수 적용.
#결과를 list로 받는다.

#hex(x) : 정수값을 받아서 16진수값으로 돌려준다.
print(hex(234)) #0xea
print(hex(3)) #0x3

#id(object) : 객체를 입력값으로 받아서 객체의 고유값(레퍼런스, 참조 주소)을 반환하는 함수이다.
a=3
print(id(3)) #135072304
print(id(a)) #135072304
b=a
print(id(b)) #135072304 a, b, 3이 모두 같은 객체를 가리키고 있다.
print(id(4)) #135072292 4는 다른 객체이므로 다른 참조값을 보여준다.

#input([prompt]) : 사용자 입력을 받는 함수
a = input()
#콘솔에 'hi'를 입력한다. 3버젼 부터는 string으로 받는데, 2버젼은 hi로 받는 듯 하다. ''를 해준다.
#a = raw_input() 로 하면 2버젼에서 바로 string으로 받는다.
print(a) #'hi'
b = input("Enter : ")

#int(x) : 스트링 형태의 숫자나 소수점 숫자등을 정수의 형태로 반환.
int('3') #3
int(3.4) #3
#int(x, radix) radix는 진수를 의미한다.
int('11', 2) #2진수에서 11에 해당하는 3을 출력한다.
int('1A', 16) #26

#isinstance(object, class) 인스턴스가 해당 클래스의 인스턴스인지 판단 후 진리값 인쇄
class Person : 
	pass
a = Person()
b = 3
isinstance(a, Person) #True
isinstance(b, Person) #False

#lambda : 함수를 생성할 때 사용되는 예약으로 def와 동일하나 한줄로 간결하게 만들때 사용한다.
sum = lambda a, b : a+b
print(sum(3, 4)) #7
#def보다 간결하고, def로 사용 불가한 자리에 lambda를 사용할 수 있는 경우가 있다.
l = [lambda a, b : a+b, lambda a, b : a*b] #2개의 함수를 하나의 변수 안에 넣어줄 수 있다.
print(l)
l[0](3, 4) #7이 나온다. l의 첫번째 위치의 합하는 함수를 불러서 3, 4를 합한다.

#len(s) : 반복가능한 자료형의 길이를 돌려준다.
print(len('python')) #6
print(len([1, 2, 3])) #3
print(len((1, 'a'))) #2 튜플도 들어갈 수 있다.

#list(s) : 반복가능한 자료형을 받아서 똑같은 순서의 리스트로 만들어주는 함수.
list("python") # ['p', 'y', 't', 'h', 'o', 'n']
list((1, 2, 3)) #[1, 2, 3]
a = [1, 2, 3]
b = list(a)
print(b) #[1, 2, 3]
print(id(a))
print(id(b)) #두 변수는 모두 [1, 2, 3]인데, 참조주소가 다른것을 알 수 있다.

#map(f, iterable) : 함수와 반복가능 자료형에 대해 각 요소의 함수값을 묶어서 리턴한다.
#벡터단위 연산에 사용 가능할 것이다.
def two_times(l):
	result = []
	for i in l:
		result.append(i*2)
	return result
#map을 이용해서 해보자.
def two_times(x) : return x*2
map(two_times, [1, 2, 3, 4]) #[2, 4, 6, 8]
#lambda까지 이용해보자.
list(map(lambda x : x*2, [1, 2, 3, 4]))

#max(iterable) : 최대값
print(max([1, 2, 3])) #3
print(max('python')) #'y'

#min(iterable) : 최소값
print(min([1, 2, 3])) #1
print(min('python')) #'h'

#oct(x) : 정수형태의 숫자를 8진수로 바꿔준다.
print(oct(34)) #'0o42'
print(oct(12345)) #'0o30071'

#open(filename, [mode]) 파일을 mode에 맞게 연다. mode가 생략되면 r로 객체를 만든다.
#w:쓰기, r:읽기, a:추가, b:바이너리 모드
#w+, r+, a+는 파일을 업데이트 할 용도로 사용된다.
#b는 w, r, a와 함께 사용된다.
f = open("binary_bile", 'rb') #바이너리 읽기모드

#ord(c) : 문자의 아스키 값을 돌려준다. (chr의 반대)
print(ord('a')) #97
print(ord('0')) #48

#pow(x,y) : x의 y승을 한 결과 출력
print(pow(2, 4)) #16
print(pow(3, 3)) #27

#range([start], stop, [step])
#인수가 하나일 경우. 끝을 의미
list(range(5)) #[0, 1, 2, 3, 4]
#인수가 두개일 경우. 시작과 끝을 의미
list(range(5, 10)) #[5, 6, 7, 8, 9]
#인수가 세개일 경우. 마지막 숫자는 step을 의미
list(range(1, 10, 2)) #[1, 3, 5, 7, 9]
list(range(0, -10, -1)) #[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

#repr(object) : 객체를 출력할 수 있는 문자열 형태로 반환.주로 eval 함수의 입력으로 쓰인다.
#str과의 차이점으로는 str으로 변환된 값은 eval의 입력이 될 수 없다는 것이다.
repr("hi".upper())
eval(repr("hi".upper()))
#eval(str("hi".upper())) #오류가 난다.

#sorted(iterable) : 소팅 후 리스트로 리턴
sorted([3, 1, 2]) #[1, 2, 3]
sorted(['a', 'c', 'b']) #['a', 'b', 'c']
sorted("zero") #['e', 'o', 'r', 'z']
sorted((3, 2, 1))
#list자료형에 대한 sort함수는 리스트 객체 그 자체를 소트한다.
#소트된 결과를 리턴하지는 않는다. (return이 없는 함수와 같다.)
a=[3, 1, 2]
result = a.sort() #result에 아무것도 저장되지 않는다.
print(result) #None이 인쇄된다. 
print(a) #a가 sorting되어 저장된다. result는 아무것도 아닌것이다.
res = sorted(a)
print(res)
#str(object) : 객체를 출력할 수 있는 문자열 형태로 돌려준다.
str(3) #'3'
str('hi') #'hi'

#tuple(iterable) : 튜플 형태로 돌려준다. 튜플이 들어오면 그대로 돌려준다.
tuple("abc") #('a', 'b', 'c')
tuple([1, 2, 3]) #(1, 2, 3)
tuple((1, 2, 3)) #(1, 2, 3)

#type(object) : 객체의 자료형이 무엇인지 알려준다.
print(type("abc")) #<class 'str'>
print(type([])) #<class 'list'>
print(type(open('test', 'w'))) #<class '_io.TextIOWrapper'>

#zip(iterable) : 동일한 개수의 요소 값을 갖는 반복 가능한 자료형을 묶어주는 역할을 한다.
#위치별로 따오는 함수인것 같다. 튜플로 각각 묶고, 리스트로 묶어서 반환한다.
list(zip([1, 2, 3], [4, 5, 6])) #[(1, 4), (2, 5), (3, 6)]
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])) #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
list(zip("abc", "def")) #[('a', 'd'), ('b', 'e'), ('c', 'f')]










