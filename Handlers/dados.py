import json


def salva(table, coluna, dado):
    with open('./dados.json', 'r') as dadosJson:
        dados = json.load(dadosJson)
        if table in dados:
            dados[table].append({coluna: dado})
        else:
            dados[table] = []
            dados[table].append({coluna: dado})

    with open('./dados.json', 'w') as dadosJson:
        json.dump(dados, dadosJson, indent=4)


def getArquivos(table):
    with open('./dados.json', 'r') as dadosJson:
        dados = json.load(dadosJson)
        return dados[table]
