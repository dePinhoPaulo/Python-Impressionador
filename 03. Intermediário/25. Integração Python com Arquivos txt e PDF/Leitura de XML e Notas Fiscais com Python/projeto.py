import xmltodict
import pprint

with open('NFs Finais/DANFEBrota.xml', 'rb') as arquivo:
    documento = xmltodict.parse(arquivo)

pprint.pprint(documento)
