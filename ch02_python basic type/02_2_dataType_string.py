###자료형 - 문자열
a = "string"
a = 'string'
a = """string"""
a = "Python's favorite food is perl"
a = 'Python\'s favorite food is perl'

#여러줄 문자열
#Life is too short
#You need python
multiline1 = "Life is too short \n You need python"
multiline2 = """
Life is too short
You need python
"""
print(multiline2)

#문자열 연산
head = "Python"
tail = " is fun!"
print(head + tail)
print(head*2)

#인덱싱과 슬라이싱
a = "Life is too short, You need Python"
print(a[3])
print(a[0])
print(a[12])
print(a[-1])
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4]) #0이상 4미만의 인덱스를 가져옴
print(a[19:]) #19번째 부터 끝까지
print(a[:17]) #처음부터 16번째 까지
print(a[:]) #처음부터 끝까지
print(a[19:-7]) #-부호도 사용 가능하다.

#자주 사용되는 슬라이싱 예
a = '20010331Rainy'
date = a[:8]
weather = a[8:]
print(date)
print(weather)
year = a[:4]
day = a[4:8]

#Pithon을 Python으로 바꾸기
a = "Pithon"
print (a[1]) #i가 나온다.
#a[1] = 'y' #로 해주면 오류가 난다. 문자열의 요소값은 바꿀 수 없다.(문자열, 튜플등)
print(a[:1] + 'y' + a[2:]) #새롭게 문자열을 만들어버리자.

#문자열 포매팅
print("I eat %d apples." %3)
print("I eat %s apples." %"five")
number=3
print("I eat %d apples." %number)
number=10
day='three'
print("I ate %d apples. so I was sick for %s days." %(number, day)) #,로 구분한다.

#문자열 포맷 코드
#%(s:문자열, c:문자한개, d:정수, f:부동소수, o:8진수, x:16진수, %:문자 % 자체)
print("I have %s apples" %3)
print("rate is %s%%" %3.234) #%s는 뒤에서 받는 내용을 문자열로 바꾸기 때문에 어떤 것이 와도 된다.

#포맷 코드의 또 다른 기능
#1. 정렬과 공백
print("%10s" %"hi") #총 10개 칸을 할당하고 오른쪽부터 채운다.
print("%-10sjane" %"hi") #총 10개 칸을 할당하고 왼쪽부터 채운다. 그 이후 jane을 채움
#2. 소수점 표현
print("%0.4f" %3.42134234) #소수점 이하 4자리만 할당
print("%10.4f" %3.42134234) #총 10자리 중 소수점 이하 4자리까지를 오른쪽 정렬한다.

#문자열 함수
#고급 문자열 포매팅. 문자열 변수이름 뒤에 '.'을 붙인 다음 함수이름을 써주면 된다.
#숫자 바로 대입
print("I eat {0} apples" .format(3))
#문자 바로 대입
print("I eat {0} apples" .format("five"))
#변수 바로 대입
number=3
print("I eat {0} apples" .format(number))
#두개 이상 값 치환
#{0}, {1}등 순서대로 숫자를 주면 되는 것 같다.
number=10
day='three'
print("I ate {0} apples. so I was sick for {1} days." .format(number, day))
#이름으로 치환하기
#이 방법이 가장 직관적인 것 같다.
print("I ate {number} apples. so I was sick for {day} days." .format(number=10, day=3))
#혼용해서 사용하기
print("I ate {0} apples. so I was sick for {day} days." .format(10, day=3))
#좌측 정렬
print("'{0:<10}'" .format('hi')) #{0}, {1}, ..., {10} 까지중에서 왼쪽(<)으로 정렬하고, 처음 0값에 hi를 준다.
#우측 정렬
print("'{0:>10}'" .format('hi')) #{0}, {1}, ..., {10} 까지중에서 오른쪽(>)으로 정렬하고, 마지막 10값에 hi를 준다.
#가운데 정렬
print("'{0:^10}'" .format('hi'))  #{0}, {1}, ..., {10} 까지중에서 가운데(^)으로 정렬하고, 가운데 5값에 hi를 준다.
#공백 채우기
print("'{0:*^10}'" .format('hi')) #위처럼 채우고, 공백에는 *로 채운다.
print("'{0:!<10}'" .format('hi'))
#소수점 표현
y=3.42134234
print("'{0:0.4f}'" .format(y))
print("'{0:10.4f}'" .format(y))
#{, } 표현하기
print("{{ and }}" .format()) #두번 연속해서 사용

#소문자를 대문자로 바꾸기
a = "hi"
print(a.upper())

#문자 개수 세기. a에서 b의 개수 세기
a = 'hobby'
print(a.count('b'))

#위치 알려주기 (find)
a = "Python is best choice"
print(a.find('b')) #b가 처음 나온 위치를 알려준다. 만약 존재하지 않으면 -1을 준다.

#위치 알려주기 (index)
a = "Life is too short"
print(a.index('t')) #find와 다른 점은, 만약 존재하지 않으면 에러를 내보낸다.

#문자열 삽입(join). R의 paste와 같다.
a = ","
print(a.join('abcd')) #'abcd'문자열과 ,를 조인한다.
a = "abcd"
print(a.join(',,,,,')) #이렇게 하면 복제되는 느낌이다. collapse를 주는 느낌

#대문자를 소문자로 바꾸기
a='HI'
print(a.lower())

#왼쪽 공백 지우기
a = '    hi'
print(a.lstrip())

#오른쪽 공백 지우기
a = 'hi     '
print(a.rstrip())

#양쪽 공백 지우기
a = '   hi   '
print(a.strip())

#문자열 바꾸기
a = "Life is too short, Life"
print(a.replace("Life", "Your leg")) #a 문자열에서 Life라는 값을 Your leg로 바꾼다. 여러개여도 다 바꾼다.

#문자열 나누기
a = "Life is too short"
print(a.split()) #공백 기준으로 나눈다.
a = "a:b:c:d"
print(a.split(':')) #공백은 따로 지정하지 않아도 되지만 다른 문자는 ''안에 지정해줘야 된다.






