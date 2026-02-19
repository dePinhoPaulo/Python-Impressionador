import win32com.client as Win32
import os

outlook = Win32.Dispatch('outlook.application')

caixas_email = outlook.GetNamespace('MAPI')

for pasta in caixas_email.Folders:
    print(pasta)

pasta_python = caixas_email.Folders.Item(2)

for sub_pasta in pasta_python.Folders:
    print(sub_pasta)

caixa_entrada = pasta_python.Folders.Item(1)

lista_emails = caixa_entrada.Items
print(len(lista_emails))

for email in lista_emails:
    if email.To == 'falseta_fake@gmail.com' and len(anexos) > 0:
        print(email.Subject)
        print(email.Cc)
        print(email.Body)
        anexos = email.Attachments
        for anexo in anexos:
            print(anexo.FileName)
            caminho_codigo = os.getcwd()
            caminho_codigo_salvar = os.path.join(caminho_codigo, f'Email {email.Subject} - {anexo.FileName}')
            anexo.SaveAsFile(caminho_codigo_salvar)

