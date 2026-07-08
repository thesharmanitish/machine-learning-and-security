# Chapter 4 — Malware Analysis

## Core message
ML helps malware triage/classification, but feature engineering quality dominates.

## Feature sources
- Static: imports, strings, permissions, metadata, structure
- Dynamic: behavior traces, process/network activity, system calls

## Modeling tips
- Keep a reproducible extraction pipeline.
- Track family-level and benign/malicious labels separately.
- Evaluate with precision/recall per family, not only accuracy.
