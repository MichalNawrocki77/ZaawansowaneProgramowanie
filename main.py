import cv2

def zadanie1():
    image = cv2.imread('example.jpg')
    cv2.imshow("Original",image)
    cv2.waitKey(0)

    wycinek = image[0:100,0:100]
    cv2.imshow("wycinek 100x100",wycinek)
    cv2.waitKey(0)


def zadanie2():
    image = cv2.imread('example.jpg')
    cv2.imshow("Original",image)
    cv2.waitKey(0)

    wycinekGora = image[0:int(image.shape[0]/2),0:image.shape[1]]
    wycinekDol = image[int(image.shape[0] / 2): image.shape[0], 0:image.shape[1]]

    cv2.imshow("Dolna Polowa",wycinekDol)
    cv2.waitKey(0)

def zadanie3():
    image = cv2.imread('example.jpg')
    cv2.imshow("Original",image)
    cv2.waitKey(0)

    wycinekPrawo = image[0:image.shape[0], int(image.shape[1]/2):image.shape[1]]

    cv2.imshow("Prawa Polowa",wycinekPrawo)
    cv2.waitKey(0)

def zadanie4():
    print("Chcesz przyciąć obraz o wymiarach: 720x960")
    startX = int(input("Podaj startX\n"))
    endX = int(input("Podaj endX\n"))
    startY = int(input("Podaj startY\n"))
    endY = int(input("Podaj endY\n"))


    image = cv2.imread('example.jpg')
    cv2.imshow("Nie pociete",image)
    cv2.waitKey(0)

    wycinek = image[startY:endY,startX:endX]

    cv2.imshow("Wycinek",wycinek)
    cv2.waitKey(0)

def zadanie5():
    image = cv2.imread('example.jpg')
    cv2.imshow("Nie pociete",image)
    cv2.waitKey(0)

    wycinek = image[0:230,0:550]

    cv2.imshow("Wycinek Twarzy",wycinek)
    cv2.waitKey(0)

def zadanie6():
    image = cv2.imread('example.jpg')
    cv2.imshow("wycinek 100x100",image)
    cv2.waitKey(0)

    wycinek = image[250:350,250:350]

    image[400:500,600:700] = wycinek
    cv2.imshow("wycinek 100x100",image)
    cv2.waitKey(0)

def zadanie7():
    image = cv2.imread('example.jpg')
    cv2.imshow("Original",image)
    cv2.waitKey(0)

    shapeY = image.shape[0]
    shapeX = image.shape[1]
    wycinki = []

    aThirdOfShapeY = int(shapeY/3)
    aThirdOfShapeX = int(shapeX/3)
    for i in range(0,3):
        for j in range(0,3):
            wycinki.append(image[
                           aThirdOfShapeY * i : aThirdOfShapeY * (i+1),
                           aThirdOfShapeX * j : aThirdOfShapeX * (j+1)
                           ])

    for wycinek in wycinki:
        cv2.imshow("wycinek",wycinek)
        cv2.waitKey(500)

def zadanie8():
    image = cv2.imread('example.jpg')
    cv2.imshow("Original",image)
    cv2.waitKey(0)

    for i in range(0,image.shape[1],10):
        wycinek = image[0:image.shape[0],0:i+1]
        cv2.imshow("wycinek",wycinek)
        cv2.waitKey(10)

def zadanie9():
    image = cv2.imread('example.jpg')
    cv2.imshow("Original", image)
    cv2.waitKey(0)

    wycinek = image[0:300,0:300]
    cv2.imshow("Zapisywany wycinek", wycinek)
    cv2.waitKey(0)
    cv2.imwrite("wycinek 300x300.jpg",wycinek)

zadanie9()