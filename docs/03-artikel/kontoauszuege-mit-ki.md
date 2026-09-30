---
title: Ein Jahr Kontoauszüge — mit KI ausgewertet
slug: kontoauszuege-mit-ki
type: article
tags: [künstliche intelligenz, prompt, praxisbeispiel, datenschutz]
author: Digi-Stammtisch Team
updated: 2026-09-30
status: published
related: [prompt-engineering, welche-ki-soll-ich-nehmen, schwaechen-und-risiken-von-ki]
---

# Ein Jahr Kontoauszüge — mit KI ausgewertet

Beim Stammtisch am 29. September haben wir geübt, was eine KI bei einer echten Alltagsarbeit
leisten kann: **ein ganzes Jahr Kontoauszüge auswerten.** Wofür geht das Geld weg? Was hat der
Urlaub gekostet? Welche Verträge laufen? Und wann wird es auf dem Konto knapp?

Dabei kamen beide Sorgen aus unserem SWOT-Workshop wieder auf den Tisch: **„Kann ich das
überprüfen?“** und **„Meine Daten gebe ich nicht einfach so heraus.“** Dieser Artikel zeigt,
wie man mit beidem umgeht — und was wir beim Ausprobieren selbst gelernt haben.

!!! tip "Wenig Zeit?"
    Alle Unterlagen stehen unten bei [Zum Herunterladen](#zum-herunterladen). Wenn du es mit
    deinen eigenen Auszügen probieren willst, lies vorher
    [Deine echten Kontoauszüge](#deine-echten-kontoauszuge).

---

## Die Übungsdaten: Familie Beispiel

Damit niemand seine eigenen Kontoauszüge zeigen muss, haben wir mit **erfundenen Daten**
geübt. Familie Beispiel aus dem ebenso erfundenen Ort Musterhausen: Thomas arbeitet Vollzeit,
Sabine Teilzeit, Tochter Lena geht in die Grundschule und lernt Klavier. Die Familie zahlt ein
Haus ab, fährt im Sommer an den Gardasee und an Ostern nach Hamburg.

Die Datei sieht aus wie ein Export aus dem Online-Banking: **486 Buchungen** vom 1. Januar bis
30. Dezember 2025, mit Datum, Empfänger, Verwendungszweck, Betrag und Kontostand. Eine zweite
Datei enthält dieselben Buchungen mit einer zusätzlichen Spalte **Kategorie** — das ist die
Lösung zum Vergleichen.

Als Einstieg gab es eine kleine Geschichte: Sabine sieht Ende Januar **minus 226 Euro** auf dem
Konto, obwohl die Familie „nichts Großes gekauft“ hat. Beim Durchscrollen findet sie die
Jahresbeiträge für Versicherungen, Kfz-Steuer und Müll — alle im selben Monat. Sie will die KI
fragen, zögert dann aber: ihre echten Daten ins Internet? Und rechnet die KI überhaupt richtig?

---

## Die Prompts: acht Bausteine, immer gleich gegliedert

Alle Prompts folgen den acht Bausteinen aus unserem Artikel
[Vom einfachen Auftrag zum guten Prompt](prompt-engineering.md): **Rolle, Ziel, Material,
Aufgabe, Muss-Regeln, „Gut ist es, wenn …“, „Wenn etwas fehlt“, Ausgabe.** Die Überschriften
stehen in Großbuchstaben, damit man sie auf einen Blick wiederfindet.

So sieht einer davon aus:

```text
ROLLE
Du bist ein genauer Buchhalter.

ZIEL
Wir planen den Urlaub 2026 und wollen wissen, was der Urlaub 2025 wirklich gekostet hat —
nicht nur die Buchung, sondern alles.

MATERIAL
Nur die hochgeladene CSV-Datei.

AUFGABE
1. Suche alle Buchungen, die zum Sommerurlaub am Gardasee gehören: Anzahlung, Restzahlung,
   Maut, Tanken unterwegs und alle Zahlungen in Italien.
2. Suche getrennt davon alle Buchungen, die zum Kurzurlaub an Ostern gehören.

MUSS-REGELN
Nur Buchungen verwenden, die in der Datei stehen. Keine Schätzungen für Dinge, die nicht
gebucht sind (zum Beispiel bar bezahlte Ausgaben).

WENN ETWAS FEHLT
Wenn du bei einer Buchung nicht sicher bist, ob sie zum Urlaub gehört, liste sie
gesondert auf und sag, warum du unsicher bist.

AUSGABE
Zwei Listen (Sommer, Ostern) mit Datum | Empfänger | Betrag, darunter jeweils die Summe.
Zum Schluss ein Satz: Was sollten wir für einen ähnlichen Urlaub 2026 einplanen?
```

Insgesamt gibt es neun Prompts, vom Einfachen zum Anspruchsvollen:

| Nr. | Frage | Worauf es ankommt |
|:---|:---|:---|
| 0 | „Wofür geben wir unser Geld aus?“ | der bewusst schlechte Anfang |
| 1 | Hast du die Datei richtig gelesen? | **erst prüfen, dann rechnen** |
| 2 | Jede Buchung in eine von zwölf Kategorien | feste Regeln, damit es jedes Jahr gleich aussieht |
| 3 | Was hat der Urlaub gekostet? | nichts schätzen, was nicht gebucht ist |
| 4 | Welche Verträge laufen? | keine erfundenen Vergleichspreise |
| 5 | Was kostet uns das Haus? | **WHAT → SO WHAT**: nicht nur Zahlen, sondern was sie bedeuten |
| 6 | Was können wir von der Steuer absetzen? | ehrlich sagen, wie sicher man ist |
| 7 | Erst Fakten, dann Rat — 300 € mehr sparen | Analyst und Beraterin getrennt |
| Bonus | Wann wird es knapp? | Ursache finden, nicht nur den Tiefpunkt |

Alle Prompts zum Kopieren stehen im Handout (siehe [Downloads](#zum-herunterladen)).

---

## Was wir beim Probelauf gelernt haben

Bevor wir die Prompts am Stammtisch ausgegeben haben, haben wir jeden einzelnen **mit einer
KI getestet, die nichts vorher wusste** — sie bekam nur die Datei ohne Kategorien und den
Prompt-Text, genau wie ihr am Abend. Die Antworten haben wir mit der Lösungsdatei verglichen.

!!! note "Womit wir getestet haben"
    Den Probelauf haben wir mit **Claude** gemacht, nicht mit ChatGPT. Die Ergebnisse zeigen,
    ob ein Prompt klar genug ist. Wie sich eine andere KI im Einzelnen verhält, kann trotzdem
    abweichen.

**Sieben von neun Prompts haben auf Anhieb funktioniert.** Interessanter sind die anderen —
und ein paar Überraschungen.

### 1. Ohne Regeln sortiert jede KI anders

Beim Einsortieren in Kategorien stimmten die **Summen**, aber die **Zuordnung** wich von der
Lösung ab: Gehört die Drogerie zu „Lebensmittel“ oder zu „Einkaufen“? Ist Netflix ein Vertrag
oder Freizeit? Der Prompt hatte dafür keine Regel — also hat die KI selbst entschieden. Das
war nicht falsch, aber im nächsten Jahr sähe es wieder anders aus.

Die KI hat das übrigens selbst gemerkt und alle Zweifelsfälle sauber auf die Liste „unsicher“
gesetzt. **Wir haben daraufhin für jede der zwölf Kategorien aufgeschrieben, was dazugehört.**

!!! tip "Regel"
    Wenn du willst, dass ein Ergebnis **jedes Mal gleich** aussieht, musst du jede
    Entscheidung vorgeben, die die KI sonst selbst trifft.

### 2. „Wie in Prompt 2“ versteht die KI nicht

Ein Prompt sagte „Kategorien wie in Prompt 2“. In einem neuen Chat kennt die KI Prompt 2
aber gar nicht — sie hat es offen gesagt und eigene Kategorien erfunden. **Jeder Prompt muss
für sich allein verständlich sein.** Was er braucht, gehört hinein.

### 3. Auch eine sehr gute Antwort kann sich verzählen

Die Antwort zu den Verträgen war inhaltlich hervorragend — und sprach nebenbei von
„480 Buchungen“, obwohl es eine weniger waren. Kein Drama, aber genau der Grund für die
Kontrollfrage nach jeder Antwort: **„Wie viele Buchungen hast du berücksichtigt?“**

### 4. „Nicht schätzen“ wirkt

Wo der Prompt es verlangt hat, hat die KI **nichts erfunden**: Den Zinsanteil im Kredit hat sie
nicht geschätzt, weil er nicht in der Datei steht. Bei den Handwerkerrechnungen für die Steuer
hat sie gesagt, dass nur der Arbeitslohn zählt und der nur auf der Rechnung steht. Und jede
Steuerfrage bekam die Angabe „sicher / wahrscheinlich / unsicher“, oft mit „bitte bei der
Steuerberatung nachfragen“. Genau dieser Satz im Prompt macht den Unterschied.

### 5. Die KI hat unsere Übungsdaten korrigiert

Die schönste Überraschung: Bei der Urlaubsfrage hat die KI bemerkt, dass während des
Gardasee-Urlaubs **zu Hause in Musterhausen eingekauft und getankt** wurde — „vielleicht ist
jemand zu Hause geblieben?“ — und dass die **Maut für die Rückfahrt fehlt**. Das waren Fehler
in unseren erfundenen Daten. Wir haben sie korrigiert.

Das zeigt, wozu so eine Auswertung auch gut ist: **Ungereimtheiten finden.** Bei echten Daten
wäre das vielleicht eine doppelte Abbuchung oder ein vergessenes Abo.

### 6. Die beste Antwort kam, als die KI urteilen durfte

Bei der Frage „Wie können wir 300 Euro im Monat mehr sparen?“ hat die KI-Beraterin nicht
einfach Posten gekürzt. Sie hat zuerst gerechnet, dass im Überschuss des Jahres Weihnachtsgeld
und Steuererstattung stecken und aus dem laufenden Einkommen nur etwa 94 Euro im Monat übrig
bleiben. Dann hat sie drei Vorschläge gemacht, **Rückfragen gestellt** („Wofür geht das Bargeld
weg?“) und ehrlich gesagt, dass es ganz ohne Verzicht nicht geht.

Das ist **WHAT → SO WHAT** in Reinform — und der Grund, warum wir Fakten sammeln und Urteilen in
zwei getrennte Schritte teilen.

---

## Wie der Abend lief

Der Abend lief wie geplant: Geschichte, Datei hochladen, Prompt für Prompt — und nach jeder
Antwort gemeinsam prüfen. Und es kam der Einwand, der bei solchen Übungen fast immer kommt:
**„Das ist nicht genau genug.“**

Der Einwand ist berechtigt — und er zeigt genau, wo die Grenze liegt. Die KI kann nur mit dem
arbeiten, was im Kontoauszug steht. Und da steht oft wenig: „AMAZON EU S.A R.L., Bestellung
302-…“ oder „PayPal“ sagt nichts darüber, **was** gekauft wurde. Bar bezahlte Ausgaben fehlen
ganz.

Die Antwort darauf ist dieselbe wie bei der Theaterstücksuche: **die Materialbasis erweitern.**
Wer genauer werden will, gibt der KI weitere Unterlagen dazu, zum Beispiel:

- die **Zahlungsliste aus PayPal** — dort steht, bei wem wirklich bezahlt wurde,
- die **Bestellübersicht aus dem Amazon-Konto** — dort steht, was gekauft wurde,
- **Rechnungen und Abrechnungen** — etwa die Jahresabrechnung der Stadtwerke oder die
  Kreditbescheinigung mit dem Zinsanteil.

Im Prompt gehört das unter **MATERIAL**, zum Beispiel: *„Zusätzlich zur Kontoauszug-Datei
liegt die PayPal-Zahlungsliste 2025 bei. Ordne PayPal-Buchungen im Kontoauszug über Datum und
Betrag der passenden Zahlung in der PayPal-Liste zu.“* So wird aus „nicht genau genug“
Schritt für Schritt „genau genug“ — und das ist wieder genau der Weg aus unserem
[Prompt-Artikel](prompt-engineering.md): nicht den perfekten Prompt suchen, sondern die
nächste Schwäche beseitigen.

!!! warning "Mehr Material heißt auch: mehr Daten"
    Jede zusätzliche Liste verrät noch mehr über dich. Für echte Daten gilt hier doppelt:
    schwärzen oder den Weg über ein eigenes Programm gehen (siehe unten).

---

## Deine echten Kontoauszüge

!!! warning "Echte Kontoauszüge nie ungeschwärzt in einen KI-Dienst laden"
    Ein Kontoauszug verrät sehr viel: Arbeitgeber, Gehalt, Kredit, Versicherungen, Arztbesuche,
    wo du einkaufst und wann du im Urlaub bist. Wenn du eine KI im Internet nutzt, **entferne
    vorher Namen, IBAN, Kunden- und Vertragsnummern** — oder nutze den zweiten Weg unten.

=== "Für Einsteiger"

    **Weg 1 — Schwärzen und dann die KI fragen.**
    Lade den Auszug aus dem Online-Banking als CSV-Datei herunter und öffne ihn in einer
    Tabellenkalkulation (Excel, Numbers, LibreOffice). Lösche die Spalten mit IBAN und Namen,
    ersetze Vertrags- und Kundennummern im Verwendungszweck durch „xxx“. Speichere die Datei
    und lade erst diese Fassung hoch.

    Starte dann mit **Prompt 1** und prüfe das Ergebnis. Stimmt die Probe nicht, lohnen sich
    die anderen Fragen noch nicht.

=== "Für Fortgeschrittene"

    **Weg 2 — Die KI schreibt das Programm, die Daten bleiben bei dir.**
    Du kannst die KI bitten, **ein Programm zu schreiben**, das deine Frage beantwortet —
    statt ihr die Daten zu geben. Das Programm läuft dann nur auf deinem Rechner.

    Für die Frage „Wann wird es knapp?“ haben wir das gemacht. Das Programm
    `wann_wird_es_knapp.py` braucht nur Python 3 und kein Internet:

    ```text
    python3 wann_wird_es_knapp.py Kontoauszug.csv
    ```

    (Unter Windows oft `python` statt `python3`.) Es macht zuerst die Probe, findet dann den
    tiefsten Kontostand, listet die großen Ausgaben seit dem letzten Hochstand und markiert,
    welche **regelmäßig** sind und welche **selten** — also die Jahresbeiträge, die man
    einplanen kann. Dazu gibt es den niedrigsten Stand je Monat als kleines Balkendiagramm.

    Mit den Übungsdaten findet es den Tiefpunkt von −226,06 € am 27. Januar und als Ursache
    vier Jahresbeiträge über zusammen 1.738,30 €.

---

## Nach jeder Antwort: prüfen!

Diese Fragen passen immer:

- „Wie viele Buchungen hast du berücksichtigt?“
- „Zeig mir die fünf größten Posten dieser Summe.“
- „Wo warst du unsicher?“
- „Woher weißt du das? Steht das in der Datei?“

Und dann die Frage aus unserem Prompt-Artikel: **„Welche Schwäche der letzten Antwort will ich
als Nächstes beseitigen?“**

---

## Zum Herunterladen

Alle Daten sind **erfunden** und dürfen frei zum Üben verwendet werden.

| Datei | Wofür |
|:---|:---|
| [Alles zusammen (ZIP)](static/kontoauszuege/kontoauszuege-komplett.zip) | alle Dateien unten in einem Paket |
| [Handout mit allen Prompts (PDF)](static/kontoauszuege/Prompts-Kontoauszuege.pdf) | zum Ausdrucken, 9 Seiten A4 |
| [Alle Prompts als Text](static/kontoauszuege/Prompts-Kontoauszuege.txt) | zum Kopieren in den Chat |
| [Kontoauszug 2025 (CSV)](static/kontoauszuege/Kontoauszug_Familie-Beispiel_2025.csv) | diese Datei in die KI laden |
| [Kontoauszug mit Lösung (CSV)](static/kontoauszuege/Kontoauszug_Familie-Beispiel_2025_mit-Kategorien.csv) | dieselben Buchungen mit Kategorie — zum Vergleichen |
| [Programm „Wann wird es knapp?“ (Python)](static/kontoauszuege/wann_wird_es_knapp.py) | Auswertung ohne KI, für echte Daten |
| [Geschichte „Minus im Januar“ (HTML)](static/kontoauszuege/Story-Familie-Beispiel.html) | Einstieg zum Vorlesen oder Zeigen |

!!! tip "CSV-Dateien öffnen"
    Ein Doppelklick öffnet die CSV-Dateien in der Tabellenkalkulation. Falls alles in einer
    Spalte landet: beim Öffnen **Semikolon** als Trennzeichen wählen.

---

## Weiterführend

- [Vom einfachen Auftrag zum guten Prompt](prompt-engineering.md) — die acht Bausteine
- [Welche KI soll ich nehmen?](welche-ki-soll-ich-nehmen.md) — auch zum Thema Datenschutz
- [Schwächen und Risiken von KI](schwaechen-und-risiken-von-ki.md)
