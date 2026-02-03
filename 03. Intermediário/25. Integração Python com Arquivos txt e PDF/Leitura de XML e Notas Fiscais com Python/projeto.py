import xmltodict
import pprint
import os
import pandas as pd


### LER XML SERVICO ####
def ler_xml_danfe(nota):

    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)

    #pprint.pprint(documento)

    #pprint.pprint(documento['nfeProc']['NFe']['infNFe']['dest']['CPF'])

    #for item in documento['nfeProc']['NFe']:
       #print(item)

    # valor_total, produtos/servicos (valores), cnpj_vendeu, nome_vendeu, cpf/cnpj_comprou,  nome_comprou

    dic_nf = documento['nfeProc']['NFe']['infNFe']

    valor_total = dic_nf['total']['ICMSTot']['vNF']
    cnpj_vendeu = dic_nf['emit']['CNPJ']
    nome_vendeu = dic_nf['emit']['xNome']
    cpf_comprou = dic_nf['dest']['CPF']
    nome_comprou = dic_nf['dest']['xNome']

    lista_produtos = []
    produtos = dic_nf['det']
    for produto in produtos:
        valor_produto = produto['prod']['vProd']
        nome_produto = produto['prod']['xProd']
        lista_produtos.append((nome_produto, valor_produto))

    resposta = {
        'Valor Total': valor_total,
        'CNPJ Vendedor': cnpj_vendeu,
        'Razão Social': nome_vendeu,
        'CPF Comprador': cpf_comprou,
        'Nome Comprador': nome_comprou,
        'Lista de Produtos': lista_produtos
    }

    return(resposta)

#print(ler_xml_danfe('NFs Finais\DANFEBrota.xml'))
#print(ler_xml_danfe('NFs Finais\DANFENespresso.xml'))


### LER XML SERVICO ####
def ler_xml_servico(nota):

    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)

    dic_nf = documento['ConsultarNfseResposta']['ListaNfse']['CompNfse']['Nfse']['InfNfse']

    valor_total = dic_nf['Servico']['Valores']['ValorServicos']
    cnpj_vendeu = dic_nf['PrestadorServico']['IdentificacaoPrestador']['Cnpj']
    nome_vendeu = dic_nf['PrestadorServico']['RazaoSocial']
    cpf_comprou = dic_nf['TomadorServico']['IdentificacaoTomador']['CpfCnpj']['Cnpj']
    nome_comprou = dic_nf['TomadorServico']['RazaoSocial']
    produtos = dic_nf['Servico']['Discriminacao']

    resposta = {
        'Valor Total': valor_total,
        'CNPJ Vendedor': cnpj_vendeu,
        'Razão Social': nome_vendeu,
        'CPF Comprador': cpf_comprou,
        'Nome Comprador': nome_comprou,
        'Lista de Produtos': produtos
    }

    return(resposta)


# Inserir informações em um Banco de dados.

lista_arquivos = os.listdir('NFs Finais')
respostas = []

for arquivo in lista_arquivos:
    if 'xml' in arquivo:
        if 'DANFE' in arquivo:
            respostas.append(ler_xml_danfe(f'NFs Finais/{arquivo}'))
        else:
            respostas.append(ler_xml_servico(f'NFs Finais/{arquivo}'))

df_tabela = pd.DataFrame(respostas)
df_tabela.to_excel('NFs.xlsx')