import os
from collections import defaultdict
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

NSL_KDD_DIR = os.path.join(os.getcwd(), "datasets", "NSL-KDD-Dataset")

features = defaultdict(list)
headers = []
with open(os.path.join(NSL_KDD_DIR, "features.txt")) as f:
    for line in f:
        feat, feat_type = line.strip().replace(":", "").replace(".", "").split()
        features[feat_type].append(feat)
        headers.append(feat)

categories = defaultdict(list)
categories["benign"].append("normal")
with open(os.path.join(NSL_KDD_DIR, "training_attack_types.txt")) as f:
    for line in f:
        attack, cat = line.strip().split(" ")
        categories[cat].append(attack)
attack_mapping = {v: k for k in categories for v in categories[k]}

train = pd.read_csv(os.path.join(NSL_KDD_DIR, "KDDTrain+.txt"), names=headers).iloc[:, :-1]
test = pd.read_csv(os.path.join(NSL_KDD_DIR, "KDDTest+.txt"), names=headers).iloc[:, :-1]

train["attack_category"] = train["attack_type"].map(attack_mapping)
test["attack_category"] = test["attack_type"].map(attack_mapping)

X_train = train.drop(["attack_type", "attack_category"], axis=1)
y_train = train["attack_category"]
X_test = test.drop(["attack_type", "attack_category"], axis=1)
y_test = test["attack_category"]

X_all = pd.concat([X_train, X_test], axis=0)
X_all = pd.get_dummies(X_all, columns=["protocol_type", "service", "flag"], drop_first=True)
X_train = X_all.iloc[: len(X_train), :].astype("float64")
X_test = X_all.iloc[len(X_train) :, :].astype("float64")

cont_cols = [c for c in features["continuous"] if c in X_train.columns]
scaler = StandardScaler().fit(X_train[cont_cols])
X_train[cont_cols] = scaler.transform(X_train[cont_cols])
X_test[cont_cols] = scaler.transform(X_test[cont_cols])

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred, digits=4))
