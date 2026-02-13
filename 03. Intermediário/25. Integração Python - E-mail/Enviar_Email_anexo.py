#SMTP

import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
import os

def enviar_email():

    load_dotenv()
    senha = os.getenv('SENHA')

    msg = MIMEMultipart()
    msg['Subject'] = "Email enviado com Python"
    msg['From'] = 'depinhopaulorogerio@gmail.com'
    msg['To'] = 'kiko.sjs@gmail.com'
    #msg['Cc']
    #msg['Bcc']

    corpo_email = """<p>Boa noite!</p>
    <p>Teste de envio do email.</p>
    <p>Att.</p>
    <img src='https://pbs.twimg.com/media/ERy1uzkXsAE0u1B.jpg'>
    """

    msg.attach(MIMEText(corpo_email, 'html'))

    #anexar arquivos
    lista_arquivos = os.listdir('anexos')
    for nome_arquivo in lista_arquivos:
        with open(f'anexos/{nome_arquivo}', 'rb') as arquivo:
            msg.attach(MIMEApplication(arquivo.read(), Name=nome_arquivo))
    
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(msg['From'], senha)
    servidor.send_message(msg)
    servidor.quit()
    print("Email enviado!")

enviar_email()