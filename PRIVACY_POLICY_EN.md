# Privacy Policy — Dopamine Monitor (English)

**Effective date**: 20 May 2026
**Document version**: 1.3
**Authoritative language**: Italian

> The Italian version of this Privacy Policy is the legally binding text. This English translation is provided in good faith for the convenience of non-Italian-speaking users. In case of any discrepancy or legal dispute, the Italian version prevails.

---

## 1. In two lines

Dopamine Monitor is a **passive self-observation** app for phone usage. Everything that concerns you personally — which apps you use, when, for how long — stays on your device. To our servers we send only, **if you accept**, a small pseudonymized daily summary to improve the statistical model. We do not sell data to anyone, we do not show advertising, we do not profile you.

If this is enough, you can stop reading. For the details, continue.

---

## 2. Who we are

**Data controller**: Angelo Toffaletti
**Address**: Via Centro di Romagnano 38, 37023 Grezzana (VR), Italy
**Contact email**: dopamine.monitor.dev@gmail.com

For any request regarding the processing of your personal data, write to the email address above. We respond within 30 days.

---

## 3. What data the app collects on your device

To work, Dopamine Monitor reads from the Android system **phone usage data**. This data **never leaves the device** except as described in §5 ("Telemetry"), and only after being aggregated into synthetic 0-100 scores (never with the names of individual apps).

### 3.1 What it reads

- **App usage statistics** (Usage Stats / Digital Wellbeing): for each app, how many minutes you have used it in the foreground and in which time slots. This is the fundamental data to build the daily "Dopa Index".
- **Notification events** (Notification Access): numerical count of notifications received and opened. We do not read the content of notifications, only that they occurred.
- **List of apps installed on the device** (launchable apps): only to categorize their type (social, gambling, productivity, etc.) during calculation. Read on-demand, never transmitted.

### 3.2 What it **NEVER** reads

- Never content of messages, calls, emails, photos, files, browser history, contacts, calendar.
- Never GPS location.
- Never microphone, camera, biometric sensors.
- Never keyboard input or accessibility services.
- Never Google account data or login.

### 3.3 Where data is stored on the device

All raw data (events of the current day) and aggregated data (daily history, up to 60 days) are stored **locally** in:

- `SharedPreferences` standard Android (preferences and state),
- private app files (persistent history).

They are accessible **only to the app itself**. When you uninstall Dopamine Monitor, they are automatically deleted by the Android system.

You can also delete all local data at any time from within the app: Settings → "Erase all data".

---

## 4. Android permissions required

The app works only if you grant the following permissions. You actively grant them from Android system settings. You can revoke them at any time.

| Permission | Purpose | What happens if you deny it |
|---|---|---|
| **Access to usage statistics** (`PACKAGE_USAGE_STATS`) | Read how much time you spend on apps | The app cannot work and will tell you |
| **Access to notifications** (`NotificationListener`) | Count notifications received (not content) | The "notifications" axis of the Dopa Index stays at zero, but the rest works |
| **Background execution** | Update history every day at midnight | You must open the app manually to see updated data |

We do not request permissions for location, contacts, microphone, camera, SMS, storage, etc.

---

## 5. Telemetry to our servers (optional, opt-in)

This is the only circumstance in which data concerning you leaves the device. **You must consent explicitly** during onboarding or from Settings: without your explicit consent, the app does not send anything to any server.

### 5.1 Purpose

To improve the statistical model of the Dopa Index and calibrate it on a population of real users. We see aggregated distributions (e.g., "the average Dopa Index of users after 30 days of use is X"), not individual data.

### 5.2 What is sent

Exactly one small JSON summary for each closed day you have on the device. The complete schema is documented in the source code (`lib/telemetry/payload_builder.dart`). It contains:

- Numbers from 0 to 100 for the overall Dopa Index and for each of the 8 axes (fragmentation, intensity, compulsive frequency, immediate reward, variable reward, anticipation, control anxiety, out-of-context use).
- Which axis was "dominant".
- Which "patterns" were activated (e.g., "post-23:00 use").
- App version, Android version.
- An observation "bucket" (`new` < 14 days, `established` 14-89, `long` ≥ 90) instead of the exact number of days of use — this to prevent the precise number from allowing us to recognize the individual device.
- Number of friction events (popups) triggered and respected during the day.
- A `dedup_hash` field: a 16-character hexadecimal string generated locally by the app as `SHA-256(install_id + "|" + observation_day)`, truncated. It serves only to prevent the server from accepting the same day twice (deduplication). The server **never receives the install_id** and **cannot reconstruct it** from the hash (one-way function). Because the observation day is part of the hash input, two different days from the same device generate different hashes that are **not linkable to each other** server-side.

### 5.3 What is **NEVER** sent

- Never the `install_id` in clear (the server only receives dedup_hash, a one-way function).
- Never the name of a specific app you used.
- Never individual usage durations (only the aggregated score).
- Never content, messages, personal identifiers, email, phone number, IMEI, MAC addresses, advertising identifiers.
- Never location, sensors, browser history.

### 5.4 Identification and legal nature of the data

The app generates locally, on first opening, a random identifier called `install_id` (UUIDv4, 32 hexadecimal characters). It is not linked to your Google account, IMEI, name or email, or any login. **The install_id never leaves the device**: it is used only as local input to generate the `dedup_hash` (see §5.2) and to allow you, on your request, to exercise the right to erasure (§7.4).

The payloads we receive on our servers are **pseudonymized**, not anonymous, within the meaning of Art. 4 No. 5 GDPR. The difference is important:

- **Anonymous** means the data cannot in any way be traced back to a specific person, not even with additional information. Anonymous data is not personal data and falls outside GDPR.
- **Pseudonymized** means the data does not contain direct identifiers (name, email, phone number), but is linked to a key (in our case, the `dedup_hash`) that could allow tracing to the person if that key were combined with other information — specifically, if you communicate your `install_id` to us, we can recompute the set of dedup_hashes that correspond to you and identify your records.

On our server, by itself, a dedup_hash is an apparently random number: we do not know which install_id it corresponds to, and we cannot link it to other payloads from the same device. It becomes an identification key only if you communicate your install_id to us (to exercise your rights — see §7). For this reason we treat your payloads **as personal data under GDPR**, applying all the safeguards of the Regulation (explicit consent, purpose limitation, limited retention, data subject rights).

The **aggregated statistical distributions** we produce from the payloads (e.g., means, distributions, standard deviations across the entire user population) are instead anonymous data, because they lose any key during the aggregation process.

### 5.5 Where the data is sent

Data is sent via HTTPS to servers operated by **Scaleway**, located in the European Union (Paris, FR). Scaleway acts as a "processor" within the meaning of GDPR. See: https://www.scaleway.com/en/privacy/

### 5.6 How long we keep it

Payloads are kept for **a maximum of 24 months** from receipt, then automatically deleted. Aggregated distributions (means, statistics) may be kept longer because they do not contain individual records.

### 5.7 How to withdraw consent

At any time you can go to Settings → "Telemetry" and choose "Do not participate". From that moment the app will no longer send anything. **What has already been sent in the past remains on our servers until the 24 months expire**, unless you explicitly request early deletion (see §7.4 — right to erasure).

---

## 6. Legal basis for processing

- For data that stays **on the device** (§3): there is no "processing" by us under GDPR, because we neither receive nor access this data. It is your data on your device, for personal use.
- For **telemetry** to our servers (§5): the legal basis is your **explicit consent** (Art. 6(1)(a) GDPR). Without consent, no transmission.

---

## 7. Your GDPR rights

To exercise your rights over the payloads transmitted to our server via optional telemetry, you must communicate your `install_id` to us (you find it in the app: Settings → Telemetry section → "Show installation ID" button). Without the `install_id` we cannot identify your specific records in the database, because on the server we only see apparently random dedup_hashes and do not know which belong to you. For data that stays on the device, you have full control from the app itself.

### 7.1 Right to information
You are reading this document.

### 7.2 Right of access (Art. 15 GDPR)
You can ask us if we process data referable to your device and receive a copy of the transmitted payloads. To do so, we need your `install_id`. Write to dopamine.monitor.dev@gmail.com.

### 7.3 Right to rectification (Art. 16 GDPR)
The transmitted data is calculated numerical scores: there is nothing to "rectify". If the app calculates a value incorrectly (e.g., engine bug), you can report it with the in-app feedback button.

### 7.4 Right to erasure (Art. 17 GDPR)
You can request early deletion of the payloads referring to your device. The procedure:

1. Retrieve your `install_id` from the app: Settings → Telemetry section → "Show installation ID" → "Copy" button.
2. Write to dopamine.monitor.dev@gmail.com with subject "GDPR data deletion request" and the `install_id` in the body.
3. Server-side we recompute the set of possible dedup_hashes for that device (one for each observation day, up to a maximum of 730) and delete all corresponding records from the database.
4. You will receive confirmation within **30 days** from receipt of the request, as required by Art. 17 GDPR.

See also the dedicated page: https://atoffa978.github.io/dopamine-monitor-legal/data-deletion-en.html

### 7.5 Right to restriction (Art. 18 GDPR)
You can request that your data be "frozen" without further processing. Write to us.

### 7.6 Right to object and portability (Art. 20-21 GDPR)
You can request a copy of the transmitted payloads in JSON format. They are already structured, just request them (with install_id, as for deletion).

### 7.7 Right to lodge a complaint (Art. 77 GDPR)
If you believe the processing of your data violates GDPR, you can lodge a complaint with the supervisory authority:

- **Italy**: Garante per la Protezione dei Dati Personali — https://www.garanteprivacy.it/
- Or the authority of the EU country where you habitually reside.

---

## 8. Children's data

The app is intended for adults (18 years or older), consistent with the target age range declared on the Google Play Store. We do not intentionally request data from minors. If you are a parent or guardian and believe that a minor under your responsibility uses the app, contact us and we will delete any data that may have been transmitted.

---

## 9. Extra-EU transfers

Telemetry servers are in the EU (Scaleway, Paris). We do not transfer data outside the EU.

---

## 10. Cookies, trackers, advertising

The app **does not use**: cookies, advertising trackers, fingerprinting, third-party analytics SDKs (no Google Analytics, no Firebase Analytics, no Crashlytics, no Mixpanel, no Amplitude, etc.), advertising of any kind, marketing communications.

The app **uses**:

- an internal logging library of the Flutter framework (development/debug, not telemetry),
- the network connection only for the transmission of telemetry (§5) and, in the future, any update notice of the model.

---

## 11. Changes to this policy

When we update this policy, we will inform you by:

1. Updating the version number and date at the top.
2. Showing an in-app notice the first time you open a new version with updated policy.

If the update concerns the expansion of transmitted data or new processing purposes, **we will request your explicit consent again** before applying them.

---

## 12. Contacts

For any question, access request, or report, write to us at:

**dopamine.monitor.dev@gmail.com**

We respond within 30 days.