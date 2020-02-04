# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 18:10:18 2018

@author: xin.men
"""

import cv2
import numpy as np
# =============================================================================
# 
# frame = np.zeros((800,800,3),np.uint8)
# last_mes = current_mes = np.array((2,1),np.float32)
# last_pre = current_pre = np.array((2,1),np.float32)
# 
# def mousemove(event, x,y,s,p):
#     global frame, current_mes, mes, last_mes, current_pre, last_pre
#     last_pre = current_pre
#     last_mes = current_mes
#     current_mes = np.array([[np.float32(x)],[np.float32(y)]])
#     current_pre = kalman.predict()
#     kalman.correct(current_mes)
#     print(current_pre)
# 
#     lmx, lmy = last_mes[0],last_mes[1]
#     lpx, lpy = last_pre[0],last_pre[1]
#     cmx, cmy = current_mes[0],current_mes[1]    
#     cpx, cpy = current_pre[0],current_pre[1]    
#     #cv2.line(frame, (lmx,lmy),(cmx,cmy),(0,200,0))
#     #cv2.line(frame, (lpx,lpy),(cpx,cpy),(0,0,200))
# =============================================================================
def get_kalman():
    k = cv2.KalmanFilter(4,2)
    k.measurementMatrix = np.array([[1,0,0,0],[0,1,0,0]],np.float32)
    k.transitionMatrix = np.array([[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]], np.float32)
    k.processNoiseCov = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], np.float32) * 0.003
    k.measurementNoiseCov = np.array([[1,0],[0,1]], np.float32) * 0.00001
    return k

#cv2.namedWindow("Kalman")
#cv2.setMouseCallback("Kalman", mousemove)
kalman = get_kalman()
kk = get_kalman()
print(kalman)
print(kk)
cnt = 0
while(True):
    #cv2.imshow('Kalman',frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
    cnt += 1
    print(np.array([[cnt],[cnt]],np.float32))
    kalman.correct(np.array([[cnt],[cnt]],np.float32))
    kalman.correct(np.array([[cnt],[cnt]],np.float32))
    kalman.correct(np.array([[cnt],[cnt]],np.float32))
    kalman.correct(np.array([[cnt],[cnt]],np.float32))
    print("------------------------")
    print(kalman.predict())
    print("########################")
    print(kalman.transitionMatrix)
    if cnt >= 5 :
        break
#cv2.destroyAllWindows()