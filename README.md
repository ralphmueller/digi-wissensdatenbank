# Digi-Stammtisch Wissensseite (Starter)

Ein leichtgewichtiges, schnelles Wissens-Wiki für unseren Stammtisch – gebaut mit **MkDocs + Material**.  
Zwei Zielgruppen je Seite: **Für Einsteiger** und **Für Fortgeschrittene** (über Tabs).

## Schnellstart

1. **Python einschalten** (optional, aber empfohlen):  
   ```bash
   python -m venv .venv && source .venv/bin/activate
   ```
2. **Pakete installieren**:  
   ```bash
   pip install mkdocs-material mkdocs-glightbox
   ```
3. **Lokal starten**:  
   ```bash
   mkdocs serve
   ```
   Dann im Browser öffnen: http://127.0.0.1:8000
4. **Deploy** (z. B. GitHub Pages):  
   - Repository auf GitHub erstellen
   - In den Settings → Pages → Build from GitHub Actions (oder `mkdocs gh-deploy` verwenden)

## Beitragen

- **Einfach**: über die Issue-Vorlagen im Tab **Issues** („Beitrag vorschlagen“, „Änderung melden“).
- **Direkt**: Markdown bearbeiten und Pull Request stellen. Details in `CONTRIBUTING.md`.

## Struktur

```
docs/
  01-glossar/
  02-anleitungen/
  03-artikel/
  99-intern/
```

## Lizenz

Sofern nichts anderes vermerkt ist, CC BY 4.0 für Inhalte, MIT für Code (anpassbar in `LICENSE`).
