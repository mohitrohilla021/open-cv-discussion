import cv2

capture = cv2.VideoCapture(0)

while (True):
    ret,frame=capture.read()
    # ret saves the true or false value and frame saves frame...
    cv2.imshow("frame", frame)
    if cv2.waitKey(0)==ord('q'):
        # 0xff is the mask for 64 bit machines...
        break
capture.release()
cv2.destroyAllWindows()
