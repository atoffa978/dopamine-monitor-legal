# Termini d'uso — Dopamine Monitor

**In vigore dal**: 18 maggio 2026
**Versione documento**: 1.0
**Lingua autoritativa**: italiano

---

## 1. Cos'è Dopamine Monitor

Dopamine Monitor è un'applicazione Android per Android 9.0 e successivi che osserva passivamente come usi il telefono e ti restituisce uno "specchio strutturale" giornaliero — un indice composito chiamato **Body Load Index (BLI)** — che vuole aiutarti a riconoscere pattern d'uso compulsivi (uso post-23:00, frammentazione attentiva, eccessiva esposizione a contenuti dopaminici).

**L'app è uno strumento di auto-osservazione, non un dispositivo medico.** I numeri che vedi sono indicatori statistici basati su un modello dichiarato (vedi §5), non diagnosi cliniche.

---

## 2. Accettazione

Installando e utilizzando Dopamine Monitor, accetti questi Termini d'uso e la Privacy Policy collegata. Se non sei d'accordo, ti basta disinstallare l'app.

---

## 3. A chi è destinata

A maggiorenni interessati a osservare il proprio uso del telefono per fini di auto-consapevolezza. Non è uno strumento clinico, terapeutico, diagnostico, di prevenzione o trattamento di disturbi mentali, comportamentali o da uso di sostanze.

L'app **non è destinata**: a minori sotto i 14 anni, a persone in trattamento clinico per disturbi correlati all'uso di tecnologia o dipendenze comportamentali senza la supervisione del proprio specialista, a uso professionale (HR, scuole, monitoraggio di terzi).

---

## 4. Cosa NON è Dopamine Monitor

Per evitare malintesi:

- **Non è un'app di parental control**. Non è progettata per monitorare i figli, dipendenti, partner o altre persone. È un'app di **auto**-osservazione.
- **Non è un sistema di blocco app**. Esistono popup di "frizione" opzionali, ma sono inviti, non blocchi: l'utente può sempre proseguire.
- **Non è un'app medica**. I punteggi BLI non sostituiscono valutazioni cliniche. Se hai preoccupazioni serie sul tuo rapporto con la tecnologia, rivolgiti a un professionista.
- **Non è un coach motivazionale**. Non ti dice cosa fare, non ti invia messaggi push di "incoraggiamento", non gamifica l'astinenza. Mostra dati e basta.
- **Non è un servizio cloud**. I tuoi dati di utilizzo restano sul tuo dispositivo (vedi Privacy Policy §3-§4). L'unica trasmissione possibile è una telemetria aggregata anonima opzionale (§5.5 Privacy Policy).

---

## 5. Cosa fa concretamente

L'app legge dal sistema Android tre categorie di dati (con il tuo permesso esplicito):

1. **Tempo di utilizzo per app** (Usage Stats)
2. **Conteggio notifiche ricevute/aperte** (Notification Listener)
3. **Lista app installate** (solo per categorizzarle)

Da questi calcola, una volta al giorno, otto "assi" (social high-dopamine, video binge, infomania, body monitoring, produttività iperattiva, notifiche, uso notturno, frammentazione) e li combina in un indice 0-100 chiamato BLI.

Il modello statistico e le sue limitazioni sono documentate nelle specifiche tecniche del progetto (vedi `docs/bli-v5-proposta-v0.5.2.md` nel repository). Il modello viene chiamato "v0.1" in fase di lancio ed è suscettibile di revisioni successive.

---

## 6. Limitazioni del modello

Sii consapevole dei limiti dello strumento:

- **Il BLI è una stima, non una misura.** I pesi assegnati alle diverse categorie di app sono basati su letteratura e best-guess clinico, non sono validati epidemiologicamente.
- **La categorizzazione delle app è imperfetta.** L'app classifica i pacchetti installati secondo una baseline interna che copre le app più diffuse in Italia. Le app non riconosciute finiscono in categoria "altro" con peso ridotto. Puoi correggere a mano dalle Impostazioni.
- **Il "tempo di utilizzo" Android misura solo il primo piano con schermo acceso.** Un'app come Spotify in background non viene contata; un'app come WhatsApp aperta ma non guardata sì.
- **Pattern personali estremi (uso lavorativo notturno, fasce orarie invertite per shift work, ecc.) possono produrre falsi positivi.** L'app non lo sa.
- **Non c'è ground truth.** Non sappiamo "qual è il BLI giusto" per te. Lo strumento serve a osservare variazioni nel tempo, non a fissare soglie assolute.

Se vedi un BLI molto alto o pattern allarmanti, **non è una diagnosi**. È un invito a fermarti a pensare. Se ti senti veramente preoccupato del tuo rapporto con il telefono, parlane con qualcuno di fiducia o un professionista qualificato.

---

## 7. Frizione: cos'è e cosa non è

L'app può, in alcuni casi, mostrare popup di "frizione" (es. prima di aprire un'app social dopo le 23:00). Sono:

- **Inviti, non blocchi**: puoi sempre proseguire premendo "Continua".
- **Statisticamente registrati**: l'app conta quanti popup hai visto e quanti hai rispettato. È una metrica di auto-osservazione, non un punteggio di "bravura".
- **Disattivabili**: dalle Impostazioni puoi disabilitare i popup di frizione mantenendo attivo il calcolo del BLI.

---

## 8. Telemetria opzionale

Vedi Privacy Policy §5. Per chiarezza:

- L'invio di telemetria verso i nostri server è **opt-in esplicito**, mai attivo di default.
- Puoi disattivarlo in qualsiasi momento.
- Non condiziona il funzionamento dell'app: il BLI funziona identico con o senza telemetria.

---

## 9. Disponibilità e garanzie

L'app è fornita **"così com'è"** (as-is). Nei limiti consentiti dalla legge italiana, non rilasciamo garanzie esplicite o implicite oltre quelle previste dal Codice del Consumo per gli utenti consumatori italiani.

In particolare:

- Non garantiamo che il calcolo del BLI sia esente da bug.
- Non garantiamo continuità del servizio di telemetria (i server potrebbero essere temporaneamente non disponibili — l'app continuerà a funzionare localmente).
- Possiamo aggiornare l'app, modificare le funzionalità, ritirare l'app dal Play Store. In caso di ritiro, l'installazione esistente continuerà a funzionare localmente finché compatibile col sistema Android.

---

## 10. Limitazione di responsabilità

Nei limiti massimi consentiti dalla legge:

- Non siamo responsabili per decisioni che prendi sulla base dei numeri mostrati dall'app. Sono indicatori statistici, non consigli professionali.
- Non siamo responsabili per malfunzionamenti del dispositivo, dei suoi sistemi o di terze parti.
- Non siamo responsabili per perdita di dati locali in caso di disinstallazione, crash, factory reset, o errori utente.

Nulla in questo paragrafo esclude o limita responsabilità per dolo, colpa grave, danno alla persona, o qualunque altra responsabilità non escludibile per legge.

---

## 11. Proprietà intellettuale

- Il codice sorgente di Dopamine Monitor è ospitato in un repository privato non accessibile pubblicamente. I documenti legali (questa Privacy Policy e i Termini d'uso) sono pubblicati pubblicamente all'indirizzo https://atoffa978.github.io/dopamine-monitor-legal/ . Diritti di copia e modifica del codice riservati al titolare.
- "Body Load Index" e il modello v5 sono concetti originali sviluppati per questo progetto; descritti pubblicamente nelle specifiche tecniche del repository.
- Loghi, nome dell'app e identità visiva restano di proprietà del titolare (vedi Privacy Policy §2).

---

## 12. Modifiche a questi termini

Se aggiorniamo questi termini in modo significativo, te lo comunicheremo all'interno dell'app prima di applicarli, e ti chiederemo di rileggerli. Continuando a usare l'app dopo le modifiche, accetti la nuova versione.

---

## 13. Risoluzione

Puoi smettere di usare l'app in qualunque momento — basta disinstallarla. Non c'è abbonamento, non c'è disdetta da fare.

Possiamo sospendere o terminare l'erogazione del servizio di telemetria (non l'app stessa) in qualsiasi momento, dandone preavviso quando possibile.

---

## 14. Legge applicabile e foro

I presenti termini sono regolati dalla legge italiana. Per controversie con utenti consumatori italiani, è competente il foro del luogo di residenza o domicilio elettivo del consumatore.

---

## 15. Contatti

**dopamine.monitor.dev@gmail.com**

Vedi anche Privacy Policy §12.
