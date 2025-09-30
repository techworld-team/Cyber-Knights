# 🚀 AI-Powered Phishing Detection System (Emails + URLs)

An AI-based system to detect **phishing emails** and **malicious URLs** using a dual-model approach:  
- **Email Model (NLP-based)** → Detects phishing emails with TF-IDF & DistilBERT.  
- **URL Model (Feature-based ML)** → Detects phishing websites using feature engineering + XGBoost.  
- **Frontend (Streamlit)** → Simple, interactive web app to test email/URL inputs in real-time.  

---

## 👥 Team Members
- **Member 1: Ayushi Sharma** – Data Scientist (Dataset Collection, Preprocessing, Evaluation)  
- **Member 2: Amit Kumar** – Email Model Engineer (Phishing Email Detection – NLP)  
- **Member 3: Khushi Sonkar** – URL Model Engineer (Phishing URL Detection – Feature Engineering + ML)  
- **Member 4: Akash Bhujabal** – Frontend & Integration Developer (Streamlit UI + Deployment)  

---

## 🏗 Project Workflow
1. **Data Collection & Preprocessing** → Kaggle Phishing Emails Dataset + UCI Phishing Websites Dataset.  
2. **Email Model (NLP)** → TF-IDF baseline + DistilBERT advanced model.  
3. **URL Model (ML)** → Feature extraction + Random Forest + XGBoost.  
4. **Integration** → Models integrated into a **Streamlit web app**.  
5. **Deployment** → Streamlit Cloud / Hugging Face Spaces.  

---

## ⚙️ Tech Stack
- **Languages**: Python  
- **ML Libraries**: scikit-learn, XGBoost, TensorFlow/PyTorch, Hugging Face Transformers  
- **Data Processing**: pandas, numpy, nltk, regex  
- **Visualization**: matplotlib, plotly  
- **Frontend**: Streamlit  
- **Collaboration**: GitHub, Trello/Notion, Google Drive  

---

## 📂 Repository Structure
phishing-detection-ai/
│── data/ # datasets (emails.csv, urls.csv)
│── preprocessing/ # cleaning & feature extraction
│ ├── email_cleaning.py
│ ├── url_features.py
│── models/ # trained models
│ ├── email_model.pkl
│ ├── url_model.pkl
│── app/ # frontend (Streamlit app)
│ ├── streamlit_app.py
│── docs/ # documentation & results
│ ├── model_results.md
│ ├── workflow.png
│ └── ppt/
│── requirements.txt # dependencies
│── README.md # project overview


---

## 🚀 How to Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/phishing-detection-ai.git
   cd phishing-detection-ai
Install dependencies:

pip install -r requirements.txt
Run the app:

streamlit run app/streamlit_app.py
Open in browser at: http://localhost:8501

🌍 Deployment
The project will be deployed on Streamlit Cloud (or Hugging Face Spaces).
👉 Demo link will be added here once deployed.

🎯 Future Scope
Support SMS phishing detection.

Deploy as browser extension for real-time URL checks.

Integrate with corporate email security systems.

Continuous learning with active retraining on new phishing data.

🙌 Acknowledgments
Datasets: Kaggle Phishing Emails, UCI Phishing Websites

Open-source libraries & tools that made this project possible.
