#!/usr/bin/env python3
import os
import subprocess
import time
import json
import urllib.request
import shutil

def clear():
    os.system('clear')

def logo():
    print(r"""
███████╗████████╗██╗ ██████╗ ██████╗  ██████╗  ██████╗  ██████╗  ██████╗██╗  ██╗
██╔════╝╚══██╔══╝██║██╔═══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██║ ██╔╝
███████╗   ██║   ██║██║   ██║██████╔╝██║   ██║██║  ███╗██║  ███╗██║     █████╔╝ 
╚════██║   ██║   ██║██║   ██║██╔═══╝ ██║   ██║██║   ██║██║   ██║██║     ██╔═██╗ 
███████║   ██║   ██║╚██████╔╝██║     ╚██████╔╝╚██████╔╝╚██████╔╝╚██████╗██║  ██╗
╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝      ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝
""")

def modifica_file():
    print("Prego premere per scegliere e modificare:")
    print("1 - Modifica HTML (index.html)")
    print("2 - Modifica CSS (style.css)")
    print("3 - Modifica entrambi")
    print("4 - Continua senza modificare (⚠ ATTENZIONE)")
    scelta = input("Scelta: ")

    if scelta == "1":
        os.system("nano index.html")
    elif scelta == "2":
        os.system("nano style.css")
    elif scelta == "3":
        os.system("nano index.html")
        os.system("nano style.css")
    elif scelta == "4":
        conferma = input("\n⚠ ATTENZIONE: vuoi continuare senza modificare?\n1 = Sì, continua | 2 = No, torna indietro: ")
        if conferma != "1":
            modifica_file()

def registra_ngrok():
    print("\n--- IMPORTAZIONE CHIAVE NGROK ---")
    token = input("Inserisci la tua chiave Ngrok: ").strip()

    comando = f"ngrok config add-authtoken {token}"
    result = subprocess.run(comando.split(), capture_output=True, text=True)

    if result.returncode == 0:
        print("[✔] Chiave Ngrok registrata con successo.")
    else:
        print("[✘] Errore nella registrazione della chiave.")
        print(f"👉 Copia e incolla manualmente in un'altra finestra: {comando}")
        apri_terminale_con_comando(comando)
        input("✅ Premi [INVIO] qui dopo aver eseguito il comando nella nuova finestra...")

def apri_terminale_con_comando(cmd):
    if shutil.which("gnome-terminal"):
        subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"echo '{cmd}'; bash"])
    elif shutil.which("x-terminal-emulator"):
        subprocess.Popen(["x-terminal-emulator", "-e", f"bash -c '{cmd}; bash'"])
    else:
        print(f"[!] Impossibile aprire automaticamente un nuovo terminale. Comando: {cmd}")

def avvia_server_locale():
    print("\n🌀 Avvio server locale sulla porta 8080...")
    comando = "echo ⚠ ATTENZIONE: NON CHIUDERE QUESTA FINESTRA. SERVER HTTP IN ESECUZIONE SULLA PORTA 8080; python3 -m http.server 8080"
    apri_terminale_con_comando(comando)

def avvia_ngrok():
    print("🌍 Avvio ngrok su porta 8080...")
    apri_terminale_con_comando("ngrok http 8080")
    time.sleep(5)
    try:
        with urllib.request.urlopen("http://localhost:4040/api/tunnels") as response:
            data = json.load(response)
            url = data['tunnels'][0]['public_url']
            print("\n✅ Tutto pronto! Stigrock è online!")
            print("- File serviti: index.html, style.css")
            print("- Porta locale: 8080")
            print(f"- Link pubblico ngrok: {url}")
    except Exception as e:
        print("❌ Errore nel recuperare il link pubblico di ngrok.")
        print("➡ Assicurati che ngrok sia in esecuzione e riprova.")

def main():
    clear()
    logo()
    modifica_file()
    registra_ngrok()
    avvia_server_locale()
    avvia_ngrok()
    print("\n🎉 Finito! Vai nella finestra o apri il link per vedere il tuo progetto.")

if __name__ == "__main__":
    main()

