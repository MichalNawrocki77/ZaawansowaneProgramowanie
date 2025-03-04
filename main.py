import cv2


def Zadanie1():
    image = cv2.imread("example.jpg")
    cv2.imshow("Linuxiarze", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Zadanie1ZlaSciezka():
    image = cv2.imread("e.jpg") #Jeśli wezwe imshow() na tym zdjęciu to zrobi error
    try:                        #więc wrzuce to do try catcha
        cv2.imshow("Linuxiarze", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except :
        print("Zła ścieżka do pliku proszę sprawdź nazwe pliku")

def Zadanie2():
    image = cv2.imread("example.jpg")
    print(f"Liczba kanałów: {image.shape[2]}")

def Zadanie3():
    image = cv2.imread("example.jpg", cv2.IMREAD_GRAYSCALE)
    #Greyscale ma width i height, nie ma kanalów :c
    #Co ma sens bo greyscale potrzebuje tylko jednej wartości
    #więc domyślam się, że zapisywana jest bezpośrednio w arrayu pixelów
    if(len(image.shape) > 2):
        print(f"Liczba kanałów w grayscale'u: {image.shape[2]}")

def Zadanie4():
    image = cv2.imread("example.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("Czarno-Bialy.jpg",image)

def Zadanie5():
    image = cv2.imread("example.jpg")
    image2 = cv2.imread("example2.jpg")

    cv2.imshow("example",image)
    cv2.imshow("example2",image2)

    cv2.waitKey(0)
    cv2.destroyWindow("example")
    cv2.waitKey(0)
    cv2.destroyWindow("example2")

def Zadanie6():
    image = cv2.imread("example.jpg")
    cv2.namedWindow("example", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("example", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("example", image)
    cv2.waitKey()
    cv2.destroyAllWindows()

Zadanie6()