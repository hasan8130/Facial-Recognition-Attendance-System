import cv2, numpy as np;
from firebase import firebase
import xlwrite;
import time
import sys
from playsound import playsound
start=time.time()
period=8

face_cas = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW);
recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('attendance/trainer.yml');
flag = 0;
id=0;
filename='filename';
dict = {
            'item1': 1
}

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, 1.3, 7)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2);
        roi_color = img[y:y+h, x:x+w]
        
        
        id,conf=recognizer.predict(roi_gray)
        
        
        if(conf < 50):
         if(id==1):
            id='Hasan'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',1,id,'yes');
                dict[str(id)]=str(id);
                
         elif(id==2):
            id = 'Aaryak'
            if ((str(id)) not in dict):
                filename =xlwrite.output('attendance', 'class1', 2, id, 'yes');
                dict[str(id)] = str(id);

         elif(id==3):
            id = 'Yash'
            if ((str(id)) not in dict):
                filename =xlwrite.output('attendance', 'class1', 3, id, 'yes');
                dict[str(id)] = str(id);

         elif(id==4):
            id = 'Vaibhav'
            if ((str(id)) not in dict):
                filename =xlwrite.output('attendance', 'class1', 4, id, 'yes');
                dict[str(id)] = str(id);
         elif(id==5):
            id = 'Gaurav'
            if ((str(id)) not in dict):
                filename =xlwrite.output('attendance', 'class1', 5, id, 'yes');
                dict[str(id)] = str(id);

        else:
             id = 'Unknown, can not recognize'
             flag=flag+1
             break
        
        cv2.putText(img,str(id)+" "+str(conf+48),(x,y-10),font,0.55,(255,0,0),1)
        
    cv2.imshow('frame',img);
    #cv2.imshow('gray',gray);
    if flag == 10:
        print("Transaction Blocked")
        break;
    if time.time()>start+period:
        break;
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;

cap.release();
cv2.destroyAllWindows();
