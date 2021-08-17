from pyautogui import position,moveTo,click,typewrite,press
import time
from keyboard import wait
import os

name=input("工程名字？")

totimes=int(input("共有多少张图片？"))

print("鼠标指向按钮,按等于号录入browse位置")
wait("=")
browse=position()
print("录入完成")

print("鼠标指向按钮,按等于号录入Create Minecraft Blueprint位置")
wait("=")
CMB=position()
print("录入完成")

print("鼠标指向按钮,按等于号录入Save Schematic位置")
wait("=")
SaveSchem=position()
print("录入完成")

print("鼠标指向按钮,按等于号录入关闭第二个窗口的位置")
wait("=")
Close=position()
print("录入完成")

print("按等于号开始")

wait("=")
times=1
while times<=totimes:
    time.sleep(0.4)
    moveTo(browse)
    click()
    time.sleep(0.5)
    typewrite(str(times)+".jpg")
    press("\n")
    print(str(times)+".jpg")
    
    time.sleep(0.4)
    moveTo(CMB)
    click()
    
    time.sleep(0.5)
    moveTo(SaveSchem)
    time.sleep(0.5)
    click()
    
    time.sleep(0.5)
    typewrite(message=name+str(times),interval=0.1)
    press("\n")
    
    time.sleep(0.5)
    moveTo(Close)
    click()
    
    times+=1
    

    


print("完成")
time.sleep(5)
exit(0)
