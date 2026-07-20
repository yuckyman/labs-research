---
title: |
  Enhancing PatchCore with Dynamic Scaling and Vision–Language Models for Explainable Industrial Defect Inspection
authors:
  - "Oğuz Ergin"
  - "Emre Güçlü"
  - "İlhan Aydın"
  - "Erhan Akın"
year: 2026
journal: "Applied Sciences"
doi: "10.3390/app16147096"
url: "https://doi.org/10.3390/app16147096"
lab: "radboud-university"
faculty:
  - "Umut Güçlü"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  <jats:p>Although unsupervised anomaly detection has shown promising performance in industrial visual inspection, many architectures still struggle with variable input resolutions, and anomaly scores are often difficult for end users to interpret. This study proposes a multi-stage hybrid workflow for pixel-level defect localization and structured reporting in bolt head images. The proposed SA-PatchCore framework customizes PatchCore by extracting multi-scale representations from a frozen deep feature extractor and supporting resolution-adaptive anomaly-map reconstruction through dynamic feature-map sizing. After anomaly detection, a Qwen3-VL-32B-based reporting module, adapted with GRPO, uses both the original image and the anomaly overlay as visual evidence. It generates structured JSON outputs containing defect presence, a 3 × 3 location label, and a concise textual description. On the industrial bolt dataset, SA-PatchCore achieved 98.69% pixel-level AUROC, 29.73% Pixel-AP, and 39.24% oracle Pixel-F1max. Compared with PatchCore, PaDiM, DRÆM, and CS-Flow, the method delivered strong results, especially in Pixel-AUROC. In the reporting stage, defect presence/absence accuracy improved from 76.63% to 96.41%, while defective-sample recall increased from 74.23% to 96.14% over the baseline Qwen3-VL-32B. Exact location match rose from 28.15% to 53.78%, and mean partial location score improved from 32.29% to 65.34%. Overall, the framework combines accurate anomaly localization with structured reporting, improving interpretability and usability.</jats:p>
fulltext_available: false
fulltext_source: "none"
created: "2026-07-20T11:48:30.906699"
---

# Enhancing PatchCore with Dynamic Scaling and Vision–Language Models for Explainable Industrial Defect Inspection

## Abstract

<jats:p>Although unsupervised anomaly detection has shown promising performance in industrial visual inspection, many architectures still struggle with variable input resolutions, and anomaly scores are often difficult for end users to interpret. This study proposes a multi-stage hybrid workflow for pixel-level defect localization and structured reporting in bolt head images. The proposed SA-PatchCore framework customizes PatchCore by extracting multi-scale representations from a frozen deep feature extractor and supporting resolution-adaptive anomaly-map reconstruction through dynamic feature-map sizing. After anomaly detection, a Qwen3-VL-32B-based reporting module, adapted with GRPO, uses both the original image and the anomaly overlay as visual evidence. It generates structured JSON outputs containing defect presence, a 3 × 3 location label, and a concise textual description. On the industrial bolt dataset, SA-PatchCore achieved 98.69% pixel-level AUROC, 29.73% Pixel-AP, and 39.24% oracle Pixel-F1max. Compared with PatchCore, PaDiM, DRÆM, and CS-Flow, the method delivered strong results, especially in Pixel-AUROC. In the reporting stage, defect presence/absence accuracy improved from 76.63% to 96.41%, while defective-sample recall increased from 74.23% to 96.14% over the baseline Qwen3-VL-32B. Exact location match rose from 28.15% to 53.78%, and mean partial location score improved from 32.29% to 65.34%. Overall, the framework combines accurate anomaly localization with structured reporting, improving interpretability and usability.</jats:p>

## Links

- DOI: [10.3390/app16147096](https://doi.org/10.3390/app16147096)
- URL: [Link](https://doi.org/10.3390/app16147096)

## Faculty

- [[radboud-university/faculty#umut-güçlü|Umut Güçlü]]
