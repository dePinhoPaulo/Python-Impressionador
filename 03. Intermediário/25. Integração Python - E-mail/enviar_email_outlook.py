import win32com.client as Win32
import os

outlook = Win32.Dispatch('outlook.application')

email = outlook.CreateItem(0)

conta = outlook.Session.Accounts['email.selecionado@outlook.com']
email._oleobj_.Invoke(*(64209, 0, 8, 0, conta))  #metodo oculto de alteração do email de envio

email.To = "exemplo@hotmil.com"
email.Cc = "pythonimpressionador@gmail.com"
email.Bcc = "kiko.sjs@gmail.com"
email.Subject = "Envio Email Outlook"
email.HTMLBody = """ <p>Enviando Email com Python</p>
<p>att.</p>
<img src='https://pbs.twimg.com/media/ERy1uzkXsAE0u1B.jpg'>
"""

caminho_script = os.getcwd()
lista_arquivos = os.listdir('anexos')

for nome_arquivo in lista_arquivos:
    caminho_anexo = os.path.join(caminho_script, 'anexos', nome_arquivo)
    email.Attachments.Add(caminho_anexo)

email.Send()