import cv2
import pyautogui
import time
import keyboard
keyboard.wait("=")
shipinshili = cv2.VideoCapture("1.mp4")

pyautogui.screenshot("zhuomian.jpg")
imgsr=cv2.imread("zhuomian.jpg")
imgtm=cv2.imread("sc.jpg")
#与模版比对
res=cv2.matchTemplate(imgsr,imgtm,cv2.TM_CCOEFF_NORMED)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
x,y=max_loc

print(x)
print(y)
vx=int(shipinshili.get(3))
vy=int(shipinshili.get(4))

while vy>=257:
    vy=int(vy/2)
    vx=int(vx/2)
pyautogui.moveTo(x+767-660,y+498-146)
pyautogui.click()
pyautogui.hotkey("ctrl","a")
pyautogui.typewrite(message=str(vx))

pyautogui.moveTo(x+764-660,y+526-146)
pyautogui.click()
pyautogui.hotkey("ctrl","a")
pyautogui.typewrite(message=str(vy))

time.sleep(1)
pyautogui.screenshot("zhuomian2.jpg")
imgsr2=cv2.imread("zhuomian2.jpg")
imgtm2=cv2.imread("sc2.jpg")
#与模版比对
res2=cv2.matchTemplate(imgsr2,imgtm2,cv2.TM_CCOEFF_NORMED)
a,b,c,max_loc2 = cv2.minMaxLoc(res2)
x2,y2=max_loc2

times10=1
while times10<=3533: 
    print(x2,"       ",y2)
    pyautogui.moveTo(x2,y2)
    time.sleep(1)
    pyautogui.moveTo(x+189-137,y+137-84)
    keyboard.wait("=")

    time.sleep(0.5)
    pyautogui.moveTo(x+189-137,y+137-84)
    pyautogui.click()
    pyautogui.typewrite(message=str(times10)+".jpg")
    pyautogui.press("\n")

    time.sleep(0.5)
    pyautogui.moveTo(x+962-660,y+565-146)
    pyautogui.click()

    time.sleep(0.5)
    pyautogui.moveTo(x2+590-119,y2+496-140)
    pyautogui.click()

    time.sleep(0.5)
    pyautogui.typewrite(message="sangeheshang"+str(times10))
    pyautogui.press("\n")

    time.sleep(0.5)
    pyautogui.moveTo(x2+882-122,y2+110-82)
    pyautogui.click()
    
    times10=times10+1
