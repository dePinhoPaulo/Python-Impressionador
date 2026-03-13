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
import pandas as pd
import pyperclip

pyautogui.FAILSAFE = True #interrompe o programa a qualquer momento em caso de falaha, mexendo o mouse pa extremidade

def encontrar_imagem(imagem):
    while not pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9): # Recnhecimento de imagem
        time.sleep(1)
    encontrou = pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
    return encontrou

def direita(posicaoes_imagem):
    return posicaoes_imagem[0] + posicaoes_imagem[2], posicaoes_imagem[1] + posicaoes_imagem[3]/2 #Localiza dirieta da imgem

# Passo 7 - Mostrar cacteres com Acento
def escrever_texto(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')

# Passo 1 - Abrir Fakturama
subprocess.Popen([r'C:\Program Files\Fakturama2\Fakturama.exe'])

encontrou = encontrar_imagem('arquivo.png') # Recnhecimento de imagem
# Fakturama aberto!

# Passo 6 - Integar preenchimento com planilha no Excel
df_produtos = pd.read_excel('Produtos.xlsx')

for linha in df_produtos.index:
    nome = df_produtos.loc[linha, 'Nome']
    id = df_produtos.loc[linha, 'ID']
    categoria = df_produtos.loc[linha, 'Categoria']
    gtin = df_produtos.loc[linha, 'Categoria']
    supplier = df_produtos.loc[linha, 'Categoria']
    descricao = df_produtos.loc[linha, 'Descrição']
    imagem = df_produtos.loc[linha, 'Imgem']
    preco = df_produtos.loc[linha, 'Preço']
    custo = df_produtos.loc[linha, 'Custo']
    estoque = df_produtos.loc[linha, 'Estoque']


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
    pyautogui.write(str(id))

    # Name
    pyautogui.press('tab') #Pular para proximo campo
    pyautogui.write(str(nome))

    # Category
    pyautogui.press('tab') 
    pyautogui.write(str(categoria))

    # GTIN
    pyautogui.press('tab') 
    pyautogui.write(str(gtin))

    # Supplier code
    pyautogui.press('tab') 
    pyautogui.write(str(supplier))

    # Description
    pyautogui.press('tab') 
    pyautogui.write(str(descricao))

    # Price
    pyautogui.press('tab') 
    preco_texto = f'{preco:.2f}'.replace('.', ',')
    pyautogui.write(str(preco_texto)) 

    # Cost Price
    encontrou = encontrar_imagem('coste-price.png')
    pyautogui.click(direita(encontrou))
    custo_texto = f'{preco:.2f}'.replace('.', ',')
    pyautogui.write(str(custo_texto))

    # Stock
    encontrou = encontrar_imagem('coste-price.png')
    pyautogui.click(direita(encontrou))
    estoque_texto = f'{preco:.2f}'.replace('.', ',')
    pyautogui.write(str(estoque_texto))

    # Passo 4 - Upload imagem
    encontrou = encontrar_imagem('select-picture.png')
    pyautogui.click(pyautogui.center(encontrou))

    # Navegação Windows
    encontrou = encontrar_imagem('nome-arquivo.png')
    pyautogui.click(pyautogui.center(encontrou))
    pyautogui.write(rf'C:\Users\Kiko\Documents\Projetos Programação\Python-Impressionador\04. Avançado\29. RPA com Python - Automações de Processos\Automações de ERPs\{str(imagem)}')
    pyautogui.press('enter') 

    # Passo 5 - Salvar Cadastro
    # Salvar
    encontrou = encontrar_imagem('salvar.png')
    pyautogui.click(pyautogui.center(encontrou))
