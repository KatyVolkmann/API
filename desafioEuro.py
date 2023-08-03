import requests as request
import json as conversorJson


resposta = request.get("https://economia.awesomeapi.com.br/last/EUR-BRL")

euroReal = conversorJson.loads(resposta.content)

valorEuro = float(euroReal["EURBRL"]["bid"])
print(valorEuro)

class Cambio():
    def comprarEuro(self):
        valor = float(input("Quantos euros você precisa comprar?"))
        converter = valor * valorEuro
        print ("Para comprar EUR ", valor, "você precisará de R$ ", converter)

    def venderEuro(self):
        valor = float(input("Quantos euros você deseja vender?"))
        converter = valor / valorEuro
        print ("A sua venda de ", valor, " euros renderá R$ ", converter)
        
cambio = Cambio()
    
def menuadm():
    while True:
        match int(input("1- Comprar Euro\n2- Vender Euro\n3- Sair")):
            case 1:
                cambio.comprarEuro()
            case 2: 
                cambio.venderEuro()
            case 3:
                print("Menu Câmbio encerrado!")
                break
            
menuadm()