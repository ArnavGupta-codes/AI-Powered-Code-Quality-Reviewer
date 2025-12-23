import sys
import os
import joblib
import numpy as np

# -------------------- PATH SETUP --------------------
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)

MODEL_DIR = os.path.join(ROOT_DIR, "models", "saved")

# -------------------- IMPORTS --------------------
from service.language_detect import detect_language
from analyzers.python_analyzer import analyze_python_file
from analyzers.cpp_analyzer import analyze_cpp_file
from analyzers.java_analyzer import analyze_java_file
from features.feature_extractor import to_common_features

# -------------------- MODEL CONFIG --------------------
METRICS = ["readability", "maintainability", "complexity", "security"]

# -------------------- LOAD MODELS SAFELY --------------------
MODELS = {}

for m in METRICS:
    model_path = os.path.join(MODEL_DIR, f"{m}_rf.pkl")
    # ensure model dir exists
    os.makedirs(MODEL_DIR, exist_ok=True)

    if not os.path.exists(model_path):
        # don't raise at import time; allow running without trained models
        print(f"Warning: missing model file for '{m}': {model_path}. Using fallback.")
        MODELS[m] = None
    else:
        MODELS[m] = joblib.load(model_path)

# -------------------- MAIN ANALYSIS FUNCTION --------------------
def analyze_file(path: str, selected_metrics=None):
    if selected_metrics is None:
        selected_metrics = METRICS

    if not selected_metrics:
        raise ValueError("selected_metrics cannot be empty")

    invalid = set(selected_metrics) - set(METRICS)
    if invalid:
        raise ValueError(f"Invalid metrics requested: {invalid}")

    # Detect language
    lang = detect_language(path)

    # Run correct analyzer
    if lang == "python":
        metrics = analyze_python_file(path)
    elif lang == "cpp":
        metrics = analyze_cpp_file(path)
    elif lang == "java":
        metrics = analyze_java_file(path)
    else:
        raise ValueError(f"Unsupported language: {lang}")

    # Convert to common ML features
    feats = to_common_features(lang, metrics).reshape(1, -1)

    # Predict scores
    scores = {}
    for m in selected_metrics:
        model = MODELS.get(m)
        if model is None:
            # fallback prediction when model missing
            pred = 0.5
        else:
            pred = model.predict(feats)[0]

        # Normalize to 0-1 range (models predict 0-100)
        scores[m] = float(max(0, min(1, pred / 100.0)))

    overall = sum(scores[m] for m in selected_metrics) / len(selected_metrics)

    return overall, scores, metrics


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py <source_file> [metric1,metric2,...]")
        sys.exit(1)

    src = sys.argv[1]
    metrics_arg = None
    if len(sys.argv) >= 3:
        metrics_arg = sys.argv[2].split(",")

    overall, scores, raw_metrics = analyze_file(src, selected_metrics=metrics_arg)

    print("\nAnalysis Results")
    print("---------------")
    print(f"File: {src}")
    print(f"Language metrics: {raw_metrics}")
    print(f"Scores (0-1): {scores}")
    print(f"Overall ({', '.join(metrics_arg) if metrics_arg else ', '.join(METRICS)}): {overall:.3f}")
