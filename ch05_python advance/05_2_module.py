#날개달기_모듈
#모듈 : 함수, 변수, 클래스들을 모아놓은 파일


###모듈 불러오는 방법

# 1. PYTHONPATH환경변수를 사용하는 방법
#cmd에서 C:\Users\home>set PYTHONPATH=C:\Python\Mymodules 이렇게 set함수를 이용해서 PYTHONPATH를 설정해준다.

# 2. sys.path에 경로를 추가해서 사용하는 방법
#sys모듈을 이용해서 파이썬 라이브러리가 설치되어 있는 디렉토리를 확인 할 수 있다.
import sys
print(sys.path)
#sys.path에 우리의 모듈의 위치를 추가해주자. 리스트 형태이므로 append로 저장 가능
sys.path.append('./ch05_python advance')

###모듈 만들고 불러보기
#mod1.py
import sys
sys.path.append('./ch05_python advance')
import mod1
print(mod1.sum(3, 4)) #7이 나온다.

#mod1.py에 safe_sum 함수 추가
print(mod1.safe_sum(3, 4))
print(mod1.safe_sum(1, 'a'))

#sum을 바로 쓰고 싶을 때
from mod1 import sum
print(sum(3, 4))

#sum과 safe_sum모두 사용하고 싶을 때
from mod1 import sum, safe_sum
from mod1 import *

# mod1.py
# if __name__ == "__main__":
# def sum(a, b):
#     return a+b
#
# def safe_sum(a, b):
#     if type(a) != type(b):
#         print("더할수 있는 것이 아닙니다.")
#         return
#     else:
#         result = sum(a, b)
#     return result
# print(safe_sum('a', 1))
# print(safe_sum(1, 4))
# print(sum(10, 10.4))
#이렇게 mod1.py를 만들고 이를 import 하려하면 아래의 3개의 print문이 실행되어버린다.

#이때 이렇게 수정하자
if __name__ == "__main__" :
	print(safe_sum('a', 1))
	print(safe_sum(1, 4))
	print(sum(10, 10.4))
#이렇게 했을 때는 cmd에서 C:/Python> c:\Python34\python mod1.py 이렇게 직접 실행했을때는
#실행이 되는데, 대화형 인터프리터나 다른 파일에서 import 할때는 if문이 거짓이 되어
#print가 실행되지 않게 된다는 의미이다.


##클래스나 변수등을 포함한 모듈
#mod2.py
# PI = 3.141592
#
# class Math:
# 	def solv(self, r):
# 		return PI * (r**2)
#
# def sum(a, b):
# 	return a+b
#
# if __name__ == "__main__":
# 	print(PI)
# 	a = Math()
# 	print(a.solv(2))
# 	print(sum(PI, 4.4))

import mod2
print(mod2.PI) #3.141592 출력. mod2의 변수를 사용할 수 있다.
a = mod2.Math()
print(a.solv(2)) #mod2의 Math 클래스의 인스턴스를 만들어서 사용할 수 있다.


