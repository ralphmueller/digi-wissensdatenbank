---
title: Denial of Service (DoS)
slug: denial-of-service
type: term
tags: [sicherheit, internet, angriff]
author: Digi-Stammtisch Team
updated: 2026-03-03
status: published
---

# Denial of Service (DoS-Angriff)

Ein **Denial of Service-Angriff** (kurz: **DoS**, englisch für „Dienstverweigerung") ist ein **gezielter Angriff auf eine Webseite oder einen Online-Dienst**, um ihn **zum Absturz zu bringen oder unzugänglich zu machen**.

👉 **Merksatz:**
*Ein DoS-Angriff ist wie hunderte Leute, die gleichzeitig durch eine einzige Drehtür wollen – niemand kommt mehr durch.*

---

### 💥 Wie funktioniert das?

Ein Angreifer schickt **massenhaft Anfragen** an einen Server – so viele, dass dieser **überlastet wird und zusammenbricht**.
Normale Nutzer können die Seite dann nicht mehr aufrufen.

---

### 🌐 DDoS – der große Bruder

Beim **DDoS-Angriff** (Distributed Denial of Service) kommen die Anfragen nicht von einem einzigen Rechner, sondern von **tausenden Geräten gleichzeitig** – das macht ihn deutlich schwerer abzuwehren.

Diese Geräte sind oft **ohne Wissen ihrer Besitzer** Teil des Angriffs. Angreifer schleusen Schadsoftware auf schlecht gesicherte Heimgeräte und steuern sie aus der Ferne – das nennt man ein **Botnetz**.

!!! warning "Auch dein Zuhause könnte betroffen sein"
    Nicht nur PCs und Laptops werden gekapert – häufig trifft es **smart vernetzte Heimgeräte** wie Router, IP-Kameras, smarte Fernseher oder Lautsprecher. Diese haben oft veraltete Software oder unsichere Standardpasswörter und sind deshalb ein beliebtes Angriffsziel.

    **Was du tun kannst:**

    * Router und Smart-Home-Geräte **regelmäßig aktualisieren**
    * **Standardpasswörter sofort ändern**
    * Geräte, die du nicht mehr nutzt, **vom Netz trennen**

---

### 🏠 Wen trifft das im Alltag?

* Webseiten von Behörden, Banken oder Nachrichtenportalen
* Online-Shops (z. B. zu Stoßzeiten wie Black Friday als Angriffsziel)
* Gaming-Server
* Kleine Vereine oder Organisationen als politisches Statement

Als normaler Nutzer bist du **nicht direkt Ziel** – aber du merkst es, wenn eine Seite plötzlich nicht erreichbar ist.

---

### ⚠️ Was kann man dagegen tun?

Als Privatperson: **nichts direkt** – der Schutz liegt beim Betreiber der Webseite.
Betreiber setzen auf:

* **Traffic-Filter** (verdächtige Anfragen herausfiltern)
* **Content Delivery Networks (CDN)** (Last auf viele Server verteilen)
* **Spezialisierte DoS-Schutzdienste** (z. B. Cloudflare)

[Mehr dazu bei Wikipedia](https://de.wikipedia.org/wiki/Denial_of_Service)
