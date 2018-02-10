import random


#生成八位随机字符串#
def code():
	char_random=''
	lib_list=[str(x) for x in range(10)]+[chr(x) for x in range(65,91)]+[chr(x) for x in range(97,123)]   #生成库列表#
	
	while True:
		num_random=int(random.random()*100)
		if num_random<62:
			char_random+=lib_list[num_random]
		if len(char_random)==8:
			break
	return char_random

with open('code.txt','w') as f:
	for i in range(200):
		f.write(code())
		f.write('\n')
	
# if __name__=='__main__':
	# a=code()
	# print (a)