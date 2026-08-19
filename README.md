# Credit Card Fraud Detection

An end-to-end machine learning application for detecting potentially fraudulent credit card transactions through an interactive Streamlit dashboard.

The project combines **machine learning, data analysis, visualization, and real-time prediction** into a single web-based application. A trained Random Forest classifier analyzes transaction attributes and classifies transactions as either **genuine** or **potentially fraudulent**.

---

## Overview

Credit card fraud detection is a classification problem where the goal is to identify suspicious transactions while minimizing false positives.

This project provides an interactive interface that allows users to:

* Analyze transaction datasets
* Explore fraud-related patterns
* Visualize transaction distributions and correlations
* Enter individual transaction details
* Generate real-time fraud predictions using a trained machine learning model

The application is built with **Python and Streamlit**, making the model accessible through a simple and responsive web interface.

---

## Key Features

### Machine Learning Prediction

* Random Forest classification model
* Real-time transaction classification
* Supports individual transaction prediction
* Pre-trained model loaded using Joblib

### Data Analysis

* CSV dataset upload
* Dataset preview
* Row and column statistics
* Missing-value analysis
* Fraud transaction distribution

### Data Visualization

* Fraud vs. genuine transaction analysis
* Numerical feature correlation heatmap
* Interactive dashboard-based data exploration

### Interactive Dashboard

Users can provide transaction attributes such as:

* Transaction amount
* Transaction hour
* Merchant category
* Foreign transaction indicator
* Location mismatch indicator
* Device trust score
* Transaction velocity
* Cardholder age

The application processes these features and generates a fraud classification.

---

## Machine Learning Model

The application uses a trained **Random Forest Classifier** for binary classification.

The serialized model is stored in:

```text
credit_card_fraud_model.pkl
```

### Model Features

| Feature               | Description                                       |
| --------------------- | ------------------------------------------------- |
| `amount`              | Transaction amount                                |
| `transaction_hour`    | Hour at which the transaction occurred            |
| `merchant_category`   | Encoded merchant category                         |
| `foreign_transaction` | Foreign transaction indicator                     |
| `location_mismatch`   | Location mismatch indicator                       |
| `device_trust_score`  | Device trust score                                |
| `velocity_last_24h`   | Transaction velocity during the previous 24 hours |
| `cardholder_age`      | Cardholder age                                    |

### Output

The model produces a binary classification:

```text
0 → Genuine Transaction
1 → Fraudulent Transaction
```

---

## Technology Stack

| Technology   | Purpose                         |
| ------------ | ------------------------------- |
| Python       | Core programming language       |
| Streamlit    | Interactive web application     |
| Pandas       | Data processing and analysis    |
| Scikit-learn | Machine learning                |
| Joblib       | Model serialization and loading |
| Matplotlib   | Data visualization              |
| Seaborn      | Statistical visualization       |

---

## Project Structure

```text
credit-card-fraud-detection/
│
├── application.py
├── credit_card_fraud_model.pkl
├── credit_card_fraud_10k.csv
├── requirements.txt
└── README.md
```

### File Description

**`application.py`**
Main Streamlit application containing the dashboard, data analysis, visualizations, and prediction functionality.

**`credit_card_fraud_model.pkl`**
Pre-trained Random Forest classification model.

**`credit_card_fraud_10k.csv`**
Sample credit card transaction dataset used for analysis.

**`requirements.txt`**
Python dependencies required to run the application.

---

## Dataset

The project includes a sample dataset containing approximately 10,000 transaction records.

The dataset contains transaction attributes such as:

```text
transaction_id
amount
transaction_hour
merchant_category
foreign_transaction
location_mismatch
device_trust_score
velocity_last_24h
cardholder_age
is_fraud
```

The target variable is:

```text
is_fraud
```

where:

```text
0 → Genuine
1 → Fraudulent
```

---

## Getting Started

### Prerequisites

Make sure the following are installed:

* Python 3.9+
* pip
* Git

### Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
```

Navigate to the project directory:

```bash
cd <your-repository>
```

### Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** The machine learning model was created using `scikit-learn 1.6.1`. The project therefore pins this version in `requirements.txt` to maintain compatibility with the serialized model.

---

## Running the Application

Start the Streamlit application using:

```bash
streamlit run application.py
```

Streamlit will provide a local URL where the application can be accessed in your browser.

---

## Application Workflow

```text
                  Transaction Data
                         │
                         ▼
                Streamlit Dashboard
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
        Dataset Analysis       Transaction Input
              │                     │
              ▼                     ▼
       Data Visualization     Feature Processing
                                    │
                                    ▼
                          Random Forest Classifier
                                    │
                                    ▼
                           Fraud Classification
                                    │
                         ┌──────────┴──────────┐
                         ▼                     ▼
                     Genuine                Fraud
```

---

## Deployment

The application can be deployed using **Streamlit Community Cloud** or any platform capable of running a Python Streamlit application.

### Streamlit Deployment

1. Push the project to a GitHub repository.
2. Open Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the project repository.
5. Set the main file to:

```text
application.py
```

6. Deploy the application.

Streamlit will automatically install the dependencies specified in:

```text
requirements.txt
```

### Required Repository Structure

Ensure the following files are available in the repository root:

```text
application.py
requirements.txt
credit_card_fraud_model.pkl
credit_card_fraud_10k.csv
README.md
```

---

## Important Considerations

* The prediction pipeline must use the same feature representation expected by the trained model.
* `merchant_category` must be encoded consistently with the representation used during model training.
* The serialized `.pkl` model should only be loaded from a trusted source.
* The included model and dataset are intended for demonstration and educational purposes.
* Production deployment would require additional security, monitoring, validation, and model governance.

---

## Future Enhancements

Potential improvements include:

* Model prediction probability and confidence scores
* Precision, Recall, F1-Score and ROC-AUC evaluation
* Confusion matrix visualization
* Batch fraud prediction for uploaded datasets
* Automatic categorical feature encoding
* Downloadable prediction reports
* Explainable AI for transaction-level predictions
* Model monitoring and drift detection
* Authentication and role-based access control
* Production-grade API integration

---

## Project Objective

The objective of this project is to demonstrate the practical application of **machine learning for financial fraud detection** through an accessible and interactive web application.

It integrates:

```text
Data Processing
      ↓
Exploratory Data Analysis
      ↓
Machine Learning
      ↓
Fraud Classification
      ↓
Interactive Visualization
      ↓
Real-Time Prediction
```

---

## Author

**Santhosh Jothi**

Machine Learning | Python | Data Analytics | Streamlit

---

## License

This project is intended for educational and demonstration purposes.

---

## Acknowledgements

Built using the Python data science and machine learning ecosystem, including **Pandas, Scikit-learn, Joblib, Matplotlib, Seaborn, and Streamlit**.
