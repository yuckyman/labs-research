---
title: "Generative Modeling of Clinical Time Series via Latent Stochastic Differential Equations"
authors:
  - "Muhammad Aslanimoghanloo"
  - "Ahmed ElGazzar"
  - "Marcel van Gerven"
year: 2025
journal: "arXiv"
arxiv_id: "2511.16427v1"
url: "https://arxiv.org/abs/2511.16427v1"
lab: "radboud-university"
faculty:
  - "Marcel van Gerven"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  Clinical time series data from electronic health records and medical registries offer unprecedented opportunities to understand patient trajectories and inform medical decision-making. However, leveraging such data presents significant challenges due to irregular sampling, complex latent physiology, and inherent uncertainties in both measurements and disease progression. To address these challenges, we propose a generative modeling framework based on latent neural stochastic differential equations (SDEs) that views clinical time series as discrete-time partial observations of an underlying controlled stochastic dynamical system. Our approach models latent dynamics via neural SDEs with modality-dependent emission models, while performing state estimation and parameter learning through variational inference. This formulation naturally handles irregularly sampled observations, learns complex non-linear interactions, and captures the stochasticity of disease progression and measurement noise within a unified scalable probabilistic framework. We validate the framework on two complementary tasks: (i) individual treatment effect estimation using a simulated pharmacokinetic-pharmacodynamic (PKPD) model of lung cancer, and (ii) probabilistic forecasting of physiological signals using real-world intensive care unit (ICU) data from 12,000 patients. Results show that our framework outperforms ordinary differential equation and long short-term memory baseline models in accuracy and uncertainty estimation. These results highlight its potential for enabling precise, uncertainty-aware predictions to support clinical decision-making.
fulltext_available: false
fulltext_source: "none"
created: "2025-11-24T09:30:11.930958"
---

# Generative Modeling of Clinical Time Series via Latent Stochastic Differential Equations

## Abstract

Clinical time series data from electronic health records and medical registries offer unprecedented opportunities to understand patient trajectories and inform medical decision-making. However, leveraging such data presents significant challenges due to irregular sampling, complex latent physiology, and inherent uncertainties in both measurements and disease progression. To address these challenges, we propose a generative modeling framework based on latent neural stochastic differential equations (SDEs) that views clinical time series as discrete-time partial observations of an underlying controlled stochastic dynamical system. Our approach models latent dynamics via neural SDEs with modality-dependent emission models, while performing state estimation and parameter learning through variational inference. This formulation naturally handles irregularly sampled observations, learns complex non-linear interactions, and captures the stochasticity of disease progression and measurement noise within a unified scalable probabilistic framework. We validate the framework on two complementary tasks: (i) individual treatment effect estimation using a simulated pharmacokinetic-pharmacodynamic (PKPD) model of lung cancer, and (ii) probabilistic forecasting of physiological signals using real-world intensive care unit (ICU) data from 12,000 patients. Results show that our framework outperforms ordinary differential equation and long short-term memory baseline models in accuracy and uncertainty estimation. These results highlight its potential for enabling precise, uncertainty-aware predictions to support clinical decision-making.

## Links

- arXiv: [arXiv:2511.16427v1](https://arxiv.org/abs/2511.16427v1)
- URL: [Link](https://arxiv.org/abs/2511.16427v1)

## Faculty

- [[radboud-university/faculty#marcel-van-gerven|Marcel van Gerven]]
