# Stigrock

**Stigrock** è un progetto Python che avvia un server HTTP locale sulla porta 8080 e lo espone su internet tramite un tunnel sicuro di Ngrok. Questo permette di condividere facilmente un sito web o applicazione locale su un URL pubblico temporaneo.

---

## Funzionalità principali

- Server HTTP locale sulla porta 8080
- Tunnel pubblico sicuro con Ngrok
- Avvio separato di Ngrok e server HTTP in terminali diversi
- Inserimento della chiave authtoken Ngrok tramite input
- Visualizzazione dell’URL pubblico generato da Ngrok
- Servizio di file statici (es. index.html, style.css)

---

## Prerequisiti

- Python 3.8+ installato
- Ngrok account e authtoken (https://dashboard.ngrok.com/get-started/your-authtoken)
- Git (per clonare il repository)
- Sistema Linux/Windows/macOS

---

## Installazione e avvio

1. Clona il repository:

   ```bash
   git clone https://github.com/dnfhacktm/stigrock.git
   cd stigrock

    Crea e attiva un ambiente virtuale Python:

python3 -m venv stigrock-venv
source stigrock-venv/bin/activate  # Linux/macOS
.\stigrock-venv\Scripts\activate   # Windows

Installa le dipendenze:

pip install -r requirements.txt

Avvia il launcher:

    python3 stigrock_launcher.py

    Inserisci la tua chiave Ngrok quando richiesta.

    Accedi all’URL pubblico mostrato per visualizzare il sito.

Struttura dei file

    stigrock_launcher.py – script principale per avviare server e ngrok

    index.html – file HTML servito dal server

    style.css – file CSS per la pagina web

    requirements.txt – dipendenze Python

    .gitignore – file per ignorare cartelle/file indesiderati

    README.md – questa documentazione

Contribuire

Contributi, suggerimenti e segnalazioni di bug sono benvenuti!
Per favore apri una issue o una pull request.
Licenza

MIT License

Creato da dnfhacktm
