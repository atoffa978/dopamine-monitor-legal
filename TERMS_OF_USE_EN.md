# Terms of Use — Dopamine Monitor

**Effective from**: 18 May 2026
**Document version**: 1.1
**Authoritative language**: Italian

> **English-language notice.** This document is the English translation of the official Italian Terms of Use. We provide it in good faith to make our terms accessible to non-Italian-speaking users. In case of any discrepancy, ambiguity, or legal dispute, **the Italian version (`terms_of_use.md`) is the legally binding text**. The Italian version is published at https://atoffa978.github.io/dopamine-monitor-legal/ and inside the app.

---

## 1. What Dopamine Monitor is

Dopamine Monitor is an Android application for Android 9.0 and later that passively observes how you use your phone and returns a daily "structural mirror" — a composite index called the **Dopa Index** — meant to help you recognise compulsive usage patterns (post-23:00 use, attentional fragmentation, excessive exposure to dopaminergic content).

**The app is a tool for self-observation, not a medical device.** The numbers you see are statistical indicators based on a documented model (see §5), not clinical diagnoses.

---

## 2. Acceptance

By installing and using Dopamine Monitor, you accept these Terms of Use and the linked Privacy Policy. If you do not agree, simply uninstall the app.

---

## 3. Who it is intended for

Adults interested in observing their own phone use for purposes of self-awareness. It is not a clinical, therapeutic, diagnostic, preventive or treatment tool for mental, behavioural or substance-use disorders.

The app is **not intended** for: minors under 14, people undergoing clinical treatment for technology-related disorders or behavioural addictions without their specialist's supervision, professional use (HR, schools, monitoring of third parties).

---

## 4. What Dopamine Monitor is NOT

To avoid misunderstandings:

- **It is not a parental-control app.** It is not designed to monitor children, employees, partners, or other people. It is a **self**-observation app.
- **It is not an app blocker.** Optional "friction" popups exist, but they are invitations, not blocks: the user can always proceed.
- **It is not a medical app.** Dopa Index scores do not replace clinical assessments. If you have serious concerns about your relationship with technology, consult a professional.
- **It is not a motivational coach.** It does not tell you what to do, it does not send "encouragement" push notifications, it does not gamify abstinence. It shows data, full stop.
- **It is not a cloud service.** Your usage data stays on your device (see Privacy Policy §3-§4). The only possible transmission is an optional, aggregated, anonymous telemetry payload (Privacy Policy §5).

---

## 5. What it actually does

The app reads three categories of data from the Android system (with your explicit permission):

1. **Per-app usage time** (Usage Stats)
2. **Count of notifications received/opened** (Notification Listener)
3. **List of installed apps** (only to categorise them)

From these it computes, once a day, eight "axes" (social high-dopamine, video binge, infomania, body monitoring, hyperactive productivity, notifications, night use, fragmentation) and combines them into a 0-100 index called the Dopa Index.

The statistical model and its limitations are documented in the project's technical specifications (see `docs/bli-v5-proposta-v0.5.2.md` in the repository). The model is referred to as "v0.1" at launch and is subject to subsequent revisions.

---

## 6. Limitations of the model

Be aware of the tool's limits:

- **The Dopa Index is an estimate, not a measurement.** The weights assigned to the various app categories are based on literature and clinical best-guess; they are not epidemiologically validated.
- **App categorisation is imperfect.** The app classifies installed packages according to an internal baseline that covers the most popular apps in Italy. Unrecognised apps end up in the "other" category with reduced weight. You can correct this manually from Settings.
- **Android "usage time" only measures foreground with the screen on.** An app like Spotify in the background is not counted; an app like WhatsApp that is open but not being watched is counted.
- **Extreme personal patterns (night-shift work, inverted time bands, etc.) can produce false positives.** The app cannot know.
- **There is no ground truth.** We do not know "what your correct Dopa Index is". The tool exists to observe variations over time, not to set absolute thresholds.

If you see a very high Dopa Index or alarming patterns, **it is not a diagnosis**. It is an invitation to pause and think. If you are genuinely worried about your relationship with the phone, talk to someone you trust or to a qualified professional.

---

## 7. Friction: what it is and what it is not

The app may, in some cases, display "friction" popups (e.g. before opening a social app after 23:00). They are:

- **Invitations, not blocks**: you can always proceed by pressing "Continue".
- **Statistically recorded**: the app counts how many popups you have seen and how many you have respected. It is a self-observation metric, not a "performance" score.
- **Deactivatable**: from Settings you can disable friction popups while keeping the Dopa Index calculation active.

---

## 8. Optional telemetry

See Privacy Policy §5. For clarity:

- Telemetry transmission to our servers is **explicit opt-in**, never on by default.
- You can disable it at any time.
- It does not condition the operation of the app: the Dopa Index works identically with or without telemetry.

---

## 9. Availability and warranties

The app is provided **"as is"**. Within the limits allowed by Italian law, we make no express or implied warranties beyond those provided by the Italian Consumer Code for Italian consumer users.

In particular:

- We do not warrant that the Dopa Index calculation is free of bugs.
- We do not warrant continuity of the telemetry service (the servers may be temporarily unavailable — the app will continue to function locally).
- We may update the app, modify its features, or withdraw the app from the Play Store. In the event of withdrawal, an existing installation will continue to function locally as long as it remains compatible with the Android system.

---

## 10. Limitation of liability

To the maximum extent permitted by law:

- We are not liable for decisions you make on the basis of the numbers shown by the app. They are statistical indicators, not professional advice.
- We are not liable for malfunctions of the device, its systems, or third parties.
- We are not liable for loss of local data resulting from uninstallation, crashes, factory reset, or user error.

Nothing in this paragraph excludes or limits liability for wilful misconduct, gross negligence, personal injury, or any other liability that cannot be excluded under applicable law.

---

## 11. Intellectual property

- Dopamine Monitor's source code is hosted in a private repository not publicly accessible. The legal documents (this Privacy Policy and the Terms of Use) are published publicly at https://atoffa978.github.io/dopamine-monitor-legal/ . Rights to copy and modify the code are reserved by the controller.
- "Dopa Index" (the user-facing name of the composite index; in internal technical documentation it is still referenced as "Body Load Index / BLI v5") and the underlying model are original concepts developed for this project; they are publicly described in the technical specifications in the repository.
- The app's logos, name, and visual identity remain the property of the controller (see Privacy Policy §2).

---

## 12. Changes to these terms

If we update these terms significantly, we will notify you inside the app before applying them, and ask you to re-read them. By continuing to use the app after the changes, you accept the new version.

---

## 13. Termination

You can stop using the app at any time — just uninstall it. There is no subscription, no cancellation to handle.

We may suspend or terminate provision of the telemetry service (not the app itself) at any time, providing notice where possible.

---

## 14. Governing law and venue

These Terms are governed by Italian law. For disputes with Italian consumer users, the court of the consumer's place of residence or elected domicile has jurisdiction.

---

## 15. Contact

**dopamine.monitor.dev@gmail.com**

See also Privacy Policy §12.
