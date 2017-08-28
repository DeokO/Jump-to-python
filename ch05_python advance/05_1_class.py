#파이썬 날개달기_클래스
class Calculator: #계산기라는 클래스
	# 생성자
    def __init__(self):
        self.result = 0 #만든 객체(인스턴스)에 result라는 필드값을 0으로 초기화 한다.

	#메소드 정의
    def adder(self, num):
        self.result += num #result 필드에 대해 연산을 적용
        return self.result

cal1 = Calculator() #계산기 클래스의 인스턴스
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))

class Service:
	secret = "영구는 배꼽이 두 개다." #인스턴스의 필드로 secret을 만들고 값을 '영구는 배꼽이 두 개다.'라고 준다.
    #class의 method를 정의할 때는 그 객체가 어떤것인가 라는 것을 지목하는 self가 필요하다. 여기서 self는 pey 자체를 의미
	def setname(self, name): #setname이라는 메소드를 생성하고 그 값은 객체 생성시 입력 받는다.
	    self.name = name
	def sum(self, a, b): #self의 역할은 이 인스턴스가 등록이 된것인지 확인. 부를땐 입력하지 않는것이 원칙
		result = a+b
		print("%s님 %s + %s = %s 입니다." %(self.name, a, b, result))
pey = Service()
print(pey.secret)

#이름을 입력
pey = Service() #self 자체이다.
pey.setname('홍길동')
print(pey.secret)
print(pey.name)
# print(pey.name) 이렇게 이름을 확인할 수 있다. self.name에서 self가 pey이므로, pey.name = name을 입력한 효과이다.

#sum함수 이용
pey.sum(1, 1) #sum의 self부분에 pey를 적지 않는것이 원칙이다. 등록된 인스턴스인지의 확인은 인스턴스명에서 한번만 한다.
Service.sum(pey, 1, 1) #위와 같은 결과이다. 클래스의 메소드에 직접 접근 가능하다.


## __init__
#인스턴스를 만들 때 항상 실행된다. 즉 아이디를 부여받을 때 항상 실행 된다.
#인스턴스를 받을때 애초에 필요한 정보를 미리받는 함수이다.
class Service:
	secret = "영구는 배꼽이 두 개다."
	def __init__(self, name): #setname함수의 이름이 __init__으로 바뀌었다.
		self.name = name
	def sum(self, a, b): 
		result = a+b
		print("%s님 %s + %s = %s 입니다." %(self.name, a, b, result))
#pey = Service() 이렇게 하면 안된다.
pey = Service('홍길동') #가입하면서 이름도 저장한다.
pey.sum(1, 1)
#원래는 이렇게 했어야 한다.
#pey = Service()
#pey.setname('홍길동')
#pey.sum(1, 1)



###클래스 자세히 알기
#class 클래스이름(상속 클래스명):
#    <클래스 변수 1>
#    <클래스 변수 2>
#    ...
#    def 클래스함수1(self[, 인수1, 인수2,,,]):
#        <수행할 문장 1>
#        <수행할 문장 2>
#        ...
#    def 클래스함수2(self[, 인수1, 인수2,,,]):
#        <수행할 문장1>
#       <수행할 문장2>
#        ...
#    ...

###사칙연산 클래스 만들기
class FourCal:
	pass
a = FourCal()
print(type(a)) #<class '__main__.FourCal'>
#class 객체이며, main클래스 내의 Fourcal 클래스이다.

#데이터셋 저장
class FourCal:
	def setdata(self, first, second): #setdata라는 FourCal 클래스의 메소드라고도 한다.
		self.first = first
		self.second = second
	def sum(self):
		result = self.first + self.second
		return result
	def mul(self):
		result = self.first * self.second
		return result
	def sub(self):
		result = self.first - self.second
		return result
	def div(self):
		result = self.first / self.second
		return result
	
a = FourCal()
a.setdata(4, 2)
print(a.first)
print(a.second)
print(a.sum()) #a라는 객체가 self 들어가서 sum(a)가 불러지고, result = a.first + a.second = 4+2 = 6이 나온다.
print(a.mul())
print(a.sub())
print(a.div())

#위의 a와는 따로 저장된 정보라는 것을 알 수 있다. a, b는 고유한 저장영역(네임스페이스)을 갖고 있다.
b = FourCal()
b.setdata(3, 7)
print(b.first)
print(b.second)
print(b.sub())
print(b.mul())
print(b.sub())
print(b.div())




###서씨네 집 클래스
class HouseSeo:
	lastname = "서" #lastname이라는 필드를 초기화 해준다.
	def setname(self, name): #setname 메소드에서 fullname이라는 필드를 초기화해준다.
		self.fullname = self.lastname + name
	def travel(self, where): #travel 메소드 정의
		print("%s, %s여행을 가다." %(self.fullname, where))
pey = HouseSeo()
pey.setname("덕오")
pey.travel("부산")
print(pey.lastname)
print(pey.fullname)


#초기값 설정하기. __init__ 이를 생성자라고 한다.
#pey = HousePark()
#pey.travel("부산")
#이렇게 하면 오류가 난다. pey.setname("덕오")이부분이 있어야 이름이 완성되고 travel이 실행 가능해진다.

class HouseSeo:
	lastname = "서"
	def __init__(self, name):
		self.fullname = self.lastname + name
	def travel(self, where):
		print("%s, %s여행을 가다." %(self.fullname, where))
#pey = HousePark() #TypeError: __init__() missing 1 required positional argument: 'name'. 이름을 넣자.
pey = HouseSeo("덕오")
pey.travel("태국")

##상속
#서씨네집을 이용해서 김씨네집을 만들어 보자.
class HouseKim(HouseSeo): #이렇게 해서 HousePark을 상속받는다.
	lastname = "김" #수정되는 부분만 적어준다. 이런 것을 override라 함
#이것과 완전 동일하게 작용한다.
#class HouseKim:
#      lastname = "김"
#    def __init__(self, name):
#        self.fullname = self.lastname + name
#	def travel(self, where):
#        print("%s, %s여행을 가다." % (self.fullname, where))
juliet = HouseKim('줄리엣')
juliet.travel("독도")

#상속을 살짝 수정
class HouseKim(HouseSeo):
	lastname = "김"
	def travel(self, where, day): #메소드에서 바꾸고 싶은 부분만 살짝 바꿔준다. 메소드명을 동일하게 재구현하는 것을 메소드 오버라이딩이라고 한다.
		print("%s, %s여행 %d일 가네." %(self.fullname, where, day))
juliet = HouseKim('줄리엣')
juliet.travel("독도", 3)


##연산자 오버로딩
#연산자 오버로딩(Overloading)이란 연산자(+, -, *, /,,, )등을 객체끼리 사용할 수 있게 하는 기법을 말한다.
pey = HouseSeo('덕오')
juliet = HouseKim('줄리엣')
#pey + juliet #결과 : 박응용, 김줄리엣 결혼했네
#객체끼리 연산자 기호를 사용하는 방법을 의미

#서 클래스
class HouseSeo:
    lastname = "서"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다." % (self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
    def fight(self, other):
        print("%s, %s 싸우네" % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullname, other.fullname))


#김 클래스
class HouseKim(HouseSeo):
    lastname = "김" #필드값 다른것으로 변경해서 사용
    def travel(self, where, day): #다른 메소드는 모두 HousePark의 메소드를 상속받고, travel 메소드는 살짝 변경
        print("%s, %s여행 %d일 가네." % (self.fullname, where, day))

pey = HouseSeo("덕오") #객체 생성
juliet = HouseKim("줄리엣") #객체 생성
pey.love(juliet) #love메소드 호출
pey + juliet #+연산자를 객체에 사용하게 되면 클래스의 __add__ 함수가 호출된다.
#pey + juliet을 하면 __add__(self, other)가 호출되는데 __add__(pey, juliet)과 같다.
pey.fight(juliet)
pey-juliet
