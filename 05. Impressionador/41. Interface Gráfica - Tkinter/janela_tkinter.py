import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pandas as pd

janela = tk.Tk()

janela.title("Cotação de Moedas")

janela.rowconfigure([0], weight=1) # ativa o redmiensionamento autmatico da 1° linha
janela.columnconfigure([0, 1], weight=1) # ativa o redmiensionamento autmatico da 1° e 2° coluna

menssagem = tk.Label(text="Sistema de busca de cotações de moedas!", fg='white', bg='black', width=35, height=5) #fg: letra, bg: fundo, width: largura, height: altura
menssagem.grid(row=0, column=0, columnspan=2, sticky='ewns')

menssagem2 = tk.Label(text="Selecione a moeda desajada:")
menssagem2.grid(row=1, column=0)

# moeda = tk.Entry()
# moeda.grid(row=1, column=1)


cotacoes = {
    'Dolar': 5.87,
    'Euro': 6.30,
    'Libra': 7.10
}

moedas = list(cotacoes.keys())

moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)

def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = cotacoes.get(moeda_preenchida)
    label_cotacao = tk.Label(text="Cotação Não encontrada!")
    label_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        label_cotacao['text'] = f'Cotação de {moeda_preenchida} é de {cotacao_moeda} reais'


botao = tk.Button(text="Buscar cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

menssagem3 = tk.Label(text="Caso queira pegar mais de 1 cotação ao mesmo tempo, digite uma em cada linha")
menssagem3.grid(row=4, column=0, columnspan=2)

caixa_texto = tk.Text(width=10, height=5)
caixa_texto.grid(row=5, column=0, sticky='ewns')


def buscar_cotacoes():
    texto = caixa_texto.get("1.0", tk.END)
    lista_moedas = texto.split("\n")
    menssagem_cotacao = []
    for item in lista_moedas:
        cotacao = cotacoes.get(item)
        if cotacao:
            menssagem_cotacao.append(f'{item}: {cotacao}')
    menssagem4 = tk.Label(text='\n'.join(menssagem_cotacao))
    menssagem4.grid(row=6, column=1)

botao_multiplas= tk.Button(text="Buscar cotação", command=buscar_cotacoes)
botao_multiplas.grid(row=5, column=1)

### Check Button ###

var_promocoes = tk.IntVar()
check_box = tk.Checkbutton(text="Deseja receber informações de promoção?", variable=var_promocoes)
check_box.grid(row=6, column=0)


def enviar():
    pass
    if var_promocoes.get() == 1:
        print("usuario deseja receber informções")
    else:
        print("usuario NÃO deseja receber informções")


botao_enviar = tk.Button(text="Enviar", command=enviar)
botao_enviar.grid(row=7, column=0)

### Radio Button ###

var_passagem = tk.StringVar(value='nenhum')


def enviar_passagem():
    print(var_passagem.get())


botao_classe_economica = tk.Radiobutton(text="Classe Economica", variable=var_passagem, value='Classe Economica')
botao_classe_executiva = tk.Radiobutton(text="Classe Executiva", variable=var_passagem, value='Classe Executiva')
botao_primeira_classe = tk.Radiobutton(text="Primeira Classe", variable=var_passagem, value='Primeira Classe')
botao_classe_economica.grid(row=8, column=0)
botao_classe_executiva.grid(row=8, column=1)
botao_primeira_classe.grid(row=8, column=2)

botao_enviar_passagem = tk.Button(text="Enviar", command=enviar_passagem)
botao_enviar_passagem.grid(row=9, column=0)


### askopenfilename ###

caminho_arquivo = askopenfilename(title="Selecione um arquivo excel para abrir!")

df = pd.read_excel(caminho_arquivo)
print(df)

janela.mainloop()