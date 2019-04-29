import cv2
import numpy as np

cam_src = 'http://10.105.1.149:8080/video'
cap = cv2.VideoCapture(cam_src)

flag = True

while True:
  _, frame = cap.read()

  if flag:
    length = len(frame[0])
    width = len(frame)
    center_color = frame[ width//2 ][ length//2 ]
    print(center_color)
    flag = False
  
  cv2.rectangle(frame, (384, 0), (510,128),(0,255,0), 3)
  cv2.imshow("Frame", frame)

  key = cv2.waitKey(1)
  if key == 27:
    break

cap.release()
cv2.destroyAllWindows()
