# 🛡️ E-Commerce Customer Churn Prediction & Retention System

## 📌 Overview

This project is a complete **Customer Analytics Platform** designed to predict customer churn and automate retention strategies for e-commerce and subscription-based businesses.

The system uses machine learning to identify customers who are likely to stop purchasing within the next 30 days and provides actionable insights such as segmentation, personalized campaigns, and revenue impact estimation.

---

## 🚀 Features

### 🔍 Churn Prediction

* Predicts probability of customer churn within 30 days
* Built using a classification model (Random Forest)
* Achieves strong performance (~0.80 AUC)

### 📊 Customer Segmentation

* Customers are categorized into:

  * Critical
  * High Risk
  * Medium Risk
  * Low Risk

### 📈 RFM Analysis

* Uses Recency, Frequency, Monetary metrics
* Generates RFM scores for customer behavior analysis

### 🧠 Churn Reason Identification

* Identifies why a customer is likely to churn:

  * Low engagement
  * High cart abandonment
  * Inactivity
  * Behavioral decline

### 📧 Automated Retention Campaigns

* Generates professional, personalized emails
* Segment-based campaign strategies
* Editable email before sending
* Ready for real email integration (SMTP)

### 💰 Customer Lifetime Value (CLV)

* Uses CLV to prioritize high-value customers
* Helps focus retention efforts where it matters most

### 📉 Revenue Impact Dashboard

* Estimates revenue saved by preventing churn
* Displays business impact of retention strategies

### 🛒 Product Recommendation Strategy

* Suggests actions like:

  * Cart recovery offers
  * Trending product recommendations
  * Premium product targeting

---

## 🏗️ Project Structure

```
churn_prediction/
│
├── data/                     # Generated dataset
├── models/                   # Trained model & outputs
│
├── generate_dataset.py       # Synthetic data generation
├── train.py                  # Model training & segmentation
├── retention.py              # Retention logic
├── email_templates.py        # Email content
└── app.py                    # Streamlit dashboard

```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/churn-prediction.git
cd churn-prediction
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Step 1: Generate dataset

```bash
python generate_dataset.py
```

### Step 2: Train model

```bash
python train.py
```

### Step 3: Run dashboard

```bash
streamlit run app.py
```

---

## 🖥️ Dashboard Features

* Churn probability prediction
* Risk segmentation
* Feature importance visualization
* Customer grouping by segment
* Email campaign generation
* Editable email interface
* Send email (simulation + future ready)
* Revenue impact metrics
* RFM scoring display

---

## 📊 Tech Stack

* **Python**
* **Pandas / NumPy**
* **Scikit-learn**
* **Streamlit**
* **Plotly**
* **SMTP (for email integration)**

---

## 🧪 Dataset

A synthetic dataset of 5000+ customers is generated including:

* Customer behavior
* Purchase history
* Engagement metrics
* Support interactions
* CLV values

---

## 🔮 Future Work

Currently, due to the lack of access to real e-commerce data, a realistic synthetic dataset has been created to simulate customer behavior and validate the system.

In future, the system will be:

* Integrated with real e-commerce platforms
* Connected to live databases
* Fully automated for real-time prediction and campaign execution
* Enhanced with real product recommendation systems

---

## 🎯 Target Users

* E-commerce companies
* D2C brands
* Subscription-based platforms

---

## 🧠 Key Highlights

* End-to-end ML pipeline
* Business-focused analytics
* Real-world use case
* Scalable and modular design

---

## 📌 Author

Developed as a final year project in Computer Science.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!

