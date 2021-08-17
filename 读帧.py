#coding=utf-8
import os
import cv2
import time
ShiPinZhenLv=int(input("隔多少帧储存一次："))
shipin=cv2.VideoCapture(input("视频名称?"))
times=0
times2=0
outPutDirName=os.path.normpath("images")
while True:
    times+=1
    res, image = shipin.read()
    if not res:
        print('没帧了，没图了，弄完了')
        break
    if times%ShiPinZhenLv==0:
        times2=times2+1
        times2/ShiPinZhenLv
        a=cv2.imwrite(outPutDirName+os.path.normpath("/") + str(times2)+'.jpg', image)
        print(a)
        print(outPutDirName + str(times2)+'.jpg')
        print()
        print(times2)
        
        
        
time.sleep(5)
print('图片提取结束')
time.sleep(5)
shipin.release()
