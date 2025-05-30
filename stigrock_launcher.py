#!/usr/bin/env python3

import os
import sys
import time
import socket
from pyngrok import ngrok
from threading import Thread

# Scritta iniziale
def print_ascii_banner():
    os.system("clear")
    print(r"""
███████╗████████╗██╗ ██████╗ ██████╗  ██████╗  ██████╗  ██████╗  ██████╗██╗  ██╗
██╔════╝╚══██╔══╝██║██╔═══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██║ ██╔╝
███████╗   ██║   ██║██║   ██║██████╔╝██║   ██║██║  ███╗██║  ███╗██║     █████╔╝ 
╚════██║   ██║   ██║██║   ██║██╔═══╝ ██║   ██║██║   ██║██║   ██║██║     ██╔═██╗ 
███████║   ██║   ██║╚██████╔╝██║     ╚██████╔╝╚██████╔╝╚██████╔╝╚██████╗██║  ██╗
╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝      ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝
""")

# Controlla se la porta è già in uso
def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

# Avvia server HTTP locale in un altro terminale
def start_http_server():
    os.system("xterm -e 'cd ~/stigrock && python3 -m http.server 8080' &")

# Avvia ngrok tunnel su porta 8080
def start_ngrok_tunnel():
    public_url = ngrok.connect(8080, bind_tls=True)
    print("✅ Tutto pronto! Stigrock è online!")
    print(f"🌐 URL pubblico: {public_url}")
    print("🔐 Non chiudere questa finestra finché il progetto è attivo.")
    print("📂 File serviti: index.html, style.css")
    print("📡 Porta locale: 8080")
    print("➡ Vai al link per visualizzare il tuo sito!")
    return public_url

# Main launcher
def main():
    print_ascii_banner()

    # Scelta modifica file
    print("Prego premere per scegliere e modificare:")
    print("1 - Modifica HTML (index.html)")
    print("2 - Modifica CSS (style.css)")
    print("3 - Modifica entrambi")
    print("4 - Continua senza modificare (⚠ ATTENZIONE)")
    choice = input("Scelta: ")

    if choice == "1":
        os.system("nano stigrock/index.html")
    elif choice == "2":
        os.system("nano stigrock/style.css")
    elif choice == "3":
        os.system("nano stigrock/index.html && nano stigrock/style.css")
    else:
        print("⚠ Continuando senza modifiche...")

    # Inserisci chiave Ngrok
    print("\n--- IMPORTAZIONE CHIAVE NGROK ---")
    token = input("Inserisci la tua chiave Ngrok (https://dashboard.ngrok.com/get-started/your-authtoken): ")
    ngrok.set_auth_token(token)

    # Controllo porta
    if is_port_in_use(8080):
        print("❌ ERRORE: La porta 8080 è già in uso. Chiudi il processo e riprova.")
        os.system("lsof -i :8080")
        sys.exit(1)

    print("\nAvvio server locale su porta 8080...")
    Thread(target=start_http_server).start()

    print("✅ Tunnel in creazione con Ngrok...\n")
    try:
        start_ngrok_tunnel()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🔴 Interruzione manuale. Chiusura...")
        ngrok.kill()

if __name__ == "__main__":
    main()
