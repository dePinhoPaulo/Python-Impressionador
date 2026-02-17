from imap_tools import MailBox, OR
from dotenv import load_dotenv
import os

load_dotenv()
senha = os.getenv('SENHA')
usuario = 'depinhopaulorogerio@gmail.com'

meu_email = MailBox('imap.gmail.com').login(usuario, senha)

#verificar pastas do email
# for pasta in meu_email.folder.list():
#     print(pasta)

meu_email.folder.set('[Gmail]/Sent Mail')

lista_email = meu_email.fetch(OR(from_='depinhopaulorogerio@gmail.com', to='kiko.sjs@gmail.com'))

for email in lista_email:
    if len(email.attachments) > 0:
        print(email.subject)
        print(email.text)
        print(email.html)
        for anexo in email.attachments:
            print('anexo: ', anexo.filename)