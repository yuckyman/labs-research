---
title: "Feasibility of Time-Domain DNN-Based Speech Enhancement on Embedded FPGA for Hearing Aid"
authors:
  - "Feyisayo Olalere"
  - "Umut Altin"
  - "Kiki van der Heijden"
  - "Marcel van Gerven"
year: 2026
journal: "arXiv"
arxiv_id: "2606.04221v1"
url: "https://arxiv.org/abs/2606.04221v1"
lab: "radboud-university"
faculty:
  - "Marcel van Gerven"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  Hearing aids impose strict latency and power constraints that current DNN-based speech enhancement systems struggle to meet on embedded hardware. We characterize this gap by deploying both speech separation and denoising using the lightweight SuDoRM-RF++ architecture on the AMD-Xilinx Kria KV260, evaluated at FP32 and 16-bit fixed-point precision for each task. Across these configurations, first-sample latency tracks with on-chip parameter caching rather than arithmetic throughput, identifying data movement as the primary bottleneck. Precision reduction halves the model memory footprint without compromising objective speech quality. The fixed-point denoising accelerator achieves a first-sample latency of 9.7~ms, meeting the 10~ms clinical threshold, while speech separation reaches 16.0~ms. These measurements establish concrete resource requirements for embedded DNN-based speech enhancement and quantify the remaining gap to hearing aid deployment.
fulltext_available: false
fulltext_source: "none"
created: "2026-06-08T13:12:04.750463"
---

# Feasibility of Time-Domain DNN-Based Speech Enhancement on Embedded FPGA for Hearing Aid

## Abstract

Hearing aids impose strict latency and power constraints that current DNN-based speech enhancement systems struggle to meet on embedded hardware. We characterize this gap by deploying both speech separation and denoising using the lightweight SuDoRM-RF++ architecture on the AMD-Xilinx Kria KV260, evaluated at FP32 and 16-bit fixed-point precision for each task. Across these configurations, first-sample latency tracks with on-chip parameter caching rather than arithmetic throughput, identifying data movement as the primary bottleneck. Precision reduction halves the model memory footprint without compromising objective speech quality. The fixed-point denoising accelerator achieves a first-sample latency of 9.7~ms, meeting the 10~ms clinical threshold, while speech separation reaches 16.0~ms. These measurements establish concrete resource requirements for embedded DNN-based speech enhancement and quantify the remaining gap to hearing aid deployment.

## Links

- arXiv: [arXiv:2606.04221v1](https://arxiv.org/abs/2606.04221v1)
- URL: [Link](https://arxiv.org/abs/2606.04221v1)

## Faculty

- [[radboud-university/faculty#marcel-van-gerven|Marcel van Gerven]]
