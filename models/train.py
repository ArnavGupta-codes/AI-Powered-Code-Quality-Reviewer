import sys
import os
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from analyzers.python_analyzer import analyze_python_file
from analyzers.cpp_analyzer import analyze_cpp_file
from analyzers.java_analyzer import analyze_java_file

from features.feature_extractor import to_common_features


def load_metrics(path, lang):
    if lang == "python":
        return analyze_python_file(path)
    elif lang == "cpp":
        return analyze_cpp_file(path)
    elif lang == "java":
        return analyze_java_file(path)
    else:
        raise ValueError("Unknown language")


def build_dataset(csv_path):
    df = pd.read_csv(csv_path)

    X = []
    y_read = []
    y_main = []
    y_comp = []
    y_sec = []

    for _, row in df.iterrows():
        path = row["path"]
        lang = row["language"]

        # make paths absolute relative to project root
        if not os.path.isabs(path):
            path = os.path.join(ROOT_DIR, path)

        metrics = load_metrics(path, lang)
        feats = to_common_features(lang, metrics)

        X.append(feats)
        y_read.append(row["readability"])
        y_main.append(row["maintainability"])
        y_comp.append(row["complexity"])
        y_sec.append(row["security"])

    return np.array(X), {
        "readability": np.array(y_read),
        "maintainability": np.array(y_main),
        "complexity": np.array(y_comp),
        "security": np.array(y_sec),
    }


def train_and_evaluate(csv_path=None):
    if csv_path is None:
        csv_path = os.path.join(ROOT_DIR, "data", "labels.csv")

    X, targets = build_dataset(csv_path)

    results = {}

    for metric, y in targets.items():
        print(f"\n🔵 Training model for: {metric.upper()}")

        # Use 5-fold cross-validation for smaller dataset
        cv_scores_r2 = cross_val_score(
            Pipeline([
                ("scaler", StandardScaler()),
                ("rf", RandomForestRegressor(
                    n_estimators=700,
                    max_depth=12,
                    random_state=42,
                    n_jobs=-1
                ))
            ]),
            X, y, cv=5, scoring='r2'
        )
        
        cv_scores_mae = cross_val_score(
            Pipeline([
                ("scaler", StandardScaler()),
                ("rf", RandomForestRegressor(
                    n_estimators=700,
                    max_depth=12,
                    random_state=42,
                    n_jobs=-1
                ))
            ]),
            X, y, cv=5, scoring='neg_mean_absolute_error'
        )

        # Now train on full data for final model save
        model = Pipeline([
            ("scaler", StandardScaler()),
            ("rf", RandomForestRegressor(
                n_estimators=700,
                max_depth=12,
                random_state=42,
                n_jobs=-1
            ))
        ])

        model.fit(X, y)

        # Report cross-validation metrics (more reliable for small datasets)
        mean_r2 = cv_scores_r2.mean()
        std_r2 = cv_scores_r2.std()
        mean_mae = -cv_scores_mae.mean()
        std_mae = cv_scores_mae.std()

        results[metric] = {
            "CV_R2_Mean": mean_r2,
            "CV_R2_Std": std_r2,
            "CV_MAE_Mean": mean_mae,
            "CV_MAE_Std": std_mae
        }

        print(f"CV R2      = {mean_r2:.4f} ± {std_r2:.4f}")
        print(f"CV MAE     = {mean_mae:.2f} ± {std_mae:.2f}")

        # ensure save directory is under project root
        save_dir = os.path.join(ROOT_DIR, "models", "saved")
        os.makedirs(save_dir, exist_ok=True)
        joblib.dump(model, os.path.join(save_dir, f"{metric}_rf.pkl"))

    return results


if __name__ == "__main__":
    stats = train_and_evaluate()
    print("\n🎉 Training Complete! Cross-Validation Metrics (more reliable for small datasets):")
    for metric, stats_dict in stats.items():
        print(f"\n{metric.upper()}:")
        for k, v in stats_dict.items():
            if isinstance(v, float):
                print(f"  {k}: {v:.4f}")
            else:
                print(f"  {k}: {v}")
