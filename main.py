"""
Main entry point for the Student Performance ML project.

Run:
    python main.py train
    python main.py predict
"""

import subprocess
import sys


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {"train", "predict"}:
        print("Usage:")
        print("  python main.py train")
        print("  python main.py predict")
        sys.exit(1)

    script = "src/train_model.py" if sys.argv[1] == "train" else "src/predict.py"
    subprocess.run([sys.executable, script], check=True)


if __name__ == "__main__":
    main()
