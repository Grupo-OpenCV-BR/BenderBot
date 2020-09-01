import requests
import threading

def DontStopmeNOW():
    threading.Timer(600.0, DontStopmeNOW).start()
    requests.get('http://www.google.com')
    print("I did a request!")