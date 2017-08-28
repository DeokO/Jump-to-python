#튜플(터플)
#튜플은 ()로 생성하고, 값을 생성, 삭제, 수정이 불가능하다.
t1 = ()
t2 = (1, )
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
#t2와 같이 한개일 경우엔 뒤에 콤마를 써준다.
#t4와 같이 괄호를 하지 않아도 된다.

##튜플의 인덱싱, 슬라이싱, 더하기, 반복
#인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

#슬라이싱
print(t1[1:])

#더하기
t2 = (3, 4)
print(t1 + t2) #뒤에 확장되는 형태로 된다.

#반복
print(t2*3)

#튜플을 지우려고 할 때의 에러
#del t1[0]
#TypeError: 'tuple' object doesn't support item deletion

#튜플을 수정하려고 할 때의 에러
#t1[0] = 'c'
#TypeError: 'tuple' object does not support item assignment
