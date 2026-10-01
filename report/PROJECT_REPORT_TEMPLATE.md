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

The output of the classification model is one of the following three performance categories:

Low
Medium
High

#5. TOOLS AND TECHNOLOGIES
5.1 Python

Python was used as the primary programming language for implementing the machine learning project. Python provides a simple syntax and a wide range of libraries for data processing, machine learning, and visualization.

5.2 Pandas

Pandas was used to read and manipulate the CSV dataset. It was used for loading the data, selecting columns, and preparing the input and target variables.

5.3 NumPy

NumPy is used for numerical computing and provides supporting functionality for numerical operations used by machine learning libraries.

5.4 Scikit-learn

Scikit-learn was used for the machine learning implementation. It provides the Random Forest Classifier, train-test splitting, prediction functions, and evaluation metrics.

5.5 Matplotlib

Matplotlib was used to create graphical results, including the confusion matrix and feature importance visualization.

5.6 Joblib

Joblib was used to save the trained machine learning model to a file so that it could be loaded later for prediction.

The saved model is:

models/student_performance_model.joblib
6. METHODOLOGY

The complete project follows a sequence of machine learning steps.

6.1 Data Loading

The dataset is stored in a CSV file:

data/student_data.csv

The file is loaded using Pandas and converted into a DataFrame.

6.2 Feature and Target Separation

The seven input variables are selected as model features, while the Performance column is selected as the target variable.

Therefore:

X = Input Features
y = Performance
6.3 Train-Test Split

The dataset is divided into training and testing data using an 80:20 split.

Total Records     = 600
Training Records  = 480
Testing Records   = 120

Stratified splitting is used to maintain the representation of the three target classes in the training and testing datasets.

6.4 Model Training

A Random Forest Classifier is used for the classification task.

The model configuration used in the project is:

Number of Trees (n_estimators) = 150
Maximum Tree Depth             = 8
Random State                   = 42

The model is trained using the training dataset.

6.5 Prediction

After training, the model predicts the performance class of the testing records.

The saved model is also used to predict the performance of a new student entered through the command-line interface.

6.6 Evaluation

The trained model is evaluated using:

Accuracy
Precision
Recall
F1-score
Confusion Matrix

Feature importance is also generated to understand how the trained Random Forest model used the input variables.

6.7 Model Persistence

The trained model is saved using Joblib:

models/student_performance_model.joblib

Saving the model allows it to be loaded later without training it again.

7. RANDOM FOREST ALGORITHM

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to perform classification.

The general procedure used in this project is:

Load the prepared dataset.
Separate the input features and target variable.
Divide the dataset into training and testing sets.
Create multiple decision trees using the training data.
Train the individual trees.
Obtain predictions from the trained trees.
Combine the individual tree predictions.
Select the final class based on the combined predictions.
Compare the predicted classes with the actual classes.
Calculate evaluation metrics.
Save the trained model.

Using multiple decision trees allows the model to consider different patterns in the training data.

8. IMPLEMENTATION

The project is divided into separate Python files.

8.1 main.py

The main.py file is the main entry point of the application.

It supports two commands:

python main.py train

This command trains the Random Forest model.

python main.py predict

This command loads the saved model and starts the command-line prediction interface.

8.2 src/preprocessing.py

This file handles the data preparation process.

Its main responsibilities are:

Loading the CSV dataset
Selecting the input features
Separating the target variable
Splitting the dataset into training and testing data
8.3 src/train_model.py

This file performs the complete model training and evaluation process.

It:

Loads the dataset.
Separates the features and target.
Splits the dataset.
Creates the Random Forest Classifier.
Trains the model.
Generates predictions.
Calculates evaluation metrics.
Generates the confusion matrix.
Generates the feature importance graph.
Saves the trained model.
Saves the evaluation results.
8.4 src/predict.py

This file provides the command-line prediction interface.

It loads the saved model and asks the user to enter:

Attendance
Study Hours
Previous Marks
Assignment Score
Internal Marks
Participation
Sleep Hours

The input values are converted into the format expected by the machine learning model.

The model then produces a predicted performance category.

9. EXPERIMENTAL RESULTS

The project was executed successfully using a Python virtual environment.

The experiment produced the following results:

Dataset size      : 600
Training samples  : 480
Testing samples   : 120
Accuracy          : 77.50%
9.1 Classification Report

The classification report generated during the experiment was:

              precision    recall  f1-score   support

High              0.82      0.82      0.82        40
Low               0.80      0.90      0.85        40
Medium            0.69      0.60      0.64        40

accuracy                               0.78       120
macro avg         0.77      0.78      0.77       120
weighted avg      0.77      0.78      0.77       120
9.2 Result Interpretation

The model achieved an overall test accuracy of 77.50% on the 120 test records.

The performance differs across the three classes. The High class achieved precision, recall, and F1-score values of approximately 0.82. The Low class achieved a recall of 0.90, while the Medium class had a recall of 0.60.

This demonstrates that overall accuracy alone does not completely describe the behavior of a classification model. Precision, recall, and F1-score provide additional information about the predictions for individual classes.

10. CONFUSION MATRIX

The confusion matrix generated by the program is stored in:

results/confusion_matrix.png

The confusion matrix compares actual classes with the classes predicted by the model.

The rows represent the actual classes, while the columns represent the predicted classes.

The diagonal entries represent correctly classified records, while off-diagonal entries represent misclassifications.

Insert Figure

Insert the image:

results/confusion_matrix.png
Figure Caption

Figure 1: Confusion Matrix of the Random Forest Classifier

The confusion matrix helps identify which performance categories are correctly classified and which categories are sometimes confused with each other.

11. FEATURE IMPORTANCE

The Random Forest model provides feature importance values for the input variables.

The generated feature importance graph is stored in:

results/feature_importance.png
Insert Figure

Insert the image:

results/feature_importance.png
Figure Caption

Figure 2: Feature Importance of the Random Forest Model

The feature importance graph shows how the trained model used the input features during classification.

The importance values describe the contribution of the features within the trained model. They should not be interpreted as proof that one feature directly causes a student's academic performance.

12. COMMAND-LINE EXECUTION

The project was designed to run from the command line without requiring a graphical interface.

12.1 Creating the Virtual Environment

The Python virtual environment was created using:

python -m venv .venv
12.2 Activating the Environment

On Windows:

.venv\Scripts\activate
12.3 Installing Dependencies

The required Python libraries were installed using:

pip install -r requirements.txt
12.4 Training the Model

The model was trained using:

python main.py train

Observed output:

=== Student Performance ML Project ===
Dataset rows       : 600
Training samples   : 480
Testing samples    : 120
Accuracy           : 77.50%
12.5 Prediction

The prediction program was executed using:

python main.py predict

A sample test input was:

Attendance: 88
Study Hours: 3
Previous Marks: 76
Assignment Score: 82
Internal Marks: 79
Participation: 8
Sleep Hours: 7

The observed prediction was:

Predicted Performance: HIGH
12.6 Screenshots

The following screenshots should be inserted into the report from the actual project execution:

Project folder structure in VS Code.
Dependency installation.
Model training output.
Prediction output.
GitHub repository.

The screenshots should represent the student's actual execution environment.

13. PROJECT STRUCTURE

The project repository is organized as follows:

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

GitHub Repository:

https://github.com/bhavishya-lodhi/student-performance-ml
14. LIMITATIONS
14.1 Synthetic Dataset

The dataset is synthetic and was created for educational purposes. It does not represent actual student records.

14.2 Limited Feature Set

The project uses seven input features. Real academic performance may depend on many additional factors.

14.3 Dataset Size

The dataset contains 600 records. A larger dataset may provide a broader basis for machine learning experimentation.

14.4 Model Performance

The observed model accuracy is dependent on the dataset, selected features, train-test split, and model configuration.

14.5 Real-World Validation

The model has not been validated using real institutional data and has not been deployed in an actual educational environment.

14.6 Responsible Use

Because the dataset is synthetic and the project is an academic demonstration, predictions should not be used for real educational decisions.

15. FUTURE SCOPE

The project can be extended in several ways.

15.1 Algorithm Comparison

Other classification algorithms can be implemented and compared, including:

Logistic Regression
Decision Tree
K-Nearest Neighbors
Support Vector Machine
Random Forest
15.2 Cross-Validation

Cross-validation can be used to evaluate the model over multiple data splits.

15.3 Hyperparameter Tuning

The Random Forest hyperparameters can be optimized using techniques such as Grid Search or Randomized Search.

15.4 Larger Validated Dataset

A larger, properly documented, and validated public dataset could be used to conduct more realistic experiments.

15.5 Explainable AI

Explainability techniques could be added to provide additional insight into model predictions.

15.6 User Interface

After the command-line implementation is stable, a web-based interface could be developed for easier interaction.

16. CONCLUSION

This project demonstrates the development of a supervised machine learning system for predicting student performance categories.

A synthetic dataset containing 600 records was used, and the data was divided into 480 training records and 120 testing records. A Random Forest Classifier was trained to classify the performance of students into Low, Medium, and High categories.

The model achieved an observed test accuracy of 77.50%. Precision, recall, and F1-score were also calculated for each class. A confusion matrix was generated to analyze classification errors, and feature importance was used to understand how the trained model utilized the available input features.

The project also demonstrates model persistence using Joblib and provides a command-line interface through which new student information can be entered for prediction.

Through this project, the complete basic machine learning workflow was implemented, including dataset handling, feature preparation, train-test splitting, model training, evaluation, visualization, model saving, and prediction.

The project provides a practical foundation for further study of machine learning classification and can be extended with additional algorithms, validated datasets, cross-validation, hyperparameter tuning, and explainable AI techniques.

REFERENCES
Python Documentation. Python Programming Language Documentation.
https://docs.python.org/
Pandas Documentation. Pandas User Guide and API Reference.
https://pandas.pydata.org/docs/
NumPy Documentation. NumPy User Guide.
https://numpy.org/doc/
Scikit-learn Documentation. Machine Learning in Python.
https://scikit-learn.org/stable/
Matplotlib Documentation. Visualization with Python.
https://matplotlib.org/stable/
Joblib Documentation. Python Object Persistence.
https://joblib.readthedocs.io/
