import json


def salva(table, dado):
    with open('D:\\opencvismo\\BenderBot\\eventos\\dados.json', 'r') as dadosJson:
        dados = json.load(dadosJson)
        if table in dados:
            dados[table].append(dado)
        else:
            dados[table] = []
            dados[table].append(dado)

    with open('D:\\opencvismo\\BenderBot\eventos\\dados.json', 'w+') as dadosJson:
        json.dump(dados, dadosJson, indent=4)


def getArquivos(table):
    with open('D:\\opencvismo\\BenderBot\eventos\\dados.json', 'r') as dadosJson:
        dados = json.load(dadosJson)
        return dados[table]
