import cv2
import time
import numpy as np
import pyautogui


def get_positions():
    imagem = np.array(pyautogui.screenshot())

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    classificador = cv2.CascadeClassifier(
                    'Recursos/haarcascade_frontalface_default.xml')

    deteccoes = classificador.detectMultiScale(imagem_cinza, scaleFactor=1.2,
                                               minNeighbors=5, minSize=(30, 30),
                                               maxSize=(100, 100))

    if len(deteccoes) > 0:
        return imagem, deteccoes
    else:
        return None, None


def show_face(imagem, deteccoes):
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)

    cv2.imshow('Detector de Faces', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


pyautogui.hotkey('ctrl', 'alt', 't')
time.sleep(2)
pyautogui.write('firefox', interval=0.25)
pyautogui.press('enter')

time.sleep(2)
search_space = pyautogui.locateCenterOnScreen('/home/davi/Imagens/search.png', confidence=0.7)
pyautogui.click(search_space)

time.sleep(2)
pyautogui.write('Mico Leão Dourado', interval=0.25)
pyautogui.press('enter')

time.sleep(5)
images_btn = pyautogui.locateCenterOnScreen('/home/davi/Imagens/images_btn.png', confidence=0.7)
pyautogui.click(images_btn)

time.sleep(2)
X, Y = pyautogui.position()
pyautogui.moveTo(X, Y + 200)

stop = 10

while True:
    time.sleep(2)
    imagem, deteccoes = get_positions()
    print(deteccoes)
    if deteccoes is not None:
        pyautogui.click((deteccoes[0][0], deteccoes[0][1]))
        show_face(imagem, deteccoes)
        break
    if stop <= 0:
        break
    stop -= 1
    print(stop)
    pyautogui.scroll(-10)
