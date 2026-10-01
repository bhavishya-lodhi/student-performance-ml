"""
Data loading and preprocessing utilities.
"""

from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

FEATURES = [
    "Attendance",
    "Study_Hours",
    "Previous_Marks",
    "Assignment_Score",
    "Internal_Marks",
    "Participation",
    "Sleep_Hours",
]
TARGET = "Performance"


def load_data(path):
    df = pd.read_csv(path)
    return df


def prepare_data(df):
    X = df[FEATURES].copy()
    y = df[TARGET].copy()
    return X, y


def split_data(X, y, test_size=0.20, random_state=42):
    return train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
