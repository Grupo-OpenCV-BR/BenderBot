import json


def salva(mensagem, table, colum):
    with open('./dados.json', 'r') as dados:
        eventos = json.load(dados)
        if table in eventos:
            eventos[table].append({colum: mensagem})
        else:
            eventos[table] = []
            eventos[table].append({colum: mensagem})

    with open('./dados.json', 'w') as dados:
        json.dump(eventos, dados, indent=4)


def getArquivos(table):
    with open('./dados.json', 'r') as dados:
        dado = json.load(dados)
        return dado[table]
