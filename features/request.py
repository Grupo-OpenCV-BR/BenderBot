import threading

import requests


def DontStopmeNOW():
    threading.Timer(600000, DontStopmeNOW).start()
    requests.get('http://www.google.com')
    print("I did a request!")