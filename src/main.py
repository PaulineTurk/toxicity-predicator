from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from compute_dataset import sdf_to_dataset
from sklearn.pipeline import Pipeline
import json
import joblib
import os
import pandas as pd


SDF_FILE_PATH = "data/tox21.sdf.gz"
TOXICOLOGY_TEST = "SR-p53"
MODEL = "RandomForestClassifier"

BASE_PATH = f"experiment/{TOXICOLOGY_TEST}/{MODEL}"
DATASET_FILE_PATH = f"{BASE_PATH}/dataset.pkl"
MODEL_FILE_PATH = f"{BASE_PATH}/model.pkl"
REPORT_FILE_PATH = f"{BASE_PATH}/report.json"

os.makedirs(BASE_PATH, exist_ok=True)

if os.path.exists(DATASET_FILE_PATH):
    X, y = joblib.load(DATASET_FILE_PATH)
else:
    X, y = sdf_to_dataset(SDF_FILE_PATH, TOXICOLOGY_TEST)
    joblib.dump((X, y), DATASET_FILE_PATH)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

if os.path.exists(MODEL_FILE_PATH):
    pipeline = joblib.load(MODEL_FILE_PATH)
else:
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", RandomForestClassifier(class_weight="balanced", random_state=42))
    ])
    pipeline.fit(X_train, y_train)
    joblib.dump(pipeline, MODEL_FILE_PATH)

y_pred = pipeline.predict(X_test)


report = classification_report(y_test, y_pred, output_dict=True)
pd.DataFrame(report)

with open(REPORT_FILE_PATH, "w") as f:
    json.dump(report, f, indent=4)


