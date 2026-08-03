# CLARYEL RemoteOps — instalace a soukromé nastavení

RemoteOps spravuje váš vlastní počítač Windows, Ubuntu/Linux nebo macOS prostřednictvím vámi zvoleného AI chatu.

## 1. Instalace

- [Instalátor Windows](../../installers/install-windows.ps1)
- [Instalátor macOS](../../installers/install-macos.sh)
- [Instalátor Ubuntu](../../installers/install-ubuntu.sh)

Spusťte stažený soubor. RemoteOps se nainstaluje do vašeho uživatelského profilu, vytvoří soukromý místní pracovní prostor a nevypne ochrany operačního systému.

## 2. Vytvořte osobní repozitář Private

Nainstalujte GitHub CLI, spusťte `gh auth login` a potom příkaz zobrazený instalátorem:

```text
remoteops connect --path VASE-SOUKROMA-CESTA --create-private remoteops-muj-pocitac
```

Repozitář vznikne ve vašem účtu GitHub s viditelností `Private`. RemoteOps jej nezveřejní ani nepřidá spolupracovníky.

Private znamená skrytý před veřejností. Přístup stále máte vy, osoby nebo aplikace, které výslovně povolíte, a GitHub jako provozovatel služby. Chraňte účet přístupovým klíčem nebo dvoufaktorovým ověřením.

Do Git nikdy neukládejte hesla, tokeny, klíče, obnovovací kódy, osobní soubory, chaty, surové protokoly, databáze ani zálohy.

## 3. Ověřte soukromí

```text
remoteops privacy-check --path VASE-SOUKROMA-CESTA
```

Pokračujte jen pokud výsledek ukáže `"ok": true`, `"visibility": "PRIVATE"` a žádné nálezy.

## 4. Připojte ChatGPT

1. Otevřete **ChatGPT > Nastavení > Apps > GitHub**.
2. Zvolte **Pouze vybrané repozitáře**.
3. Vyberte jen `remoteops-muj-pocitac`.
4. Před schválením zkontrolujte oprávnění.
5. Zkontrolujte **Nastavení > Ovládání dat > Zlepšovat model pro všechny**.
6. Do chatu nikdy nevkládejte tajné údaje ani osobní soubory.

Dostupnost aplikace GitHub a možnost zápisu závisí na tarifu a režimu ChatGPT. Připojení jen pro čtení nemůže použít změny.

## Hranice komunikace

RemoteOps kontaktuje GitHub pouze při připojení nebo synchronizaci soukromého repozitáře, ChatGPT pouze při vašem použití a zdroje balíčků pouze pro schválené operace. Instalátory nepřidávají reklamu ani cizí analytiku.

Podrobné návody: [soukromý repozitář](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [soukromí a síť](../../docs/PRIVACY_AND_NETWORK.md).
