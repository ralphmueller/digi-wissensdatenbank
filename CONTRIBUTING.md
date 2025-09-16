# CONTRIBUTING

Danke fürs Mitmachen! So klappt die Zusammenarbeit reibungslos.

## Rollen
- **Redaktion**: Review & Freigabe, Strukturpflege
- **Autor*innen**: Schreiben/Überarbeiten von Beiträgen
- **Community**: Themen vorschlagen, Fehler melden (Issues)

## Schreibregeln (Kurz)
- „Du“-Form, klare Verben, kurze Sätze
- Erst **Einsteiger**, dann **Fortgeschrittene**
- Schritt-für-Schritt, Tipps/Warnungen als Admonitions
- Barrierearm: Alt-Texte, Kontraste, keine Farbcodes allein
- Screenshots mit Markierung + Datum/Version

## Frontmatter (Meta)
Jede Seite bekommt einen YAML-Block ganz oben:
```yaml
---
title: Titel
slug: sprechbarer-slug
type: term | howto | article
tags: [smartphone, cloud, sicherheit]
author: Dein Name
updated: 2025-09-15
status: draft | published
related: [andere-seite]
---
```

## Review-Checkliste
Siehe `docs/99-intern/Redaktions-Checkliste.md`.

## Branch & PR
- neue Inhalte in Feature-Branch
- PR stellen, 1 Review OK
- „Squash & merge“ empfohlen
