# [실습 9] Whule loop를 이용하여 IMU Data 취합하기

import socket, traceback
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from time import sleep
import pandas as pd

# ip address 알아내기
# Windows - command prompt 창에서 ipconfig
# Max - command prompt 창에서 ifconfig |grep inet
host = '192.168.0.11'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

imuData = np.empty((0,11), float)

intCnt = 0    
MAX_COUNT = 50

while 1:
    try:
        message, address = s.recvfrom(8192)
        strData = message.decode("utf-8")    # convert a byte type to a string
        strData = strData.split(',')         # convert a string to a list
        
        print (strData)
        
        curTime = dt.datetime.now()
#        curTime2 = dt.datetime.now()
        
#        delTime = (curTime1 - curTime2).microseconds / 1000
        
#        print(curTime)
        
        if len(strData) == 13:
            intCnt += 1
            
            if intCnt == 1:
                strTime = curTime
                
#            delTime = (curTime - strTime).microseconds / 1000
            
            imuData = np.append(imuData, \
                      np.array([[intCnt, intCnt, \
                                 float(strData[2]), float(strData[3]), float(strData[4]), \
                                 float(strData[6]), float(strData[7]), float(strData[8]), \
                                 float(strData[10]),float(strData[11]),float(strData[12])]]), axis=0)
            
            
            if intCnt > MAX_COUNT:
                break
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc() 
        
#print(imuData)   

imuIdx = imuData[:,0]
imuT = imuData[:,1]

accX = imuData[:,2]
accY = imuData[:,3]
accZ = imuData[:,4]

plt.figure(1, figsize = (10, 5))
plt.plot(imuIdx, accX, color='b', linestyle='-', marker='o', markersize=10)
plt.legend(loc=0)
plt.grid(True, color='0.7', linestyle=':', linewidth=1)
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Stock Price')
plt.show()
#

