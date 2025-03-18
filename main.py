import cv2
import imutils


def zadanie1():
    image = cv2.imread("example.jpg")
    cv2.imshow("example",image)
    cv2.waitKey(0)

    newWidth = int(image.shape[0]/2)
    newHeight = int(image.shape[0]/2)
    image2 = cv2.resize(image,(newWidth,newHeight))
    cv2.imshow("Resized",image2)
    cv2.waitKey(0)

def zadanie2():
    image = cv2.imread("example.jpg")
    cv2.imshow("example",image)
    cv2.waitKey(0)

    newWidth = image.shape[0]*2
    newHeight = image.shape[0]*2
    image2 = cv2.resize(image,(newWidth,newHeight), cv2.INTER_LINEAR)
    cv2.imshow("Resized",image2)
    cv2.waitKey(0)

def zadanie3():
    image = cv2.imread("example.jpg")
    cv2.imshow("example",image)
    cv2.waitKey(0)

    image2 = cv2.resize(image,(200,300))
    cv2.imshow("Resized",image2)
    cv2.waitKey(0)

def zadanie4():
    image = cv2.imread("example.jpg")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    methods = [
        ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
        ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
        ("cv2.INTER_AREA", cv2.INTER_AREA),
        ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
        ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]

    for (name, method) in methods:
        print("[INFO] {}".format(name))
        resized = imutils.resize(image, width=image.shape[1] * 3,
                                 inter=method)
        cv2.imshow("Method: {}".format(name), resized)
        cv2.waitKey(0)

def zadanie5():
    image = cv2.imread("example.jpg")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    resized = imutils.resize(image, width = 500)
    cv2.imshow("resized", resized)
    cv2.waitKey(0)

def zadanie6():
    image = cv2.imread("example.jpg")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    resized = imutils.resize(image, height = 400)
    cv2.imshow("resized", resized)
    cv2.waitKey(0)

def zadanie7():
    image = cv2.imread("example.jpg")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    resized = cv2.resize(image, (int(image.shape[1] / 5), int(image.shape[0] / 5)),
                              interpolation=cv2.INTER_AREA
                             # interpolation=cv2.INTER_LINEAR
                             # interpolation=cv2.INTER_CUBIC
                             # interpolation=cv2.INTER_NEAREST
                             # interpolation=cv2.INTER_LANCZOS4
                         )

    cv2.imshow("resized", resized)
    cv2.waitKey(0)

def zadanie8():
    image = cv2.imread("example.jpg")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    resized1 = cv2.resize(image, (int(image.shape[1] * 4), int(image.shape[0] * 4)),
                              interpolation=cv2.INTER_CUBIC)

    resized2 = cv2.resize(image,(int(image.shape[1] * 4), int(image.shape[0] * 4)),
                              interpolation=cv2.INTER_LANCZOS4)

    cv2.imshow("Inter_Cubic", resized1)
    cv2.imshow("Inter_Lanczos4", resized2)
    cv2.waitKey(0)

def zadanie9():
    image = cv2.imread("example.jpg")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    for i in range(100,301,20):
        resized = imutils.resize(image,width = int(image.shape[1] * (i/100)))
        cv2.imshow(f"Scaled {i}%", resized)
        cv2.waitKey(500)

def zadanie10():
    image = cv2.imread("example.jpg")
    cv2.imshow("example", image)
    cv2.waitKey(0)

    resized = imutils.resize(image, width = 800)
    cv2.imshow("resized with width = 800",resized)
    cv2.waitKey(0)
    cv2.imwrite("resized_output.jpg", resized)

zadanie10()
