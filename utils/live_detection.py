import cv2
import numpy as np

det=cv2.CascadeClassifier('haarcascade_eye.xml')
vid=cv2.VideoCapture(0)
while 1:
    _,frame=vid.read()
    frameg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    e=det.detectMultiScale(frameg,1.3,5)
    for ex,ey,xx,yy in e:
            crp=frame[ey:ey+yy,ex:ex+xx]
            crp=cv2.resize(crp,(112,112))
            crp=np.reshape(crp,(1,112,112,3))
            print(np.argmax(model.predict(crp)))
    if cv2.waitKey(1)==ord('q'):
            break
vid.release()
cv2.destroyAllWindows()
