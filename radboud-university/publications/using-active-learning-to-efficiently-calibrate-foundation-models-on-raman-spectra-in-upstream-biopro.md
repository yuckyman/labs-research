---
title: |
  Using Active Learning to Efficiently Calibrate Foundation Models on Raman Spectra in Upstream Bioprocess Fermentations
authors:
  - "Christoph Lange"
  - "Ernesto Martínez"
  - "Peter Neubauer"
  - "Mariano Nicolas Cruz Bournazou"
year: 2026
journal: "Systems and Control Transactions"
doi: "10.69997/sct.147199"
url: "https://doi.org/10.69997/sct.147199"
lab: "radboud-university"
faculty:
  - "Floris de Lange"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  <jats:p>Real-time monitoring of metabolite concentrations is critical for optimising bioprocess performance. While Raman spectroscopy offers a non-invasive solution, translating spectra into metabolite concentration estimates requires robust machine learning models. Foundation models such as TabPFN demonstrate exceptional predictive performance but suffer from high inference complexity when trained on large calibration datasets, hindering their use in real-time laboratory settings. This study proposes a batch Active Learning (AL) strategy to efficiently calibrate TabPFN using a minimal subset of data. We employ a weighted K-means clustering strategy that balances model uncertainty and dataset diversity to select the most informative calibration samples. We evaluated this method on a dataset of nearly 7, 000 Raman spectra covering eight substances. Our AL strategy achieved a mean R² score greater than 0.95 with approximately 1, 000 samples, significantly outperforming random sampling. Notably, the method matched the accuracy of a model trained on the full dataset using only 20% of the data. This reduction lowers computational complexity by a factor of 25, enabling millisecond-scale inference times suitable for high-throughput bioprocess monitoring.</jats:p>
fulltext_available: false
fulltext_source: "none"
created: "2026-06-22T14:44:00.374888"
---

# Using Active Learning to Efficiently Calibrate Foundation Models on Raman Spectra in Upstream Bioprocess Fermentations

## Abstract

<jats:p>Real-time monitoring of metabolite concentrations is critical for optimising bioprocess performance. While Raman spectroscopy offers a non-invasive solution, translating spectra into metabolite concentration estimates requires robust machine learning models. Foundation models such as TabPFN demonstrate exceptional predictive performance but suffer from high inference complexity when trained on large calibration datasets, hindering their use in real-time laboratory settings. This study proposes a batch Active Learning (AL) strategy to efficiently calibrate TabPFN using a minimal subset of data. We employ a weighted K-means clustering strategy that balances model uncertainty and dataset diversity to select the most informative calibration samples. We evaluated this method on a dataset of nearly 7, 000 Raman spectra covering eight substances. Our AL strategy achieved a mean R² score greater than 0.95 with approximately 1, 000 samples, significantly outperforming random sampling. Notably, the method matched the accuracy of a model trained on the full dataset using only 20% of the data. This reduction lowers computational complexity by a factor of 25, enabling millisecond-scale inference times suitable for high-throughput bioprocess monitoring.</jats:p>

## Links

- DOI: [10.69997/sct.147199](https://doi.org/10.69997/sct.147199)
- URL: [Link](https://doi.org/10.69997/sct.147199)

## Faculty

- [[radboud-university/faculty#floris-de-lange|Floris de Lange]]
