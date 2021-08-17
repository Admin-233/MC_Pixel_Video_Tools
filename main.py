#coding=utf-8
import os
try:
	os.system("cls")
	os.system("clear")
except:pass

print("*----------------------------*")
print("    欢迎使用MC像素视频工具包")
print("*----------------------------*")
print("")
print("*----------主要工具-----------*")
print("         1.读帧.py")
print("         2.转换.py")
print("         3.录入.py")
print("*----------主要工具-----------*")
print("")
print("*----------其他脚本-----------*")
print("         4.像素画.py")
print("        5.像素视频.py")
print("    6.转换wasted.py(不稳定)")
print("      7.test.py(不可用)")
print("*----------其他脚本-----------*")
print("")
print(" 有大佬的话可以帮我改进一下脚本QwQ")
print("")

number=str(input("输入数字以运行脚本:"))

try:
	number=int(number)
except ValueError or NameError:
	print("请输入有效的数字")

if number>7 or number<1:
	print("请输入1-7内的数字")

if number==1:
	exec("import 读帧")
elif number==2:
	exec("import 转换")
elif number==3:
	exec("import 录入")
elif number==4:
	exec("import 像素画")
elif number==5:
	exec("import 像素视频")
elif number==6:
	exec("import 转换wasted")
elif number==7:
	exec("import test")
