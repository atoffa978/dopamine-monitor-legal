# Privacy Policy — Dopamine Monitor

**In vigore dal**: 18 maggio 2026
**Versione documento**: 1.1
**Lingua autoritativa**: italiano

---

## 1. In due righe

Dopamine Monitor è un'app di **auto-osservazione passiva** dell'uso del telefono. Tutto quello che riguarda te personalmente — quali app usi, quando, per quanto — resta sul tuo dispositivo. Verso i nostri server inviamo solo, **se tu lo accetti**, un piccolo riassunto giornaliero anonimo per migliorare il modello statistico. Non vendiamo dati a nessuno, non mostriamo pubblicità, non ti profiliamo.

Se questa premessa ti basta, puoi smettere di leggere. Per i dettagli, prosegui.

---

## 2. Chi siamo

**Titolare del trattamento**: Angelo Toffaletti
**Indirizzo**: Via Centro di Romagnano 38, 37023 Grezzana (VR), Italia
**Email di contatto**: dopamine.monitor.dev@gmail.com

Per qualunque richiesta sul trattamento dei tuoi dati personali puoi scrivere all'indirizzo email sopra. Rispondiamo entro 30 giorni.

---

## 3. Quali dati raccoglie l'app sul tuo dispositivo

Per funzionare, Dopamine Monitor legge dal sistema Android **dati di utilizzo del telefono**. Questi dati **non lasciano mai il dispositivo** salvo quanto descritto al §5 ("Telemetria"), e solo dopo essere stati aggregati e anonimizzati.

### 3.1 Cosa legge

- **Statistiche di utilizzo delle app** (Usage Stats / Digital Wellbeing): per ogni app, quanti minuti l'hai usata in primo piano e in quali fasce orarie. Questo è il dato fondamentale per costruire il "Dopa Index" giornaliero.
- **Eventi di notifica** (Notification Access): conteggio numerico delle notifiche ricevute e aperte. Non leggiamo il contenuto delle notifiche, solo che siano avvenute.
- **Lista delle app installate sul dispositivo** (launchable apps): solo per categorizzare il loro tipo (social, gambling, produttività, ecc.) in fase di calcolo. Letta on-demand, mai trasmessa.

### 3.2 Cosa **NON** legge

- Mai contenuto di messaggi, chiamate, email, foto, file, browser cronologia, contatti, calendario.
- Mai posizione GPS.
- Mai microfono, fotocamera, sensori biometrici.
- Mai input da tastiera o accessibility services.
- Mai dati account Google o login.

### 3.3 Dove vengono salvati i dati sul dispositivo

Tutti i dati grezzi (eventi del giorno corrente) e aggregati (storia giornaliera, fino a 60 giorni) sono salvati **localmente** in:

- `SharedPreferences` standard Android (preferenze e stato),
- file privati dell'app (history persistente).

Sono accessibili **solo all'app stessa**. Quando disinstalli Dopamine Monitor, vengono cancellati automaticamente dal sistema Android.

Puoi inoltre cancellare in qualsiasi momento tutti i dati locali dall'interno dell'app: Impostazioni → "Cancella tutti i dati".

---

## 4. Permessi Android richiesti

L'app funziona solo se concedi i seguenti permessi. Tu li concedi attivamente, dalle impostazioni di sistema Android. Puoi revocarli in qualsiasi momento.

| Permesso | A cosa serve | Cosa succede se lo neghi |
|---|---|---|
| **Accesso alle statistiche di utilizzo** (`PACKAGE_USAGE_STATS`) | Leggere quanto tempo passi sulle app | L'app non può funzionare e te lo dirà |
| **Accesso alle notifiche** (`NotificationListener`) | Contare le notifiche ricevute (non il contenuto) | L'asse "notifiche" del Dopa Index resta a zero, ma il resto funziona |
| **Esecuzione in background** | Aggiornare la storia ogni giorno a mezzanotte | Devi aprire l'app manualmente per veder aggiornati i dati |

Non chiediamo permessi su localizzazione, contatti, microfono, fotocamera, SMS, storage, ecc.

---

## 5. Telemetria verso i nostri server (opzionale, opt-in)

Questa è l'unica circostanza in cui dei dati che ti riguardano lasciano il dispositivo. **Devi acconsentire esplicitamente** in fase di onboarding o dalle Impostazioni: senza il tuo consenso esplicito, l'app non invia nulla a nessun server.

### 5.1 A cosa serve

Migliorare il modello statistico del Dopa Index e calibrarlo su una popolazione di utenti reali. Vediamo distribuzioni aggregate (es. "il Dopa Index medio degli utenti dopo 30 giorni d'uso è X"), non dati individuali.

### 5.2 Cosa viene inviato

Esattamente un piccolo riassunto JSON per ogni giorno chiuso che hai sul dispositivo. Lo schema completo è documentato nel codice sorgente (`lib/telemetry/payload_builder.dart`). Contiene:

- Numeri da 0 a 100 per il Dopa Index complessivo e per ognuno degli 8 assi (social, video, notifiche, ecc.).
- Quale asse è risultato "dominante".
- Quali "pattern" sono stati attivati (es. "uso post-23:00").
- Un identificativo casuale del dispositivo (`install_id`, generato dall'app stessa la prima volta), versione dell'app, versione di Android.
- Un "secchio" di osservazione (`nuovo` < 14 giorni, `assestato` 14-89, `lungo` ≥ 90) invece del numero esatto di giorni di uso — questo per evitare che il numero preciso ci permetta di riconoscere il singolo dispositivo.
- Numero (anonimo) di eventi di frizione (popup) attivati e rispettati nella giornata.

### 5.3 Cosa **NON** viene mai inviato

- Mai il nome di un'app specifica che hai usato.
- Mai durate di uso individuali (solo il punteggio aggregato).
- Mai contenuti, messaggi, identificativi personali, email, numero di telefono, IMEI, indirizzi MAC, identificativi pubblicitari.
- Mai posizione, sensori, cronologia browser.

### 5.4 Identificazione

L'unico identificativo è un `install_id` casuale generato dall'app la prima volta che la apri (UUID). Non è collegato al tuo account Google, al tuo numero IMEI, ad alcun login. Se disinstalli e reinstalli l'app, ottieni un nuovo `install_id` non collegabile al precedente.

Riteniamo che il payload trasmesso sia **anonimo** ai sensi del GDPR: l'insieme dei campi non permette di identificarti, neppure tramite combinazione con altre fonti pubbliche. Se in futuro scoprissimo un rischio di re-identificazione, aggiorneremo questa policy e te lo comunicheremo all'interno dell'app.

### 5.5 Dove vengono inviati

I dati sono inviati via HTTPS a server gestiti da **Scaleway**, situati nell'Unione Europea (Paris, FR). Scaleway agisce come "responsabile del trattamento" ai sensi del GDPR. Vedi: https://www.scaleway.com/en/privacy/

### 5.6 Per quanto tempo li conserviamo

I payload sono conservati per **massimo 24 mesi** dalla ricezione, poi cancellati automaticamente. Le distribuzioni aggregate (medie, statistiche) possono essere conservate più a lungo perché non contengono record individuali.

### 5.7 Come ritirare il consenso

In qualsiasi momento puoi andare in Impostazioni → "Telemetria" e scegliere "Non partecipare". Da quel momento l'app non invierà più nulla. **Quello che è già stato inviato in passato resta sui nostri server fino allo scadere dei 24 mesi**, a meno che tu non richieda esplicitamente la cancellazione anticipata (vedi §7.4 — diritto di cancellazione).

---

## 6. Base giuridica del trattamento

- Per i dati che restano **sul dispositivo** (§3): non c'è "trattamento" da parte nostra ai sensi GDPR, perché non riceviamo né accediamo a questi dati. Sono dati tuoi sul tuo dispositivo, per uso personale.
- Per la **telemetria** verso i nostri server (§5): la base giuridica è il tuo **consenso esplicito** (art. 6, par. 1, lett. a del GDPR). Senza consenso, niente trasmissione.

---

## 7. I tuoi diritti GDPR

Dato che la telemetria è basata su un identificativo casuale non legato a te, potremmo non essere in grado di estrarre dati specificamente "tuoi" dal nostro database. Tuttavia, puoi sempre esercitare i seguenti diritti:

### 7.1 Diritto di informazione
Stai leggendo questo documento.

### 7.2 Diritto di accesso (art. 15 GDPR)
Puoi chiederci se trattiamo dati riferibili al tuo dispositivo e ricevere copia dei payload trasmessi. Per farlo, ci serve il tuo `install_id` (lo trovi in Impostazioni → "Telemetria" → "Mostra ID installazione"). Scrivici a dopamine.monitor.dev@gmail.com.

### 7.3 Diritto di rettifica (art. 16 GDPR)
I dati trasmessi sono punteggi numerici calcolati: non c'è qualcosa da "rettificare". Se l'app calcola male un valore (es. bug nell'engine), puoi segnalarlo con il pulsante feedback in-app.

### 7.4 Diritto di cancellazione (art. 17 GDPR)
Puoi chiedere la cancellazione anticipata dei payload riferiti al tuo `install_id`, scrivendoci a dopamine.monitor.dev@gmail.com e includendo l'ID. Procediamo entro 30 giorni.

### 7.5 Diritto di limitazione (art. 18 GDPR)
Puoi richiedere che i tuoi dati siano "congelati" senza ulteriore trattamento. Scrivici.

### 7.6 Diritto di opposizione e portabilità (art. 20-21 GDPR)
Puoi chiedere copia dei payload trasmessi in formato JSON. Sono già strutturati, ti basta richiederli.

### 7.7 Diritto di reclamo (art. 77 GDPR)
Se ritieni che il trattamento dei tuoi dati violi il GDPR, puoi presentare reclamo all'autorità di controllo:

- **Italia**: Garante per la Protezione dei Dati Personali — https://www.garanteprivacy.it/
- Oppure all'autorità del Paese UE in cui risiedi abitualmente.

---

## 8. Dati di minori

L'app non è destinata a minori di 14 anni. Non chiediamo intenzionalmente dati di minori. Se sei genitore/tutore e ritieni che un minore sotto la tua tutela usi l'app, contattaci.

---

## 9. Trasferimenti extra-UE

I server di telemetria sono in UE (Scaleway, Parigi). Non trasferiamo dati al di fuori dell'UE.

---

## 10. Cookie, tracker, pubblicità

L'app **non usa**: cookie, tracker pubblicitari, fingerprinting, SDK di analytics di terze parti (no Google Analytics, no Firebase Analytics, no Crashlytics, no Mixpanel, no Amplitude, ecc.), pubblicità di qualunque tipo, comunicazioni di marketing.

L'app **usa**:

- una libreria di logging interna del framework Flutter (sviluppo/debug, non telemetria),
- la connessione di rete solo per la trasmissione di telemetria (§5) e, in futuro, eventuali update notice del modello.

---

## 11. Modifiche a questa policy

Quando aggiorneremo questa policy, te lo comunicheremo:

1. Aggiornando il numero di versione e la data in cima.
2. Mostrando una notifica in-app la prima volta che apri una nuova versione con policy aggiornata.

Se l'aggiornamento riguarda l'ampliamento dei dati trasmessi o nuove finalità di trattamento, **chiederemo nuovamente il tuo consenso esplicito** prima di applicarle.

---

## 12. Contatti

Per ogni domanda, richiesta di accesso, segnalazione, scrivici a:

**dopamine.monitor.dev@gmail.com**

Rispondiamo entro 30 giorni.
