from tkinter import *
from tkinter import ttk
import tkinter.filedialog as dir

import statistics as st

import re

'''
一个输入框，一个按钮，一个选项
输入绝对路径
点击开始统计查询
选择是否累加/清零

一个输出框，或者弹窗？
'''

class AppUI():

	def __init__(self):
		root = Tk()
		self.create_menu(root)
		self.create_content(root)
		root.title("代码工作量统计工具")
		root.update()
		curWidth=root.winfo_width()
		curHeight=root.winfo_height()
		scnWidth, scnHeight=root.maxsize()
		tmpcnf='+%d+%d'%((scnWidth-curWidth)/2,(scnHeight-curHeight)/2)
		root.mainloop()
		
	
	def create_menu(self,root):
		menu=Menu(root)		
		
		quit_menu=Menu(menu, tearoff=0)
		quit_menu.add_command(label="退出",command=root.quit)
				
		about_menu=Menu(menu, tearoff=0)
		about_menu.add_command(label="v0.04")
		
		menu.add_cascade(label="文件",menu=quit_menu)
		menu.add_cascade(label="关于",menu=about_menu)
		root['menu']=menu


	def create_content(self,root):
		lf=ttk.LabelFrame(root,text="代码行数统计")
		lf.pack(fill=X,padx=15,pady=8)		
		
		top_frame=Frame(lf)
		top_frame.pack(fill=X,expand=YES,side=TOP,padx=15,pady=8)
		
		left_frame=Frame(top_frame)
		left_frame.pack(fill=X,expand=YES,side=TOP,padx=15,pady=8)
		
		label_text=Label(left_frame,text='路径:')
		label_text.pack(side=LEFT)
		self.static_key=StringVar()
		ttk.Entry(left_frame,textvariable=self.static_key,width=50).pack(fill=X,expand=YES,side=LEFT)
		ttk.Button(left_frame,text='开始',command=self.static_file).pack(padx=15,fill=X,expand=YES)

		
		right_frame=Frame(top_frame)
		right_frame.pack(side=TOP,fill=X,expand=YES,padx=15,pady=8)
		
		self.var=IntVar()
		self.var.set(0)
		R1=Radiobutton(right_frame, text='统计所有输入目录',variable=self.var,value=0)
		R2=Radiobutton(right_frame, text='只统计单个目录',variable=self.var,value=1)
		R1.pack(side=RIGHT,padx=15,fill=X,expand=YES)
		R2.pack(side=RIGHT,padx=15,fill=X,expand=YES)
		
		bottom_frame=Frame(lf)
		bottom_frame.pack(fill=BOTH,expand=YES,side=TOP,padx=15,pady=8)
		
		band=Frame(bottom_frame)
		band.pack(fill=BOTH,expand=YES,side=TOP)
		
		self.list_val=StringVar()
		self.list_val2=StringVar()
		
		listbox2=Listbox(band,listvariable=self.list_val2,height=1)
		listbox2.pack(side=TOP,fill=X,expand=YES)
		
		listbox=Listbox(band,listvariable=self.list_val,height=17)
		listbox.pack(side=LEFT,fill=BOTH,expand=YES)
				
		vertical_bar = ttk.Scrollbar(band,orient=VERTICAL,command=listbox.yview)
		vertical_bar.pack(side=RIGHT,fill=Y)
		listbox['yscrollcommand'] = vertical_bar.set
		
			
	def static_file(self):
		global path
		path.add(self.static_key.get())
		if	self.var.get()==0:
			clear='no'
		elif self.var.get()==1:
			clear='yes'
			path=set()
		self.list_val2.set(st.op(self.static_key.get(),clear))
		path=list(path)
		path.sort()
		path=tuple(path)
		self.list_val.set(path)
		path=set(path)
		
	
	def clear_flie(self):
		static_file(self,'yes')


if __name__ == "__main__":
	path=set()	
	AppUI()
#print(st.op('D:\\PyCharm\\gitlab\\practice\\'))