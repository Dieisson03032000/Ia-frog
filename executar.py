import cv2 as cv

camera = cv.VideoCapture("video4.mp4")
#2IH2F7SXSTFS.jpg
cascade = cv.CascadeClassifier("treinamento/cascade.xml")
while True:
    #imagem = cv.imread("chicken/test/TDFAKEMSPE9G.jpg")
    _, imagem = camera.read()
    gray = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
    objetos = cascade.detectMultiScale(gray, 6, 5)

    for (x,y,w,h) in objetos:
        cv.rectangle(imagem, (x,y),(x+w,y+h),(0,0,255),2)

    cv.imshow("Sapo", imagem)
    k = cv.waitKey(60)
    if k == 27:
        break
    
cv.destroyAllWindows()
camera.release()
