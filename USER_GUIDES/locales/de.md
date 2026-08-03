# CLARYEL RemoteOps — Installation und private Einrichtung

RemoteOps verwaltet Ihren eigenen Windows-, Ubuntu/Linux- oder macOS-Computer über einen von Ihnen gewählten KI-Chat.

## 1. Installieren

- [Windows-Installer](../../installers/install-windows.ps1)
- [macOS-Installer](../../installers/install-macos.sh)
- [Ubuntu-Installer](../../installers/install-ubuntu.sh)

Starten Sie die heruntergeladene Datei. RemoteOps wird in Ihrem Benutzerprofil installiert, erstellt einen privaten lokalen Arbeitsbereich und deaktiviert keine Betriebssystem-Sicherheitsfunktionen.

## 2. Ihr persönliches Private-Repository erstellen

Installieren Sie GitHub CLI, führen Sie `gh auth login` aus und danach den vom Installer angezeigten Befehl:

```text
remoteops connect --path IHR-PRIVATER-PFAD --create-private remoteops-mein-computer
```

Das Repository wird in Ihrem GitHub-Konto mit Sichtbarkeit `Private` erstellt. RemoteOps macht es nicht öffentlich und fügt keine Mitwirkenden hinzu.

Private bedeutet vor der Öffentlichkeit verborgen. Zugriff haben weiterhin Sie, von Ihnen autorisierte Personen oder Anwendungen und GitHub als Dienstbetreiber. Schützen Sie das Konto mit Passkey oder Zwei-Faktor-Authentifizierung.

Speichern Sie niemals Passwörter, Token, Schlüssel, Wiederherstellungscodes, persönliche Dateien, Chats, Rohprotokolle, Datenbanken oder Backups in Git.

## 3. Privatsphäre prüfen

```text
remoteops privacy-check --path IHR-PRIVATER-PFAD
```

Fahren Sie nur fort, wenn `"ok": true`, `"visibility": "PRIVATE"` und keine Funde angezeigt werden.

## 4. ChatGPT verbinden

1. Öffnen Sie **ChatGPT > Einstellungen > Apps > GitHub**.
2. Wählen Sie **Nur ausgewählte Repositories**.
3. Wählen Sie ausschließlich `remoteops-mein-computer`.
4. Prüfen Sie alle Berechtigungen vor der Zustimmung.
5. Prüfen Sie **Einstellungen > Datenkontrollen > Das Modell für alle verbessern**.
6. Fügen Sie niemals Geheimnisse oder persönliche Dateien in den Chat ein.

Verfügbarkeit und Schreibzugriff der GitHub-App hängen vom ChatGPT-Tarif und Modus ab. Eine schreibgeschützte Verbindung kann keine Änderungen anwenden.

## Kommunikationsgrenze

RemoteOps kontaktiert GitHub nur beim Verbinden oder Synchronisieren Ihres privaten Repositories, ChatGPT nur bei Ihrer Nutzung und Paketquellen nur für genehmigte Softwarevorgänge. Die Installer enthalten keine Werbung oder fremde Analysefunktionen.

Ausführliche Anleitungen: [privates Repository](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [Datenschutz und Netzwerk](../../docs/PRIVACY_AND_NETWORK.md).
