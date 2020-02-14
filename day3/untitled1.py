# -*- coding: utf-8 -*-
#video cam test
import cv2

cap = cv2.VideoCapture(0) #첫번째 카메라

#cap = cv2.VideoCapture(http://192.     /) #ip webcam

if cap.isOpened():                      # 캡쳐 객체 연결 확인
    while True:
        ret, img = cap.read()           # 다음 프레임 읽기
        if ret:
            cv2.imshow('camera', img)   # 다음 프레임 이미지 표시
            if cv2.waitKey(1) != -1:    # 1ms 동안 키 입력 대기
                break                   # 아무 키라도 입력이 있으면 중지
        else:
            print('no frame')
            break
else:
    print("can't open camera.")
cap.release()                           # 자원 반납
cv2.destroyAllWindows()
# 노트북이 리소스를 반납하지 않는 오류가 난다면 IPython console에서 
# 마지막 2줄 code 실행해줘야 카메라 리소스 반납