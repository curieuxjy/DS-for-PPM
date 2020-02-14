# -*- coding: utf-8 -*-


import cv2

cap = cv2.VideoCapture(0)    # 0번 카메라 연결
if cap.isOpened:
    file_path = './record.avi'    # 저장할 파일 경로 이름
    fps = 30.0                     # FPS, 초당 프레임 수
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 인코딩 포맷 문자
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #속성값을 가져올 때 get, set은 값을 정의할때
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))                        # 프레임 크기
    out = cv2.VideoWriter(file_path, fourcc, fps, size) # VideoWriter 객체 생성
    while True:
        ret, frame = cap.read() #스냅샷 찍음
        if ret:
            cv2.imshow('camera-recording',frame)
            out.write(frame)  # 프레임이 많을 수록 슬로우 모션임    # 파일 저장
            if cv2.waitKey(int(1000/fps)) != -1: 
                break
        else:
            print("no frame!")
            break
    out.release()                                   # 파일 닫기
else:
    print("can't open camera!")
cap.release()
cv2.destroyAllWindows()