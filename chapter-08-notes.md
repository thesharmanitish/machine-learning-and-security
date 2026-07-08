# Chapter 8 — Adversarial Machine Learning

## Core idea
ML systems in security are attack surfaces themselves.

## Poisoning takeaway
If attackers influence training streams, they can shift decision boundaries.

## Defenses
- Batch updates (reduce instant feedback loops)
- Data quality gates and anomaly filtering
- Monitor boundary-adjacent sample rates
- Compare incoming data vs trusted reference distributions
