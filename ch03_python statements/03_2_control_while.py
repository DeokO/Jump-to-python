#조건문_while문
treeHit=0
while treeHit<10:
	treeHit = treeHit+1
	print("나무를 %d번 찍었습니다." %treeHit)
	if treeHit==10:
		print("나무 넘어갑니다.")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """
number=0
while number != 4:
	print(prompt)
	number = int(input())

coffee = 10
money = 300
while money:
	print("돈을 받았으니 커피를 줍니다.")
	coffee = coffee-1
	print("남은 커피의 양은 %d 입니다." %coffee)
	if not coffee:
		print("커피가 다 떨어졌습니다.")
		break


coffee = 10
while True:
    money = int(input(u"돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
		
#while 맨처음으로 돌아가기
a = 0
while a<10:
	a = a+1
	if a%2 == 0: continue #continue때문에 while의 조건식으로 돌아가고 a+1이 된다.
	print(a)
