---
title: "A Modular Static Cost Analysis for GPU Warp-Level Parallelism"
authors:
  - "Gregory Blike"
  - "Hannah Zicarelli"
  - "Udaya Sathiyamoorthy"
  - "Julien Lange"
  - "Tiago Cogumbreiro"
year: 2026
journal: "Proceedings of the ACM on Programming Languages"
doi: "10.1145/3776693"
url: "https://doi.org/10.1145/3776693"
lab: "radboud-university"
faculty:
  - "Floris de Lange"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  <jats:p>Graphics Processing Units (GPUs) are the accelerator of choice for performance-critical applications, yet optimizing for performance requires mastery of the complex interactions between its memory architecture and its execution model. Existing static analysis tools for GPU kernels either identify performance bugs without quantifying costs or cannot handle thread-divergent control flow, leading to significant over-approximations. We present the first static relational-cost analysis for GPU warp-level parallelism that can give exact bounds even in the presence of thread divergence. Our analysis is general and flexible, as it is parametric on the resource metric (uncoalesced accesses, bank conflicts) and on the cost relation (=, ≤, ≥). We establish a soundness theorem for our technique, provide mechanized proofs in Rocq and implement our theory in a tool called Pico. In a reproducibility experiment, Pico produced the tightest bounds in every input, outperforming the state-of-the-art tool RaCUDA in 10 kernels (1.7×better), while RaCUDA produced 4 incorrect bounds and crashed on 2 kernels. In an experiment to measure the accuracy of Pico, we studied the impact of thread-divergence in control-flow in a dataset of 226 kernels. We found that at least 75.3% of conditionals and 85.4% of loops can be captured exactly, without introducing approximation.</jats:p>
fulltext_available: false
fulltext_source: "none"
created: "2026-01-12T09:36:06.123379"
---

# A Modular Static Cost Analysis for GPU Warp-Level Parallelism

## Abstract

<jats:p>Graphics Processing Units (GPUs) are the accelerator of choice for performance-critical applications, yet optimizing for performance requires mastery of the complex interactions between its memory architecture and its execution model. Existing static analysis tools for GPU kernels either identify performance bugs without quantifying costs or cannot handle thread-divergent control flow, leading to significant over-approximations. We present the first static relational-cost analysis for GPU warp-level parallelism that can give exact bounds even in the presence of thread divergence. Our analysis is general and flexible, as it is parametric on the resource metric (uncoalesced accesses, bank conflicts) and on the cost relation (=, ≤, ≥). We establish a soundness theorem for our technique, provide mechanized proofs in Rocq and implement our theory in a tool called Pico. In a reproducibility experiment, Pico produced the tightest bounds in every input, outperforming the state-of-the-art tool RaCUDA in 10 kernels (1.7×better), while RaCUDA produced 4 incorrect bounds and crashed on 2 kernels. In an experiment to measure the accuracy of Pico, we studied the impact of thread-divergence in control-flow in a dataset of 226 kernels. We found that at least 75.3% of conditionals and 85.4% of loops can be captured exactly, without introducing approximation.</jats:p>

## Links

- DOI: [10.1145/3776693](https://doi.org/10.1145/3776693)
- URL: [Link](https://doi.org/10.1145/3776693)

## Faculty

- [[radboud-university/faculty#floris-de-lange|Floris de Lange]]
