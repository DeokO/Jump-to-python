#제어문_if문
#들여쓰기가 중요하다.
#수행할 문장이 모두 같은 깊이로 들여쓰여져야 한다.
money=1
if money:
	print("택시를 타고 가라")
else:
	print("걸어가라")

#부등식을 이용한 조건문
money=2000
if money>=3000:
    print("택시")
else :
    print("걸어가라")

#두 조건중 하나 만족하는 경우에 대한 조건문
money = 2000
card = 1
if money >= 3000 or card:
    print("택시")
else :
    print("걸어가라")

#해당 원소가 list(혹은 tuple)에 있는지에 대한 조건문
pocket = ['paper', 'cellphone', 'money'] #리스트가 아니라 튜플도 가능
if 'money' in pocket:
    print('택시')
else :
    print('걷기')

#elif를 이용해 다른 조건을 주는 조건문
pocket = ['paper', 'handphone']
card = 1
if 'money' in pocket:
    print('택시')
elif card:
    print('택시')
else :
    print('걷기')

#pass 이해하기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass #아무런 결과도 일어나지 않게 해준다. next와 같은 역할인 듯 하다.
else :
    print('카드를 꺼내라')

#간결하게 코딩
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket : pass
else : print('카드를 꺼내라')


