import cv2

def zadanie1():
    image = cv2.imread("example.png")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    flipped = cv2.flip(image,0)
    cv2.imshow("flipped Horizontally", flipped)
    cv2.waitKey(0)

def zadanie2():
    image = cv2.imread("example.png")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    flipped = cv2.flip(image,1)
    cv2.imshow("flipped Vertically", flipped)
    cv2.waitKey(0)

def zadanie3():
    image = cv2.imread("example.png")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    flipped = cv2.flip(image,-1)
    cv2.imshow("flipped symmetrically", flipped)
    cv2.waitKey(0)

def zadanie4():
    image = cv2.imread("example.png")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    flipped2 = cv2.flip(image,0)
    cv2.imshow("flipped Vertically", flipped2)
    cv2.waitKey(0)
    flipped1 = cv2.flip(image,1)
    cv2.imshow("flipped Horizontally", flipped1)
    cv2.waitKey(0)
    flipped3 = cv2.flip(image,-1)
    cv2.imshow("flipped symmetrically", flipped3)
    cv2.waitKey(0)

def zadanie5():
    image = cv2.imread("example.png")
    srodekX = image.shape[1] // 2

    LewaPolowa = image[0:image.shape[0],0:srodekX]

    LewaPolowa= cv2.flip(LewaPolowa,1)
    image[0:image.shape[0],0:srodekX] = LewaPolowa[0:image.shape[0],0:srodekX]

    cv2.imshow("wynik",image)
    cv2.waitKey(0)

def zadanie6():
    howToFlip = int(input("Jak chcesz obrócić obraz?\n"
                      "1 aby obrócić pionowo\n"
                      "0 aby obrócić poziomo\n"
                      "-1 aby obrócić symetrycznie\n"))

    image = cv2.imread("example.png")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    flipped = cv2.flip(image,howToFlip)
    cv2.imshow("flipped symmetrically", flipped)
    cv2.waitKey(0)

zadanie6()