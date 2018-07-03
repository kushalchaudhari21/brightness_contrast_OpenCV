import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# defining the required alpha and beta values.
alpha = 1.33
beta = -50

while True:
    _, frame = cap.read()
    # result gives the adjusted output according to the alpha and beta values
    result = cv2.addWeighted(frame,alpha,np.zeros(frame.shape,frame.dtype),0,beta)
    cv2.imshow("result", result)
    
    cv2.imshow('original frame',frame)
    #cv2.imshow('res',res)

    k=cv2.waitKey(5) & 0xFF
    if k == 27:
            break

cv2.destroyAllWindows()
cap.release()
