import logging
import random

import requests


def generateOffense():
    try:

        jose = requests.get("https://raw.githubusercontent.com/Grupo-OpenCV-BR/shakespyriano/master/DataSet.txt")
        values = jose.content.splitlines()
        nums = [random.randint(1, len(values)) for i in range(len(values))][1]

        values[nums] = values[nums].decode(encoding="ISO-8859-1")
        return (values[nums])

    except Exception as error:
        logging.error(error)
        return ('Erro ao buscar frases')
