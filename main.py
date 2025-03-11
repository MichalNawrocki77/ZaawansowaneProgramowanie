import cv2
import imutils


def Rotate(image, pivot, angle):
    (h, w) = image.shape[:2]
    M = cv2.getRotationMatrix2D(pivot, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def zadanie1():
    image = cv2.imread("example.png")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)


    rotated = Rotate(image, (cX,cY),45)
    cv2.imshow("Rotated image", rotated)
    cv2.waitKey(0)

def zadanie2():
    image = cv2.imread("example.png")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    rotated = Rotate(image, (cX, cY), 90)
    cv2.imshow("Rotated image", rotated)
    cv2.waitKey(0)

def zadanie3():
    image = cv2.imread("example.png")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    rotated = Rotate(image, (0,0), 30)
    cv2.imshow("Rotated image", rotated)
    cv2.waitKey(0)

def zadanie4():
    angle = int(input("O ile stopni mam obrócić zdjęcie?\n"))
    image = cv2.imread("example.png")
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    rotated = Rotate(image, (cX,cY), 30)
    cv2.imshow("Rotated image", rotated)
    cv2.waitKey(0)

def zadanie5():
    image = cv2.imread("example.png")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    rotated = imutils.rotate(image, 180)
    cv2.imshow("Rotated image", rotated)
    cv2.waitKey(0)

def zadanie6():
    image = cv2.imread("example.png")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    rotated = imutils.rotate_bound(image, -33)
    cv2.imshow("Rotated image", rotated)
    cv2.waitKey(0)

def zadanie7():
    image = cv2.imread("example.png")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    rotated = Rotate(image, (cX, cY), 60)
    cv2.imshow("warpAffine", rotated)
    cv2.waitKey(0)

    rotated2 = imutils.rotate(image, 60)
    cv2.imshow("Imutil", rotated2)
    cv2.waitKey(0)

def zadanie8():
    image = cv2.imread("example.png")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    for _ in range(1,4):
        rotated = Rotate(image, (cX, cY), 30*_)
        cv2.imshow("Rotated image", rotated)
        cv2.waitKey(0)

    rotated = Rotate(image, (cX, cY), 90)
    cv2.imshow("Rotated image", rotated)
    cv2.waitKey(0)

def zadanie9():
    image = cv2.imread("example.png")
    cv2.imshow("Rotated image", image)
    cv2.waitKey(0)

    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    rotated = Rotate(image, (cX, cY), 75)
    cv2.imwrite("rotatedImageExercise9.png",rotated)

def zadanie10():
    image = cv2.imread("example.png")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    for _ in range(0, (360//15 + 1)):
        rotated = Rotate(image, (cX, cY), 15 * _)
        cv2.imshow("Rotated image", rotated)
        cv2.waitKey(500)

zadanie10()