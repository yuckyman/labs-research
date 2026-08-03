---
title: "A General Framework for Stability Assessment of Non-Deterministic Prediction Models"
authors:
  - "Thomas Martin Lange"
  - "Armin Otto Schmitt"
  - "Felix Heinrich"
year: 2026
doi: "10.21203/rs.3.rs-10317283/v1"
url: "https://doi.org/10.21203/rs.3.rs-10317283/v1"
lab: "radboud-university"
faculty:
  - "Floris de Lange"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  <title>Abstract</title>
                  <p>
                    Prediction models are widely used to forecast outcomes and support decision-making across diverse applications. However, many modern prediction models are inherently non-deterministic, meaning that repeated training on identical data can yield different predictions and potentially inconsistent decisions. Assessing
                    <italic>prediction stability</italic>
                    is therefore important for evaluating the reliability of such models. Existing approaches to quantifying prediction stability were primarily developed for repeated fits of random forest models using the intraclass correlation coefficient (ICC) for metric predictions and Fleiss’ \\((\\kappa)\\) for categorical predictions. However, these measures have important limitations: they do not naturally extend to ordinal predictions, require multiple test objects, and depend on the structure of the test data, potentially confounding prediction stability with data characteristics. We therefore propose a general framework for quantifying prediction stability in non-deterministic prediction models. Specifically, we introduce the
                    <italic>data-based</italic>
                    and
                    <italic>model-based prediction stability</italic>
                    , defined as one minus the ratio of observed to expected instability estimated from training data or model predictions. The proposed measures are applicable to metric, categorical, and ordinal predictions, can be evaluated for individual test objects, and are substantially less sensitive to the composition of the test data. The framework is implemented in the R package \\texttt{APS} for practical use.
                  </p>
fulltext_available: false
fulltext_source: "none"
created: "2026-08-03T12:26:08.452809"
---

# A General Framework for Stability Assessment of Non-Deterministic Prediction Models

## Abstract

<title>Abstract</title>
                <p>
                  Prediction models are widely used to forecast outcomes and support decision-making across diverse applications. However, many modern prediction models are inherently non-deterministic, meaning that repeated training on identical data can yield different predictions and potentially inconsistent decisions. Assessing
                  <italic>prediction stability</italic>
                  is therefore important for evaluating the reliability of such models. Existing approaches to quantifying prediction stability were primarily developed for repeated fits of random forest models using the intraclass correlation coefficient (ICC) for metric predictions and Fleiss’ \((\kappa)\) for categorical predictions. However, these measures have important limitations: they do not naturally extend to ordinal predictions, require multiple test objects, and depend on the structure of the test data, potentially confounding prediction stability with data characteristics. We therefore propose a general framework for quantifying prediction stability in non-deterministic prediction models. Specifically, we introduce the
                  <italic>data-based</italic>
                  and
                  <italic>model-based prediction stability</italic>
                  , defined as one minus the ratio of observed to expected instability estimated from training data or model predictions. The proposed measures are applicable to metric, categorical, and ordinal predictions, can be evaluated for individual test objects, and are substantially less sensitive to the composition of the test data. The framework is implemented in the R package \texttt{APS} for practical use.
                </p>

## Links

- DOI: [10.21203/rs.3.rs-10317283/v1](https://doi.org/10.21203/rs.3.rs-10317283/v1)
- URL: [Link](https://doi.org/10.21203/rs.3.rs-10317283/v1)

## Faculty

- [[radboud-university/faculty#floris-de-lange|Floris de Lange]]
