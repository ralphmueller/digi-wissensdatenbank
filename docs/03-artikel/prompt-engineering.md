---
title: Vom einfachen Auftrag zum guten Prompt
slug: prompt-engineering
type: article
tags: [künstliche intelligenz, prompt, praxisbeispiel]
author: Digi-Stammtisch Team
updated: 2026-08-19
status: published
related: [prompt-ki]
---

# Vom einfachen Auftrag zum guten Prompt

Bei unserem SWOT-Workshop im Juli war eure größte Sorge, dass eine KI falsche Informationen
liefert und man ihr das nicht ansieht — „Kann ich das überprüfen?“ stand quer über dem
Risiken-Blatt. Und euer größter Wunsch war, Dinge zu automatisieren, die aktuell viel Zeit
kosten; dieser Punkt bekam die meisten Klebepunkte des ganzen Workshops.

Dieser Artikel zeigt an einem echten Fall beides: wie aus einer vagen Frage eine Aufgabe
wird, die eine KI zuverlässig erledigt — und wie man ihr abgewöhnt, so zu tun, als wüsste
sie etwas.

!!! tip "Wenig Zeit?"
    Spring direkt zu [Für deine eigene Aufgabe](#fur-deine-eigene-aufgabe) — dort stehen die
    fünf Schritte zum Selbermachen, ohne die Vorgeschichte.

Prompt Engineering bedeutet nicht, eine möglichst komplizierte Frage an eine KI zu stellen.
Ein guter Prompt beschreibt vielmehr **klar, was die KI tun soll, unter welchen Bedingungen
sie arbeitet und woran ein gutes Ergebnis zu erkennen ist**.

---

## Wie wir das am Beispiel der Theaterstücksuche entwickelt haben

!!! note "Womit wir gearbeitet haben"
    Wir haben in der Sitzung **ChatGPT** benutzt. Die Vorgehensweise funktioniert aber
    genauso mit anderen KI-Assistenten — es geht um die Art der Aufgabenstellung, nicht um
    ein bestimmtes Werkzeug.

Unser Ausgangspunkt war denkbar einfach:

> **„Suche die lustigsten Komödien für unser Theater.“**

Dazu gab es einige erste Bedingungen: fünf Frauen, fünf Männer, maximal 110 Minuten, kein
Dialekt und nur ein Bühnenbild.

Das lieferte bereits Ergebnisse. Aber schnell zeigte sich das eigentliche Problem:

**Was bedeutet überhaupt „lustig“?**

Eine KI kann problemlos schreiben:

> „Dieses Stück ist sehr lustig.“

Damit können wir aber wenig anfangen.

Also haben wir den Begriff **„lustig“ zerlegt**. Wir wollten wissen:

* Wie hoch ist die Pointendichte?
* Gibt es Situationskomik?
* Gibt es guten Dialogwitz?
* Entsteht Humor aus den Figuren?
* Gibt es Running Gags?
* Wie schnell kommt das Stück in Fahrt?
* Wie wahrscheinlich funktioniert der Humor vor unserem Publikum?

Dazu kam ein sehr praktisches Kriterium aus der Theatererfahrung:

> **„Wenn auf den ersten zehn Seiten noch nicht gelacht wurde, macht es keinen Sinn.“**

Damit war „lustig“ plötzlich keine abstrakte Forderung mehr. Die KI musste erklären,
**wann, warum und wodurch ein Stück komisch wird**.

## Harte Kriterien von Qualitätskriterien trennen

Als Nächstes haben wir festgestellt, dass nicht alle Kriterien gleich behandelt werden dürfen.

Ein Stück kann hervorragend sein und trotzdem für unser Theater ausscheiden.

Deshalb unterscheiden wir nun zwischen **harten Kriterien** wie 5 Frauen/5 Männer, alle zehn
spielen, maximal zwei Generationen, ein Bühnenbild, höchstens 110 Minuten und kein Dialekt –
und **weichen Kriterien** wie Humor, Tempo, Figurenqualität, Rollenbalance und
Publikumswirkung.

Das verhindert beispielsweise, dass die KI ein Stück begeistert empfiehlt, das elf
Schauspieler benötigt.

## Ein einheitliches Bewertungssystem

Damit die Stücke vergleichbar werden, entwickelten wir eine **100-Punkte-Matrix**.

Bewertet werden unter anderem Einstieg, Humor und Pointendichte, Figuren, Tempo,
Rollenbalance, Publikumswirkung, Finale, Amateurtauglichkeit und praktische Passung.

Die Zahl selbst ist dabei gar nicht das Entscheidende. Viel wichtiger ist:

> **Jedes Stück muss dieselben Fragen beantworten.**

Ein 82-Punkte-Stück lässt sich dadurch sinnvoll mit einem 74-Punkte-Stück vergleichen.

## Die KI darf nicht so tun, als wüsste sie etwas

Dann trat ein weiteres Problem auf: Von manchen Stücken hatten wir vollständige Texte, von
anderen nur Leseproben.

Eine KI könnte trotzdem leicht schreiben:

> „Das Finale funktioniert hervorragend.“

obwohl das Finale gar nicht vorliegt.

Deshalb haben wir die **Materialbasis** ausdrücklich in den Prompt aufgenommen:

* vollständiger Stücktext,
* Ansichtsexemplar,
* Leseprobe,
* Verlagsbeschreibung,
* Katalogdaten.

Daraus entstand eine unserer wichtigsten Regeln:

!!! warning "Nicht gelesen = nicht beurteilt"
    Fehlt das Finale, muss die KI sagen, dass sie das Finale nicht beurteilen kann. Sie darf
    es nicht aus dem bisherigen Handlungsverlauf extrapolieren und anschließend wie eine
    Tatsache behandeln.

## Eine Aufgabe wurde in zwei Aufgaben zerlegt

Ursprünglich wollten wir die KI einfach anweisen:

> Lies das Stück, analysiere es, bewerte es und schreibe einen Bericht.

Dann haben wir erkannt, dass wir damit sehr unterschiedliche Tätigkeiten in einen einzigen
Prompt packen.

Also trennten wir sie:

```text
Theaterstück
      ↓
    Analyst
      ↓
Fakten + Analyse
      ↓
Chefdramaturg
      ↓
Urteil + Empfehlung
```

Der **Analyst** soll möglichst nüchtern arbeiten. Er ermittelt Besetzung, Spieldauer,
Bühnenbild und Materialbasis und untersucht Einstieg, Humor, Figuren, Rollenbalance, Tempo
und Finale. Seine Ergebnisse werden in einer festen Form festgehalten, damit sie für jedes
Stück gleich aussehen.

Der **Chefdramaturg** bekommt diese geprüften Informationen und macht daraus die eigentliche
Beurteilung. (Ein Dramaturg ist am Theater derjenige, der Stücke sichtet, auswählt und
begründet, warum eines auf die Bühne gehört und ein anderes nicht — also genau die Arbeit,
die wir hier von der KI wollen.)

Das erwies sich als großer Qualitätssprung:

> **Der Analyst muss nicht schön schreiben. Er muss zuverlässig sein.
> Der Dramaturg muss nicht neu recherchieren. Er muss urteilen.**

## Aus einem Prompt wurde ein Regelwerk

Statt eines einzigen riesigen Prompts haben wir die Vorgaben schließlich getrennt
aufgeschrieben — jede Sorte Regel für sich:

* **Was für ein Theater sind wir?** Ensemble, Bühne, Publikum, harte Anforderungen.
* **Wie wird bewertet?** Die 100-Punkte-Matrix.
* **Wie soll der Bericht aussehen?** Aufbau und Reihenfolge der Abschnitte.
* **In welchem Ton?** Sachlich, keine Werbesprache.

Damit ist der Prompt nicht mehr ein langer Textblock, sondern ein **kleines Regelwerk**. Der
praktische Vorteil: Wenn ein Ergebnis nicht passt, musst du nicht alles umschreiben, sondern
nur die eine Regel ändern, an der es lag.

Am Ende dieses Prozesses steht eine **Tabelle** — eine Zeile je Stück, die Bewertungskriterien
als Spalten. Erst dadurch lassen sich die Stücke nebeneinander legen und vergleichen, statt
einzelne Berichte gegeneinander im Kopf zu behalten.

## Der erste Bericht war gut – aber noch kein Dramaturg

Dann kam der Praxistest mit **„Männergrippe“**.

Das Ergebnis war überraschend gut: faktenfest, nachvollziehbar, vorsichtig und mit sauberer
Trennung zwischen gelesenem und nicht gelesenem Material.

Aber etwas fehlte.

Der Bericht beschrieb sehr gut. Er **urteilte noch zu wenig**.

Also haben wir nicht die Analyse geändert, sondern die Rolle des zweiten Arbeitsschritts.

Aus:

> „Schreibe einen dramaturgischen Bericht.“

wurde sinngemäß:

> **„Du bist ein erfahrener Chefdramaturg. Theatervereine verlassen sich auf dein Urteil.
> Deine Aufgabe ist nicht, das Stück zusammenzufassen. Deine Aufgabe ist es, eine
> Auswahlentscheidung zu ermöglichen.“**

Das war eine wichtige Erkenntnis:

!!! tip "Die Rolle verändert mehr als den Ton"
    Die Rolle einer KI beeinflusst nicht nur ihren Schreibstil, sondern auch, **welche Fragen
    sie sich bei der Bearbeitung stellt**.

## Vom „Was?“ zum „Was bedeutet das?“

Wir führten eine weitere zentrale Regel ein:

> **Nicht nur beschreiben – beurteilen.**

Nicht:

> „Die Komik entsteht aus Verwechslungen.“

Sondern beispielsweise:

> „Die Verwechslungen funktionieren auf einer Amateurbühne zuverlässig, weil das Publikum den
> Figuren häufig einen Schritt voraus ist.“

Die erste Aussage sagt, **was passiert**. Die zweite sagt zusätzlich, **warum das für unsere
Entscheidung wichtig ist**.

Das ist ein grundlegendes Prinzip, das sich auf sehr viele KI-Aufgaben übertragen lässt:

> **WHAT → SO WHAT**

## Die KI bekam einen Platz im Zuschauerraum

Der Chefdramaturg bekam außerdem konkrete Fragen:

* Wann lacht das Publikum vermutlich zum ersten Mal?
* Wo entstehen die größten Lacher?
* Wo könnte das Stück einen Durchhänger haben?
* Welche Figur wird vermutlich Publikumsliebling?
* Welche Rolle entscheidet über den Erfolg?
* Wo muss die Regie besonders auf das Timing achten?
* Würde ich dieses Stück selbst inszenieren?

Dadurch änderte sich die Perspektive. Die KI analysierte nicht mehr nur einen Text. Sie
begann, über einen **konkreten Theaterabend** nachzudenken.

## Und dann kam „Butler heißen immer James“

Der nächste Bericht zeigte deutlich, dass die Änderungen funktionierten.

Der Chefdramaturg erkannte durchaus die Qualitäten des Stückes: guter Einstieg,
verständlicher Humor, interessante Rollen und erfolgversprechende Bühnenfiguren.

Trotzdem lautete seine Entscheidung:

> **Für dieses Ensemble nicht geeignet.**

Warum?

Die Fassung verlangt sechs Frauen und fünf Männer und liegt mit rund 120 Minuten über unserer
Grenze.

Das ist genau die Art von Urteil, die wir erreichen wollten.

Die KI sollte nicht fragen:

> „Ist das ein gutes Stück?“

Sondern:

> **„Ist das ein gutes Stück für genau dieses Theater?“**

## Wir haben den Prompt nicht auf einmal geschrieben

Vielleicht ist das die wichtigste Erkenntnis des gesamten Experiments.

Wir haben uns **nicht hingesetzt und den perfekten Prompt geschrieben**.

Unser tatsächlicher Prozess sah so aus:

```text
einfacher Prompt
       ↓
erstes Ergebnis
       ↓
Was gefällt uns nicht?
       ↓
Prompt gezielt ändern
       ↓
nächstes Ergebnis
       ↓
erneut beurteilen
       ↓
wieder verbessern
```

Das ist eigentlich der Kern von Prompt Engineering.

Nicht:

> „Wie schreibe ich sofort den perfekten Prompt?“

Sondern:

> **„Welche konkrete Schwäche des letzten Ergebnisses möchte ich mit der nächsten
> Prompt-Version beseitigen?“**

## Und irgendwann muss man aufhören

Auch das haben wir gelernt.

Nach mehreren Iterationen waren die Berichte gut genug, um alle Stücke zu bearbeiten.

Weitere Prompt-Optimierung hätte möglicherweise noch kleine Verbesserungen gebracht. Aber
irgendwann wird der Nutzen jeder zusätzlichen Änderung kleiner.

Deshalb kam die Entscheidung:

> **Jetzt machen wir erstmal alle Stücke.**

Erst wenn genügend echte Ergebnisse vorliegen, lohnt sich die nächste Qualitätsrunde.

---

## Die Kurzfassung unserer Kurzfassung

Aus

> **„Suche lustige Theaterstücke.“**

wurde schrittweise ein System, das sinngemäß sagt:

> **„Arbeite als erfahrener Dramaturg für Amateurtheater. Prüfe zunächst alle zwingenden
> formalen Anforderungen. Analysiere anschließend nach einer einheitlichen Bewertungsmatrix
> Einstieg, Humor, Figuren, Tempo, Rollenbalance und Publikumswirkung. Unterscheide belegte
> Tatsachen von dramaturgischen Einschätzungen. Beurteile nichts, was im vorliegenden
> Material nicht geprüft werden konnte. Begründe deine Urteile aus Sicht von Bühne, Regie und
> Publikum und gib am Ende eine eindeutige Empfehlung für unser konkretes Ensemble.“**

Das ist der Unterschied zwischen einer einfachen Frage und einem guten Prompt.

**Prompt Engineering bedeutet also nicht, immer längere Prompts zu schreiben. Es bedeutet,
eine zunächst unscharfe Aufgabe so lange zu präzisieren, bis Rolle, Ziel, Kontext, Kriterien,
Unsicherheiten, Arbeitsweise und gewünschtes Ergebnis klar sind.**

## Für deine eigene Aufgabe

Du brauchst kein Theater, um das zu nutzen. Nimm irgendetwas, das dich regelmäßig Zeit
kostet — Vereinsprotokolle zusammenfassen, aus vielen Angeboten das passende heraussuchen,
Fotos beschriften, einen Text für den Gemeindebrief kürzen. Dann geh diese fünf Schritte
durch:

1. **Fang klein an.** Stell die Aufgabe zuerst so, wie du sie einem Menschen sagen würdest.
   Der erste Prompt darf schlecht sein — er ist nur dein Ausgangspunkt.
2. **Schau dir das Ergebnis genau an und frage: Was stört mich daran?** Nicht „ist das gut?“,
   sondern „was fehlt konkret?“. Genau das ist der Satz, den du als Nächstes ergänzt.
3. **Zerlege deine unklaren Wörter.** „Gut“, „schön“, „passend“, „seriös“ — solche Begriffe
   versteht die KI anders als du. Schreib auf, woran *du* es festmachst.
4. **Trenne, was sein muss, von dem, was schön wäre.** Was nicht erfüllt ist, fliegt raus —
   ganz gleich, wie gut der Rest ist. Sag das der KI ausdrücklich.
5. **Verbiete Erfindungen.** „Wenn dir Informationen fehlen, schreib das hin, statt zu raten.“
   Dieser eine Satz löst den größten Teil der Sorge, dass eine KI Dinge behauptet, die nicht
   stimmen.

Und dann wiederhol Schritt 2, bis es reicht. Nicht bis es perfekt ist — bis es reicht.

!!! tip "Der eine Satz, den du dir merken solltest"
    Frag nicht: „Wie schreibe ich sofort den perfekten Prompt?“ Frag: **„Welche Schwäche des
    letzten Ergebnisses will ich als Nächstes beseitigen?“**

## Die acht Bausteine eines guten Prompts

Zum Nachschlagen — alles, was in der Geschichte oben vorkam, noch einmal als Liste. Ein guter
Prompt sollte möglichst diese Elemente enthalten:

* **Rolle:** Wer soll die KI sein? Dramaturg, Lehrer, Techniker, Jurist?
* **Ziel:** Was soll mit dem Ergebnis erreicht oder entschieden werden?
* **Kontext:** Welche Informationen über die konkrete Situation sind wichtig?
* **Harte Kriterien:** Welche Bedingungen müssen zwingend erfüllt sein?
* **Qualitätskriterien:** Woran erkennst du ein gutes Ergebnis?
* **Arbeitsweise:** Soll recherchiert, verglichen, analysiert oder bewertet werden?
* **Umgang mit Unsicherheit:** Was soll passieren, wenn Informationen fehlen?
* **Ausgabeformat:** Wie soll das Ergebnis strukturiert sein?

!!! tip "Die zwei wichtigsten Regeln"
    **Unklare Begriffe musst du konkretisieren.**
    „Finde ein gutes Stück“ ist schwierig. „Bewerte Einstieg, Pointendichte, Figuren,
    Rollenbalance und Publikumswirkung“ ist wesentlich besser.

    **Lass nicht nur beschreiben, sondern beurteilen.**
    Die KI soll nicht nur sagen, *was* sie gefunden hat, sondern auch, **was das für
    deine konkrete Aufgabe bedeutet**.

## Wenn die Aufgabe größer wird

Für den Anfang brauchst du das alles nicht. Wenn eine Aufgabe aber wächst, reicht ein
einzelner Prompt irgendwann nicht mehr. Drei Hebel haben sich bei uns als besonders wirksam
erwiesen:

* **Rollen trennen:** Recherche/Analyse und Urteil in **zwei** Arbeitsschritte aufteilen.
  Der eine Schritt sammelt belegte Fakten, der andere bewertet sie. Das erhöht die
  Zuverlässigkeit deutlich.
* **Regeln getrennt aufschreiben:** Kontext, Bewertungsmaßstab, Aufbau des Berichts und Ton
  jeweils für sich. Der Prompt wird dadurch zum **kleinen Regelwerk**, in dem du gezielt eine
  einzelne Regel ändern kannst.
* **Materialbasis deklarieren:** Der KI ausdrücklich sagen, welches Material vorliegt —
  und ihr verbieten, über nicht vorliegendes Material zu urteilen.

!!! warning "Harte und weiche Kriterien nicht vermischen"
    Harte Kriterien (Besetzung, Länge, Budget) schließen ein Ergebnis **aus**, egal wie
    gut es sonst ist. Qualitätskriterien (Humor, Tempo, Wirkung) machen es nur besser
    oder schlechter. Wenn du beides in einen Topf wirfst, empfiehlt dir die KI
    begeistert etwas, das gar nicht in Frage kommt.

## Weiterführend

- [Prompt (KI)](../01-glossar/prompt-ki.md) – die Kurzdefinition im Glossar
