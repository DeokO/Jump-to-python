#날개달기_패키지
#패키지는 도트를 이용하여 모듈을 계층적으로 관리할 수 있게 해준다.
#A.B의 경우 A는 패키지명, B는 A패키지의 B모듈이 된다.

#패키지는 디렉토리와 모듈로 이루어진다.
#game이라는 패키지의 예
#game/					#루트 디렉토리
#	__init__.py
#	sound/				#서브 디렉토리1
#		__init__.py
#		echo.py
#		wav.py
#	graphic/			#서브 디렉토리2
#		__init__.py
#		screen.py
#		render.py
#	play/				#서브 디렉토리3
#		__init__.py
#		run.py
#		test.py

#game이라는 폴더를 만들고
#그 안에 __init__.py를 빈 파일로 만든다.

#echo를 import
import game.sound.echo
game.sound.echo.echo_test()
#실행후엔 껐다켜자.

#2번째 방법
from game.sound.echo import echo_test
echo_test()

#이렇게 하는것은 불가능하다.
import game
game.sound.echo.echo_test()
#import game을 하면 game 디렉토리의 모듈 또는 game디렉토리의 __init__.py에 정의된 것들만 참조가능하다.

#이것도 불가능하다.
import game.sound.echo.echo_test
#. 뒤에 제일 마지막에 나오는 것은 패키지여야 한다. 이럴경우엔 from A import B를 이용한다.

###__init__.py의 용도
#해당 디렉토리가 패키지의 일부임을 알려주는 역할을 한다.
#만약 위 game내의 어떤 폴더이든 __init__.py가 없다면 
#import game.sound.echo가 돌아가지 않는다.
#3.3버전부터는 __init__.py없어도 되지만, 하위 버젼 호환을 위해 생성하는 것이 안전하다.

###__all__의 용도
from game.sound import *
echo.echo_test()
#오류가 난다...*을 사용하려면 __init__.py내부에 __all__이라는 변수를 설정하고 import 가능한 모듈을 정의해줘야 한다.
#sound의 __init__.py를 이렇게 바꾸자.
__all__ = ['echo']
#from a.b.c import * 에서 from의 마지막 항목인 c가 모듈인 경우에는 import가 된다.
#위의 안되는 예시에는 a.b에서 b가 패키지이기 때문에 안된다.

###relative 패키지
#graphic 디렉토리의 render.py모듈이 sound 디렉토리의 echo.py를 사용하고 싶다면?
#render.py를 이렇게 수정하자.
from game.sound.echo import echo_test #render 내부에서 애초에 echo를 import 한다.

def render_test():
	print("render")
	echo_test()

#실행해보자.
from game.graphic.render import render_test
render_test()

#조금 다르게 할수도 있다. render.py를 이렇게 수정하자.
from ..sound.echo import echo_test #game 디렉토리는 sound와 graphic이 동시에 부모로 갖는 디렉토리다. '.'으로 생략가능하다.

def render_test():
	print("render")
	echo_test()







