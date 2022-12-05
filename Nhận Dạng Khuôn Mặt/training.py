import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path='dataset'

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L');
        faceNp=np.array(faceImg,'uint8')
        #split to get ID of the image
        id=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print (id)
        IDs.append(id)
        cv2.imshow("traning",faceNp)
        cv2.waitKey(100)
    return IDs, faces

Ids,faces=getImagesAndLabels(path)
#trainning
recognizer.train(faces,np.array(Ids))
recognizer.save('recognizer/trainningData.yml')
cv2.destroyAllWindows()