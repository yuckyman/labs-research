---
title: "On Parallel and Distributed N-Body Simulations"
authors:
  - "Alexander Brandt"
year: 2026
journal: "Mathematics"
doi: "10.3390/math14091403"
url: "https://doi.org/10.3390/math14091403"
lab: "berlin-bccn"
faculty:
  - "Stephan Brandt"
tags:
  - "publication"
  - "berlin-bccn"
abstract: |
  <jats:p>The N-body problem is a classic problem involving a system of N discrete bodies mutually interacting in a dynamical system. At any moment in time there are N(N−1)/2 such interactions occurring. This N2 scaling leads to computational difficulties where simulations range from tens of thousands of bodies to billions or trillions. Approximation algorithms, such as the famous Barnes–Hut algorithm, simplify the number of interactions to scale as NlogN. Even still, this improvement in complexity is insufficient to achieve the desired performance for very large simulations on computing clusters with many nodes and many cores. In this work we explore a variety of algorithmic techniques for parallel and distributed variations on the Barnes–Hut algorithm to improve parallelism and reduce inter-process communication requirements. This includes the costzones and hashed octree techniques. We implement these techniques in a gravitational N-body simulation and show that they can be applied to both a parallel and distributed context. This work collects and unifies over 30 years of research, while filling in missing details, to provide a comprehensive and reproducible source.</jats:p>
fulltext_available: false
fulltext_source: "none"
created: "2026-04-27T11:09:04.680080"
---

# On Parallel and Distributed N-Body Simulations

## Abstract

<jats:p>The N-body problem is a classic problem involving a system of N discrete bodies mutually interacting in a dynamical system. At any moment in time there are N(N−1)/2 such interactions occurring. This N2 scaling leads to computational difficulties where simulations range from tens of thousands of bodies to billions or trillions. Approximation algorithms, such as the famous Barnes–Hut algorithm, simplify the number of interactions to scale as NlogN. Even still, this improvement in complexity is insufficient to achieve the desired performance for very large simulations on computing clusters with many nodes and many cores. In this work we explore a variety of algorithmic techniques for parallel and distributed variations on the Barnes–Hut algorithm to improve parallelism and reduce inter-process communication requirements. This includes the costzones and hashed octree techniques. We implement these techniques in a gravitational N-body simulation and show that they can be applied to both a parallel and distributed context. This work collects and unifies over 30 years of research, while filling in missing details, to provide a comprehensive and reproducible source.</jats:p>

## Links

- DOI: [10.3390/math14091403](https://doi.org/10.3390/math14091403)
- URL: [Link](https://doi.org/10.3390/math14091403)

## Faculty

- [[berlin-bccn/faculty#stephan-brandt|Stephan Brandt]]
