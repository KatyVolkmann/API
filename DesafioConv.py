import requests as request
import json as conversorJson


resposta = request.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL")

dolarReal = conversorJson.loads(resposta.content)

valorDolar = float(dolarReal["USDBRL"]["bid"])
print(valorDolar)

class Cambio():
    def comprarDolar(self):
        valor = float(input("Quantos dolares você precisa comprar?"))
        converter = valor * valorDolar
        print ("Para comprar $ ", valor, "você precisará de R$ ", converter)

    def venderDolar(self):
        valor = float(input("Quantos dolares você deseja vender?"))
        converter = valor / valorDolar
        print ("A sua venda de $ ", valor, "renderá R$ ", converter)
        
cambio = Cambio()
    
def menuadm():
    while True:
        match int(input("1- Comprar Dolar\n2- Vender Dolar\n3- Sair")):
            case 1:
                cambio.comprarDolar()
            case 2: 
                cambio.venderDolar()
            case 3:
                print("Menu Câmbio encerrado!")
                break
            
menuadm()
