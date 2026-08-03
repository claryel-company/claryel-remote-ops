# CLARYEL RemoteOps — installazione e configurazione privata

RemoteOps gestisce il tuo computer Windows, Ubuntu/Linux o macOS tramite una chat IA scelta da te.

## 1. Installa

- [Programma di installazione Windows](../../installers/install-windows.ps1)
- [Programma di installazione macOS](../../installers/install-macos.sh)
- [Programma di installazione Ubuntu](../../installers/install-ubuntu.sh)

Esegui il file scaricato. RemoteOps viene installato nel tuo profilo utente, crea uno spazio locale privato e non disattiva le protezioni del sistema operativo.

## 2. Crea il tuo repository personale Private

Installa GitHub CLI, esegui `gh auth login` e poi il comando mostrato dall’installer:

```text
remoteops connect --path PERCORSO-PRIVATO --create-private remoteops-mio-computer
```

Il repository viene creato nel tuo account GitHub con visibilità `Private`. RemoteOps non lo rende pubblico e non aggiunge collaboratori.

Private significa nascosto al pubblico. Possono comunque accedervi tu, persone o applicazioni autorizzate da te e GitHub come gestore del servizio. Proteggi l’account con passkey o autenticazione a due fattori.

Non inserire mai in Git password, token, chiavi, codici di recupero, file personali, chat, log grezzi, database o backup.

## 3. Verifica la privacy

```text
remoteops privacy-check --path PERCORSO-PRIVATO
```

Continua solo se il risultato mostra `"ok": true`, `"visibility": "PRIVATE"` e nessuna segnalazione.

## 4. Collega ChatGPT

1. Apri **ChatGPT > Impostazioni > App > GitHub**.
2. Scegli **Solo repository selezionati**.
3. Seleziona soltanto `remoteops-mio-computer`.
4. Controlla i permessi prima di approvare.
5. Controlla **Impostazioni > Controlli dati > Migliora il modello per tutti**.
6. Non incollare mai segreti o file personali nella chat.

La disponibilità dell’app GitHub e la possibilità di scrittura dipendono dal piano e dalla modalità di ChatGPT. Una connessione in sola lettura non può applicare modifiche.

## Limite delle comunicazioni

RemoteOps contatta GitHub solo quando colleghi o sincronizzi il tuo repository privato, ChatGPT solo quando scegli di usarlo e le fonti dei pacchetti solo per operazioni software approvate. Gli installer non aggiungono pubblicità o analisi estranee.

Guide dettagliate: [repository privato](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [privacy e rete](../../docs/PRIVACY_AND_NETWORK.md).
