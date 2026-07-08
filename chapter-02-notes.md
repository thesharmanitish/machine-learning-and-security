# Chapter 2 — Classifying and Clustering

## What this chapter covers
- Security-oriented machine learning basics
- Supervised methods (classification/regression)
- Unsupervised methods (clustering)
- Model families, loss functions, optimization
- Practical ML issues in security settings

## Practical pipeline
1. Load and inspect data
2. Encode categorical variables (one-hot)
3. Train/test split (use stratification for imbalanced labels)
4. Train baseline model (e.g., Logistic Regression)
5. Evaluate with confusion matrix + precision/recall/F1
6. Iterate with better features/models

## Important takeaways
- High accuracy can be misleading on imbalanced data.
- Feature engineering and data quality dominate model outcomes.
- Threshold tuning matters in security operations.
- Clustering helps discover patterns without labels.

## Algorithms discussed
- Logistic Regression
- Decision Trees / Random Forests / Boosted Trees
- SVM
- Naive Bayes
- kNN
- Neural Networks
- k-means, Hierarchical clustering, DBSCAN, LSH, k-d trees

## Security-specific cautions
- Class imbalance is common (rare attacks).
- Data drift and attacker adaptation are continuous.
- Prefer robust evaluation, not a single metric.
