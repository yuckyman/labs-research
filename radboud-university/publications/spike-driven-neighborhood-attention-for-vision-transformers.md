---
title: "Spike-Driven Neighborhood Attention for Vision Transformers"
authors:
  - "Marzieh Hassanshahi Varposhti"
  - "Mahyar Shahsavari"
  - "Marcel van Gerven"
year: 2026
doi: "10.20944/preprints202608.2305.v1"
url: "https://doi.org/10.20944/preprints202608.2305.v1"
lab: "radboud-university"
faculty:
  - "Marcel van Gerven"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  <jats:p>Spiking Neural Networks (SNNs) promise ultra-low-power, event-driven computation; however, current efforts to integrate self-attention into spiking transformers predominantly rely on global attention mechanisms, introducing growing token complexity when scaling and diluting discriminative feature representations. We introduce Spike-Driven Neighborhood Attention (SDNA) over the full k×k neighbors window in two forms, Pairwise SDNA, which gates each query–neighbor interaction before aggregating, and Linear SDNA, which exploits the absence of a softmax in spiking attention to pool the key–value interaction over the window and gate it once, evaluating the spiking gate per position rather than per query–neighbor pair. Both operators are placed in a fully local hierarchical backbone that increases the receptive field without any global attention layer. Across static and neuromorphic benchmarks the two operators are competitive with global spike-driven transformers at comparable or lower parameter counts. On CIFAR-10 Pairwise SDNA reaches 97.24% and on N-Caltech101 Linear SDNA reaches 89.65%, each the highest among the compared spike-driven transformers and obtained with fewer parameters. These results indicate that dense global attention is not necessary for these tasks and that a full local neighborhood, with the gate reordered, is sufficient.</jats:p>
fulltext_available: false
fulltext_source: "none"
created: "2026-09-07T14:57:41.941193"
---

# Spike-Driven Neighborhood Attention for Vision Transformers

## Abstract

<jats:p>Spiking Neural Networks (SNNs) promise ultra-low-power, event-driven computation; however, current efforts to integrate self-attention into spiking transformers predominantly rely on global attention mechanisms, introducing growing token complexity when scaling and diluting discriminative feature representations. We introduce Spike-Driven Neighborhood Attention (SDNA) over the full k×k neighbors window in two forms, Pairwise SDNA, which gates each query–neighbor interaction before aggregating, and Linear SDNA, which exploits the absence of a softmax in spiking attention to pool the key–value interaction over the window and gate it once, evaluating the spiking gate per position rather than per query–neighbor pair. Both operators are placed in a fully local hierarchical backbone that increases the receptive field without any global attention layer. Across static and neuromorphic benchmarks the two operators are competitive with global spike-driven transformers at comparable or lower parameter counts. On CIFAR-10 Pairwise SDNA reaches 97.24% and on N-Caltech101 Linear SDNA reaches 89.65%, each the highest among the compared spike-driven transformers and obtained with fewer parameters. These results indicate that dense global attention is not necessary for these tasks and that a full local neighborhood, with the gate reordered, is sufficient.</jats:p>

## Links

- DOI: [10.20944/preprints202608.2305.v1](https://doi.org/10.20944/preprints202608.2305.v1)
- URL: [Link](https://doi.org/10.20944/preprints202608.2305.v1)

## Faculty

- [[radboud-university/faculty#marcel-van-gerven|Marcel van Gerven]]
