import time
import pyautogui

# Pegando a data da etiqueta

data = input("Digite a data de validade): ")
# validade = input("Digite a data de validade: ")

visual = 151, 37
etiqueta = 189, 211
produto = 174, 125
coddebarras = 285, 138
primcod = '2'
produtos = ['3990', '3991', '3992', '3993', '3994', '4913', '4311', '4304', '4306', '4307', '4302', '4303', '5467', '3167', '3168', '12307', '10078', '8526', '4984',
            '4438', '1', '3', '4', '63', '11', '12', '13', '14', '16', '17', '4312', '4313', '4563', '1441', '5394', '8563', '74', '72', '7262', '1503', '1652', '6565']

caminholoja = "C:\Solidcon\LOJA2\Loja2.exe"

# abrindo e fazendo login no loja
pyautogui.hotkey("win", "r"), time.sleep(1), pyautogui.write(caminholoja), pyautogui.press("enter")
time.sleep(10), pyautogui.write("usuario"), pyautogui.press("enter"), time.sleep(4), 
pyautogui.press("enter"), time.sleep(2)

#abrindo a tela de etiqueta
pyautogui.click(visual),time.sleep(0.5), pyautogui.click(etiqueta),time.sleep(0.5), pyautogui.rightClick(produto),time.sleep(0.5), pyautogui.click(coddebarras)
time.sleep(1)

#teste para confirmar se todos os produtos estão certos
"""for cod in produtos:
    pyautogui.write(cod), pyautogui.press("tab"), pyautogui.press("tab"), pyautogui.press("tab"), pyautogui.press("tab"), time.sleep(1)"""


#primeira etiqueta (alimentando a data)
pyautogui.write(primcod), pyautogui.press("tab"), pyautogui.press("tab"), pyautogui.press("tab"),
pyautogui.write(data), pyautogui.press("tab"), pyautogui.press("tab"), pyautogui.press("enter"),
time.sleep(3.2),pyautogui.press("tab"),pyautogui.press("tab"),pyautogui.press("enter"), time.sleep(4), pyautogui.hotkey("alt", "f4"),
pyautogui.press("tab"), pyautogui.press("tab"), pyautogui.press("tab")

for cod in produtos:
    pyautogui.write(cod),pyautogui.press("tab"), pyautogui.press("enter"),
    time.sleep(3.2),pyautogui.press("tab"),pyautogui.press("tab"),pyautogui.press("enter"),time.sleep(4), pyautogui.hotkey("alt", "f4"),
    pyautogui.press("tab"), pyautogui.press("tab"), pyautogui.press("tab")