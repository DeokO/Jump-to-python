#제어문_if문
#들여쓰기가 중요하다.
#수행할 문장이 모두 같은 깊이로 들여쓰여져야 한다.
money=1
if money:
	print("택시를 타고 가라")
else:
	print("걸어가라")

money=2000
if money>=3000:
 print("택시")
else :
 print("걸어가라")

money = 2000
card = 1
if money >= 3000 or card:
 print("택시")
else :
 print("걸어가라")

pocket = ['paper', 'cellphone', 'money'] #리스트가 아니라 튜플도 가능
if 'money' in pocket:
 print('택시')
else :
 print('걷기')

pocket = ['paper', 'handphone']
card = 1
if 'money' in pocket:
 print('택시')
elif card:
 print('택시')
else :
 print('걷기')
 
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
 pass #아무런 결과도 일어나지 않게 해준다. next와 같은 역할인 듯 하다.
else :
 print('카드를 꺼내라')

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket : pass
else : print('카드를 꺼내라')


