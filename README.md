# Student Performance Prediction Using Machine Learning

## 1. Project Overview

This project uses supervised machine learning to classify a student's academic performance as **Low, Medium, or High** using academic and study-related features.

The project is implemented as a command-line application and can be executed through a terminal without requiring a graphical interface.

## 2. Problem Statement

Educational performance can be influenced by several academic and study-related factors. The objective of this project is to build a machine learning classification model that learns patterns from a student dataset and predicts a performance category for a new student record.

## 3. Objectives

- Prepare and inspect a tabular dataset.
- Separate input features and the target variable.
- Train a supervised machine learning classification model.
- Evaluate the model using accuracy, precision, recall, F1-score, and a confusion matrix.
- Analyze feature importance.
- Save the trained machine learning model.
- Provide a command-line prediction interface.

## 4. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

## 5. Dataset

The file `data/student_data.csv` contains **600 synthetic educational records** created for this academic project.

### Input Features

- Attendance
- Study Hours
- Previous Marks
- Assignment Score
- Internal Marks
- Participation
- Sleep Hours

### Target Variable

- Performance: Low / Medium / High

The dataset is explicitly identified as synthetic and is intended only for educational and demonstration purposes.

## 6. Machine Learning Method

The project uses a **Random Forest Classifier** for supervised multi-class classification.

### Machine Learning Pipeline

1. Load the CSV dataset.
2. Select input features and target variable.
3. Split the dataset into training and testing sets.
4. Train the Random Forest classification model.
5. Generate predictions.
6. Calculate evaluation metrics.
7. Save the trained model.
8. Use the saved model for command-line prediction.

## 7. Project Structure

```text
student-performance-ml/
│
├── data/
│   └── student_data.csv
│
├── models/
│   └── student_performance_model.joblib
│
├── report/
│   └── PROJECT_REPORT_TEMPLATE.md
│
├── results/
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   └── metrics.txt
│
├── screenshots/
│
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   └── predict.py
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt