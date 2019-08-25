import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	img = cap.read()[1]

	imggray = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
	lower=np.array([35,30,5])
	upper=np.array([70,255,250])
	mask = cv2.inRange(imggray, lower, upper)
	contours, hierarchy =cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	C=max(contours, key=cv2.contourArea)
    
	x, y, w, h = cv2.boundingRect(C)#計算邊界框座標
	cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)
    
	rect = cv2.minAreaRect(C)#計算包圍目標的最小矩形區域
	box = cv2.boxPoints(rect) #計算最小矩形的座標
	box = np.int0(box) #座標變為整數
	cv2.drawContours(frame, [box], 0, (0,0,255),1)
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
