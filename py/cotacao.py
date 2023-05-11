import urllib.request
import json

# faz a requisição para a API de cotação do Banco Central do Brasil
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1?formato=json"
response = urllib.request.urlopen(url).read()

# decodifica a resposta da API em formato JSON
data = json.loads(response)

# extrai a cotação do dólar da resposta da API
cotacao = data[0]['valor']
print(f'Cotação do dólar: {cotacao}')

# solicita ao usuário o valor em dólares a ser convertido
valor_dolar = float(input("Digite o valor em dólares a ser convertido: "))

# realiza a conversão para reais
valor_real = valor_dolar * float(cotacao)
print(f'Valor em reais: {valor_real}')