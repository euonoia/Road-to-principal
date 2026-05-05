# ICU Silent Deterioration Spotter (VitalBeat)  
### IBM Dev Day: Bob Edition Hackathon | May 2026

## 🚩 The Problem: The "Snapshot" Trap
Every year, 1.75 million ICU nurses conduct over 300 million patient handoffs in the U.S. alone[cite: 1]. Communication failure during these handoffs is the leading cause of preventable adverse events[cite: 1]. 

The standard protocol, **SBAR**, captures a **snapshot**, not a **trajectory**[cite: 1]:
* **The Reality:** A heart rate of 92 looks "fine" in isolation, but if it was 74 six hours ago and is climbing while urine output drops, the patient is in a countdown to a code[cite: 1].
* **Invisible Killers:** Compensated shock, early AKI, and pre-respiratory failure are undetectable by snapshot-based tools[cite: 1].

## 💡 The Solution: VitalBeat
**VitalBeat** is a multi-agent clinical intelligence system built with **IBM Bob**[cite: 1]. It transforms raw EHR data into **trajectory-aware patient intelligence** to support nurses at the most critical moment: the shift change[cite: 1].

The system ingests six hours of ICU data and synthesizes it into a single-page **SBAR+ brief** that can be read in under 60 seconds[cite: 1].

## 🤖 Multi-Agent Architecture
Our system utilizes four specialized agents running in parallel to mimic a multidisciplinary clinical team[cite: 1]:

*   **Trend Agent:** Calculates velocity and acceleration of vital signs, scoring patients on direction rather than static thresholds[cite: 1].
*   **Lab-Conflict Agent:** Detects cross-signal patterns that appear normal individually but are dangerous together (e.g., rising lactate with stable blood pressure)[cite: 1].
*   **Time Bomb Agent:** A forward-looking agent tracking pending labs, upcoming medications, and untouched PRN orders[cite: 1].
*   **Coordinator Agent:** The "Synthesizer" that compiles the three outputs into a color-coded (Red, Yellow, Green) brief with full auditability[cite: 1].

## 📊 Technical Validation (MIMIC-IV)
To validate the concept, we built a simulation environment using the **MIMIC-IV** dataset[cite: 1].
* **Scale:** 100 concurrent ICU patients monitored in real-time[cite: 1].
* **Effectiveness:** The system identified clinically significant flags in **37% of patients**—including shock signatures—that traditional tools would have missed[cite: 1].

## 🔗 Project Links
* **Repository:** [GitHub - ICU Silent Deterioration Spotter](https://github.com/NeelNakrani/icu-silent-deterioration-spotter)
* **Presentation:** [VitalBeat IBM Demo](https://www.youtube.com/watch?v=Mnu0Q7xomD4)

---
*Built for IBM Dev Day: Bob Edition*