#!/usr/bin/env python3
"""
Wann wird es knapp? — Auswertung eines Kontoauszugs ohne KI.

Dieses Programm macht dasselbe wie der Bonus-Prompt „Wann wird es knapp?“,
aber komplett auf dem eigenen Rechner. Die Daten verlassen den Computer nicht:
Es gibt keine Internetverbindung, keine Cloud, kein Hochladen.

So benutzt du es
----------------
1. Den Kontoauszug bei deiner Bank als CSV-Datei herunterladen.
2. Im Terminal (Mac) bzw. in der Eingabeaufforderung (Windows) eingeben:

       python3 wann_wird_es_knapp.py Kontoauszug.csv

   (Unter Windows heißt der Befehl oft nur „python“ statt „python3“.)

   Das Programm schaut vom Tiefpunkt zurück bis zum letzten Hochstand, höchstens
   aber 45 Tage. Beides lässt sich ändern, ebenso ab welchem Betrag eine Ausgabe
   als „groß“ gilt (Standard: 150):

       python3 wann_wird_es_knapp.py Kontoauszug.csv --tage 30 --gross 200

Was die Datei enthalten muss
----------------------------
Eine Kopfzeile und je Buchung eine Zeile, getrennt durch Semikolon (;), mit
mindestens diesen Spalten (die Namen dürfen etwas abweichen, siehe SPALTEN unten):
    - Buchungstag   (z. B. 27.01.2025)
    - Betrag        (z. B. -638,60 — minus heißt Ausgabe)
    - Saldo         (Kontostand nach der Buchung)
    - Empfänger     (wer das Geld bekommt oder schickt)
Fehlt die Spalte Saldo, fragt das Programm nach dem Kontostand vor der ersten Buchung.

Benötigt nur Python 3 — keine zusätzlichen Pakete.
"""

import argparse
import csv
import sys
from datetime import datetime, timedelta

# Welche Spaltennamen verschiedene Banken benutzen. Erweitern, falls deine Bank
# anders heißt: einfach den Namen in die passende Liste schreiben (kleingeschrieben).
SPALTEN = {
    "datum": ["buchungstag", "buchungsdatum", "datum", "valuta", "wertstellung"],
    "betrag": ["betrag", "betrag (eur)", "umsatz", "betrag in eur"],
    "saldo": ["saldo", "kontostand", "saldo nach buchung"],
    "empfaenger": ["auftraggeber/empfaenger", "auftraggeber/empfänger", "empfänger",
                   "empfaenger", "name zahlungsbeteiligter", "beguenstigter/zahlungspflichtiger",
                   "begünstigter/zahlungspflichtiger"],
    "zweck": ["verwendungszweck", "buchungstext", "vorgang"],
}


MONATE = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August",
          "September", "Oktober", "November", "Dezember"]


def finde_spalte(kopfzeile, art):
    """Sucht in der Kopfzeile die Spalte für 'datum', 'betrag' usw."""
    namen = [k.strip().lower() for k in kopfzeile]
    for kandidat in SPALTEN[art]:
        if kandidat in namen:
            return namen.index(kandidat)
    return None


def als_zahl(text):
    """Macht aus '1.234,56' oder '-638,60' eine Zahl."""
    text = text.strip().replace("€", "").replace("EUR", "").replace(" ", "")
    if "," in text:
        text = text.replace(".", "").replace(",", ".")
    return float(text)


def euro(betrag):
    """Zahl schön als Euro-Betrag: 1234.5 -> '1.234,50 €'."""
    s = f"{betrag:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{s} €"


def lies_datei(pfad):
    """Liest die CSV-Datei und gibt eine Liste von Buchungen zurück."""
    # 'utf-8-sig' versteht auch Dateien mit unsichtbarem Startzeichen (Excel).
    for kodierung in ("utf-8-sig", "latin-1"):
        try:
            with open(pfad, encoding=kodierung, newline="") as f:
                zeilen = list(csv.reader(f, delimiter=";"))
            break
        except UnicodeDecodeError:
            continue

    # Manche Banken schreiben vor die Tabelle noch Kontoinfos: Kopfzeile suchen.
    for nr, zeile in enumerate(zeilen):
        if finde_spalte(zeile, "datum") is not None and finde_spalte(zeile, "betrag") is not None:
            kopf, daten = zeile, zeilen[nr + 1:]
            break
    else:
        sys.exit("Keine Kopfzeile mit Datum und Betrag gefunden. Ist das eine Kontoauszug-CSV "
                 "mit Semikolon als Trennzeichen?")

    sp = {art: finde_spalte(kopf, art) for art in SPALTEN}
    buchungen = []
    for zeile in daten:
        if len(zeile) <= max(i for i in (sp["datum"], sp["betrag"]) if i is not None):
            continue  # leere oder abgeschnittene Zeile
        try:
            b = {
                "datum": datetime.strptime(zeile[sp["datum"]].strip(), "%d.%m.%Y").date(),
                "betrag": als_zahl(zeile[sp["betrag"]]),
                "saldo": als_zahl(zeile[sp["saldo"]]) if sp["saldo"] is not None else None,
                "empfaenger": zeile[sp["empfaenger"]].strip() if sp["empfaenger"] is not None else "",
                "zweck": zeile[sp["zweck"]].strip() if sp["zweck"] is not None else "",
            }
        except ValueError:
            continue  # z. B. Summenzeile am Ende
        buchungen.append(b)

    if not buchungen:
        sys.exit("Keine Buchungen gefunden.")

    # Die Reihenfolge der Datei bleibt erhalten, falls sie schon chronologisch ist,
    # damit der laufende Saldo stimmt. Absteigende Dateien (neueste oben) drehen wir um.
    if buchungen[0]["datum"] > buchungen[-1]["datum"]:
        buchungen.reverse()

    # Kein Saldo in der Datei? Dann selbst ausrechnen.
    if buchungen[0]["saldo"] is None:
        start = als_zahl(input("Die Datei hat keinen Kontostand. Wie hoch war er vor der "
                               "ersten Buchung (z. B. 1234,56)? "))
        for b in buchungen:
            start += b["betrag"]
            b["saldo"] = round(start, 2)
    return buchungen


def auswerten(buchungen, tage, gross):
    erste, letzte = buchungen[0], buchungen[-1]
    print()
    print("=" * 64)
    print(" WANN WIRD ES KNAPP?")
    print("=" * 64)
    print(f"Zeitraum:   {erste['datum']:%d.%m.%Y} bis {letzte['datum']:%d.%m.%Y}")
    print(f"Buchungen:  {len(buchungen)}")
    anfang = erste["saldo"] - erste["betrag"]
    print(f"Kontostand: am Anfang {euro(anfang)}, am Ende {euro(letzte['saldo'])}")

    # Probe: Stimmen Anfang + alle Beträge = Ende? (wie Prompt 1)
    probe = round(anfang + sum(b["betrag"] for b in buchungen), 2)
    if abs(probe - letzte["saldo"]) > 0.01:
        print(f"⚠️  Probe stimmt NICHT: gerechnet {euro(probe)}, laut Datei {euro(letzte['saldo'])}.")
        print("    Vielleicht fehlen Buchungen. Ergebnisse mit Vorsicht lesen.")
    else:
        print("Probe:      stimmt (Anfang + alle Buchungen = Ende)")

    # 1. Der Tiefpunkt
    tief = min(buchungen, key=lambda b: b["saldo"])
    print()
    print(f"1. TIEFSTER KONTOSTAND: {euro(tief['saldo'])} am {tief['datum']:%d.%m.%Y}")
    im_minus = sorted({b["datum"] for b in buchungen if b["saldo"] < 0})
    if im_minus:
        print(f"   ⚠️  An {len(im_minus)} Tag(en) war das Konto im Minus: "
              + ", ".join(f"{d:%d.%m.}" for d in im_minus[:10])
              + (" …" if len(im_minus) > 10 else ""))

    # 2. Was davor passiert ist: vom letzten Hochstand bis zum Tiefpunkt,
    #    höchstens --tage Tage zurück.
    grenze = tief["datum"] - timedelta(days=tage)
    idx_tief = buchungen.index(tief)
    fenster = [b for b in buchungen[:idx_tief + 1] if b["datum"] >= grenze]
    hoch_saldo, hoch_datum = anfang, erste["datum"]
    for b in fenster:
        vorher = b["saldo"] - b["betrag"]
        if vorher >= hoch_saldo or b is fenster[0]:
            hoch_saldo, hoch_datum = vorher, b["datum"]
    davor = [b for b in fenster if b["datum"] >= hoch_datum]
    ausgaben = sorted((b for b in davor if b["betrag"] <= -gross), key=lambda b: b["betrag"])

    # Kommt diese Ausgabe öfter vor? Verglichen wird Empfänger UND Betrag, denn derselbe
    # Empfänger (z. B. eine Versicherung) kann monatlich und einmal im Jahr abbuchen.
    ausgaben_je_empfaenger = {}
    for b in buchungen:
        if b["betrag"] < 0:
            ausgaben_je_empfaenger.setdefault(b["empfaenger"], []).append(-b["betrag"])

    def rhythmus(b):
        betraege = ausgaben_je_empfaenger.get(b["empfaenger"], [])
        gleich = sum(1 for x in betraege if abs(x + b["betrag"]) <= 0.05 * abs(b["betrag"]))
        if gleich >= 3:
            return f"regelmäßig ({gleich}× ähnlicher Betrag)"
        if len({round(x) for x in betraege}) >= 6:
            return "Alltag (wechselnde Beträge)"
        return "SELTEN — einmalig/jährlich?"

    print()
    print(f"2. WAS DAVOR PASSIERT IST — seit dem letzten Hoch am {hoch_datum:%d.%m.}"
          f" ({euro(hoch_saldo)})")
    print(f"   Große Ausgaben ab {euro(gross)}:")
    if not ausgaben:
        print("   keine")
    for b in ausgaben:
        print(f"   {b['datum']:%d.%m.}  {euro(-b['betrag']):>12}  {b['empfaenger'][:28]:28}  "
              f"{b['zweck'][:28]:28}  {rhythmus(b)}")
    summe = -sum(b["betrag"] for b in ausgaben)
    selten = -sum(b["betrag"] for b in ausgaben if rhythmus(b).startswith("SELTEN"))
    print(f"   Zusammen: {euro(summe)}, davon selten/einmalig: {euro(selten)}")
    if selten:
        print("   → Die SELTENEN Posten sind die üblichen Verdächtigen: Jahresbeiträge, die alle")
        print("     auf einmal kommen. Sie lassen sich vorhersehen und einplanen.")

    # 3. Monatsübersicht: niedrigster Stand je Monat
    print()
    print("3. NIEDRIGSTER KONTOSTAND JE MONAT:")
    monate = {}
    for b in buchungen:
        m = b["datum"].strftime("%Y-%m")
        monate[m] = min(monate.get(m, b["saldo"]), b["saldo"])
    kleinster = min(monate.values())
    for m, wert in monate.items():
        balken = "█" * max(0, int((wert - kleinster) / max(1, (max(monate.values()) - kleinster)) * 30))
        warn = "  ⚠️" if wert < 0 else ""
        print(f"   {m}  {euro(wert):>13}  {balken}{warn}")

    # 4. Einschätzung — bewusst vorsichtig formuliert
    print()
    print("4. EINSCHÄTZUNG")
    tage_im_jahr = (letzte["datum"] - erste["datum"]).days + 1
    if tage_im_jahr < 330:
        print("   Die Datei umfasst weniger als ein Jahr. Ob der Engpass jedes Jahr")
        print("   wiederkommt, lässt sich daraus nicht sagen.")
    else:
        print(f"   Der Engpass liegt im {MONATE[tief['datum'].month - 1]}. Große Einmalzahlungen in dieser Zeit")
        print("   (Versicherungen, Steuern, Gebühren) kommen meist jedes Jahr zur selben Zeit.")
        print("   Ob das hier so ist, zeigt erst der Vergleich mit den Auszügen des Vorjahres.")
    if tief["saldo"] < 0:
        puffer = -tief["saldo"] + 500
        print(f"   Um nicht ins Minus zu rutschen, hätte ein Puffer von rund {euro(puffer)}")
        print("   gereicht (Fehlbetrag plus 500 € Sicherheit).")
    print()
    print("Hinweis: Das Programm rechnet nur mit den Buchungen in der Datei. Es weiß nichts")
    print("über Bargeld, andere Konten oder Verträge, die noch nicht abgebucht wurden.")
    print()


def main():
    parser = argparse.ArgumentParser(description="Wann wird es knapp? — Kontoauszug auswerten, ohne KI.")
    parser.add_argument("datei", help="CSV-Datei mit dem Kontoauszug")
    parser.add_argument("--tage", type=int, default=45,
                        help="höchstens so viele Tage vor dem Tiefpunkt zurückschauen (Standard 45)")
    parser.add_argument("--gross", type=float, default=150,
                        help="ab welchem Betrag eine Ausgabe groß ist (Standard 150)")
    args = parser.parse_args()
    auswerten(lies_datei(args.datei), args.tage, args.gross)


if __name__ == "__main__":
    main()
