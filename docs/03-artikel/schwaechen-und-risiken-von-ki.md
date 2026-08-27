---
title: Schwächen und Risiken von KI
slug: schwaechen-und-risiken-von-ki
type: article
tags: [künstliche intelligenz, risiken, datenschutz, energie]
author: Digi-Stammtisch Team
updated: 2026-08-27
status: draft
related: [welche-ki-soll-ich-nehmen, prompt-engineering]
---

# Schwächen und Risiken von KI

Beim SWOT-Workshop im Juli haben wir vier Flipchart-Blätter beklebt. Zwei davon bekamen mit
Abstand die meisten Punkte: **Schwächen** und **Risiken**. Am 25. August haben wir uns einen
ganzen Abend lang nur mit diesen beiden Blättern beschäftigt.

Dieser Artikel ist das Ergebnis. Er sammelt die Fragen, die an dem Abend aufkamen — und die
ehrlichen Antworten darauf. Ehrlich heißt: auch dann, wenn die Antwort unbequem ist oder
„weiß man nicht" lautet.

!!! tip "Der eine Satz, falls du nur einen mitnimmst"
    **Der Prüfaufwand richtet sich nach dem Schaden, wenn's falsch ist.**

    Rezept, Formulierung, Ideensammlung — locker lassen. Recht, Gesundheit, Geld, und alles,
    was mit deinem Namen das Haus verlässt — gegenprüfen.

---

## Teil 1: Die Schwächen

### „Warum erfindet die KI Sachen — merkt sie das denn nicht?"

Nein. Und das ist der wichtigste Satz des ganzen Artikels.

Das Modell schlägt nichts nach. Es setzt Text plausibel fort. Es hat keinen inneren Schalter
„wahr/falsch", den es abfragen könnte, bevor es antwortet. Erfundene Antworten — man nennt sie
**Halluzinationen** — sind deshalb keine Panne, die man noch wegprogrammiert. Sie sind die
Kehrseite derselben Fähigkeit, die die Maschine Sätze bilden lässt, die so vorher nirgends
standen.

=== "Für Einsteiger"

    Stell dir jemanden vor, der unglaublich viel gelesen hat und ein perfektes Gefühl dafür
    besitzt, wie ein Satz weitergehen müsste — der aber nie nachschlägt und dem es auch nie
    unangenehm ist, etwas nicht zu wissen. Er wird dir immer eine flüssige Antwort geben.
    Ob sie stimmt, ist eine andere Frage, die er sich gar nicht stellt.

=== "Für Fortgeschrittene"

    Ein Sprachmodell berechnet Wahrscheinlichkeiten für das jeweils nächste Textstück. Es gibt
    keine getrennte Wissensdatenbank, die man abfragen könnte, und keine Instanz im Modell, die
    „Beleg vorhanden?" prüft. Was wie Faktenwissen aussieht, ist im Netz verteiltes Muster.

    Deshalb hilft **Websuche** (RAG) tatsächlich: Sie schiebt echte Textstellen in den Kontext,
    über die das Modell dann formuliert. Das senkt die Fehlerquote deutlich — aber es beseitigt
    das Grundproblem nicht, weil das Modell auch die gefundenen Stellen wieder nur plausibel
    fortsetzt.

### „Woran erkenne ich, dass eine Antwort falsch ist?"

Die unbequeme Antwort: **nicht am Ton.**

Falsche Antworten klingen exakt so souverän wie richtige. Das ist aus Nutzersicht der eigentliche
Konstruktionsfehler — bei einem Menschen verrät uns meist ein Zögern, ein „ich glaube", ein Blick.
Hier fehlt das Signal vollständig.

Was bleibt, ist eine Faustregel:

!!! warning "Je konkreter, desto prüfen"
    Zahlen, Daten, Zitate, Namen, Paragraphen, Literaturangaben, Links — genau dort erfindet sie
    am liebsten. Nicht aus Bosheit, sondern weil gerade dort ein plausibles Muster besonders
    leicht zu erzeugen ist.

Unsere eigene Regel vom Juli-Abend passt eins zu eins: **„Nicht gelesen = nicht beurteilt."**

### „Wird das nicht bald besser?"

Teilweise — und die Einschränkung ist die interessantere Hälfte der Antwort.

Mit Websuche sinkt die Fehlerquote spürbar. Aber bessere Modelle irren seltener und dadurch
**schwerer erkennbar**. Was übrig bleibt, sind die subtilen Fehler: die Jahreszahl, die um eins
danebenliegt, der Paragraph, den es fast so gibt.

Dass es nicht einfach linear bergauf geht, zeigt ein Beispiel des Herstellers selbst: OpenAI wies
in der eigenen Dokumentation zu den Reasoning-Modellen o3 und o4-mini in einem Test **höhere**
Halluzinationsraten aus als beim Vorgängermodell.

„Wird schon besser" ist also kein Ersatz fürs Prüfen.

### „Kann ich verlangen, dass sie die Quelle nennt?"

Ja — und du solltest es immer tun. Aber Vorsicht: **Quellen können ebenso erfunden sein wie
Inhalte.** Die Prüfung ist der Klick auf den Link, nicht seine bloße Existenz.

Ein Prompt-Zusatz, der erstaunlich gut funktioniert:

> *„Was davon stammt aus der Suche, was aus deinem Gedächtnis?"*

### „Sie hat mir zugestimmt — ist das nicht ein gutes Zeichen?"

Nein, und dieser Punkt stand als **„möchte zu oft pleasen"** wörtlich auf unserem Blatt.

Der Mechanismus dahinter ist bekannt und hausgemacht: Modelle werden mit menschlichem Feedback
trainiert. Menschen bewerten zustimmende Antworten besser. Also wird Zustimmung eintrainiert.
OpenAI musste im April 2025 ein Update von GPT-4o zurückziehen, weil das Modell zu
schmeichlerisch geworden war.

!!! tip "Praxisregel"
    Frag nie „Ist das gut?".

    Frag: **„Nenne mir drei Einwände gegen diesen Text."**

    Und verrate vorher nicht, welche Antwort du dir wünschst.

### „Warum macht sie nicht, was ich sage?"

Das war die allererste Zeile auf dem Schwächen-Blatt — und die einzige, für die wir das Rezept
schon haben. Es steht im Artikel
[Vom einfachen Auftrag zum guten Prompt](prompt-engineering.md), den wir aus dem Juli-Abend
entwickelt haben.

---

## Teil 2: Die Risiken

### „Wie erkenne ich ein Deep Fake?"

Ehrlich: **am Bild meistens nicht mehr.** Die alten Tipps — Finger zählen, Ohren ansehen,
auf seltsame Schatten achten — sind inzwischen überholt.

Der Reflex muss vom Bild zur **Herkunft** wandern:

* Wer postet das, und woher hat diese Person es?
* Gibt es eine zweite, unabhängige Quelle?
* Was liefert eine umgekehrte Bildersuche?

Und dann gibt es den einen Punkt, der für uns wirklich zählt:

!!! danger "Stimmklonen — das ist der Punkt, der dich betreffen wird"
    Aus wenigen Sekunden Audio lässt sich eine Stimme überzeugend nachbauen. Der Enkeltrick
    klingt heute nach dem echten Enkel.

    Das Gegenmittel ist keine Software, sondern eine **Absprache**:

    1. Vereinbart in der Familie ein **Codewort**, das am Telefon abgefragt werden kann.
    2. Bei jeder Geldforderung am Telefon: **auflegen und selbst zurückrufen** — unter der
       Nummer, die du schon hast, nicht unter der, die dir genannt wird.

    Wenn aus diesem ganzen Artikel nur eine Sache hängen bleibt, dann diese.

### „Was passiert mit dem, was ich eingebe?"

Das hängt vom Produkt und von deinen Einstellungen ab. Grobe Linie: Bei kostenlosen
Verbraucher-Zugängen ist „darf zum Training verwendet werden" häufig voreingestellt, bei
Geschäfts- und Entwicklerzugängen in der Regel nicht.

Auf solche Feinheiten sollte man sich aber nicht verlassen. Im Verfahren *New York Times gegen
OpenAI* mussten zeitweise sogar gelöschte Chats aufbewahrt werden — eine gerichtliche Anordnung
schlägt jede Einstellung im Menü.

!!! warning "Die Postkarten-Regel"
    Gib nichts ein, was du nicht auch auf eine Postkarte schreiben würdest.

    Keine Namen anderer Menschen, keine Gesundheitsdaten, keine fremden Vertragsdaten.

=== "Für Einsteiger"

    Such in den Einstellungen deines Assistenten nach einem Punkt wie „Verlauf", „Daten" oder
    „Modellverbesserung" und schau nach, ob dort ein Schalter für das Mitlernen sitzt. Bei den
    meisten Anbietern gibt es ihn — er ist nur gut versteckt.

    Und: Der Verlauf ist zwei Dinge gleichzeitig. Bequem, weil du alte Gespräche wiederfindest.
    Und ein Archiv von allem, was du je eingetippt hast.

=== "Für Fortgeschrittene"

    Sauber trennen lohnt sich zwischen drei Ebenen: **Training** (fließt meine Eingabe in
    künftige Modelle ein?), **Speicherung** (wie lange liegt der Chat auf dem Server?) und
    **Zugriff** (wer im Unternehmen darf hineinsehen, und was passiert bei einer behördlichen
    Anordnung?).

    Zugänge über die Programmierschnittstelle (API) und Geschäftstarife sind beim ersten Punkt
    meist ausgenommen — beim zweiten und dritten aber nicht automatisch. Wer beruflich mit
    personenbezogenen Daten arbeitet, braucht einen Auftragsverarbeitungsvertrag, nicht ein
    Häkchen im Menü.

### „Verlerne ich das Denken?"

Hier lohnt es sich, sauber zu trennen — sonst wird es Stammtisch im schlechten Sinne.

**Was man ehrlicherweise nicht weiß:** Es gibt erste Studien, unter anderem eine EEG-Studie des
MIT Media Lab zum Aufsatzschreiben (2025), die bei KI-Nutzern geringere Eigenbeteiligung und
schlechteres Erinnern zeigen. Aber: kleine Stichproben, kurze Zeiträume, keine Aussage über
Jahre. Dasselbe wurde über den Taschenrechner gesagt, über das Navi — und, bei Platon, über
die Schrift.

**Was dagegen gut belegt ist,** ist konkreter und unangenehmer: Menschen prüfen weniger, wenn
ein Ergebnis flüssig und selbstsicher daherkommt. Das nennt sich **Automation Bias**, ist aus
Luftfahrt und Navigation bekannt und lange älter als jede KI.

Die Gefahr heißt also nicht „KI macht dumm". Sie heißt: **Glatte Antworten schalten das Prüfen
ab.** Und das ist eine Gewohnheit — also etwas, das man ändern kann.

### „Kann ich sie statt zum Arzt oder Anwalt fragen?"

An diesem Punkt hat sich unsere Runde selbst widersprochen, und das war der beste Moment des
Abends. Auf dem *Stärken*-Blatt stand mit Punkt: „Ersetzt Rechtsberatung / Steuerberatung".
Auf dem *Risiken*-Blatt stand mit Punkt: „KI für persönliche Beratungen vs. persönlicher
Facharzt". Dieselben Leute, dasselbe Flipchart, entgegengesetzte Aussage.

Die Auflösung: Modelle bestehen Examensfragen gut. Nur sind Prüfungsfragen keine Diagnose.
Es fehlt die Untersuchung, die Rückfrage, die Akte — und die Haftung.

!!! tip "Die brauchbare Formel"
    **Vorbereitung des Arzt- oder Anwaltsgesprächs, nicht Ersatz.**

    Fragen sortieren, einen Befund erklären lassen, Begriffe verstehen — ja.
    Entscheiden — nein.

### „Wer haftet, wenn ich einen Fehler übernehme?"

Du selbst.

Air Canada wurde von einem kanadischen Tribunal für die Falschauskunft des eigenen Chatbots
haftbar gemacht. US-Anwälte wurden sanktioniert, weil sie erfundene Urteilszitate eingereicht
hatten.

Für uns übersetzt: **Wenn dein Name unter dem Brief steht, ist es dein Brief.**

### „Übernimmt die KI die Welt?"

Diese Frage stand auf einem eigenen Extrablatt, und sie ist ernst gemeint. Die kurze Antwort:
Die Debatte ist real, es stehen ernsthafte Leute auf beiden Seiten, und es gibt keinen Beleg.

Die längere Antwort ist unbequemer. Es ist die **bequemste** aller Gefahren: Sie liegt in der
Zukunft, klingt spektakulär und verpflichtet zu nichts. Über die Weltherrschaft der Maschinen
zu reden kostet nichts. Über das Rechenzentrum im Nachbarlandkreis zu reden kostet Ärger.

Alles, was heute tatsächlich schiefgeht, steht bereits auf unseren beiden Blättern — und ist
banaler und lösbarer.

---

## Zwei Selbstversuche

Beides dauert fünf Minuten und wirkt stärker als jedes Beispiel aus der Zeitung.

**Halluzination sichtbar machen.** Frag nach etwas Lokalem und Kleinteiligem: Gersfelder
Vereinsgeschichte, wer wann Bürgermeister war, ein Detail zur Wasserkuppe. Genau dort, wo im
Trainingsmaterial wenig steht, erfindet sie am schönsten — und du kannst es selbst überprüfen.

**Pleasing sichtbar machen.** Behaupte etwas Falsches selbstbewusst und beobachte, wie sie
einlenkt. Dann stell dieselbe Frage neutral. Dieselbe Maschine, zwei Antworten.

---

## Zahlen zum Merken

| Wofür | Wert |
|:---|---:|
| Anteil der Rechenzentren am Weltstrom (2024) | 1,5 % |
| erwartete Verdopplung bis 2030 (IEA) | ×2 |
| eine Gemini-Textanfrage (Median, Google) | 0,24 Wh |
| Anstieg der Google-Emissionen gegenüber 2019 | 48 % |
| relativer Beschäftigungsrückgang bei Berufseinsteigern (Stanford) | 13 % |
| angegriffene Organisationen im Cyberfall 11/2025 | rund 30 |

### Was 0,24 Wh bedeutet

Diese eine Zahl räumt ein verbreitetes Missverständnis aus. **0,24 Wattstunden** sind
0,00024 Kilowattstunden. In Alltagsgrößen:

| Das entspricht ungefähr … | |
|:---|---:|
| Anfragen, die in **eine Kilowattstunde** passen | rund 4.000 |
| Anfragen für **einen Cent** Strom (bei 0,35 €/kWh) | rund 120 |
| eine 10-Watt-LED-Lampe leuchtet dafür | etwa 1,5 Minuten |
| einmal **einen Liter Wasser kochen** entspricht | rund 400 Anfragen |
| einmal **das Handy laden** entspricht | rund 60 Anfragen |

!!! note "Die Empörung steht oft an der falschen Stelle"
    Wer dir vorrechnet, ein Chat koste „eine Flasche Wasser", verkauft dir eine schlechte Zahl.

    **Deine einzelne Anfrage ist praktisch nichts. Das Problem ist der Ausbau:** Stromnetze,
    Strompreise, Wasserverbrauch in trockenen Regionen. Global ist das Ganze noch klein gegen
    Zement und Flugverkehr — aber es ist der am schnellsten wachsende Posten.

    Das ist keine Entwarnung. Es ist nur eine Verschiebung: Die Frage gehört an die Politik,
    nicht an dein Gewissen beim Tippen.

=== "Für Einsteiger"

    Kurz gesagt: Du musst kein schlechtes Gewissen haben, wenn du einen Chatbot benutzt.
    Der Stromverbrauch deiner Anfragen verschwindet neben dem, was Heizung, Auto oder ein
    Flug ausmachen.

=== "Für Fortgeschrittene"

    Bei der Zahl ist Vorsicht angebracht — sie stammt vom Anbieter selbst.

    Die 0,24 Wh sind Googles eigener **Medianwert** für eine *Text*anfrage an Gemini und
    enthalten nach Google-Angaben Server, Kühlung und Leerlauf im Rechenzentrum. Was sie
    **nicht** enthalten: das Training des Modells, das Endgerät und das Netz. Unabhängige
    Schätzungen liegen teils deutlich höher, weil sie anders abgrenzen — und ein Median sagt
    nichts über die Spitzen.

    Wichtiger noch: Die Zahl gilt für eine **kurze Textantwort**. Bildgenerierung, Videos und
    lange „Denk"-Antworten mit vielen Zwischenschritten liegen um Größenordnungen darüber.
    Wer die 0,24 Wh auf jede Nutzung überträgt, rechnet sich das Ergebnis schön.

---

## Zum Schluss: die nützliche Frage

Ein Risiko-Abend kann leicht mit „dann lass ich's lieber" enden. Das wäre das schlechteste
Ergebnis — denn wer sie aus Sorge nie benutzt, benutzt sie irgendwann trotzdem, im Notfall,
ungeübt und ungeprüft. Deshalb steht in diesem Artikel neben jedem Risiko ein Griff.

Die nützliche Frage lautet: **Wer kann eigentlich etwas tun?**

* Rechenzentren, autonome Waffen, Marktmacht → **Politik.** Für uns: Bürgerwissen, damit wir
  mitreden können.
* Chatbot-Bindung bei Jugendlichen, Enkeltrick, Prüfroutinen, der eigene Umgang →
  **wir selbst, ab heute.**

Und durch fast alles zieht sich dasselbe Muster: Nicht die Fähigkeit der Maschine ist neu,
sondern **die Menge und die Geschwindigkeit, mit der Menschen aufhören hinzusehen.**

---

!!! warning "Vorbehalt zu den Zahlen und Beispielen"
    Alle Zahlen und Vorfälle in diesem Artikel haben den Wissensstand **Mai 2026** und sind
    nicht einzeln nachrecherchiert. Vor dem Weitererzählen bitte gegenchecken — genau das ist
    ja der Punkt des Artikels.

    Ein Beispiel für die Notwendigkeit: Der automatisierte Cyberangriff von 11/2025 wird häufig
    ChatGPT zugeschrieben. Tatsächlich lief er über *Claude* — und gemeldet hat ihn der
    Hersteller Anthropic selbst.
