#딕셔너리
#대응관계를 자료형으로 만듦.
#Associative array, Hash 라고도 불린다.
#key와 value가 쌍으로 존재한다.
#리스트나 튜플처럼 순차적으로 요소값을 구하지 않고,
#key를 통해 value를 얻는다.
dic = {'name':'pey', 'phone':'01199993323', 'birth':'1118'}
a = {1:'hi'} #key를 정수1로, value를 'hi'로 줄 수 있다.
a = {'a':[1, 2, 3]} #value에 리스트가 들어갈 수도 있다.

#key를 이용하여 value 얻기
grade = {'pey':10, 'julliet':99}
print(grade['pey']) #리스트나 튜플은 인덱싱과 슬라이싱으로 값을 얻었지만 딕셔너리는 변수[key]로 얻는다.
a = {1:'a', 2:'b'}
print(a[1])
dic = {'name':'pey', 'phone':'01199993323', 'birth':'1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

#딕셔너리 쌍 추가, 삭제하기
#딕셔너리는 순서를 따지지 않는다.
a = {1:'a'}
a[2] = 'b'
print(a) #a라는 딕셔너리에 key=2, value=b인 쌍을 넣었다.
a['name'] = 'pey'
print(a) #a라는 딕셔너리에 key=name, value=pey인 쌍을 넣었다.
a[3] = [1, 2, 3]
print(a) #a라는 딕셔너리에 key=3, value=[1, 2, 3]인 쌍을 넣었다.
#삭제하기
del a[1]
print(a) #del a[key]를 하면 해당하는 key:value 쌍이 삭제된다.

###주의사항
#key는 고유한 값이므로 중복되면 안된다.
#중복 된다면 어떤 것이 지워지는지 모르므로 최대한 중복하지 말자.
a = {1:'a', 1:'b'}
print(a) #1:'a'가 지워짐
#key에는 리스트를 쓸 수 없다. 하지만 튜플은 key로 사용 가능하다.
#즉, 변하지 않는 값은 key로 사용 가능하다.

#리스트를 넣었을 경우의 에러
#a = {[1, 2] : 'hi'}
#print(a)
#TypeError: unhashable type: 'list'

#key 리스트 만들기
a = {'name':'pey', 'phone':'01199993323', 'birth':'1118'}
print(a.keys())
#원래는 list를 리턴했지만 3버젼 이후에는 list를 리턴할 때 발생하는 메모리 낭비를 줄이기 위해
#dict_key라는 객체를 리턴한다.이후 소개되는 dict_values dict_items역시 마찬가지이다.
#만약 리스트가 필요한 경우는 다음과 같이 사용한다..
print(list(a.keys())) #리스트로 형 변환
#하지만 리스트로 변환하지 않아도 for문 등에서 사용 가능하다.
#리스트의 고유 메소드인 append, insert, pop, remove, sort등은 사용 불가
for k in a.keys():
	print(k)

#value 리스트 만들기
print(a.values())
print(list(a.values()))

#item 쌍 얻기
print(a.items())
print(list(a.items())) #리스트로 만들 경우, 각 쌍이 튜플형태로 고정된다.

#쌍 모두 지우기
a.clear()
print(a)

#key로 value 얻기(get)
a = {'name':'pey', 'phone':'01199993323', 'birth':'1118'}
print(a.get('name')) #a['name']과 같은 결과를 나타내는데,
print(a.get('nam'))
a['nam']
#차이점으로는 만약 없는 key를 가져오려고 할 경우에 a['nokey']는 KeyError를 발생시키고,
#a.get('nokey')는 지정해 준 None을 리턴하는 차이가 있다.

#print(a.get('nokey')) #None
#print(a['nokey']) #KeyError: 'nokey'

#딕셔너리 내에 찾으려는 key가 없을 경우 default 값으로 가져오고 싶을때는
#get(x, 'defualt')을 사용하면 편리하다.
print(a.get('foo', 'bar')) #bar

#key가 있는지 조사 (in)
a = {'name':'pey', 'phone':'01199993323', 'birth':'1118'}
print('name' in a) #있을 경우 True
print('email' in a) #없을 경우 False
