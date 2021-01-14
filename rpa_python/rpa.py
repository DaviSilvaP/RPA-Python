import pyautogui
import time


pyautogui.hotkey('ctrl', 'alt', 't')
time.sleep(2)
pyautogui.write('firefox', interval=0.25)
pyautogui.press('enter')

time.sleep(2)
search_space = pyautogui.locateCenterOnScreen('/home/davi/Imagens/search.png', confidence=0.7)
pyautogui.click(search_space)

time.sleep(2)
pyautogui.write('animais', interval=0.25)
pyautogui.press('enter')

time.sleep(5)
images_btn = pyautogui.locateCenterOnScreen('/home/davi/Imagens/images_btn.png', confidence=0.7)
pyautogui.click(images_btn)

time.sleep(2)
X, Y = pyautogui.position()
pyautogui.moveTo(X, Y + 200)

stop = 5
time.sleep(2)
figure = pyautogui.locateCenterOnScreen('/home/davi/Imagens/doginho.png', confidence=0.7)

while True:
    pyautogui.scroll(-10)
    time.sleep(2)
    figure = pyautogui.locateCenterOnScreen('/home/davi/Imagens/doginho.png', confidence=0.7)
    print(figure)
    print(figure is None)
    if figure is not None:
        pyautogui.click(figure)
        break
    if stop <= 0:
        break
    stop -= 1
    print(stop)
