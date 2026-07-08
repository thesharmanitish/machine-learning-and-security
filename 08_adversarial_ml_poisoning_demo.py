import numpy as np
from sklearn.datasets import make_classification
from sklearn.neural_network import MLPClassifier

X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    weights=[0.5, 0.5],
    random_state=42,
)

clf = MLPClassifier(max_iter=600, random_state=42)
clf.fit(X[:100], y[:100])

num_chaff = 20
X_chaff = np.c_[np.linspace(-2, -1, num_chaff), np.full(num_chaff, 0.1)]
y_chaff = np.ones(num_chaff)

for _ in range(50):
    clf.partial_fit(X_chaff, y_chaff)

acc = clf.score(X[100:], y[100:])
print(f"Post-poison holdout accuracy: {acc:.4f}")
