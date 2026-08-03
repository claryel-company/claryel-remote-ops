# CLARYEL RemoteOps — asennus ja yksityinen käyttöönotto

RemoteOps hallitsee omaa Windows-, Ubuntu/Linux- tai macOS-tietokonettasi valitsemasi AI-keskustelun kautta.

## 1. Asenna

- [Windows-asennusohjelma](../../installers/install-windows.ps1)
- [macOS-asennusohjelma](../../installers/install-macos.sh)
- [Ubuntu-asennusohjelma](../../installers/install-ubuntu.sh)

Suorita ladattu tiedosto. RemoteOps asentuu käyttäjäprofiiliisi, luo yksityisen paikallisen työtilan eikä poista käyttöjärjestelmän suojausta käytöstä.

## 2. Luo henkilökohtainen Private-tietovarasto

Asenna GitHub CLI, suorita `gh auth login` ja sen jälkeen asennusohjelman näyttämä komento:

```text
remoteops connect --path OMA-YKSITYINEN-POLKU --create-private remoteops-oma-tietokone
```

Tietovarasto luodaan GitHub-tilillesi näkyvyydellä `Private`. RemoteOps ei tee siitä julkista eikä lisää yhteistyökumppaneita.

Private tarkoittaa yleisöltä piilotettua. Sinä, erikseen hyväksymäsi henkilöt tai sovellukset sekä GitHub palvelun ylläpitäjänä voivat silti käyttää sitä. Suojaa tili passkey-avaimella tai kaksivaiheisella tunnistautumisella.

Älä koskaan tallenna Gitiin salasanoja, tokeneita, avaimia, palautuskoodeja, henkilökohtaisia tiedostoja, keskusteluja, raakalokeja, tietokantoja tai varmuuskopioita.

## 3. Tarkista yksityisyys

```text
remoteops privacy-check --path OMA-YKSITYINEN-POLKU
```

Jatka vain, jos tulos näyttää `"ok": true`, `"visibility": "PRIVATE"` eikä löydöksiä.

## 4. Yhdistä ChatGPT

1. Avaa **ChatGPT > Asetukset > Apps > GitHub**.
2. Valitse **Vain valitut tietovarastot**.
3. Valitse vain `remoteops-oma-tietokone`.
4. Tarkista oikeudet ennen hyväksymistä.
5. Tarkista **Asetukset > Tietojen hallinta > Paranna mallia kaikille**.
6. Älä koskaan liitä salaisuuksia tai henkilökohtaisia tiedostoja keskusteluun.

GitHub-sovelluksen saatavuus ja kirjoitusoikeus riippuvat ChatGPT-tilauksesta ja tilasta. Vain luku -yhteys ei voi tehdä muutoksia.

## Viestintäraja

RemoteOps ottaa yhteyden GitHubiin vain yhdistettäessä tai synkronoitaessa yksityistä tietovarastoa, ChatGPT:hen vain käyttäessäsi sitä ja pakettlähteisiin vain hyväksytyissä ohjelmisto-operaatioissa. Asennusohjelmat eivät lisää mainoksia tai ulkopuolista analytiikkaa.

Yksityiskohtaiset oppaat: [yksityinen tietovarasto](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [yksityisyys ja verkko](../../docs/PRIVACY_AND_NETWORK.md).
