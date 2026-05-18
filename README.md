# dopamine-monitor-legal

Documenti legali pubblici di [Dopamine Monitor](https://github.com/atoffa978/dopamine-monitor),
app Android di auto-osservazione passiva dell'uso del telefono.

Servito via GitHub Pages all'indirizzo dichiarato nei documenti stessi e nell'app:

**https://atoffa978.github.io/dopamine-monitor-legal/**

## Contenuto

- `index.html` — landing con link ai due documenti
- `privacy.html` — Privacy Policy renderizzata in HTML
- `terms.html` — Termini d'uso renderizzati in HTML
- `PRIVACY_POLICY.md` — sorgente Markdown (stesso file bundlato nell'app sotto `assets/legal/`)
- `TERMS_OF_USE.md` — sorgente Markdown (idem)
- `404.html` — fallback

## Aggiornamento

I file `.md` di questo repo devono restare **identici** alle copie in
`dopamine-monitor/docs/PRIVACY_POLICY.md` e `dopamine-monitor/docs/TERMS_OF_USE.md`
(che sono a loro volta replicate in `dopamine-monitor/assets/legal/`).

Quando si aggiorna un documento:

1. Modificare il sorgente nel repo principale (`dopamine-monitor/docs/`).
2. Replicare in `dopamine-monitor/assets/legal/` e rebuildare l'app.
3. Copiare gli stessi `.md` qui e rigenerare gli `.html`
   (script `build.py` allegato — richiede Python 3 e `pip install markdown`).
4. Bumpare il numero di versione e la data "In vigore dal" in cima ai documenti.

```bash
python3 build.py
git add . && git commit -m "Update docs vX.Y" && git push
```

## Stile

Pagina statica, HTML+CSS inline, zero JavaScript, zero tracker, zero cookie.
Coerente con la Privacy Policy stessa (§10).

## Lingua autoritativa

Italiano. Nessuna traduzione ufficiale al momento.

## Licenza

I documenti sono pubblicati per trasparenza e per permettere agli utenti
di leggerli prima di installare l'app. Diritti di copia e modifica dei
testi riservati al titolare (vedi `TERMS_OF_USE.md` §11).
