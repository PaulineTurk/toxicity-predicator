# toxicity-predicator
Predict molecular toxicity from chemical structure using machine learning.

## Problem
Early toxicity prediction is a key challenge in drug discovery.
This project builds a machine learning model that predicts toxicity from molecular structure using the Tox21 dataset.

## Dataset
Tox21 dataset containing chemical compounds represented as SMILES strings and toxicity assay results.

## Method
SMILES → molecular descriptors (RDKit) → machine learning model (scikit-learn)

## Results
## How to run


## Goal Stack
Python  
RDKit  
Pandas  
scikit-learn  
Matplotlib  
MLflow  
Poetry   
- mac install locally: `brew install poetry`
- access poetry info: `poetry env info`

## Machine Learning

### Model Evaluation
- Confusion Matrix
- Metrics: accuracy, precision, recall, F1-score  

👉 https://excalidraw.com/#json=otaEid9BdgdhHRdjkvSvV,y1wfEMpp5JuxvzRr6wGDOw 

---

### Classification

#### Decision Tree Algorithm

**Nodes**:
- Decision Node: a condition used to split the data
- Leaf Node: final prediction (most probable class)

**Split Criteria**:
- Gini Index (default): measures the probability of misclassification
- Entropy: measures uncertainty (amount of information needed)
- Goal: maximize impurity reduction (Information Gain)

👉 https://quantdare.com/decision-trees-gini-vs-entropy/

---

### Ensemble Learning: Wisdom of the Crowd

- Combine multiple models to improve performance
- Reduces variance
- Requires diversity between models

**Bagging (Bootstrap Aggregating)**:
- Train multiple models on random subsets of the dataset (with replacement)
- Aggregate predictions (e.g., majority voting)

---

#### Random Forest Algorithm

- Base model: Decision Tree
- Technique: Bagging + additional randomness

**Randomness introduced**:
- Bootstrap sampling: each tree is trained on a different subset of data
- Feature sampling: at each split, only a random subset of features is considered  
→ reduces correlation between trees and improves generalization

**Out-of-Bag (OOB)**:
- Data not used during bootstrap for a given tree
- Used as a validation set to estimate model performance without a separate dataset


### Key Learnings

- Random Forest reduces variance by averaging multiple de-correlated trees
- Feature randomness is crucial to avoid dominant predictors
- OOB error provides a built-in validation mechanism
- Gini is a fast approximation of entropy with similar performance