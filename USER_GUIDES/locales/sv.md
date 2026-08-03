# CLARYEL RemoteOps — installation och privat konfiguration

RemoteOps hanterar din egen Windows-, Ubuntu/Linux- eller macOS-dator genom den AI-chatt du väljer.

## 1. Installera

- [Windows-installation](../../installers/install-windows.ps1)
- [macOS-installation](../../installers/install-macos.sh)
- [Ubuntu-installation](../../installers/install-ubuntu.sh)

Kör den nedladdade filen. RemoteOps installeras i din användarprofil, skapar en privat lokal arbetsyta och stänger inte av operativsystemets säkerhet.

## 2. Skapa ditt personliga Private-arkiv

Installera GitHub CLI, kör `gh auth login` och därefter kommandot som visas av installationen:

```text
remoteops connect --path DIN-PRIVATA-SOKVAG --create-private remoteops-min-dator
```

Arkivet skapas i ditt GitHub-konto med synlighet `Private`. RemoteOps gör det inte offentligt och lägger inte till samarbetspartner.

Private betyder dolt för allmänheten. Du, personer eller appar som du uttryckligen godkänner och GitHub som tjänsteoperatör kan fortfarande ha åtkomst. Skydda kontot med passkey eller tvåfaktorsautentisering.

Lagra aldrig lösenord, token, nycklar, återställningskoder, personliga filer, chattar, råa loggar, databaser eller säkerhetskopior i Git.

## 3. Kontrollera integriteten

```text
remoteops privacy-check --path DIN-PRIVATA-SOKVAG
```

Fortsätt endast om resultatet visar `"ok": true`, `"visibility": "PRIVATE"` och inga fynd.

## 4. Anslut ChatGPT

1. Öppna **ChatGPT > Inställningar > Apps > GitHub**.
2. Välj **Endast valda arkiv**.
3. Välj bara `remoteops-min-dator`.
4. Granska behörigheterna före godkännande.
5. Granska **Inställningar > Datakontroller > Förbättra modellen för alla**.
6. Klistra aldrig in hemligheter eller personliga filer i chatten.

GitHub-appens tillgänglighet och skrivrättigheter varierar med ChatGPT-plan och läge. En skrivskyddad anslutning kan inte tillämpa ändringar.

## Kommunikationsgräns

RemoteOps kontaktar GitHub endast när du ansluter eller synkroniserar ditt privata arkiv, ChatGPT endast när du väljer att använda det och paketkällor endast för godkända programåtgärder. Installationerna lägger inte till reklam eller extern analys.

Detaljerade guider: [privat arkiv](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [integritet och nätverk](../../docs/PRIVACY_AND_NETWORK.md).
