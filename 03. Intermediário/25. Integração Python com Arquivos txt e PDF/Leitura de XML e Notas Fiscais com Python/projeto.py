import xmltodict
import pprint

with open('NFs Finais/DANFENespresso.xml', 'rb') as arquivo:
    documento = xmltodict.parse(arquivo)

pprint.pprint(documento)

pprint.pprint(documento['nfeProc']['NFe']['infNFe']['dest']['CPF'])

for item in documento['nfeProc']['NFe']:
    print(item)

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

pprint.pprint(resposta)

# Inserir informações em um Banco de dados.