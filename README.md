# Disnake Bot Vorlage

Die aktuelle Vorlage ist eine Grundstruktur für einen Discord-Bot, der auf der disnake-Bibliothek basiert. Die Bot-Klasse enthält bereits eine Implementierung für die Initialisierung des Bots, das Laden von Erweiterungen und das Abrufen des Bot-Prefix aus einer Umgebungsvariable. Es ist auch ein Logger implementiert, um die Ausgabe des Bots zu protokollieren. Die README-Datei enthält eine kurze Anleitung zur Einrichtung des Bots und zur Verwendung der verfügbaren Funktionen.

## Installation

1. Laden Sie das Repository herunter.
2. Installieren Sie die Abhängigkeiten mit `pip install -r requirements.txt`.
3. Passe die `.env`-Datei an.

## Verwendung

1. Führen Sie `python main.py` aus, um den Bot zu starten.
2. Der Standardpräfix ist, wenn man den Bot pingt.

## Erweiterungen

Sie können neue Funktionen durch das Erstellen von Erweiterungen hinzufügen. Fügen Sie die Dateien in das Verzeichnis `extensions` ein, der Bot läd die Erweiterung beim nächsten Neustart.

## Fehlerbehebung

1. Stellen Sie sicher, dass alle Abhängigkeiten installiert sind.
2. Überprüfen Sie, ob alle erforderlichen Variablen in der `.env`-Datei vorhanden sind.
3. Überprüfen Sie die Log-Dateien im `logs`-Verzeichnis auf Fehlermeldungen.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der Datei `LICENSE`.