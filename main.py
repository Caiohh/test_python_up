import json 

with open("assets/db/mercado_livre.json", encoding='utf-8') as mercadoLivre_json:
    dados = json.load(mercadoLivre_json)


print(dados) 