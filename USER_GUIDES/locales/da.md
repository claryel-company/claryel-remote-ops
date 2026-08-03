# CLARYEL RemoteOps — installation og privat opsætning

RemoteOps administrerer din egen Windows-, Ubuntu/Linux- eller macOS-computer gennem den AI-chat, du vælger.

## 1. Installer

- [Windows-installationsprogram](../../installers/install-windows.ps1)
- [macOS-installationsprogram](../../installers/install-macos.sh)
- [Ubuntu-installationsprogram](../../installers/install-ubuntu.sh)

Kør den downloadede fil. RemoteOps installeres i din brugerprofil, opretter et privat lokalt arbejdsområde og deaktiverer ikke operativsystemets sikkerhed.

## 2. Opret dit personlige Private-repository

Installer GitHub CLI, kør `gh auth login`, og kør derefter kommandoen fra installationsprogrammet:

```text
remoteops connect --path DIN-PRIVATE-STI --create-private remoteops-min-computer
```

Repositoryet oprettes i din GitHub-konto med synlighed `Private`. RemoteOps gør det ikke offentligt og tilføjer ikke samarbejdspartnere.

Private betyder skjult for offentligheden. Du, personer eller apps, du udtrykkeligt godkender, og GitHub som tjenesteoperatør kan stadig have adgang. Beskyt kontoen med passkey eller tofaktorgodkendelse.

Gem aldrig adgangskoder, tokens, nøgler, gendannelseskoder, personlige filer, chats, rå logfiler, databaser eller sikkerhedskopier i Git.

## 3. Kontrollér privatliv

```text
remoteops privacy-check --path DIN-PRIVATE-STI
```

Fortsæt kun, hvis resultatet viser `"ok": true`, `"visibility": "PRIVATE"` og ingen fund.

## 4. Forbind ChatGPT

1. Åbn **ChatGPT > Indstillinger > Apps > GitHub**.
2. Vælg **Kun valgte repositories**.
3. Vælg kun `remoteops-min-computer`.
4. Gennemgå tilladelserne før godkendelse.
5. Gennemgå **Indstillinger > Datakontroller > Forbedr modellen for alle**.
6. Indsæt aldrig hemmeligheder eller personlige filer i chatten.

GitHub-appens tilgængelighed og skriveadgang afhænger af ChatGPT-plan og tilstand. En skrivebeskyttet forbindelse kan ikke anvende ændringer.

## Kommunikationsgrænse

RemoteOps kontakter kun GitHub, når du forbinder eller synkroniserer dit private repository, ChatGPT kun når du bruger det, og pakkekilder kun ved godkendte softwarehandlinger. Installationsprogrammerne tilføjer ingen reklamer eller fremmed analyse.

Detaljerede vejledninger: [privat repository](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [privatliv og netværk](../../docs/PRIVACY_AND_NETWORK.md).
