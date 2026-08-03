# CLARYEL RemoteOps — instalacja i prywatna konfiguracja

RemoteOps zarządza Twoim własnym komputerem z Windows, Ubuntu/Linux lub macOS przez wybrany przez Ciebie czat AI.

## 1. Instalacja

- [Instalator Windows](../../installers/install-windows.ps1)
- [Instalator macOS](../../installers/install-macos.sh)
- [Instalator Ubuntu](../../installers/install-ubuntu.sh)

Uruchom pobrany plik. RemoteOps instaluje się w profilu użytkownika, tworzy prywatny lokalny obszar roboczy i nie wyłącza zabezpieczeń systemu.

## 2. Utwórz osobiste repozytorium Private

Zainstaluj GitHub CLI, uruchom `gh auth login`, a następnie polecenie pokazane przez instalator:

```text
remoteops connect --path TWOJA-PRYWATNA-SCIEZKA --create-private remoteops-moj-komputer
```

Repozytorium powstaje na Twoim koncie GitHub z widocznością `Private`. RemoteOps nie upublicznia go i nie dodaje współpracowników.

Private oznacza ukryte przed publicznością. Nadal dostęp mają właściciel, osoby lub aplikacje wyraźnie przez niego upoważnione oraz GitHub jako operator usługi. Zabezpiecz konto kluczem dostępu lub uwierzytelnianiem dwuskładnikowym.

Nigdy nie zapisuj w Git haseł, tokenów, kluczy, kodów odzyskiwania, plików osobistych, rozmów, surowych logów, baz danych ani kopii zapasowych.

## 3. Sprawdź prywatność

```text
remoteops privacy-check --path TWOJA-PRYWATNA-SCIEZKA
```

Kontynuuj tylko wtedy, gdy wynik pokazuje `"ok": true`, `"visibility": "PRIVATE"` i brak znalezisk.

## 4. Połącz ChatGPT

1. Otwórz **ChatGPT > Ustawienia > Apps > GitHub**.
2. Wybierz **Tylko wybrane repozytoria**.
3. Wskaż wyłącznie `remoteops-moj-komputer`.
4. Sprawdź uprawnienia przed zatwierdzeniem.
5. Sprawdź **Ustawienia > Kontrola danych > Ulepszaj model dla wszystkich**.
6. Nigdy nie wklejaj sekretów ani plików osobistych do czatu.

Dostępność aplikacji GitHub i możliwość zapisu zależą od planu i trybu ChatGPT. Połączenie tylko do odczytu nie może stosować zmian.

## Granica komunikacji

RemoteOps kontaktuje GitHub tylko podczas łączenia lub synchronizacji prywatnego repozytorium, ChatGPT tylko gdy go używasz, a źródła pakietów tylko dla zatwierdzonych operacji. Instalatory nie dodają reklam ani obcej analityki.

Szczegółowe przewodniki: [prywatne repozytorium](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [prywatność i sieć](../../docs/PRIVACY_AND_NETWORK.md).
