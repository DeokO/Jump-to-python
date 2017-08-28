#날개달기_외장함수
#명령행에서 인수를 전달(sys.argv)
#argv_test.py
import sys
print(sys.argv)
#cmd창에서 
#C:/Python/Mymodules> python argv_test.py you need python 라고 입력한다면
#['argv_test.py', 'you', 'need', 'python']이 출력되는데
#python이란 명령어 뒤의 모든 것들이 공백을 기준으로 나뉘어서 sys.argv 리스트의 요소가 된다.

#강제 스크립트 종료법(sys.exit)
#sys.exit() 프로그램 파일내에서 사용되면 프로그램을 중단한다.

#자신이 만든 모듈 불러서 쓰기(sys.path)
import sys
print(sys.path) #모듈들이 저장되어 있는 위치를 나타낸다.
sys.path.append("C:/Python/Mymodules") #로 path를 추가할 수 있다.

#객체를 그 상태 그대로 파일에 저장하고 싶을 때(pickle)
#저장
import pickle
f = open("test.txt", 'wb')
data = {1:'python', 2:'you need'}
pickle.dump(data, f)
f.close()
#text.txt 파일을 쓰기모드로 열고, 딕셔너리 객체이 data를 그대로 f에 저장하는 방법이다.
#pickle.dump 메소드를 사용한다.
#불러오기
import pickle
f = open('text.txt', 'rb')
data = pickle.load(f)
print(data)
#어떤 자료형이든지 상관없이 자정하고 불러올 수 있다.
help(open)
#현재 내 시스템 환경변수값을 알고싶을 때(os.environ)
import os
print(os.environ)
#딕셔너리 객체를 돌려준다.
print(os.environ['PATH'])
#딕셔너리에서 키값이 PATH인 것만을 가져오는 방법이다.

#디렉토리에 대한 것들(os.chdir, os.getcwd)
#현재 디렉토리의 위치를 변경, 얻을 수 있다.
os.chdir("C:WINDOWS") #os. change directory 인듯 하다.
os.getcwd() #os. get current working directory 인듯 하다.

#시스템 명령(os.system, os.popen)
#os.system : 시스템의 유틸리티나 기타 명령어들을 파이썬에서 호출 할 수 있다. 
print(os.system('dir')) #dir의 결과값이 출력된다.
#os.popen : 시스템 명령어를 실행시킨 결과값을 읽기모드 형태의 파일객체로 돌려준다.
f = os.popen('dir')
print(f.read())
#os.mkdir(디렉토리) : 디렉토리를 생성한다.
#os.rmdir(디렉토리) : 디렉토리를 삭제한다. 단, 디렉토리가 비어있어야 삭제가능
#os.unlink(파일) : 파일을 지운다.
#os.rename(src, dst) : src라는 이름와 파일을 dst라는 이름으로 바꾼다.

#파일복사(shutil)
#src라는 이름의 파일을 dst로 복사한다. 만약 dst가 디렉토리 이름이면 src라는 파일이름으로 dst 디렉토리에 복사하고 그 이름이 존재하면 덮어쓴다.
import shutil
shutil.copy('src.txt', 'dst.txt')

#디렉토리에 있는 파일들을 리스트로 만들기 (glob)
#*, ?등의 메타문자를 써서 원하는 파일만을 읽어들일 수도 있다.
#C:/Python이란 디렉토리에 있는 파일중 이름이 Q문자로 시작하는 파일을 모두 찾아서 읽는 예
import glob
glob.glob("C:/Python/Q*")

#임시파일(tempfile)
#tempfile.mktemp()는 중복되지 않는 임시파일의 이름을 만들어서 돌려준다.
import tempfile
filename = tempfile.mktemp()
print(filename)
#일반적으로 w+b의 모드를 갖는다. f.close()가 호출될 때 자동으로 사라진다.
import tempfile
f = tempfile.TemporaryFile()
f.close()

#시간에 관한 것들(time)
#1970년 1월 1일 0시 0분 0초가 기준이다.
#time.time은 현재 시간을 실수형태로 반환하여준다.
import time
time.time() # ~~~~~~~

#time.localtime : time.time()에 의해 반환된 실수값을 이용해 년도, 달, 월, 시, 분, 초 ... 의 형태로 바꾸어주는 함수이다.
time.localtime(time.time())
time.struct_time(tm_year=2013, tm_mon=5, tm_mday=21, tm_hour=16, tm_min=48, tm_sec=42, tm_wday=1, tm_yday=141, tm_isdst=0)

#time.asctime : time.localtime에 의해 반환된 터플형태의 값을 인수로 받아서 알아보기 쉬운 날짜와 시간 형태의 값을 반환한다.
time.asctime(time.localtime(time.time())) #'Sat Apr 28 20:50:20 2001'

#time.ctime : 위의 time.asctime을 간단히 사용하는 버젼
time.ctime() #'Sat Apr 28 20:50:20 2001'

#time.strftime : 시간에 관계된 것을 세밀하게 표현할 수 있는 여러가지 포맷코드를 제공
#여러가지가 있다. 용도에 맞게 사용하면 도니다.
import time
time.strftime('%x', time.localtime(time.time())) #'05/01/01' %x : 현재 설정된 로케일에 기반한 날짜 출력. 06/01/01
time.strftime('%c', time.localtime(time.time())) #'05/01/01 17:22:21'  %c : 날짜와 시간을 출력.

#time.sleep : 루프 안에서 많이 쓰임. 일정시간 간격을 주기 위해 사용된다.
#sleep1.py
import time
for i in range(10):
	print(i)
	time.sleep(1)
#1초 간격으로 0부터 9까지의 숫자를 출력한다. time.sleep()안에 실수형으로 들어갈 수 있다. 0.5등

#달력쓰기(calender)
import calendar
print(calendar.calendar(2016))
calendar.prcal(2016) #이 둘은 같은 결과를 보여준다.
#2001년 4월만 보기
calendar.prmonth(2001, 4)

#요일보기
calendar.weekday(2001, 4, 28) #5
#0 : 월요일 ~~ 6 : 일요일

#calendar.monthrange(년도, 월) : 해당 당의 1일이 무슨 요일인지, 그달이 몇일까지 있는지를 보여준다.
calendar.monthrange(2001, 4) #(6, 30) 1일이 일요일이고, 30일까지 있음을 의미한다.

#난수 발생시키기(random)
import random
random.random() #0.0에서 1.0 사이의 실수값 중에서 난수값을 돌려준다.
random.randint(1, 10) #1에서 10사이의 정수중 난수로 하나를 준다.
random.randint(1, 55) #1에서 55사이
#help(random.randint)

#random_pop.py
import random
def random_pop(data):
	number = random.randint(0, len(data)-1)
	return data.pop(number)
if __name__ == '__main__' :
	data = [1, 2, 3, 4, 5]
	while data : 
		print(random_pop(data))
#data에 저장된 요소를 하나씩 무작위로 꺼내게 된다. number라는 곳에 index가 랜덤으로 정해진다.
#좀 더 직관적으로 만들수 있다.
def random_pop(data):
	number = random.choice(data)
	data.remove(number)
	return number
#random.choice는 입력받은 리스트에서 무작위로 하나를 선택하여 리턴하는 함수이다.
#리스트 항목을 무작위로 섞고싶은 경우, random.shuffle를 이용한다.
import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)

#파이썬에서의 쓰레드(threading)
#프로세스 : 동작하고 있는 프로그램. 보통 한개의 프로세스는 한가지의 일을 한다.
#스레드를 이용하면 한 프로세스에서 두가지 또는 그 이상의 일을 동시에 할 수 있게 된다.
import threading
import time

def say(msg):
	while True:
		time.sleep(1)
		print(msg)
#['you', 'need' 'python']의 리스트 길이만큼 스레드가 생성되고, 생성된 스레드는 say메서드를 수행하고, 1초에 한번씩 입력받은 msg값을 출력한다. say의 args로 msg가 들어간다.
for msg in ['you', 'need' 'python']:
	t = threading.Thread(target=say, args=(msg,))
	t.daemon = True
	t.start()
#0.1초마다 0부터 99까지 숫자를 출력한다. 이부분이 메인프로그램이 되며 메인 프로그램이 종료되는 순간 생성된 스레드들도 함께 종료된다.
#t.deamon = True와 같이 daemon 플래그를 설정해주면 주 프로그램이 종료되는 순간 데몬 스레드가 함께 종료된다.
for i in range(100):
	time.sleep(0.1)
	print(i)
#이러한 쓰레드 프로그래밍을 가능하게 해주는 것이 바로 threading.Thread 클래스로 첫 번째 인수로는 함수명을, 두 번째 인수로는 그 함수의 입력 변수로 들어갈 튜플 형태의 입력 인수를 받는다.
#다음과 같이 스레드를 클래스로 정의해도 동일한 결과를 얻을 수 있다.
import threading
import time

class MyThread(threading.Thread):
	def __init__(self, msg):
		threading.Thread.__init__(self)
		self.mas = msg
		self.daemon = True
	def run(self):
		while True:
			time.sleep(1)
			print(self.msg)
for msg in ['you', 'need', 'python']:
	t = MyThread(msg)
	t.start()
for i in range(100):
	time.sleep(0.1)
	print(i)
#스레드를 클래스로 정의할 경우에는 __init__ 메서드에서 threading.Thread.__init__(self)과 같이 부모 클래스의 생성자를 반드시 호출해야 한다.
#MyThread로 생성된 객체의 start메서드 실행 시 MyThread 클래스의 run메서드가 자동으로 수행된다.

#웹브라우저 실행시키기(webbrowser)
import webbrowser
webbrowser.open('http://google.com')
webbrowser.open_new('http://google.com') #새 창으로 연다.
