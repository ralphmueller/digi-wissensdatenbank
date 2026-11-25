---
title: Fotos vom Handy auf den PC übertragen
slug: fotos-handy-auf-pc
type: howto
tags: [smartphone, fotos, whatsapp, windows, usb]
author: Digi-Stammtisch Team
updated: 2026-11-25
status: draft
related: [screenshot-android, datensicherung-android]
---

# Fotos vom Handy auf den PC übertragen

Eine Frage aus der Runde: „Wie bekomme ich meine Fotos und die Bilder aus WhatsApp vom Handy auf meinen PC?“
Der zuverlässigste Weg ist das **USB-Kabel**. Er funktioniert bei allen Android-Handys (Samsung, Huawei, Xiaomi,
Google Pixel …) und braucht weder Internet noch ein Konto.

=== "Für Einsteiger"
    **Du brauchst:** das Handy, den PC mit Windows und ein USB-Kabel, am besten das Original-Ladekabel.

    1. **Handy entsperren** und mit dem Kabel an den PC anschließen.
    2. Auf dem Handy erscheint eine Meldung wie „Gerät über USB laden“ oder „USB-Einstellungen“.
       Darauf tippen und **„Dateiübertragung“** bzw. **„Dateien übertragen“** wählen.
       Fragt das Handy „Zugriff auf Telefondaten erlauben?“, auf **Zulassen** tippen.
    3. Am PC den **Explorer** öffnen (Ordner-Symbol in der Taskleiste oder Tasten **Windows-Taste + E**).
    4. Links unter **„Dieser PC“** steht jetzt das Handy (z. B. „Galaxy A54“ oder „HUAWEI P30“).
       Doppelklick darauf, dann auf **„Interner Speicher“** bzw. „Interner gemeinsamer Speicher“.
    5. Den richtigen Ordner öffnen:

        | Was | Ordner auf dem Handy |
        |:--|:--|
        | Fotos der Kamera | `DCIM` → `Camera` |
        | Screenshots | `Pictures` → `Screenshots` (manchmal `DCIM` → `Screenshots`) |
        | Bilder aus WhatsApp | `Android` → `media` → `com.whatsapp` → `WhatsApp` → `Media` → `WhatsApp Images` |

    6. Die gewünschten Bilder markieren (alle: **Strg + A**), **kopieren** (**Strg + C**),
       am PC den Ordner **„Bilder“** öffnen und **einfügen** (**Strg + V**).
    7. Warten, bis das Kopieren fertig ist. Danach das Kabel abziehen.

    !!! tip "Kopieren, nicht verschieben"
        Erst kopieren und am PC nachsehen, ob alles angekommen ist. Löschen auf dem Handy erst danach,
        wenn überhaupt.

    !!! warning "Das Handy erscheint nicht am PC?"
        - Ist das Handy **entsperrt**? Gesperrt zeigt es keine Dateien.
        - Steht auf dem Handy wirklich **„Dateiübertragung“** und nicht nur „Laden“?
        - **Anderes Kabel** probieren. Viele billige Kabel können nur laden, aber keine Daten übertragen.
        - Einen anderen USB-Anschluss am PC nehmen.

    **Ohne Kabel, für wenige Bilder:** Das Bild in WhatsApp öffnen, auf **Teilen** tippen und per **E-Mail an Dich
    selbst** schicken. Am PC die Mail öffnen und den Anhang speichern.

=== "Für Fortgeschrittene"
    **Mit der Windows-App „Fotos“:** Handy wie oben anschließen, die App **Fotos** öffnen, oben rechts auf
    **Importieren** → **„Von einem verbundenen Gerät“**. Die App findet die Bilder selbst, auch neue seit dem
    letzten Import.

    **WhatsApp am PC:** Mit **WhatsApp für Windows** (Microsoft Store) oder **WhatsApp Web** im Browser
    (web.whatsapp.com) erscheinen die Chats am PC. Bild im Chat öffnen und über **Herunterladen** speichern.
    Das ist praktisch für einzelne Bilder, für viele ist das Kabel schneller.

    **WhatsApp-Bilder in der Galerie:** Ob WhatsApp-Bilder in der Galerie erscheinen, steuert in WhatsApp
    *Einstellungen → Chats → Medien-Sichtbarkeit*. Der Ordner auf dem Handy ist unabhängig davon vorhanden.
    Bei älteren WhatsApp-Versionen liegt er direkt unter `WhatsApp` → `Media` → `WhatsApp Images`.

    **Huawei:** Neuere Huawei-Handys haben keine Google-Dienste, Google Fotos fehlt also. Der Weg über das
    Kabel funktioniert genauso. Huawei bietet zusätzlich das PC-Programm **HiSuite** an.

    **iPhone:** Kabel anschließen, iPhone entsperren und **„Vertrauen“** bestätigen. Am PC die App **Fotos** →
    **Importieren**. Damit die Bilder als JPG ankommen statt im HEIC-Format: am iPhone
    *Einstellungen → Fotos → „Auf Mac oder PC übertragen“ → Automatisch*.

    **Mac:** Der Mac zeigt Android-Handys nicht von allein an. Dafür braucht es ein Zusatzprogramm
    (z. B. OpenMTP). Das iPhone erkennt die App **Fotos** am Mac direkt.
