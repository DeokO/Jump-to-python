#제어문_for문
#for 변수 in 리스트 :

test_list = ['one', 'two', 'three']
for i in test_list:
	print(i)

mark = [90, 25, 67, 45, 80]
num = 0
for i in mark:
	num += 1
	if i>= 60 :
		print("%d번 학생은 합격입니다." %num)
	else:
		print("%d번 학생은 불합격입니다." %num)

#for와 continue
#continue를 만나면 for문의 증감문으로 직행한다.
mark = [90, 25, 67, 45, 80]
num = 0
for i in mark:
	num += 1
	if i < 60: continue
	print("%d번 학생은 합격입니다." %num)

#range : 숫자 리스트를 자동으로 만들어 준다.
a = range(10) #0~9
a = range(1, 11) #1~10
sum = 0
for i in range(1, 11):
	sum = sum+i
print(sum)

mark = [90, 25, 67, 45, 80]
for i in range(len(marks)):
	if marks[i] < 60 : continue
	print("%d번 학생은 합격입니다." %(i+1))

#다양한 for문의 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
	print(first+last)
#위 예는 a의 리스트 요소 값이 튜플이기 때문에 각각의 요소들이 자동으로 (first, last)라는 변수에 대입된다.
#(first, last) = (1, 2) 와 같이 들어간다.

#for, range를 이용한 구구단
for i in range(2, 10):
	for j in range(1, 10):
		print(i, "*", j, "=", i*j, end=" ") #프린트 되는 것을 띄어쓰기로 구분. end가 안먹힌다.
	print("") #각 단이 다 되면 엔터하는 역할

#리스트 내포
a = [1, 2, 3, 4]
result = []
for num in a:
	result.append(num*3)
print(result)
result = [num*3 for num in a] #리스트 안에 for를 내포한다. 위와 같은 결과를 얻는다. 조건제시법과 같은듯
result = [num*3 for num in a if num%2==0] #그중 짝수만 포함시키는 코드
#[표현식 for 항목 in 반복가능객체 if 조건] 조건부분은 생략이 가능하다.
#for를 여러개 사용할 수도 있다.
#구구단 담기
result = [x*y for x in range(2, 10)
	      for y in range(1, 10)]
print(result)