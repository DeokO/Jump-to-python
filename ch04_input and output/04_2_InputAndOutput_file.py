#입출력_파일 읽고 쓰기
#f = open("새파일.txt", 'w')
#f.close()
#r : 읽기모드 - 읽기만 함.
#w : 쓰기모드 - 내용을 씀. 해당파일이 존재할 경우 원래 내용이 다 사라짐. 존재하지 않으면 새로 생김
#a : 추가모드 - 파일의 마지막에 새로운 내용을 추가
#새로운 파일을 경로 지정해서 만들기. close를 통해 최대한 닫아주도록 하자.
#f = open("C:\Python34\새파일.txt", 'w')
#f.close()

#파일을 쓰기모드로 열어서 출력값 적기
f = open("C:\Python34\새파일.txt", 'w')

for i in range(1, 11):
	data = "%d번째 줄입니다. \n" %i
	f.write(data)
f.close()

#파일을 읽는 여러가지 방법
#1. readline()이용
f = open("C:\Python34\새파일.txt", 'r')
line = f.readline() #첫번째 라인을 저장함
print(line) #출력
f.close()
#모든 라인을 출력하고 싶다면
f = open("C:\Python34\새파일.txt", 'r')
while True:
	line = f.readline() #한줄씩 pop하는 느낌인거 같다.
	if not line : 
		break
	print(line)
f.close()

#2. readlines()를 이용
f = open("C:\Python34\새파일.txt", 'r')
lines = f.readlines() #모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트를 리턴
for line in lines:
	print(line)
f.close()

#3. read() 이용
f = open("C:\Python34\새파일.txt", 'r')
data = f.read() #파일의 내용 전체를 문자열로 리턴한다.
print(data)
f.close()

#파일에 새로운 내용 추가하기
f = open("C:\Python34\새파일.txt", 'a')
for i in range(11, 20):
	data = "%d 줄입니다.\n" %i
	f.write(data)
f.close()

#with문과 함께 사용하기
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()
#이제까지는 이렇게 열고 닫았다. close를 자동으로 하자.
with open("foo.txt", 'w') as f: #f라는 이름으로 open한다.
	f.write("Life is too short, you need python") #그 f에 ~~를 write한다.
#with를 벗어나는 순간 열린 파일객체 f가 자동으로 close 된다. with는 다른데서도 쓰인다.

#sys모듈 입력
#이를 저장하고 도스로 열어서 하는 방법.
#import sys
#for i in args:
#	print(i)
#####################################





