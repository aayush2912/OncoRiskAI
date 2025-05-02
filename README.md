# 🧬 OncoRisk AI — Breast Cancer Malignancy Prediction System



<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-FastAPI-green.svg" alt="Framework">
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen.svg" alt="Build">
  <img src="https://img.shields.io/badge/Deployment-Live-blueviolet.svg" alt="Deployment">
  <img src="https://img.shields.io/badge/Docker-Ready-blue.svg" alt="Docker">
  <img src="https://img.shields.io/badge/Deployed-AWS-ff9900.svg" alt="AWS">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>


## 📖 Project Overview

OncoRisk AI is an end-to-end machine learning system designed to predict the malignancy of breast cancer tumors based on diagnostic features obtained from fine needle aspirate (FNA) tests.  
The project covers complete stages from **data processing**, **feature engineering**, **machine learning modeling**, to **containerized API deployment on AWS** using **FastAPI and Docker**.

---

## 📦 Problem Statement

Breast cancer diagnosis can be improved significantly through automated machine learning systems that assist doctors in risk assessment.  
The goal is to build an **interpretable, scalable, and deployable system** that predicts tumor malignancy using clinical diagnostic features.

---

## 📊 Dataset

- **Source:** [UCI Machine Learning Repository — Breast Cancer Wisconsin Diagnostic Dataset](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)
- **Records:** 569 instances
- **Features:** 30 real-valued attributes + ID + Diagnosis (M = malignant, B = benign)
- **No missing values**

---

## ⚙️ Project Architecture

| Stage | Description |
|:---|:---|
| 1. Data Loading and EDA | Analyzed distribution, outliers, and feature relationships. |
| 2. Preprocessing | Cleaned data, encoded labels, feature scaling. |
| 3. Initial Classification Pipeline | Baseline models trained (Logistic Regression, Random Forest, XGBoost). |
| 4. Survival-Inspired Risk Scoring | Designed pseudo-survival risk stratification into Low, Medium, High risk groups. |
| 5. Feature Engineering | Built new statistical, ratio, and PCA features to enrich dataset. |
| 6. Modeling with Engineered Features | Retrained models achieving ROC-AUC up to 0.9931. |
| 7. Threshold Optimization | Applied Youden’s J statistic to find best decision boundary (optimal threshold ≈ 0.1939). |
| 8. SHAP Feature Selection | Selected top 15 important features to simplify model without major loss in accuracy. |
| 9. Error Analysis | Deep-dived into false positives and false negatives. |
| 10. API Deployment | Developed FastAPI backend, dockerized, and deployed via AWS App Runner. |

---

## 🛠 Technologies Used

- **Machine Learning:** Scikit-Learn, LightGBM, XGBoost, CatBoost
- **Explainability:** SHAP
- **API Framework:** FastAPI
- **Deployment:** Docker, AWS App Runner
- **EDA and Visualization:** Pandas, Matplotlib, Seaborn
- **Model Management:** joblib
- **Cloud Hosting:** AWS

---

## 📈 Key Results and Findings

| Section | Key Result |
|:---|:---|
| Initial Models (Raw Features) | Achieved ROC-AUC ≈ 0.985 |
| Feature Engineering | Improved ROC-AUC to 0.9931 |
| Threshold Optimization | Increased sensitivity (Recall = 97.62%) without sacrificing Precision |
| SHAP Feature Reduction | Selected Top 15 features; still maintained ROC-AUC ≈ 0.9977 |
| Error Analysis | Only 1 False Positive and 1 False Negative |
| Deployment | FastAPI app containerized and deployed live to AWS (public URL) |

---

## 📋 Inference by Section

### 1. EDA & Preprocessing:
- The dataset was well-structured and required minimal missing value handling.
- Significant correlation observed between "Worst Concave Points", "Worst Perimeter" and malignancy.

### 2. Initial Baseline Models:
- Random Forest and XGBoost were strong even on raw features but could be improved.

### 3. Survival Risk Scoring:
- Introduced risk categorization, providing clinical interpretability beyond just classification.

### 4. Feature Engineering:
- Adding ratio, statistical, and PCA features led to **significant model uplift**.

### 5. Threshold Optimization:
- Moving from default 0.5 to ~0.19 threshold increased clinical sensitivity, catching more malignant cases.

### 6. SHAP Feature Selection:
- Reduced feature space dramatically while maintaining predictive power, improving model interpretability.

### 7. Error Analysis:
- Confirmed that model errors occur very close to threshold, indicating careful decision-making behavior.

### 8. API Development:
- Built an industry-grade scalable backend using FastAPI.
- Easy-to-use Swagger interface for prediction input testing.

### 9. Deployment:
- Dockerization enabled complete portability.
- AWS App Runner provided instant, scalable public hosting.

---

## 🚀 Final Conclusion

OncoRisk AI demonstrates that by applying advanced feature engineering, careful threshold tuning, explainability techniques (SHAP), and professional deployment strategies,  
machine learning models can reach **extremely high accuracy and reliability** suitable for assisting in clinical decision-making. This project showcases a **full-stack machine learning deployment pipeline** from raw data to live production.

---

## 📂 Folder Structure

```plaintext
CancerPrediction/
├── notebooks/
│   ├── 01_EDA_Preprocessing.ipynb
│   ├── 02_Classification_Pipeline.ipynb
│   ├── 03_Survival_Risk_Scoring.ipynb
│   ├── 04_Feature_Engineering.ipynb
│   └── 05_Modeling_with_Engineered_Features.ipynb
├── data/
│   ├── wdbc.data
│   ├── wdbc.names
├── main.py                # FastAPI app
├── Dockerfile             # Docker build file
├── requirements.txt       # Python dependencies
└── README.md              # Project Documentation
