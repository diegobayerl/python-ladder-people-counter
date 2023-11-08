import cv2
import numpy as np

video = cv2.VideoCapture('people.mp4')

contador = 0
liberado = False

while True:
    success, img = video.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    x,y,w,h = 500,360,20,100
    imgTh = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 12)
    kernel = np.ones((8,8), np.uint8)
    imgDil = cv2.dilate(imgTh,kernel,iterations=2)


    recorte = imgDil[y:y+h,x:x+w]
    brancos = cv2.countNonZero(recorte)

    print(brancos)


    if brancos > 1950 and liberado == True:
        contador +=1
    if brancos < 1950:
        liberado = True
    else:
        liberado =False

    if liberado == False:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    else:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255, 0, 255),4)

    cv2.rectangle(imgTh, (x, y), (x + w, y + h), (255, 255, 255), 6)

    cv2.putText(img,str(brancos),(x-30,y-50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)
    cv2.putText(img, str(contador), (x-20, y+200), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)


    cv2.imshow('People',img)
    cv2.waitKey(40)