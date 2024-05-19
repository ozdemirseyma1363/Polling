import face_recognition
import cv2
import dlib
import smtplib
content1="seyma okula geldi"
mail=smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.ehlo()
mail.login("buse68454@gmail.com","Sevgimuhlis123")
detector=dlib.get_frontal_face_detector()
ben=face_recognition.load_image_file("49.PNG")
ben1=face_recognition.face_encodings(ben)[0]
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    face_log=[]
    faces=detector(frame)
    for face in faces:
        x=face.left()
        y=face.top()
        w=face.right()
        h=face.bottom()
        face_log.append((y,w,h,x))
    face2=face_recognition.face_encodings(frame,face_log)
    i=0
    for face in face2:
        y,w,h,x=face_log[i]
        sonuc=face_recognition.compare_faces([ben1],face)
        mail.sendmail("buse68454@gmail.com", "ozdemirseyma335@gmail.com", content1)
        if sonuc[0]==True:
            cv2.rectangle(frame,(x,y),(w,h),(255.255,255),2)
            cv2.putText(frame,"SEYMA",(x,h), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 3)
    cv2.imshow('Video', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
mail.close()
cv2.destroyAllWindows()
