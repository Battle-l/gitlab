from tkinter import *
from tkinter import ttk
import tkinter.filedialog as dir
import statistics as st

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
		about_menu.add_command(label="v0.01")
		
		menu.add_cascade(label="文件",menu=quit_menu)
		menu.add_cascade(label="关于",menu=about_menu)
		root['menu']=menu


	def create_content(self,root):
		lf=ttk.LabelFrame(root,text="代码行数统计")
		lf.pack(fill=X,padx=15,pady=8)		
		
		top_frame=Frame(lf)
		top_frame.pack(fill=X,expand=YES,side=TOP,padx=15,pady=8)
		
		self.static_key=StringVar()
		ttk.Entry(top_frame, textvariable=self.static_key,width=50).pack(fill=X,expand=YES,side=LEFT)
		ttk.Button(top_frame,text='开始',command=self.static_file).pack(padx=15,fill=X,expand=YES)
		self.static_key.set('请输入')
		
		bottom_frame=Frame(lf)
		bottom_frame.pack(fill=BOTH,expand=YES,side=TOP,padx=15,pady=8)
		
		band=Frame(bottom_frame)
		band.pack(fill=BOTH,expand=YES,side=TOP)
		
		self.list_val=StringVar()
		listbox=Listbox(band,listvariable=self.list_val,height=18)
		listbox.pack(side=LEFT,fill=X,expand=YES)
		
		vertical_bar = ttk.Scrollbar(band,orient=VERTICAL,command=listbox.yview)
		vertical_bar.pack(side=RIGHT,fill=Y)
		listbox['yscrollcommand'] = vertical_bar.set
		
		
	def static_file(self):
		'''
		每次点击都先把路径输出到下面的框中，最后再输出一个结果
		还有把清除选项做上去
		'''
		path.append(self.static_key.get()+'\n'+st.op(self.static_key.get()))
		self.list_val.set(path)


if __name__ == "__main__":
	path=[]	
	AppUI()
#print(st.op('D:\\PyCharm\\gitlab\\practice\\'))