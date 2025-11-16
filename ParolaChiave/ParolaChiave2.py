import os
import sqlite3
import string
import socket

print(f"Inserisci una frase")


frase = str(input())
print(frase.encode().hex())
HOST = '127.0.0.1'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.sendall(frase.encode())

client_socket.close()
HOST = '127.0.0.2'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server in ascolto su {HOST}:{PORT}...")

conn, addr = server_socket.accept()
print(f"Connessione da {addr}")
frase2 = str
while True:
    data = conn.recv(1024)  # riceve fino a 1024 byte
    if not data:
        break
    print(f"Ricevuto: {data}")  
    print(data.hex())
    frase2 = (data.decode("utf-8"))             

print(frase2)
conn.close()
server_socket.close()

contenuto = str



if os.path.exists("PasswordSegretissima.txt"):
	print("Il file esiste")
	file = open("PasswordSegretissima.txt" ,"r",encoding = "utf-8")
	contenuto = file.read()
	
	print(frase + contenuto)
	print(frase + frase2)
	
	if {frase + contenuto} == {frase + frase2}:
		print("Messaggio corretto ")
	else:
		print("Messaggio corrotto " + contenuto)
else:
    print("Il file non esiste")
    print(os.getcwd())
    
