#-*- coding: utf-8 -*-
import random


def verify_input(num):
	for i in num:
		if not i.isdigit():
			return False
	return True

def PlayMore():

	s = raw_input(u'继续玩？Y：N: ')

	if s == 'Y'or s == 'y':
		return True
	else:
		return False


def guess(num):

	
	times = 0 
	print u'********************\n开始猜：'

	while True:

		if times == 4:
			print u'你已经猜错4次了~ 正确答案应该是:',num
			return PlayMore() 

		Input = raw_input() #输入猜的数字
		

		if verify_input(Input):

			times += 1
			Input = int(Input) 
			if Input == num: 

				print u'Bingo！猜对了！'
				return PlayMore() 

			elif Input > num:

				print u'大了，请继续猜:'

			else:
				print u'小了，请继续猜：'

		else:
			print u'只允许输入数字！请重新输入:'
			continue
	

def main():

	while True:
		num = random.randint(0,100) 
		print num 
		if guess(num):
			continue
		else:
			print 'ByeBye'
			break

if __name__ == '__main__':
	main()