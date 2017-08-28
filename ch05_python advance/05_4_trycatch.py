#날개달기_예외처리(try, except)

#f = open("나없는파일", 'r')
#FileNotFoundError 라는 이름의 에러가 발생한다. 2.7버젼에서는 IOError라고 뜬다.

#0으로 다른 숫자를 나눌때 나오는 에러
#print(4/0)
#ZeroDivisionError라는 에러가 뜬다.

#a=[1,2,3]
#a[4] #IndexError가 난다.

#try, except를 이용해서 예외를 처리할 수 있다.
#try:
#	...
#except [발생에러[as 에러메시지변수]]:
#	...
#try부분에서 에러가 나지 않으면 except 실행 안됨. 에러 발생시 except 실행

#방법 1.
#에러가 나면 무조건 except 블록을 수행한다.
#try:
#	...
#except:
#	...

#방법 2.
#에러가 나면 except에 지정한 에러일때만 except 블록을 수행한다.
#try:
#	...
#except 발생에러:
#	...

#방법 3.
#에러가 나면 except에 지정한 에러일때만 except 블록을 수행한다. + 에러 메시지까지 알고 싶을때 사용
#try:
#	...
#except 발생에러 as 에러메시지변수:
#	...

try:
	4/0
except ZeroDivisionError as e:
	print(e)
#위를 실행하면 4/0이 실행되어 ZeroDivisionError라는 에러가 뜨고, except블록이 실행되어 division by zero가 출력된다.


###try ... else
#else절은 예외가 발생하지 않은 경우 실행된다. except 바로 다음에 나와야 한다.
try:
	f=open('foo.txt', 'r')
except FileNotFoundError as e:
	print(str(e))
else:
	data = f.read()
	f.close()
#foo.txt파일이 없으면 except가 수행되고 있다면 else가 실행되어 data 변수가 생겨난다.


###try ... finally
#finally절은 try문 수행 도중 예외의 발생여부 상관없이 항상 수행된다. 보통 사용한 리소스를 close해야 할 경우에 많이 사용된다.
f = open('foo.txt', 'w')
try:
	#무언가 수행한다.
finally:
	f.close()


#에러 회피하기
try:
	f = open('나없는파일', 'r')
except FileNotFoundError:
	pass #파일이 없더라도 오류가 아니다. 그냥 보내라는 의미.


##에러 발생시키기(raise)
#Bird라는 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하게 만들고 싶은 경우가 있을 수 있다.
class Bird:
	def fly(self):
		raise NotImplementedError #NotImplementedError는 파이썬 내장 에러로 구현되지 않았을 때 발생시키는 에러로 사용한다.
class Eagle(Bird):
	pass 
eagle = Eagle()
eagle.fly()
#Eagle에서는 Bird 클래스의 fly함수를 구현하지 않았기 때문에 Bird의 fly()함수가 호출되어 raise문에 의해 NotImplementedError 오류가 발생할 것이다.
#NotImplementedError를 발생시키지 않으려면 Eagle 클래스에 fly함수를 구현해야 한다.
class Eagle(Bird):
	def fly(self):
		print("very fast")
eagle = Eagle()
eagle.fly()
