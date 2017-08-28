#입출력_함수
#def 함수명(인수):
def sum(a, b):
	return a+b
a = 3
b = 4
c = sum(a, b)
print(c)

def sum(a, b):
	result = a + b
	return result
a = sum(3, 4)
print(a)

#입력값이 없는 함수
def say():
	return 'Hi'
a = say()
print(a)

#리턴값이 없는 함수
def sum(a, b):
	print("%d, %d의 합은 %d입니다." %(a, b, a+b))
a = sum(3, 4)
a
print(a) #None이 나온다. 이는 자료형에서 거짓을 의미한다. 텅비었다. 리턴이 없다.

#입력값도 리턴값도 없는 함수
def say():
	print("Hi")
say()

#입력값이 몇개가 될지 모르는 때는 어떻게?
#def 함수이름(*입력변수):
#	수행문장
def sum_many(*args): #args가 변수 입력값을 모아서 튜플로 만들어준다. *python 이렇게 바꿔도 상관없다.
	sum=0
	for i in args:
		sum = sum+i
	return sum
result = sum_many(1, 2, 3)
print(result)
result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def sum_mul(choice, *args): #*을 이용할때는 제일 뒤쪽에 적어줘야 한다. 맨앞의 것은 choice, 그다음부터는 *args에 해당한다라고 이해할 수 있다.
	if choice == "sum":
		result = 0
		for i in args:
			result = result + i
	elif choice == "mul":
		result = 1
		for i in args:
			result = result * i
	else : print("sum 또는 mul을 choice에 입력해 주세요")
	return result
result = sum_mul("sum", 1, 2, 3, 4, 5)
print(result)
result = sum_mul("mul", 1, 2, 3, 4, 5)
print(result)

#리턴값은 언제나 하나이다.
def sum_and_mul(a, b):
	return a+b, a*b
#오류가 나지 않는다. 리턴이 두개인데? 이것은 튜플 형태로 하나의 변수에 저장된다
a = sum_and_mul(3, 4) #결과는 a=(7, 12)가 된다. 튜플형태.
#이를 두개의 리턴처럼 받고싶다면 다음과 같이 입력한다. 각각을 받는 변수를 지정해주면 된다.
su, mul = sum_and_mul(3, 4)

def sum_and_mul(a, b):
	return a+b
	return a*b
#위와같은 함수는
def sum_and_mul(a, b):
	return a+b
#와 같다. return만나는 순간 함수에서 나간다.


#return의 또다른 쓰임새
def say_nick(nick):
	if nick == '바보':
		return
	print("나의 별명은 %s 입니다." %nick)
#바보가 들어오면 함수를 나가고, 바보가 아니라면 프린트한다.
say_nick('덕')
#함수에 초기치 설정하기
def say_myself(name, old, man=True): #man인수를 디폴트로 트루를 줬다.
	print("나의 이름은 %s 입니다." %name)
	print("나이는 %d살입니다." %old)
	if man:
		print("남자입니다.")
	else:
		print('여자입니다.')
say_myself('덕오', 27)
say_myself('덕오', 27, True) #이 두 결과는 같다.

#입력값 초기치 설정시 주의사항
#다음과 같이 하면 에러가 난다.
def say_myself(name, man=True, old): #위 함수와는 순서만 바뀐 함수
	print("나의 이름은 %s 입니다." %name)
	print("나이는 %d살입니다." %old)
	if man:
		print("남자입니다.")
	else:
		print('여자입니다.')
#SyntaxError: non-default argument follows default argument 이 에러가 난다.
#초기치를 설정한 인수는 초기치 없는것들 뒤에 나와야 한다.
say_myself('덕오', 27) #이렇게 하면 27을 man에 넣을지, old에 넣을지 모르기 때문이다.


#함수 내에서 선언된 변수의 효력 범위
a = 1
def vartest(a):
	a = a+1
vartest(a)
print(a) #1이 출력된다 함수 안의 변수는 함수 안에서만 정의된다.

del a
def vartest(a):
	a = a+1
vartest(3)
print(a) #a가 정의되지 않았기 때문에 오류가 난다.)
#외부의 a를 1 증가시키는 방법은?
#첫번째 방법
a = 1
def vartest(a):
	a = a+1
	return a
a = vartest(a)
print(a)

#두번째 방법
a = 1
def vartest():
	global a
	a = a+1

vartest()
print(a)
#global a 문장은 함수 안에서 함수 밖의 a를 직접 사용하겠다는 말이다.
#되도록 사용하지 말도록 하자. 함수는 독립적으로 존재하는 것이 좋다.




