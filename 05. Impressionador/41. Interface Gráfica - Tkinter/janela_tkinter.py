import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

menssagem = tk.Label(text="Sistema de busca de cotações de moedas!", fg='white', bg='black', width=50, height=10) #fg: letra, bg: fundo, width: largura, height: altura
menssagem.pack()

menssagem2 = tk.Label(text="Selecione a moeda desajada:", bg='green', width=100, height=10)
menssagem2.pack()

janela.mainloop()