---
title: |
  Evaluating EMOO as a Metric-Balanced Ensemble Framework for Multi-Objective Optimization in Imbalanced Medical Data
authors:
  - "Maryam Moradpour"
  - "Zully Ritter"
  - "Anne-Christin Hauschild"
year: 2026
journal: "Studies in Health Technology and Informatics"
doi: "10.3233/shti261008"
url: "https://doi.org/10.3233/shti261008"
lab: "berlin-bccn"
faculty:
  - "Petra Ritter"
tags:
  - "publication"
  - "berlin-bccn"
abstract: |
  <jats:p>Introduction: Class imbalance can hinder reliable detection of clinically relevant outcomes in binary clinical prediction. In this study, the positive class was predefined as the clinically relevant minority outcome; therefore, accuracy-only hyperparameter selection can favor the majority class and reduce sensitivity for that outcome. Methods: We evaluated the previously published Ensemble Multi-Objective Optimization (EMOO) framework as a hyperparameter-selection and ensembling method rather than a diagnostic model itself. EMOO uses the Non-dominated Sorting Genetic Algorithm II (NSGA-II) to search Random Forest hyperparameter configurations across accuracy, sensitivity, specificity, and F1-score, while additionally minimizing their standard deviation (STD) to discourage imbalanced metric performance. Final Pareto-optimal models are combined through Adaptive Boosting (AdaBoost). EMOO was compared with baseline Random Forest, the Synthetic Minority Over-sampling Technique (SMOTE), and the Multi-Objective Optimization Framework (MOOF) on three public binary clinical datasets with imbalance ratios of 1.16–2.11, using repeated 10×5-fold stratified cross-validation and Decision Curve Analysis (DCA). Results: EMOO achieved the highest sensitivity and geometric mean across all datasets and the highest specificity on the Heart Failure Clinical Records and Mammographic Mass datasets. On the Pima Indians Diabetes dataset, its higher sensitivity was accompanied by lower specificity than baseline Random Forest and MOOF. DCA showed higher net benefit than treat-all and treat-none strategies across relevant threshold ranges. Conclusion: EMOO provides a metric-balanced approach to selecting and ensembling classifier configurations for moderately imbalanced clinical prediction tasks. External validation on independent clinical cohorts is required before routine use. The EMOO package and evaluation code are available at github.com/HauschildLab/EMOO and github.com/HauschildLab/EMOO4IMD.</jats:p>
fulltext_available: false
fulltext_source: "none"
created: "2026-09-21T15:44:06.909357"
---

# Evaluating EMOO as a Metric-Balanced Ensemble Framework for Multi-Objective Optimization in Imbalanced Medical Data

## Abstract

<jats:p>Introduction: Class imbalance can hinder reliable detection of clinically relevant outcomes in binary clinical prediction. In this study, the positive class was predefined as the clinically relevant minority outcome; therefore, accuracy-only hyperparameter selection can favor the majority class and reduce sensitivity for that outcome. Methods: We evaluated the previously published Ensemble Multi-Objective Optimization (EMOO) framework as a hyperparameter-selection and ensembling method rather than a diagnostic model itself. EMOO uses the Non-dominated Sorting Genetic Algorithm II (NSGA-II) to search Random Forest hyperparameter configurations across accuracy, sensitivity, specificity, and F1-score, while additionally minimizing their standard deviation (STD) to discourage imbalanced metric performance. Final Pareto-optimal models are combined through Adaptive Boosting (AdaBoost). EMOO was compared with baseline Random Forest, the Synthetic Minority Over-sampling Technique (SMOTE), and the Multi-Objective Optimization Framework (MOOF) on three public binary clinical datasets with imbalance ratios of 1.16–2.11, using repeated 10×5-fold stratified cross-validation and Decision Curve Analysis (DCA). Results: EMOO achieved the highest sensitivity and geometric mean across all datasets and the highest specificity on the Heart Failure Clinical Records and Mammographic Mass datasets. On the Pima Indians Diabetes dataset, its higher sensitivity was accompanied by lower specificity than baseline Random Forest and MOOF. DCA showed higher net benefit than treat-all and treat-none strategies across relevant threshold ranges. Conclusion: EMOO provides a metric-balanced approach to selecting and ensembling classifier configurations for moderately imbalanced clinical prediction tasks. External validation on independent clinical cohorts is required before routine use. The EMOO package and evaluation code are available at github.com/HauschildLab/EMOO and github.com/HauschildLab/EMOO4IMD.</jats:p>

## Links

- DOI: [10.3233/shti261008](https://doi.org/10.3233/shti261008)
- URL: [Link](https://doi.org/10.3233/shti261008)

## Faculty

- [[berlin-bccn/faculty#petra-ritter|Petra Ritter]]
