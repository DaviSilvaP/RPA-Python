import numpy as np
import pyautogui

#img = pyautogui.screenshot('/home/davi/Documentos/RPA_Python/my_screenshot.png')
img = np.array(pyautogui.screenshot())
print(img.shape)
