---
title: |
  Artificial intelligence-based ECG reconstruction error as a continuous predictor of all-cause mortality: a multi-cohort retrospective validation study
authors:
  - "Angus Nicolson"
  - "Samuel Pröll"
  - "Riccardo Lunelli"
  - "Hagen Blankenburg"
  - "Peter Pramstaller"
  - "Christian Fuchsberger"
  - "Axel Bauer"
  - "Clemens Dlaska"
year: 2026
doi: "10.64898/2026.07.10.26357749"
url: "https://doi.org/10.64898/2026.07.10.26357749"
lab: "berlin-bccn"
faculty:
  - "Felix Blankenburg"
tags:
  - "publication"
  - "berlin-bccn"
abstract: |
  <jats:title>Abstract</jats:title>
                  <jats:sec>
                    <jats:title>Background</jats:title>
                    <jats:p>Recent artificial intelligence (AI) models applied to the electrocardiogram (ECG) for risk stratification typically rely on supervised learning, defining risk as the error relative to an external target such as age or sex. This couples the risk score to the choice of target rather than the cardiac signal alone, and may limit generalisability. We aimed to develop a self-supervised AI-ECG risk score based on the error in reconstructing a partially masked ECG.</jats:p>
                  </jats:sec>
                  <jats:sec>
                    <jats:title>Methods</jats:title>
                    <jats:p>A transformer-based masked autoencoder was trained on 85% of the CODE dataset (n = 7,212,109 ECGs) to reconstruct ECG signals from partially masked inputs. The association between reconstruction error and all-cause mortality was assessed internally in CODE-15% and externally validated in four independent cohorts: MIMIC-IV-ECG (critical care, US), HEEDB (hospital, US), CHRIS (population-based, Italy), and Innsbruck (cardiology centre, Austria). A binary risk score (&gt;1 SD above the CODE-15% mean) was additionally evaluated in these cohorts and in the UK Biobank (population-based, UK).</jats:p>
                  </jats:sec>
                  <jats:sec>
                    <jats:title>Findings</jats:title>
                    <jats:p>In Cox proportional hazards models adjusted for age and sex, each 1-SD increase in reconstruction error was associated with higher all-cause mortality (all p&lt;0.001; cohort median follow-up 1.4-11.0 years): CODE-15% (HR 1.39, 95% CI 1.37-1.42), MIMIC-IV-ECG (HR 1.39, 95% CI 1.37-1.40), HEEDB (HR 1.41, 95% CI 1.40-1.41), Innsbruck (HR 1.23, 95% CI 1.21-1.26), and CHRIS (HR 1.25, 95% CI 1.14-1.38). The binary threshold identified a high-risk group with increased mortality in all six cohorts, including the UK Biobank (HR 1.27, 95% CI 1.08-1.50, p=0.004).</jats:p>
                  </jats:sec>
                  <jats:sec>
                    <jats:title>Interpretation</jats:title>
                    <jats:p>Reconstruction error is a generalisable predictor of all-cause mortality across diverse clinical and population-based settings. Unlike supervised approaches, it reflects the model’s uncertainty about the ECG signal itself rather than error relative to an external target, providing a direct measure of how much each recording deviates from normal cardiac electrical patterns.</jats:p>
                  </jats:sec>
fulltext_available: false
fulltext_source: "none"
created: "2026-07-20T11:47:28.389994"
---

# Artificial intelligence-based ECG reconstruction error as a continuous predictor of all-cause mortality: a multi-cohort retrospective validation study

## Abstract

<jats:title>Abstract</jats:title>
                <jats:sec>
                  <jats:title>Background</jats:title>
                  <jats:p>Recent artificial intelligence (AI) models applied to the electrocardiogram (ECG) for risk stratification typically rely on supervised learning, defining risk as the error relative to an external target such as age or sex. This couples the risk score to the choice of target rather than the cardiac signal alone, and may limit generalisability. We aimed to develop a self-supervised AI-ECG risk score based on the error in reconstructing a partially masked ECG.</jats:p>
                </jats:sec>
                <jats:sec>
                  <jats:title>Methods</jats:title>
                  <jats:p>A transformer-based masked autoencoder was trained on 85% of the CODE dataset (n = 7,212,109 ECGs) to reconstruct ECG signals from partially masked inputs. The association between reconstruction error and all-cause mortality was assessed internally in CODE-15% and externally validated in four independent cohorts: MIMIC-IV-ECG (critical care, US), HEEDB (hospital, US), CHRIS (population-based, Italy), and Innsbruck (cardiology centre, Austria). A binary risk score (&gt;1 SD above the CODE-15% mean) was additionally evaluated in these cohorts and in the UK Biobank (population-based, UK).</jats:p>
                </jats:sec>
                <jats:sec>
                  <jats:title>Findings</jats:title>
                  <jats:p>In Cox proportional hazards models adjusted for age and sex, each 1-SD increase in reconstruction error was associated with higher all-cause mortality (all p&lt;0.001; cohort median follow-up 1.4-11.0 years): CODE-15% (HR 1.39, 95% CI 1.37-1.42), MIMIC-IV-ECG (HR 1.39, 95% CI 1.37-1.40), HEEDB (HR 1.41, 95% CI 1.40-1.41), Innsbruck (HR 1.23, 95% CI 1.21-1.26), and CHRIS (HR 1.25, 95% CI 1.14-1.38). The binary threshold identified a high-risk group with increased mortality in all six cohorts, including the UK Biobank (HR 1.27, 95% CI 1.08-1.50, p=0.004).</jats:p>
                </jats:sec>
                <jats:sec>
                  <jats:title>Interpretation</jats:title>
                  <jats:p>Reconstruction error is a generalisable predictor of all-cause mortality across diverse clinical and population-based settings. Unlike supervised approaches, it reflects the model’s uncertainty about the ECG signal itself rather than error relative to an external target, providing a direct measure of how much each recording deviates from normal cardiac electrical patterns.</jats:p>
                </jats:sec>

## Links

- DOI: [10.64898/2026.07.10.26357749](https://doi.org/10.64898/2026.07.10.26357749)
- URL: [Link](https://doi.org/10.64898/2026.07.10.26357749)

## Faculty

- [[berlin-bccn/faculty#felix-blankenburg|Felix Blankenburg]]
