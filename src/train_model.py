"""
Train, evaluate, and save the student performance classifier.
"""

from pathlib import Path
import sys
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    ConfusionMatrixDisplay
)

sys.path.append(str(Path(__file__).resolve().parent))
from preprocessing import load_data, prepare_data, split_data

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "student_data.csv"
MODEL_DIR = ROOT / "models"
RESULTS_DIR = ROOT / "results"


def main():
    MODEL_DIR.mkdir(exist_ok=True)
    RESULTS_DIR.mkdir(exist_ok=True)

    df = load_data(DATA_PATH)
    X, y = prepare_data(df)
    X_train, X_test, y_train, y_test = split_data(X, y)

    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=8,
        random_state=42
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("\n=== Student Performance ML Project ===")
    print(f"Dataset rows       : {len(df)}")
    print(f"Training samples   : {len(X_train)}")
    print(f"Testing samples    : {len(X_test)}")
    print(f"Accuracy           : {accuracy:.2%}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))

    cm = confusion_matrix(y_test, y_pred, labels=["Low", "Medium", "High"])
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Low", "Medium", "High"]
    )
    disp.plot()
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "confusion_matrix.png", dpi=150)
    plt.close()

    importance = pd.Series(
        model.feature_importances_, index=X.columns
    ).sort_values(ascending=True)
    importance.plot(kind="barh")
    plt.title("Feature Importance")
    plt.xlabel("Importance")
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "feature_importance.png", dpi=150)
    plt.close()

    joblib.dump(model, MODEL_DIR / "student_performance_model.joblib")

    with open(RESULTS_DIR / "metrics.txt", "w", encoding="utf-8") as f:
        f.write(f"Accuracy: {accuracy:.4f}\n\n")
        f.write(classification_report(y_test, y_pred, zero_division=0))

    print("\nSaved:")
    print("- models/student_performance_model.joblib")
    print("- results/confusion_matrix.png")
    print("- results/feature_importance.png")
    print("- results/metrics.txt")


if __name__ == "__main__":
    main()
