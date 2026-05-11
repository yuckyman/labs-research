---
title: "Neural Co-state Policies: Structuring Hidden States in Recurrent Reinforcement Learning"
authors:
  - "David Leeftink"
  - "Max Hinne"
  - "Marcel van Gerven"
year: 2026
journal: "arXiv"
arxiv_id: "2605.05373v1"
url: "https://arxiv.org/abs/2605.05373v1"
lab: "radboud-university"
faculty:
  - "Marcel van Gerven"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  A key capability of intelligent agents is operating under partial observability: reasoning and acting effectively despite missing or incomplete state observations. While recurrent (memory-based) policies learned via reinforcement learning address this by encoding history into latent state representations, their internal dynamics remain uninterpretable black boxes. This paper establishes a formal link between these hidden states and the Pontryagin minimum principle (PMP) from optimal control. We demonstrate that for standard recurrent architectures, latent representations map directly to PMP co-states, which allows the readout layer to be interpreted as performing Hamiltonian minimization. Because standard reward maximization does not naturally discover this alignment, we introduce a PMP-derived co-state loss to explicitly structure the internal dynamics. Empirically, this approach matches or improves performance on partially observable DMControl tasks, and is robust against zero-shot out-of-distribution sensor masking. By framing recurrent networks as dynamic processes governed by the minimum principle, we provide a principled approach to designing robust continuous control policies.
fulltext_available: false
fulltext_source: "none"
created: "2026-05-11T12:15:45.087814"
---

# Neural Co-state Policies: Structuring Hidden States in Recurrent Reinforcement Learning

## Abstract

A key capability of intelligent agents is operating under partial observability: reasoning and acting effectively despite missing or incomplete state observations. While recurrent (memory-based) policies learned via reinforcement learning address this by encoding history into latent state representations, their internal dynamics remain uninterpretable black boxes. This paper establishes a formal link between these hidden states and the Pontryagin minimum principle (PMP) from optimal control. We demonstrate that for standard recurrent architectures, latent representations map directly to PMP co-states, which allows the readout layer to be interpreted as performing Hamiltonian minimization. Because standard reward maximization does not naturally discover this alignment, we introduce a PMP-derived co-state loss to explicitly structure the internal dynamics. Empirically, this approach matches or improves performance on partially observable DMControl tasks, and is robust against zero-shot out-of-distribution sensor masking. By framing recurrent networks as dynamic processes governed by the minimum principle, we provide a principled approach to designing robust continuous control policies.

## Links

- arXiv: [arXiv:2605.05373v1](https://arxiv.org/abs/2605.05373v1)
- URL: [Link](https://arxiv.org/abs/2605.05373v1)

## Faculty

- [[radboud-university/faculty#marcel-van-gerven|Marcel van Gerven]]
