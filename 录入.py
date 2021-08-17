from pyautogui import click as c
from pyautogui import position as pos
from pyautogui import moveTo as m
from pyautogui import press as p
from pyautogui import typewrite as w
import keyboard,time
schemname=str(input("工程名字？"))
number=int(input("文件个数？"))
print("鼠标移到停止录制处，按等于号录入坐标")
keyboard.wait("=")
stoppos=pos()
print("按等于键开始")
keyboard.wait("=")
for i in range(number):
	time.sleep(0.5)
	p("/")
	time.sleep(0.1)
	w(message="/schem load "+schemname+str(i+1))
	time.sleep(0.1)
	p("\n")

	time.sleep(0.5)
	p("/")
	time.sleep(0.1)
	w(message="/paste")
	time.sleep(0.1)
	p("\n")
p("esc")
time.sleep(0.5)
m(stoppos)
time.sleep(0.5)
c()
print("finish")
