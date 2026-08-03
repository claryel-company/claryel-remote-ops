# CLARYEL RemoteOps — instalare și configurare privată

RemoteOps administrează propriul computer Windows, Ubuntu/Linux sau macOS prin chatul AI ales de dvs.

## 1. Instalare

- [Instalator Windows](../../installers/install-windows.ps1)
- [Instalator macOS](../../installers/install-macos.sh)
- [Instalator Ubuntu](../../installers/install-ubuntu.sh)

Rulați fișierul descărcat. RemoteOps se instalează în profilul utilizatorului, creează un spațiu local privat și nu dezactivează securitatea sistemului de operare.

## 2. Creați depozitul personal Private

Instalați GitHub CLI, rulați `gh auth login`, apoi comanda afișată de instalator:

```text
remoteops connect --path CALEA-DVS-PRIVATA --create-private remoteops-computerul-meu
```

Depozitul este creat în contul dvs. GitHub cu vizibilitate `Private`. RemoteOps nu îl face public și nu adaugă colaboratori.

Private înseamnă ascuns publicului. Totuși, acces pot avea proprietarul, persoanele sau aplicațiile autorizate explicit și GitHub ca operator al serviciului. Protejați contul cu passkey sau autentificare în doi pași.

Nu salvați niciodată în Git parole, tokenuri, chei, coduri de recuperare, fișiere personale, conversații, jurnale brute, baze de date sau copii de siguranță.

## 3. Verificați confidențialitatea

```text
remoteops privacy-check --path CALEA-DVS-PRIVATA
```

Continuați numai când rezultatul arată `"ok": true`, `"visibility": "PRIVATE"` și nicio constatare.

## 4. Conectați ChatGPT

1. Deschideți **ChatGPT > Setări > Apps > GitHub**.
2. Alegeți **Numai depozitele selectate**.
3. Selectați doar `remoteops-computerul-meu`.
4. Verificați permisiunile înainte de aprobare.
5. Verificați **Setări > Controlul datelor > Îmbunătățește modelul pentru toți**.
6. Nu introduceți niciodată secrete sau fișiere personale în chat.

Disponibilitatea aplicației GitHub și dreptul de scriere depind de planul și modul ChatGPT. O conexiune doar pentru citire nu poate aplica modificări.

## Limita comunicațiilor

RemoteOps contactează GitHub numai când conectați sau sincronizați depozitul privat, ChatGPT numai când îl utilizați, iar sursele de pachete numai pentru operații aprobate. Instalatoarele nu adaugă reclame sau analiză externă.

Ghiduri detaliate: [depozit privat](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [confidențialitate și rețea](../../docs/PRIVACY_AND_NETWORK.md).
