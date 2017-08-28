#집합
s1 = set([1, 2, 3])
print(s1)
s2 = set("Hello")
print(s2) #unique하게 나온다.
# 특징 : 순서가 없다. 중복을 허용하지 않는다. 중복없애는 필터의 역할을 종종 한다.
# 순서가 없기 때문에 인덱싱이나 슬라이싱 불가.

#인덱싱으로 접근하기 위해서는 list나 터플로 변환 후 사용 가능
s1 = set([1, 2, 3])
print(s1)
l1 = list(s1)
print(l1)
print(l1[0])

#교집합, 합집합, 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
#교집합 &
print(s1&s2)
print(s1.intersection(s2))
#합집합 |
print(s1|s2)
print(s1.union(s2))
#차집합 -
print(s1-s2)
print(s1.difference(s2))

#추가와 삭제
s1 = set([1, 2, 3])
s1.add(4) #한개의 값만 추가
print(s1)

s1 = set([1, 2, 3])
s1.update([4, 5, 6]) #여러 값 추가
print(s1)

s1 = set([1, 2, 3])
s1.remove(2) #제거
print(s1)


