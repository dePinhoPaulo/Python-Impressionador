# Passo a passo
# Abrir o ERP (Fakturama)
# Clicar no menu new
# Clicar em new product
# preencher todos campos
# selecionar imagem
# Clicar em salvar

import pyautogui
import subprocess
import time

pyautogui.FAILSAFE = True #interrompe o programa a qualquer momento em caso de falaha, mexendo o mouse pa extremidade

def encontrar_imagem(imagem):
    while not pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9): # Recnhecimento de imagem
        time.sleep(1)
    encontrou = pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
    return encontrou

def direita(posicaoes_imagem):
    return posicaoes_imagem[0] + posicaoes_imagem[2], posicaoes_imagem[1] + posicaoes_imagem[3]/2 #Localiza dirieta da imgem

# Passo 1 - Abrir Fakturama
subprocess.Popen([r'C:\Program Files\Fakturama2\Fakturama.exe'])

encontrou = encontrar_imagem('arquivo.png') # Recnhecimento de imagem
# Fakturama aberto!

# Passo 2 - Clicar no menu
# Esperar menu carregar
encontrou = encontrar_imagem('menu-new.png')
# Clicar no menu
pyautogui.click(pyautogui.center(encontrou))

# Esperar menu new product carregar
encontrou = encontrar_imagem('menu-new-product.png')
# Clicar no menu
pyautogui.click(pyautogui.center(encontrou))

# Passo 3 - Preencher todos campos
# Item number
encontrou = encontrar_imagem('item-number.png')
# Clicar na dirieta da imgem
pyautogui.click(direita(encontrou))
# Digitar
pyautogui.write("2")

# Name
pyautogui.press('tab') #Pular para proximo campo
pyautogui.write("Computador")

# Category
pyautogui.press('tab') 
pyautogui.write("Tech")

# GTIN
pyautogui.press('tab') 
pyautogui.write("12354")

# Supplier code
pyautogui.press('tab') 
pyautogui.write("6584")

# Description
pyautogui.press('tab') 
pyautogui.write("PC Gamer")

# Price
pyautogui.press('tab') 
pyautogui.write('1250,00') 

# Cost Price
encontrou = encontrar_imagem('coste-price.png')
pyautogui.click(direita(encontrou))
pyautogui.write('550,00')

# Stock
encontrou = encontrar_imagem('coste-price.png')
pyautogui.click(direita(encontrou))
pyautogui.write('5,00')

# Passo 4 - Upload imagem
encontrou = encontrar_imagem('select-picture.png')
pyautogui.click(pyautogui.center(encontrou))

# Navegação Windows
encontrou = encontrar_imagem('select-picture.png')
pyautogui.click(pyautogui.center(encontrou))
pyautogui.write(r'C:\Users\Kiko\Documents\Projetos Programação\Python-Impressionador\04. Avançado\29. RPA com Python - Automações de Processos\Automações de ERPs\notebook.jpg')
pyautogui.press('enter') 