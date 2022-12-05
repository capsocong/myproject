import cv2
import sqlite3
import os
cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#insert or update vào sqlite
def insertOrupdate(id,name,age,gender):
    conn = sqlite3.connect("C:\Al\\facebase1.db")
    querry = 'Select * from people where ID = '+str(id)
    cursor = conn.execute(querry)
    isRecordexist = 0
    for row in cursor:
        isRecordexist = 1
    if(isRecordexist == 0):
        querry = "Insert into people(ID,Name,Age,Gender) values("+str(id)+",'"+str(name)+"','"+str(age)+"','"+str(gender)+"')"
    else :
        querry = "Update people set name = '"+str(name)+"', Age= '"+str(age)+"', Gender = '"+str(gender)+"' Where ID = "+str(id)
    conn.execute(querry)
    conn.commit()
    conn.close()

#insert vao db
id = input("Enter your ID: ")  
name = input("Enter your Name: ") 
age = input("Enter your Age: ") 
gender = input("Enter your gender: ")
insertOrupdate(id,name,age,gender)
#áddas

sampleNum = 0
while True:
    #camera read
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor= 1.3,
        minNeighbors= 5,
        minSize=(30, 30)
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        sampleNum += 1
        cv2.imwrite('dataset/User.'+id+'.'+str(sampleNum)+ '.jpg', gray[y:y+h,x:x+h])    
        cv2.imshow('Cap',img)
    # lưu ảnh vào file dữ liệu
    if not os.path.exists('dataset'):
        os.makedirs('dataset')
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    elif sampleNum>100:
        break
cap.release()
cv2.destroyAllWindows()