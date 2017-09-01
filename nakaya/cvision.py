import numpy as np
import cv2

def toAlpha(src):

    whiteColor = (255,255,255)

    laughFace = cv2.imread(src,cv2.IMREAD_UNCHANGED)
    fh, fw, ch = laughFace.shape

    alphaLaughFace = np.zeros([fh,fw,4], dtype=np.uint8)
    gray = cv2.cvtColor(laughFace, cv2.COLOR_BGR2GRAY)
    ret, nichi = cv2.threshold(gray, 0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    for i,row in enumerate(nichi):
        for j,p in enumerate(row):
            if np.allclose(p,whiteColor):
                alphaLaughFace[i,j] = [255,255,255,0]
            else :
                pixel = laughFace[i,j].tolist()
                alphaLaughFace[i,j] = pixel

    return alphaLaughFace

def detectiveFace(src, faces):
    cascadeFolder = "/usr/local/Cellar/opencv3/3.2.0/share/OpenCV/haarcascades/"
    cascadeFile = "haarcascade_frontalface_alt2.xml"
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascadeFolder + cascadeFile)

    facerect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=faces, minSize=(1, 1))

    return facerect