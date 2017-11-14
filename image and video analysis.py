'''  
	 *CODE CREATOR:MAHADEV SHARMA

  	 *CODE CREATED AT: CONESTOGA COLLEGE
	
	 *CODE DESCRPTION:CONVERT VIDEO INTO BLACK
                            AND WHITE AND SAVES ACCORDING TO SIZE

  	 *CODER:da_dvinci
'''
import cv2
import numpy as np

#selecting the video souce
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#setting up the frame size
out = cv2.VideoWriter('output.avi', fourcc,20.0,(640,480))


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow(' frame ', frame)
    cv2.imshow(' gray ', frame)  
    

    if cv2.waitKey(1)& 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()
