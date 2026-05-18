---
title: "Evolving Layer-Specific Scalar Functions for Hardware-Aware Transformer Adaptation"
authors:
  - "Kieran Carrigg"
  - "Sigur de Vries"
  - "Amirhossein Sadough"
  - "Marcel van Gerven"
year: 2026
journal: "arXiv"
arxiv_id: "2605.14047v1"
url: "https://arxiv.org/abs/2605.14047v1"
lab: "radboud-university"
faculty:
  - "Marcel van Gerven"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  Vision Transformers (ViTs) achieve state-of-the-art performance on challenging vision tasks, but their deployment on edge devices is severely hindered by the computational complexity and global reduction bottleneck imposed by layer normalization. Recent methods attempt to bypass this by replacing normalization layers with hardware-friendly scalar approximations. However, these homogeneous replacements do not optimally fit to all layers' behaviour and rely on expensive model retraining. In this work, we propose a highly efficient, hardware-aware framework that utilizes genetic programming (GP) to evolve heterogeneous, layer-specific scalar functions directly from pre-trained weights. Coupled with a novel post-training re-alignment strategy, our approach eliminates the need to retrain models from scratch entirely. Our evolved expressions accurately approximate the target normalization behaviours, capturing $91.6\\%$ of the variance ($R^2$) compared to only $70.2\\%$ for homogeneous baselines, allowing our modified architecture to recover $84.25\\%$ Top-1 ImageNet-1K accuracy in only 20 epochs. By preserving this performance while eliminating the global reduction bottleneck, our approach establishes a highly favourable trade-off between arithmetic complexity and off-chip memory traffic, removing a primary barrier to the efficient deployment of ViTs on edge accelerators.
fulltext_available: false
fulltext_source: "none"
created: "2026-05-18T12:38:50.289173"
---

# Evolving Layer-Specific Scalar Functions for Hardware-Aware Transformer Adaptation

## Abstract

Vision Transformers (ViTs) achieve state-of-the-art performance on challenging vision tasks, but their deployment on edge devices is severely hindered by the computational complexity and global reduction bottleneck imposed by layer normalization. Recent methods attempt to bypass this by replacing normalization layers with hardware-friendly scalar approximations. However, these homogeneous replacements do not optimally fit to all layers' behaviour and rely on expensive model retraining. In this work, we propose a highly efficient, hardware-aware framework that utilizes genetic programming (GP) to evolve heterogeneous, layer-specific scalar functions directly from pre-trained weights. Coupled with a novel post-training re-alignment strategy, our approach eliminates the need to retrain models from scratch entirely. Our evolved expressions accurately approximate the target normalization behaviours, capturing $91.6\%$ of the variance ($R^2$) compared to only $70.2\%$ for homogeneous baselines, allowing our modified architecture to recover $84.25\%$ Top-1 ImageNet-1K accuracy in only 20 epochs. By preserving this performance while eliminating the global reduction bottleneck, our approach establishes a highly favourable trade-off between arithmetic complexity and off-chip memory traffic, removing a primary barrier to the efficient deployment of ViTs on edge accelerators.

## Links

- arXiv: [arXiv:2605.14047v1](https://arxiv.org/abs/2605.14047v1)
- URL: [Link](https://arxiv.org/abs/2605.14047v1)

## Faculty

- [[radboud-university/faculty#marcel-van-gerven|Marcel van Gerven]]
