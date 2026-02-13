#SMTP

import smtplib
import email.message
from dotenv import load_dotenv
import os

def enviar_email():

    load_dotenv()
    senha = os.getenv('SENHA')

    msg = email.message.Message()
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

    corpo_email = corpo_email.encode('utf-8')

    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo_email)

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(msg['From'], senha)
    servidor.send_message(msg)
    servidor.quit()
    print("Email enviado!")

enviar_email()