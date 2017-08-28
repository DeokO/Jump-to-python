###자료형 - 숫자형

#정수형
a = 123
print(a)
b = -178
print(b)

#소수점(Floating-point)
a=1.2
b=-3.45
c=4.24E10
d=4.24e-10
print(c)
print(d)

#8진수
#숫자0, 알파벳(O or o)으로 시작하면 된다.
a=0o177
print(a)

#16진수
#숫자0, 알파벳 x 으로 시작하면 된다.
a=0x8ff
b=0xABC
print(a)
print(b)

#복소수
a = 1+2j
b = 3-4j
print(b)
print(a.real) #실수부
print(a.imag) #허수부
print(abs(a)) #복소수의 크기

#숫자 연산
a=3
b=4.0
print(a+b)
print(a-b)
print(a*b)
print(a/b) #파이썬 3버젼 이상은 실수형으로 바꿔줄 필요 없다.
print(7%3) #나머지
print(7//4) #몫
