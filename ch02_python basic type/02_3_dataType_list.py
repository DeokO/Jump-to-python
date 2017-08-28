###리스트
odd = [1,3,5,7,9]
a = []
b = [1,2,3]
c = ['Life', 'is', 'too', 'short']
d = [1,2,'Life', 'is'] # 문자와 숫자 모두 넣을 수도 있다.
a = list()

#리스트의 인덱싱
a  = [1, 2, 3]
print(a)
print(a[0] + a[2])
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1]) #뒤에서 첫번째
print(a[3][0]) #R에서와 같이 접근한다.
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])

#리스트의 슬라이싱 알아보기
a = [1, 2, 3, 4, 5]
print(a[0:2])
a = '12345'
print(a[0:2])#문자열도 하나하나로 접근 가능하다. substring 개념으로
a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)
print(c)
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

#리스트를 더하고 반복하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b) #더하기. vector 연산이 아니고 append 된다.
print(a*3) #곱하기. 이것도 3번 append 된다. repeat

#리스트의 수정 변경
a = [1, 2, 3]
a[2] = 4
print(a) #문자열에서는 위와같은 방식의 수정이 불가했지만 리스트는 가능
a[1] = ['a', 'b', 'c']
print(a) #위의 방법과 a[1:2] = ['a', 'b', 'c']는 다른 결과가 나온다.
a = [1, 2, 3]
a[2] = 4
a[1:2] = ['a', 'b', 'c']
print(a)
#a[1:2]는 a[1]에서 a[2]사이의 리스트를 ['a', 'b', 'c']로 바꾼다는 말이고, //결과 : [1, 'a', 'b', 'c', 4]
#a[1]는 a의 두번째 요소를 바꾼다는 의미이다. //결과 : [1, ['a', 'b', 'c'], 4]
#따라서 둘은 다른 결과를 얻게 된다.

#리스트 요소 삭제
a[1:3] = []
print(a)
del a[1] #a의 1번째 요소를 제거한다. del a[x:y] 형태로 사용 가능
print(a)

##참고
a = [1, 2, 3]
#a의 2번째 요소에 hi를 붙이고 싶다면?
print(str(a[2])+'hi') #string형태로 만들어서 둘을 더해주면 된다.


###리스트 관련 함수들
#리스트에 요소 추가
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6]) #리스트도 추가 가능
print(a)
a[5:] = [5, 6]

#리스트 정렬
a = [1, 4, 3, 2]
a.sort()
print(a)
a = ['a', 'c', 'b']
a.sort()
print(a)

#리스트 뒤집기
#순서를 맞춘 뒤 거꾸로 하는것이 아니다. 그냥 그대로 뒤집어 준다.
a = ['a', 'c', 'b']
a.reverse()
print(a)

#위치 반환
a = [1, 2, 3]
print(a.index(3)) #3이 어디에 있는지 그 index를 알려준다.
print(a.index(1))
#print(a.index(0)) #0은 a 리스트에 없으므로 오류가 난다.

#리스트에 요소 삽입
#insert(a, b) : a번째 위치에 b를 삽입한다.
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

#리스트 요소 제거
#remove(x) : 처음 나오는 x를 제거하는 함수
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
a.remove(3)
print(a)

#리스트 요소 끄집어내기
#pop() : 맨 마지막 요소를 돌려주고 그 요소를 리스트에서 제거한다.
a = [1, 2, 3]
b = a.pop()
print(a) #a에서는 맨 마지막 요소인 3이 지워지고
print(b) #b에는 그 지워진 값이 저장된다.
a = [1, 2, 3]
b = a.pop(1)
print(a) #a에서는 1번째 요소인 2가 지워지고
print(b) #b에는 그 지워진 값이 저장된다.

#갯수 세기
#count(x) : 리스트 중에서 x가 몇 개 있는지를 조사하여 갯수를 돌려준다.
a = [1, 2, 3, 1]
print(a.count(1))
#R에서 sum(a==1)과 같다.
a.index(1)
a.pop(0)
a
a.index(1)
a.pop(2)
a

#리스트 확장
#extend(x) : a라는 리스트에 x라는 리스트를 더한다. x는 리스트만 가능
a = [1, 2, 3]
a.extend([4, 5])
print(a) # a.extend([4, 5]) == a + [4, 5]

