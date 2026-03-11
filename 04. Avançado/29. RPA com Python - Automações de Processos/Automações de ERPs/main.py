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

# Passo 1 - Abrir Fakturama
subprocess.Popen([r'C:\Program Files\Fakturama2\Fakturama.exe'])

while not pyautogui.locateOnScreen('arquivo.png', grayscale=True, confidence=0.9): # Recnhecimento de imagem
    time.sleep(1)
# Fakturama aberto!
