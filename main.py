import cv2
import imutils
import numpy as np


def zadanie1():
    image = cv2.imread("example.jpg")
    cv2.imshow("image", image)
    cv2.waitKey(0)

    M = np.float32([
        [1, 0, 30],
        [0, 1, 40]
    ])

    shifted = cv2.warpAffine(image,M,(image.shape[0],image.shape[1]))

    cv2.imshow("shifted", shifted)
    cv2.waitKey(0)

def zadanie2():
    image = cv2.imread("example.jpg")
    cv2.imshow("image", image)
    cv2.waitKey(0)

    M = np.float32([
        [1, 0, 20],
        [0, 1, 50]
    ])

    shifted = cv2.warpAffine(image,M,(image.shape[0],image.shape[1]))

    cv2.imshow("shifted", shifted)
    cv2.waitKey(0)

def zadanie3():
    image = cv2.imread("example.jpg")
    cv2.imshow("image", image)
    cv2.waitKey(0)

    M = np.float32([
        [1,0,image.shape[0] +50],
        [0,1,image.shape[1] +50]
    ])

    shifted = cv2.warpAffine(image, M, (image.shape[0],image.shape[1]))

    cv2.imshow("image", shifted)
    cv2.waitKey(0)

def zadanie4():
    image = cv2.imread("example.jpg")
    cv2.imshow("image", image)
    cv2.waitKey(0)

    shifted = imutils.translate(image,100,50)
    cv2.imshow("image", shifted)
    cv2.waitKey(0)

def zadanie5():
    image = cv2.imread("example.jpg")
    tx = int(input("o ile pikseli w prawo chcesz przesunąc zdjęcie?\n"))
    ty = int(input("o ile pikseli w dół chcesz przesunąc zdjęcie?\n"))

    shifted = imutils.translate(image,tx,ty)
    cv2.imshow("image", shifted)
    cv2.waitKey(0)

zadanie5()
