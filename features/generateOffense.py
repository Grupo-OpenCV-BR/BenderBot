import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def generateOffense():
    translator = Translator(service_urls=[
        'translate.google.com',
        'translate.google.com.br',
    ])

    responseRequest = requests.get(f'http://www.pangloss.com/seidel/Shaker/index.html')
    messageEnglish = BeautifulSoup(responseRequest.content,'html.parser').find('font')
    messageTranslated = translator.translate(messageEnglish.text, dest='pt')
    
    return(messageTranslated.text)
