# Post-Discharge Cardiovascular Mortality Risk Prediction in Pará, Brazil
### A Comparative Analysis of XGBoost and Logistic Regression for In-Hospital Cardiovascular Mortality (2019–2023)

[![Status](https://img.shields.io/badge/status-in%20development-lightgrey)](.)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](.)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Preprint](https://img.shields.io/badge/preprint-pending-lightgrey)](.)

---

## Overview

Project 5 (regional-health-disparities-brazil) found that cardiac catheterization in Pará is concentrated in 2 of 144 municipalities. This project moves from geography to the patient level: given a cardiovascular admission in the Pará public hospital system (SIH-SUS), can in-hospital mortality be predicted at discharge, and does predicted risk track the patient's municipality-of-origin cluster from Project 5?

**Status:** data collection and modeling in progress. This section will report the central finding once notebooks 01–05 are complete.

---

## Key Figures

### ROC Curves — Logistic Regression vs. XGBoost
*(Figure pending — notebook 04)*

Comparative discrimination performance of both models on the 2022–2023 temporal test set.

---

### SHAP Summary — Feature Importance (XGBoost)
*(Figure pending — notebook 05)*

Ranked contribution of patient- and hospital-level variables to predicted mortality risk, including the Project 5 cluster-origin feature.

---

### Predicted Risk by Municipality of Origin
*(Figure pending — notebook 06)*

Geographic view of mean predicted mortality risk, grouped by the patient's Project 5 care-access cluster.

---

## Research Question

*What patient- and hospital-level variables available in SIH-SUS at discharge predict in-hospital cardiovascular mortality in Pará, Brazil (2019–2023), and how does XGBoost compare to logistic regression in discriminative performance?*

---

## Methods

**Data sources**

| Source | Variables | Coverage |
|---|---|---|
| DATASUS / SIH-SUS (AIH Reduzida) | Diagnosis, procedure, age, sex, length of stay, in-hospital death, municipality of residence | Pará, 2019–2023 |
| DATASUS / SIM | Declaração de Óbito — used only for the secondary 30-day linkage outcome | Pará, 2019–2023 |
| Project 5 output | `para_cardiovascular_clustered.csv` — joined on `MUNIC_RES` for the care-desert-origin feature | Pará, 2019–2023 |

**Pipeline**
```
Raw SIH-SUS export (PySUS)
→ Filter to cardiovascular admissions (ICD-10 I20–I99)
→ Encoding standardization (SEXO, COD_IDADE)
→ Join with Project 5 cluster labels on MUNIC_RES
→ Primary outcome: in-hospital mortality (MORTE)
→ Secondary outcome (time-boxed): SIM linkage, 30-day post-discharge mortality
→ Temporal split: train 2019–2021, test 2022–2023
→ Logistic regression baseline (class_weight='balanced')
→ XGBoost (scale_pos_weight, TimeSeriesSplit CV)
→ SHAP interpretation (TreeExplainer)
```

**Model results**

| Model | AUC-ROC | Sensitivity | Specificity | Brier score |
|---|---|---|---|---|
| Logistic Regression | TBD | TBD | TBD | TBD |
| XGBoost | TBD | TBD | TBD | TBD |

**Tools:** `Python 3.10` · `pandas` · `scikit-learn` · `xgboost` · `shap` · `pysus` · `recordlinkage`

---

## Methodological Notes

- **Primary outcome choice:** in-hospital mortality (`MORTE`) was set as the primary outcome because it requires no record linkage. 30-day post-discharge mortality (SIM linkage) is attempted as a secondary, time-boxed analysis — there is no shared unique ID between SIH-SUS and SIM, so linkage quality is not guaranteed.
- **Temporal train/test split:** train on 2019–2021, test on 2022–2023. A random split was rejected — it would leak information across time and doesn't reflect real deployment conditions.
- **Class imbalance:** handled via `class_weight='balanced'` (logistic regression) and `scale_pos_weight` (XGBoost), not resampling — preserves the true event rate for calibration.
- **Cluster-origin feature:** `MUNIC_RES` is joined against the Project 5 cluster assignments, testing whether a patient's structural care-access profile adds predictive value beyond individual clinical variables.

---

## Repository Structure

```
cardiac-mortality-prediction/
├── data/
│   ├── raw/          not committed (gitignored)
│   └── processed/    committed CSVs
├── notebooks/
│   ├── 01_data_inspection.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda.py
│   ├── 04_modeling.py
│   ├── 05_shap_interpretation.py
│   ├── 06_figure_styling.py
│   └── figures/
├── manuscript/
│   └── manuscript.docx
├── style.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Reproducibility

```bash
git clone https://github.com/g4bfernandoo/cardiac-mortality-prediction.git
cd cardiac-mortality-prediction
pip install -r requirements.txt
```

Raw data files are not included (size). Data are downloaded directly via PySUS from DATASUS — see `notebooks/01_data_inspection.py`. All data are publicly available under Brazil's Lei de Acesso à Informação (Law 12,527/2011).

Run notebooks in order: `01 → 02 → 03 → 04 → 05 → 06`

---

## Publication Status

`In development`

- Primary target: *International Journal of Cardiology* (Elsevier) — standard subscription submission route, no author-facing fee unless gold open access is selected.
- Backup targets: *Cadernos de Saúde Pública* or *Revista Panamericana de Salud Pública/PAJPH* — diamond open access, no fee, PubMed/Scopus indexed.
- Preprint: medRxiv (pending)

---

## Author

**Gabriel Fernando**
· Prospective BME undergraduate researcher · Cardiovascular data science

[GitHub](https://github.com/g4bfernandoo) · [ORCID](https://orcid.org/0009-0003-6367-7000)

---

*Data: DATASUS (Ministério da Saúde). Publicly available under Lei nº 12.527/2011.*
