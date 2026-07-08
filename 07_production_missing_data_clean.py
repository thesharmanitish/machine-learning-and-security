import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("datasets/employee_attrition_missing.csv")

df["DailyRate"] = SimpleImputer(strategy="mean").fit_transform(df[["DailyRate"]])
df["TotalWorkingYears"] = SimpleImputer(strategy="median").fit_transform(df[["TotalWorkingYears"]])

X = df.drop("Label", axis=1)
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, pred):.4f}")
