---
title: "Beyond 99%: Auditing Leakage, Shortcuts and Calibration in COVID-19 CT Classification"
authors:
  - "Sayantan Bhattacharya"
year: 2026
doi: "10.20944/preprints202610.2142.v1"
url: "https://doi.org/10.20944/preprints202610.2142.v1"
lab: "neuro-interaction-innovation-lab"
faculty:
  - "Sylvia Bhattacharya"
tags:
  - "publication"
  - "neuro-interaction-innovation-lab"
abstract: |
  <jats:p>Public CT benchmarks for COVID-19 report slice-level accuracy above 99%, yet slices from one scan are near-duplicates and most datasets ship without patient IDs. We audit a MobileNetV3-Large classifier on a 19,685-slice, three-class CT dataset (non-COVID, COVID, non-informative) along four axes: leakage, shortcuts, external validity and calibration. Replacing a random slice split with a group split on recovered pseudo-patients lowers accuracy from 99.42% to 97.18%, and to 95.39% when groups follow file order. The error rate rises 4.9 to 8.0 times, and recall of COVID slices falls from 99.6% to 96.0% and 88.8%. Scalar acquisition features alone reach 0.996 balanced accuracy under a slice split and 0.630 under a group split (chance 0.333), and models trained without the lungs, or with only the lungs, both reach about 93%. On two external sites, discrimination drops (AUROC 0.83 on Sao Paulo; 0.86 for COVID lesion slices against normal patients in Tehran), and every model scores community-acquired pneumonia as more COVID-like than COVID (AUROC 0.43 to 0.49). Calibration does not transfer: binary ECE rises from 0.02 in-domain to 0.19 to 0.53 externally, and temperature scaling recovers at most 0.034. Because the main dataset has no patient IDs, we tested our grouping against true IDs on the Tehran cohort. It recovers patients poorly (adjusted Rand index at most 0.29). A nearest-neighbor probe scores 0.998 under a random slice split, 0.551 under a true patient split and 0.717 under our recovered groups, so the slice-versus-group gaps we report are lower bounds on true patient-level leakage.</jats:p>
fulltext_available: false
fulltext_source: "none"
created: "2026-10-26T15:58:14.503264"
---

# Beyond 99%: Auditing Leakage, Shortcuts and Calibration in COVID-19 CT Classification

## Abstract

<jats:p>Public CT benchmarks for COVID-19 report slice-level accuracy above 99%, yet slices from one scan are near-duplicates and most datasets ship without patient IDs. We audit a MobileNetV3-Large classifier on a 19,685-slice, three-class CT dataset (non-COVID, COVID, non-informative) along four axes: leakage, shortcuts, external validity and calibration. Replacing a random slice split with a group split on recovered pseudo-patients lowers accuracy from 99.42% to 97.18%, and to 95.39% when groups follow file order. The error rate rises 4.9 to 8.0 times, and recall of COVID slices falls from 99.6% to 96.0% and 88.8%. Scalar acquisition features alone reach 0.996 balanced accuracy under a slice split and 0.630 under a group split (chance 0.333), and models trained without the lungs, or with only the lungs, both reach about 93%. On two external sites, discrimination drops (AUROC 0.83 on Sao Paulo; 0.86 for COVID lesion slices against normal patients in Tehran), and every model scores community-acquired pneumonia as more COVID-like than COVID (AUROC 0.43 to 0.49). Calibration does not transfer: binary ECE rises from 0.02 in-domain to 0.19 to 0.53 externally, and temperature scaling recovers at most 0.034. Because the main dataset has no patient IDs, we tested our grouping against true IDs on the Tehran cohort. It recovers patients poorly (adjusted Rand index at most 0.29). A nearest-neighbor probe scores 0.998 under a random slice split, 0.551 under a true patient split and 0.717 under our recovered groups, so the slice-versus-group gaps we report are lower bounds on true patient-level leakage.</jats:p>

## Links

- DOI: [10.20944/preprints202610.2142.v1](https://doi.org/10.20944/preprints202610.2142.v1)
- URL: [Link](https://doi.org/10.20944/preprints202610.2142.v1)

## Faculty

- [[neuro-interaction-innovation-lab/faculty#sylvia-bhattacharya|Sylvia Bhattacharya]]
