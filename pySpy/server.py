#! /usr/bin/python3
import socket
import sys
import os
from progress.spinner import Spinner
import webbrowser
def server():
    IP = "127.0.0.1"
    PORT = 2020
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((IP, PORT))
        s.listen(5)
        return s
    except:
        return False
try: 
    directory = sys.argv[1]
except:
    print("[!!] ./server.py")
    print("[!!] TO SAVE ./server.py directory")
    directory = None

if __name__ == "__main__":
    s = server()
    if(type(s) == bool and s == False):
        print("[-] was not listening")
    else:
        print("[!] Server started")
        client, addr = s.accept()
        print("[+] Connection open with " + addr[0])
        contador = 0
        spinner = Spinner("Download status: ")
        webbrowser.open_new_tab("player.html")
        while(1):
            contador = contador + 1
            pacote = client.recv(9999999)
            if not pacote: 
                print("[-] Connection closed")
                break
            if(directory != None):
                if(not os.path.isdir(directory)): os.mkdir(directory)
                f = open(directory+"/captura"+str(contador)+".jpg", "wb")
                f.write(pacote)
                f.close()
            
            player = open("player.jpg", "wb")
            player.write(pacote)
            player.close()
            spinner.next()
        spinner.finish()
        s.close()

