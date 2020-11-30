import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import random


def generateOffense():
    # translator = Translator(service_urls=[
    #     'translate.google.com',
    #     'translate.google.com.br',
    # ])
    #
    # responseRequest = requests.get(f'http://www.pangloss.com/seidel/Shaker/index.html')
    # messageEnglish = BeautifulSoup(responseRequest.content,'html.parser').find('font')
    # messageTranslated = translator.translate(messageEnglish.text, dest='pt')

    jose = requests.get("https://raw.githubusercontent.com/Grupo-OpenCV-BR/shakespyriano/master/DataSet.txt")
    values = jose.content.splitlines()
    nums = [random.randint(1, len(values)) for i in range(len(values))][1]
    #
    # return(messageTranslated.text)
    # print("AOOOAOA")
    values[nums] = values[nums].decode(encoding="ISO-8859-1")
    return (values[nums])
