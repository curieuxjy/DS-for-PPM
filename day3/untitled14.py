# -*- coding: utf-8 -*-
# Motion Difference
# video_cam.py
import cv2

cap = cv2.VideoCapture(0)               # 0번 카메라 장치 연결 

if cap.isOpened():                      # 캡쳐 객체 연결 확인
    while True:
        ret1, img1 = cap.read()
        grey_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        
        ret2, img2 = cap.read()
        grey_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        
#        diff = grey_img2 - grey_img1
        diff = cv2.bitwise_xor(grey_img1, grey_img2)
#        print(diff)              # 다음 프레임 읽기
        
        if ret2:
            cv2.imshow('camera', diff)   # 다음 프레임 이미지 표시
            if cv2.waitKey(1) != -1:    # 1ms 동안 키 입력 대기 
                break                   # 아무 키라도 입력이 있으면 중지
        else:
            print('no frame')
            break
else:
    print("can't open camera.")
cap.release()                           # 자원 반납
cv2.destroyAllWindows()