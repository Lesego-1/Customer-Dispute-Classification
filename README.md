# 🧾 Customer Dispute Classification

A Machine Learning-powered web application that classifies and summarizes customer complaints submitted to banks — helping financial institutions better understand dissatisfaction and prioritize urgent product improvements.

## 🚀 Overview

This project analyzes real-world complaints submitted to banks and financial institutions. Users submit a customer complaint via a simple web interface, which then sends the text to a Django RESTful API. The API performs two key tasks:

1. **Dispute Prediction**  
   Predicts whether the customer is likely to escalate the complaint into a formal dispute — a strong indicator of serious dissatisfaction.

2. **Complaint Summarization**  
   Automatically summarizes the complaint using a transformer model to extract the core issue from the customer's message.

> 🔍 This dual insight helps banks and financial services:
> - Prioritize critical complaints that are likely to lead to disputes
> - Identify which products are causing the most dissatisfaction
> - Gain concise summaries for faster issue prioritization
> - Make data-driven decisions on where to improve product experience

---

## 💼 Business Impact

- **Customer Retention**: Early detection of disputes can prevent churn and reputational damage.
- **Operational Efficiency**: Summarization enables support teams to respond faster.
- **Product Feedback Loop**: Provides structured feedback from unstructured data to guide product development.
- **Risk Mitigation**: Helps flag systemic issues before they escalate into regulatory or legal concerns.

---

## 🧠 Technical Stack

- **Backend**: Django & Django REST Framework (DRF)
- **Frontend**: TailwindCSS + JavaScript (Generated with assistance from ChatGPT.)
- **ML Models**:
  - Dispute Prediction: Scikit-learn / TensorFlow (ongoing model tuning)
  - Text Summarization: Hugging Face `transformers.pipeline("summarization")`
- **Vectorization**: Word2Vec

---

## 📊 Machine Learning Workflow

- **Data Source**: Real-world customer complaints from multiple financial institutions
- **Preprocessing**:
  - Text cleaning (removal of noise, stopwords, lowercasing)
  - Tokenization and vectorization
- **Modeling**:
  - ML & DL classifiers (Logistic Regression, Dense Networks, Bi-LSTM)
  - Performance tuning and validation
- **Evaluation**:
  - Accuracy, Recall (important for dispute detection), and F1 Score

> 🎯 *Current Goal:* Improve model performance to reach at least **70–80% accuracy** for dispute prediction.

---

## 🔧 How It Works

1. **User submits complaint** via form on the frontend.
2. **AJAX POST request** is sent to the Django REST API.
3. API:
   - Loads trained ML model and vectorizer
   - Predicts dispute likelihood
   - Summarizes complaint using Hugging Face pipeline
4. **JSON Response** is sent back with:
   - Prediction (`Dispute` or `No Dispute`)
   - Confidence score
   - Complaint summary
5. Results are dynamically rendered on the same page.

---

## 🛠️ Project Setup

Clone the repository and run the app locally:

```bash
git clone https://github.com/Lesego-1/Customer-Dispute-Classification.git
cd Complaints-NLP

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the Django server
python manage.py runserver
