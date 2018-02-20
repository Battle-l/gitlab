import random,mysql.connector


#生成八位随机字符串
def code():
	char_random=''
	#生成字符库
	lib_list=[str(x) for x in range(10)]+[chr(x) for x in range(65,91)]+[chr(x) for x in range(97,123)]   
	
	while True:
		num_random=int(random.random()*100)
		if num_random<62:
			char_random+=lib_list[num_random]
		if len(char_random)==8:
			break
	return char_random

coupon=[]

#生成200个字符串并放入list中
for i in range(200):
	coupon.append(code())
	
#将生成的字符串放入code.txt文件中
with open('code.txt','w') as f:
		for s in coupon:
			f.write(s)
			f.write('\n')

#打开数据库'coupon'并将字符串插入		
conn = mysql.connector.connect(user='root',password='turnon',database='coupon')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS `code` (`code_id` INT UNSIGNED AUTO_INCREMENT, `code_data` CHAR(20) NOT NULL, PRIMARY KEY (`code_id`))')
for str in coupon:
	cursor.execute('INSERT INTO `code` (`code_data`) VALUES (%s)',[str])
conn.commit()
conn.close()