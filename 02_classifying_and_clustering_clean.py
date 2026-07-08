import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

ROOT_DIR = os.path.dirname(os.getcwd())
DATASET_PATH = os.path.join(ROOT_DIR, "datasets", "payment_fraud.csv")

dataset = pd.read_csv(DATASET_PATH)

if "paymentMethod" in dataset.columns:
    dataset = pd.get_dummies(
        dataset,
        prefix="paymentMethod",
        columns=["paymentMethod"],
        drop_first=True,
    )

X = dataset.drop("label", axis=1)
y = dataset["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=1 / 3, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nConfusion matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification report:")
print(classification_report(y_test, y_pred, digits=4))
