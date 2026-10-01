# Student Performance Prediction Using Machine Learning

## 1. Project Overview
This project uses supervised machine learning to classify a student's academic performance as **Low, Medium, or High** from academic and study-related features.

The project is designed as a command-line application so it can be executed without a GUI.

## 2. Problem Statement
Educational institutions collect many indicators of student performance. The objective of this project is to build a classification model that learns patterns from a student dataset and predicts a performance category for a new student record.

## 3. Objectives
- Prepare and inspect a tabular dataset.
- Separate input features and the target variable.
- Train a supervised classification model.
- Evaluate the model using accuracy, precision, recall, F1-score, and a confusion matrix.
- Inspect feature importance.
- Save the trained model.
- Provide a command-line prediction interface.

## 4. Technologies
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

## 5. Dataset
`data/student_data.csv` is a **synthetic educational dataset created for this project**. It contains 600 records.

Features:
- Attendance
- Study_Hours
- Previous_Marks
- Assignment_Score
- Internal_Marks
- Participation
- Sleep_Hours

Target:
- Performance: Low / Medium / High

The synthetic nature of the dataset is stated explicitly so the project does not misrepresent generated data as collected institutional data.

## 6. Machine Learning Method
A Random Forest Classifier is used for supervised multi-class classification.

Pipeline:
1. Load CSV data.
2. Select features and target.
3. Split data into training and testing sets using stratification.
4. Train Random Forest.
5. Generate predictions.
6. Calculate evaluation metrics.
7. Save model and result files.
8. Use the saved model for command-line prediction.

## 7. Project Structure

```text
student-performance-ml/
├── README.md
├── requirements.txt
├── main.py
├── data/
│   └── student_data.csv
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   └── predict.py
├── models/
├── results/
├── screenshots/
└── report/
    └── PROJECT_REPORT_TEMPLATE.md
```

## 8. Requirements
- Python 3.10 or newer
- pip
- Git

## 9. Installation

```bash
git clone https://github.com/YOUR-USERNAME/student-performance-ml.git
cd student-performance-ml

python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 10. Train the Model

```bash
python main.py train
```

This creates:
- `models/student_performance_model.joblib`
- `results/metrics.txt`
- `results/confusion_matrix.png`
- `results/feature_importance.png`

## 11. Make a Prediction

After training:

```bash
python main.py predict
```

Enter the requested student information when prompted.

## 12. Example

```text
=== Student Performance Prediction ===
Attendance (45-100): 88
Study hours (0.5-8): 3
Previous marks (30-100): 76
Assignment score (35-100): 82
Internal marks (30-100): 79
Participation (1-10): 8
Sleep hours (4-9): 7

--------------------------------
Predicted Performance: HIGH
--------------------------------
```

The exact prediction can vary with the trained model and input values.

## 13. Evaluation
The training program reports:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Feature importance

Run:

```bash
python main.py train
```

Then inspect the generated files in `results/`.

## 14. Limitations
- The dataset is synthetic and should not be used to make real educational decisions.
- The model is intended for demonstration and academic learning.
- Performance depends on the dataset and selected features.
- A real deployment would require validated, representative data and additional privacy and fairness checks.

## 15. Future Scope
- Test multiple classification algorithms.
- Add cross-validation and hyperparameter tuning.
- Compare model performance statistically.
- Use a validated public dataset.
- Add explainability methods.
- Build a web interface only after the command-line version is stable.

## 16. Academic Integrity
This repository is intended as an educational project. The author should understand, test, and document every component before submission. Any final submission should contain the student's own observations, screenshots, results, and report wording.
