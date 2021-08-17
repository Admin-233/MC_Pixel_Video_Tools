from tkinter import filedialog
import os
print("选择schematic存放的文件夹")
finder = filedialog.askdirectory()
name=str(input("工程名字？"))
amount=int(input("图片个数？"))
errorfile=[]
if os.name=="posix":
	for i in range(amount):
		if os.path.isfile(finder+"/"+name+str(i+1)+".schematic"):
			print(str(finder+name+str(i+1))+" is "+str(os.path.isfile(finder+"/"+name+str(i+1)+".schematic")))
		else:
			errorfile.append(str(name+str(i+1)+".schematic"))
elif os.name=="nt":
	for i in range(amount):
		if os.path.isfile(finder+"\\"+name+str(i+1)+".schematic"):
			print(str(finder+name+str(i+1))+" is "+str(os.path.isfile(finder+"\\"+name+str(i+1)+".schematic")))
		else:
			errorfile.append(str(name+str(i+1)+".schematic"))
else:print("未知的系统，检查失败")
print("")
for i in errorfile:
	print("错误:"+i+"不存在")
print("")
print("检查结束")
