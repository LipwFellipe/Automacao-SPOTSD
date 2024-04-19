import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.leftClick(x=629, y=633)
time.sleep(1)
pyautogui.write( link )
pyautogui.press("enter")
time.sleep(1)
pyautogui.leftClick(x=2926, y=510)
pyautogui.write("Lol ksksks")
pyautogui.press("tab")
pyautogui.write("Lol ksksks")
time.sleep(1)
pyautogui.leftClick(x=3260, y=709)

import pandas as pd

tabela = pd.read_csv("msc.csv")

print(tabela)
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=2915, y=368)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "a"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "b"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "c"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "d"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "e"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "f"]))
    pyautogui.press("tab")
    