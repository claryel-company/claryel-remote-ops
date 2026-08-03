# CLARYEL RemoteOps — installatie en privéconfiguratie

RemoteOps beheert uw eigen Windows-, Ubuntu/Linux- of macOS-computer via de AI-chat die u kiest.

## 1. Installeren

- [Windows-installatieprogramma](../../installers/install-windows.ps1)
- [macOS-installatieprogramma](../../installers/install-macos.sh)
- [Ubuntu-installatieprogramma](../../installers/install-ubuntu.sh)

Voer het gedownloade bestand uit. RemoteOps wordt in uw gebruikersprofiel geïnstalleerd, maakt een privé lokale werkruimte en schakelt geen beveiliging van het besturingssysteem uit.

## 2. Uw persoonlijke Private-repository maken

Installeer GitHub CLI, voer `gh auth login` uit en daarna de opdracht van het installatieprogramma:

```text
remoteops connect --path UW-PRIVE-PAD --create-private remoteops-mijn-computer
```

De repository wordt in uw GitHub-account gemaakt met zichtbaarheid `Private`. RemoteOps maakt deze niet openbaar en voegt geen medewerkers toe.

Private betekent verborgen voor het publiek. U, door u gemachtigde personen of apps en GitHub als dienstverlener kunnen nog steeds toegang hebben. Beveilig het account met een passkey of tweefactorauthenticatie.

Sla nooit wachtwoorden, tokens, sleutels, herstelcodes, persoonlijke bestanden, chats, ruwe logboeken, databases of back-ups op in Git.

## 3. Privacy controleren

```text
remoteops privacy-check --path UW-PRIVE-PAD
```

Ga alleen verder wanneer `"ok": true`, `"visibility": "PRIVATE"` en geen bevindingen worden weergegeven.

## 4. ChatGPT koppelen

1. Open **ChatGPT > Instellingen > Apps > GitHub**.
2. Kies **Alleen geselecteerde repositories**.
3. Selecteer uitsluitend `remoteops-mijn-computer`.
4. Controleer de rechten vóór goedkeuring.
5. Controleer **Instellingen > Gegevensbeheer > Het model voor iedereen verbeteren**.
6. Plak nooit geheimen of persoonlijke bestanden in de chat.

Beschikbaarheid en schrijfrechten van de GitHub-app verschillen per ChatGPT-abonnement en modus. Een alleen-lezen verbinding kan geen wijzigingen toepassen.

## Communicatiegrens

RemoteOps benadert GitHub alleen bij koppelen of synchroniseren van uw privé-repository, ChatGPT alleen wanneer u het gebruikt en pakketbronnen alleen voor goedgekeurde softwarehandelingen. De installers voegen geen advertenties of externe analytics toe.

Gedetailleerde gidsen: [privé-repository](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [privacy en netwerk](../../docs/PRIVACY_AND_NETWORK.md).
