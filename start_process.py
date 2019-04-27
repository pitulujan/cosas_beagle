import time 
import requests
import threading

def start_loop():
    not_started=True
    while not_started:
        try:
            r=requests.get('http://192.168.0.18/')
            print("CACA")
            if r.status_code==200:
                not_started=False
        except:
            time.sleep(2)

thread = threading.Thread(target=start_loop)
thread.start()
