# FUNDAMENTALS OF AI AND ML - EVALUATED PROJECT

# Student Performance Prediction Using Machine Learning

---

## COVER PAGE

**Project Title:**  
Student Performance Prediction Using Machine Learning

**Course:**  
Fundamentals of AI and ML

**Student Name:**  
[Bhavishya lodhi]

**Registration Number:**  
[25MIM10067]

**Programme:**  
B.Tech Computer Science and Engineering

**Year:**  
2nd Year

**College:**  
VIT Bhopal University

**Faculty:**  
[Dr. Atul Onkarrao Thakare ]

**Academic Year:**  
2026-27

---

# CERTIFICATE / DECLARATION

## Declaration

I hereby declare that this project report presents the implementation and study of a machine learning project titled **"Student Performance Prediction Using Machine Learning"** for the course Fundamentals of AI and ML.

The project was developed for academic and learning purposes. The dataset used in the project is synthetic and was created for demonstration of machine learning concepts. The implementation, experimental observations, and reported results are based on the project execution carried out for this work.

I understand the concepts used in the project and take responsibility for the information presented in this report.

**Student Name:** 

**Registration Number:** ____________________

**Signature:** ______________________________

**Date:** __________________________________

---

# ABSTRACT

Machine learning can be used to identify patterns in structured data and generate predictions for new observations. This project presents a supervised machine learning system for classifying student academic performance into three categories: Low, Medium, and High.

A synthetic dataset containing 600 educational records was used for the project. The dataset contains academic and study-related features including attendance, study hours, previous marks, assignment score, internal marks, participation, and sleep hours. The target variable is the student's performance category.

The project uses a Random Forest Classifier for multi-class classification. The dataset was divided into training and testing sets using an 80:20 split. A total of 480 records were used for training and 120 records were used for testing.

The trained model achieved an accuracy of **77.50%** on the testing dataset. Precision, recall, and F1-score were also calculated for each performance class. A confusion matrix was generated to analyze correct and incorrect predictions, and feature importance was examined to understand which input variables contributed most to the model's decisions.

The complete system was implemented in Python and designed as a command-line application. The trained model is saved using Joblib and can be reused to predict the performance category of a new student record.

---

# 1. INTRODUCTION

Artificial Intelligence and Machine Learning are widely used to analyze data and discover useful patterns. Machine learning systems learn from existing examples and use those learned patterns to make predictions on new data.

Student academic performance can be represented using several measurable factors. Attendance, previous marks, assignment scores, internal assessment, study hours, participation, and other factors can be organized into a structured dataset. A machine learning classification model can then learn relationships among these features and classify a student's performance into predefined categories.

The purpose of this project is to demonstrate the complete machine learning workflow using a student performance dataset. The project covers data loading, feature selection, train-test splitting, model training, prediction, evaluation, visualization, and model persistence.

The project is designed to run through the command line. This makes the implementation easy to reproduce in a standard Python environment without depending on a graphical application.

---

# 2. PROBLEM STATEMENT

The objective of this project is to develop a supervised machine learning model that predicts a student's academic performance category using academic and study-related information.

The model accepts the following input features:

1. Attendance
2. Study Hours
3. Previous Marks
4. Assignment Score
5. Internal Marks
6. Participation
7. Sleep Hours

The target variable is:

- Low
- Medium
- High

The problem is treated as a **multi-class classification problem**, because the model must select one category from three possible performance classes.

The system should also provide measurable evaluation results and a command-line interface for making predictions on new student data.

---

# 3. OBJECTIVES

The main objectives of the project are:

- To understand the application of supervised machine learning to a classification problem.
- To prepare and inspect a structured student dataset.
- To separate input features from the target variable.
- To divide the dataset into training and testing subsets.
- To train a Random Forest classification model.
- To generate predictions for unseen records.
- To evaluate the model using accuracy, precision, recall, and F1-score.
- To create and interpret a confusion matrix.
- To analyze feature importance.
- To save the trained model for later use.
- To develop a command-line prediction interface.
- To understand the complete workflow of a small machine learning project.

---

# 4. DATASET DESCRIPTION

The project uses a synthetic dataset stored in:

`data/student_data.csv`

The dataset contains **600 records**.

The dataset was created for educational and demonstration purposes. It does not represent real student records and should not be used to make actual educational decisions.

## 4.1 Dataset Features

| Feature | Description |
|---|---|
| Attendance | Attendance percentage of the student |
| Study_Hours | Approximate study hours |
| Previous_Marks | Marks obtained in previous academic performance |
| Assignment_Score | Score obtained in assignments |
| Internal_Marks | Internal assessment marks |
| Participation | Participation level represented on a scale of 1 to 10 |
| Sleep_Hours | Approximate hours of sleep |
| Performance | Target class: Low, Medium, or High |

## 4.2 Input and Output

The input consists of seven features:

```text
Attendance
Study_Hours
Previous_Marks
Assignment_Score
Internal_Marks
Participation
Sleep_Hours