#변수
a=3
# a는 변수 이름으로서 3이라는 정수형 객체가 저장된 메모리 위치를 가리키게 된다. 

a, b = 'python', 'life'
print(a) #앞의 python
print(b) #뒤의 life
print(a, b)

(a, b) = ('python', 'life')
print((a, b))
print(a,b)
print(a)
[a, b] = ['ython', 'ife']
print([a, b])
print(a,b) #이렇게 들어가면 튜플처럼 되므로 list를 살리려면 [a, b]로 적어줘야한다.
print(a)

#두 변수의 값 바꾸기
a = 3
b = 5
a, b = b, a
print(a)
print(b)

#리스트 복사
a = [1, 2, 3]
b = a #b라는 리스트를 a가 가리키는 리스트를 똑같이 가리키게 해줬다.
a[1] = 4 #a의 값을 바꿔주니
print(a)
print(b) #b의 값도 바뀌었다.
#가리키는 것이 아니라 새로운 리스트를 만들어 내는 방법
#1. [:]를 이용해 리스트 전체를 가리킨다.
a = [1, 2, 3]
b = a[:] #리스트 전체를 가리켜서 바꿔준다.
a[1] = 4
print(a) #a의 값만 바뀌었다.
print(b) #b의 값은 바뀌지 않았다.

#2. copy모듈 이용
from copy import copy
b = copy(a) # b=a[:]와 같은 역할을 한다.
#두 객체가 같은 것을 가리키는지 확인하기 위해서는 is를 이용한다.
print(a)
print(b) #같은 값이지만,
print(b is a) #False가 나온다.
