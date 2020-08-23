#Run using Command prompt or shell, <python filename.py>
from cv2 import cv2 #pip install opencv-python
cam = cv2.VideoCapture(0) #WebCam

while True:
	ret,frame = cam.read()
	if ret==False: # Camera not open/  Camera busy
		print("Something Went Wrong!")
		continue # Retry
	cv2.imshow("frame",frame) #RGB FRAME
	gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
	cv2.imshow("gary frame",gray) #RGB FRAME

	key_pressed = cv2.waitKey(1)&0xFF #Bitmasking to get last 8 bits
	if key_pressed==ord('q'): #ord-->ASCII Value(8 bit)
		break


cam.release()
cv2.destroyAllWindows()	
