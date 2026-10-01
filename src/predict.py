"""
Command-line prediction interface.
"""

from pathlib import Path
import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "student_performance_model.joblib"

FEATURES = [
    "Attendance",
    "Study_Hours",
    "Previous_Marks",
    "Assignment_Score",
    "Internal_Marks",
    "Participation",
    "Sleep_Hours",
]


def get_float(prompt, low, high):
    while True:
        try:
            value = float(input(prompt))
            if low <= value <= high:
                return value
            print(f"Enter a value between {low} and {high}.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    if not MODEL_PATH.exists():
        print("Model not found.")
        print("Run: python src/train_model.py")
        return

    model = joblib.load(MODEL_PATH)

    print("\n=== Student Performance Prediction ===")
    data = {
        "Attendance": get_float("Attendance (45-100): ", 45, 100),
        "Study_Hours": get_float("Study hours (0.5-8): ", 0.5, 8),
        "Previous_Marks": get_float("Previous marks (30-100): ", 30, 100),
        "Assignment_Score": get_float("Assignment score (35-100): ", 35, 100),
        "Internal_Marks": get_float("Internal marks (30-100): ", 30, 100),
        "Participation": get_float("Participation (1-10): ", 1, 10),
        "Sleep_Hours": get_float("Sleep hours (4-9): ", 4, 9),
    }

    sample = pd.DataFrame([data], columns=FEATURES)
    prediction = model.predict(sample)[0]

    print("\n--------------------------------")
    print(f"Predicted Performance: {prediction.upper()}")
    print("--------------------------------")


if __name__ == "__main__":
    main()
