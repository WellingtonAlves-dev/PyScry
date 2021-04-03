#! /usr/bin/python3
import pyautogui, socket
from time import sleep

def capturarTela():
    try:
        local = "test.jpg"
        screen = pyautogui.screenshot()
        screen.resize((300,300))
        screen.save(local)
        return local
    except Exception as e:
        return False

def connect():
    IP = "127.0.0.1"
    PORT = 2020
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    try:
        s.connect((IP, PORT))
        return s
    except Exception as e:
        return False

if(__name__ == "__main__"):
    s = connect()
    if(type(s) == bool and s == False):
        print("[-] Não foi possivel conectar!")
        sleep(1)
    else:
        while(True):
            img = capturarTela()
            if(type(img) == bool and img == False):
                print("[-] Não foi possivel capturar a tela")
            else:
                f = open(img, "rb")
                s.send(f.read())
                f.close()
                sleep(1)
