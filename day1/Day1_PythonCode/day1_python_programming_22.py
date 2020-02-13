# [실습 9] Timer를 이용하여 IMU Data 취합하기
import socket
from threading import Timer
from time import sleep
#import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Timer 출처
# https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
        
def getCurrentIMUData():
    global imuData
    global intCnt
    
#    try:
    message, address = s.recvfrom(8192)
#    curTime = dt.datetime.now()
    
    strData = message.decode("utf-8")    # convert a byte type to a string
    strData = strData.split(',')         # convert a string to a list
            
    if len(strData) >= 13:
        imuData = np.append(imuData, \
                  np.array([[intCnt, intCnt, \
                             float(strData[2]), float(strData[3]), float(strData[4] ), \
                             float(strData[6]), float(strData[7]), float(strData[8] ), \
                             float(strData[10]),float(strData[11]),float(strData[12])]]), axis=0)
        intCnt += 1
    
#        print(imuData)
#    except (KeyboardInterrupt, SystemExit):
#        raise
#    except:
#        traceback.print_exc()
    
    return 

print('Starting...')

host = '192.168.0.11'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

intCnt = 0    
imuData = np.empty((0,11), float)
 
rt = RepeatedTimer(0.1, getCurrentIMUData)
try:
    sleep(20) 
finally:
    rt.stop()


imuIdx = imuData[:,0]
accX = imuData[:,2];    accY = imuData[:,3];    accZ = imuData[:,4]
gyrX = imuData[:,5];    gyrY = imuData[:,6];    gyrZ = imuData[:,7]
magX = imuData[:,8];    magY = imuData[:,9];    magZ = imuData[:,10]

fig1 = plt.figure(1, figsize = (10, 10))
#----------------------------------------------------------------------------------------
ax1 = fig1.add_subplot(2,2,1)
ax1.plot(imuIdx, accX, color='b', linestyle='-', marker='o', markersize=3, label='AccX')
ax1.plot(imuIdx, accY, color='r', linestyle='-', marker='o', markersize=3, label='AccY')
ax1.plot(imuIdx, accZ, color='m', linestyle='-', marker='o', markersize=3, label='AccZ')

ax1.legend(loc=0)
ax1.grid(True, color='0.7', linestyle=':', linewidth=1)
ax1.set_xlabel('Time')
ax1.set_ylabel('Acceleration (m/sec^2)')
ax1.set_title('Acceleration Data')
#----------------------------------------------------------------------------------------
ax2 = fig1.add_subplot(2,2,2)
ax2.plot(imuIdx, gyrX, color='b', linestyle='-', marker='o', markersize=3, label='GyroX')
ax2.plot(imuIdx, gyrY, color='r', linestyle='-', marker='o', markersize=3, label='GyroY')
ax2.plot(imuIdx, gyrZ, color='m', linestyle='-', marker='o', markersize=3, label='GyroZ')

ax2.legend(loc=0)
ax2.grid(True, color='0.7', linestyle=':', linewidth=1)
ax2.set_xlabel('Time')
ax2.set_ylabel('Angular Velocity (deg/seg)')
ax2.set_title('Gyro Data')
#----------------------------------------------------------------------------------------
ax3 = fig1.add_subplot(2,2,3)
ax3.plot(imuIdx, magX, color='b', linestyle='-', marker='o', markersize=3, label='MagX')
ax3.plot(imuIdx, magY, color='r', linestyle='-', marker='o', markersize=3, label='MagY')
ax3.plot(imuIdx, magZ, color='m', linestyle='-', marker='o', markersize=3, label='MagZ')

ax3.legend(loc=0)
ax3.grid(True, color='0.7', linestyle=':', linewidth=1)
ax3.set_xlabel('Time')
ax3.set_ylabel('Magnetic Field (μT)')
ax3.set_title('Magnetometer Data')
#----------------------------------------------------------------------------------------
fig1.show()




dfImuData = pd.DataFrame(imuData)
dfImuData.to_csv('IMU_Data_Period_0_1s.csv')  








#ax1.rcParams['font.family'] = 'NanumGothic'
#ax1.rcParams['font.size'] = 12
#ax1.rcParams['axes.unicode_minus'] = False

