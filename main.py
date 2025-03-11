import cv2
import numpy as np

def GetCenter(canvas):
    return canvas.shape[0] // 2, canvas.shape[1] // 2

def zadanie1():
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    color = (0,255,0)
    cv2.line(canvas,
        GetCenter(canvas),   #punkt srodka
        (canvas.shape[0],canvas.shape[1]),  #prawy dolny punkt
             color)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

def zadanie2():
    canvas = np.zeros((400, 400, 3), dtype="uint8")
    cv2.rectangle(canvas,
                  (0,0),
                  (50,100),
                  (0,255,0))

    cv2.rectangle(canvas,
                  (300,300),
                  (canvas.shape[0]-1,canvas.shape[1]-1),
                  (0,0,255))

    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

def zadanie3():
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    cv2.circle(canvas,
               (40,40), #współrzędne środka
               40,  #promien
               (255,0,0)    #kolor
               )

    cv2.circle(canvas,
               GetCenter(canvas),
               60,
               (0,0,255))

    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

def zadanie4():
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    center = GetCenter(canvas)
    cv2.rectangle(canvas,
                  (center[0] - 50, center[1] - 50),
                  (center[0] + 50, center[1] + 50),
                  (255,0,0)
                  )

    cv2.circle(canvas,
               GetCenter(canvas),
               30,
               (0,255,0))

    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

def zadanie5():
    canvas = np.zeros((350, 350, 3), dtype="uint8")
    center = GetCenter(canvas)

    for r in range(0, 175, 25):
        cv2.rectangle(canvas,
                      (center[0]-r,center[1]-r),
                      (center[0]+r,center[1]+r),
                      (r+(225-175),0,0))

    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

def zadanie6():
    image = cv2.imread("example.png")
    center = GetCenter(image)


    cv2.circle(image,
               (230,190),
               20,
               (0, 0, 255),
               -1)
    cv2.circle(image,
               (270, 190),
               20,
               (0, 0, 255),
               -1)

    cv2.rectangle(image,
                  (217,217),
                  (295,275),
                  (0,255,0),
                  -1)
    cv2.circle(image,
               (255, 210),
               80,
               (255, 0, 0),
               3)

    cv2.imshow("example", image)
    cv2.waitKey(0)

zadanie6()
