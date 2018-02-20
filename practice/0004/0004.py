import sys,re


'''统计单词总数及每个单词出现的个数'''

#the total number of words in the file
def count(str):	
	l=re.split('[\n| |\[|\]:|/|\-|.|,|=|\+|(|)|\'|#|%|\\\|>|<]+',str)
	# print(l)
	return len(l),l

#the number of single word
def count_cl(str):
	dict={}
	for s in str:
		if s in dict:
			dict[s]+=1
		else:
			dict[s]=1
	
	n=0
	for key in dict:
		n = n + dict[key]
	return dict,n
	
# def dict_key_value2list(dict):
	# list_key=[]
	# list_value=[]
	# for key in dict:
		# list_key.append(key)
		# list_value.append(dict[key])
	# return list_key, list_value

def sortdict(dict,*,methed):
#	try:
		list=dict.items()
		if methed=='letter':
			list_key=sorted(list,key=lambda list : list[0])
#			print(list_key)
			return list_key
		elif methed=='num':
			list_value=sorted(list, key=lambda list : list[1],reverse=True)
#			print(list_value)
			return list_value
	# except IndexError as e:
		# print('Please input the third argument, which means the way to sort the result("letter" or "num") \nIndexError:',e)
	# except ValueError as e:
		# print('Please input a right argument(letter or num)\nValueError:',e)
		
if __name__=='__main__':
	with open (sys.argv[1],'r',encoding='utf-8',errors='ignore') as f:
		txt = f.read()
		num, str= count(txt)
		print('the number of words of "%s" is %d.'%(sys.argv[1],num))
		dict,t_num=count_cl(str)
		print('the number of words of "%s" is %d(with other methed).'%(sys.argv[1],t_num))
		try:	
			list=sortdict(dict,methed=sys.argv[2])
		except IndexError as e:
			print('Please input the third argument, which means the way to sort the result("letter" or "num") \nIndexError:',e)	
		try:
			#pass
			for i in list:
				print('%s : %s\n'%i)
		except TypeError as e:
			print('Please input a right argument(letter or num)\nValueError:',e)