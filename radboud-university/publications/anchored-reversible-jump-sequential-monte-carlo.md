---
title: "Anchored Reversible Jump Sequential Monte Carlo"
authors:
  - "Janna van Assen"
  - "Max Hinne"
year: 2026
journal: "arXiv"
arxiv_id: "2610.09930v1"
url: "https://arxiv.org/abs/2610.09930v1"
lab: "radboud-university"
faculty:
  - "Max Hinne"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  Reversible Jump Markov Chain Monte Carlo (RJMCMC) is a principled framework for Bayesian model comparison, but its practical use is often limited due to the difficulty of designing between-model proposals that reach regions of high posterior probability. In addition, its inherently sequential nature limits efficient use of modern GPU architectures. We address both challenges by introducing Anchored Reversible Jump Sequential Monte Carlo. Our approach combines RJMCMC with Sequential Monte Carlo (SMC) to explore the model space in parallel. Importantly, the particle population enables effective between-model proposals without problem-specific knowledge: particles are used to construct kernel density approximations of the target distributions within each model, which are then used to generate trans-dimensional proposals. Numerical experiments show that the proposed method is computationally efficient and competitive with state-of-the-art RJMCMC approaches, demonstrating its potential for scalable Bayesian model comparison.
fulltext_available: false
fulltext_source: "none"
created: "2026-10-12T18:45:31.178561"
---

# Anchored Reversible Jump Sequential Monte Carlo

## Abstract

Reversible Jump Markov Chain Monte Carlo (RJMCMC) is a principled framework for Bayesian model comparison, but its practical use is often limited due to the difficulty of designing between-model proposals that reach regions of high posterior probability. In addition, its inherently sequential nature limits efficient use of modern GPU architectures. We address both challenges by introducing Anchored Reversible Jump Sequential Monte Carlo. Our approach combines RJMCMC with Sequential Monte Carlo (SMC) to explore the model space in parallel. Importantly, the particle population enables effective between-model proposals without problem-specific knowledge: particles are used to construct kernel density approximations of the target distributions within each model, which are then used to generate trans-dimensional proposals. Numerical experiments show that the proposed method is computationally efficient and competitive with state-of-the-art RJMCMC approaches, demonstrating its potential for scalable Bayesian model comparison.

## Links

- arXiv: [arXiv:2610.09930v1](https://arxiv.org/abs/2610.09930v1)
- URL: [Link](https://arxiv.org/abs/2610.09930v1)

## Faculty

- [[radboud-university/faculty#max-hinne|Max Hinne]]
