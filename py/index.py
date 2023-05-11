import urllib.request
import json

# define a URL da API do Banco Central do Brasil
url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1?formato=json'

# realiza a requisição GET à URL da API
response = urllib.request.urlopen(url)

# converte o resultado da requisição para um objeto JSON
json_data = json.loads(response.read().decode())

# extrai o valor da cotação do dólar em relação ao real
cotacao_dolar = float(json_data[0]['valor'])

# solicita ao usuário o valor em dólares a ser convertido
valor_dolar = float(input("Digite o valor em dólares a ser convertido: "))

# realiza a conversão para reais
valor_real = valor_dolar * cotacao_dolar

# exibe o resultado na tela
print(f'Valor em reais: {valor_real:.2f}')