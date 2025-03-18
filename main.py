import cv2
import numpy as np


def zadanie1():
    image = cv2.imread('example.jpg')
    cv2.imshow("Original", image)
    cv2.waitKey(0)

    openCvAdded = cv2.add(image, np.ones(image.shape, dtype="uint8") * 50)
    numpyAdded = image + np.ones(image.shape, dtype="uint8") * 50

    cv2.imshow("OpenCV", openCvAdded)
    cv2.waitKey(0)
    cv2.imshow("Numpy", numpyAdded)
    cv2.waitKey(0)

def zadanie2():
    image = cv2.imread('example.jpg')
    cv2.imshow("Original", image)
    cv2.waitKey(0)

    burned = image + np.ones(image.shape, dtype="uint8") * 150

    cv2.imshow("Numpy", burned)
    cv2.waitKey(0)

def zadanie3():
    image = cv2.imread('example.jpg')
    cv2.imshow("Original", image)
    cv2.waitKey(0)

    openCvSubtracted = cv2.subtract(image, np.ones(image.shape, dtype="uint8") * 80)
    numpySubtracted = image - np.ones(image.shape, dtype="uint8") * 80

    cv2.imshow("OpenCV", openCvSubtracted)
    cv2.waitKey(0)
    cv2.imshow("Numpy", numpySubtracted)
    cv2.waitKey(0)

def zadanie4():
    image = cv2.imread('example.jpg')
    cv2.imshow("Original", image)
    cv2.waitKey(0)

    image = cv2.add(image,(10,-20,30))

    cv2.imshow("filtered",image)
    cv2.waitKey(0)

def zadanie5():
    image = cv2.imread('example.jpg')
    cv2.imshow("Original", image)
    cv2.waitKey(0)

    image2 = cv2.add(image,(10,-20,30))

    diff = cv2.absdiff(image,image2)

    #widoczne jest zdjęcie ale bardzo pociemnione, gdyż różnica to (10,20,30).
    #Z racji tego iż wartości kolorów są małe to zdjęcie wygląda jak prawie czarne
    #Widoczne sa lekke kontury zdjęcia
    cv2.imshow("diff",diff)
    cv2.waitKey(0)

zadanie5()