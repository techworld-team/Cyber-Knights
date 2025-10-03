# Cyber-Knights
# Dataset Documentation – AI Phishing Detection Project

This document explains the datasets used in our project, how they were collected, and how they were cleaned for model training.

---

## 📂 Dataset Sources

- **Emails Dataset (Emails.csv)**
  - Source: Kaggle – Phishing Email Dataset
  - Type: Text data (subject + body of emails)
  - Labels: `phishing` (1) or `safe` (0)

- **URLs Dataset (url.csv)**
  - Source: UCI Phishing Websites Dataset
  - Type: URL strings
  - Labels: `phishing` (1) or `safe` (0)

---

## 🛠️ Preprocessing Steps

### 1. Emails
- Converted all text to **lowercase**  
- Removed **punctuation, numbers, and special characters**  
- Removed **stopwords** (e.g., "the", "is", "and")  
- Applied **tokenization** (split text into words)  
- Saved clean text in **`emails_clean.csv`**  
- Feature representation: **TF-IDF vectors** (used later by ML1)

### 2. URLs
- Extracted numerical features:
  - URL length
  - Number of digits, dots, hyphens
  - Presence of `https`, `@`
  - Suspicious keywords (`login`, `bank`, `verify`)
- Saved processed features in **`urls_features.csv`**  
- Feature scaling done for ML models (used later by ML2)

---

## 📊 Data Balance

- Checked for **class imbalance** (phishing vs safe).  
- Ensured **balanced train/test splits** for fair evaluation.  

---

## 📂 File Structure

data/
├── raw/ # Original datasets
│ ├── Emails.csv
│ ├── url.csv
├── processed/ # Cleaned datasets
│ ├── emails_clean.csv
│ ├── urls_features.csv
preprocessing/
├── email_cleaning.py # Script for email preprocessing
├── url_features.py # Script for URL preprocessing
docs/
├── README.md # This file (dataset documentation)

---

## ✅ Deliverables from Member 1 (DS1)

- Collected & documented datasets  
- Created preprocessing scripts (`email_cleaning.py`, `url_features.py`)  
- Generated clean datasets (`emails_clean.csv`, `urls_features.csv`)  
- Shared cleaned datasets with:
  - **Member 2 (ML1)** → for email model training  
  - **Member 3 (ML2)** → for URL model training  
- Prepared documentation (this README + slides for PPT)  

---

## 📌 Notes for Judges/Reviewers

- Data is **real-world phishing data**, not synthetic.  
- Preprocessing ensures **fair and unbiased models**.  
- Pipeline is reusable → future data can be re-cleaned automatically.  
