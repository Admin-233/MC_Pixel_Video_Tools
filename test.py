import cv2
import keyboard
import pyautogui
keyboard.wait("=")
pyautogui.screenshot("zhuomian.jpg")
imgsr=cv2.imread("zhuomian.jpg")
imgtm=cv2.imread("sc.jpg")
#与模版比对
res=cv2.matchTemplate(imgsr,imgtm,cv2.TM_CCOEFF_NORMED)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
x,y=max_loc
pyautogui.moveTo(x,y)
