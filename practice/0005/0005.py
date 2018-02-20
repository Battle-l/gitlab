import os, re, sys

'''
第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
1	一个主目录，遍历从中找到.py文件
		a.	是文件的话判断是否为.py文件，是则将绝对路径添加到列表中，否则忽略
		b.	是文件夹的话，将目录添加上去，继续遍历
2	依次统计各个文件的行数，并将其中的空行和注释分别统计
		a.	不在字符串中的'#'和有\'\'\'的行是注释
		b.	有\n的行是空行
'''

#遍历目录
def traversal(directory):
	
	fdpath=os.listdir(os.path.dirname(directory))
	for i in fdpath:
		fdpath=os.path.join(directory,i)
		
		if os.path.isdir(fdpath):
			traversal(fdpath+'\\')
		else:
			if re.search('\.py$',i):
				#print(fdpath)
				filelists.append(fdpath)
	#print (filelists)
	#返回python源码文件列表（含绝对路径）
	return filelists						

#统计文件、注释及空行数	
def file_lines(filelists):
	n=0
	nl=[]
	note = 0
	blank = 0
	flines = 0
	for i in filelists:
		with open(i,'r',encoding='utf-8',errors='ignore') as f:
			lineoffiles=f.readlines()
			flines += len(lineoffiles)
			for l in lineoffiles:
				n+=1
				#统计注释行数
				if ((re.search('(\'.*?#.*?\')|(".*?#.*?")',l)==None) and re.search('#',l)) or re.search('\'\'\'\S+',l):
					#print(l)
					note+=1
					
				if re.search('^\'\'\'\s*$',l):
					nl.append(n)
					
				#统计空行行数
				if re.search('^\s+$',l):
					blank+=1

	for k,v in enumerate(nl):
		if k%2==0:
			note-=v
			note+=1
		else:
			note+=v
	return note,blank,flines
	
if __name__ == '__main__':
	filelists=[]	
	note,blank,flines=file_lines(traversal(sys.argv[1]))
	print('在这个练习目录中，我一共写了%d行代码，其中有%d行注释，%d行空行。'%(flines,note,blank))