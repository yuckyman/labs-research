---
title: "Solving Flood-It Puzzles: A Comparison of Tailored A* Search with Declarative Solver Approaches"
authors:
  - "Philipp von Manteuffel"
  - "Benjamin Blankertz"
year: 2026
journal: "arXiv"
arxiv_id: "2610.31100v1"
url: "https://arxiv.org/abs/2610.31100v1"
lab: "berlin-bccn"
faculty:
  - "Benjamin Blankertz"
tags:
  - "publication"
  - "berlin-bccn"
abstract: |
  We present an optimized approach for finding minimal move sequences to solve Flood-It puzzles using A* search and compare it with approaches using SAT, Integer Programming, and Constraint Programming solvers. The performance of A* search is considerably improved by using an appropriate heuristic and sophisticated equivalences of game states to limit the search space. Each aspect is systematically evaluated, providing insights that generalize to other problems. By comparing the best variant of each approach, the A* search is the fastest in finding a minimal solution in about 75 % of the Flood-It instances tested. This result is in line with our expectation since A* specifically looks for a minimum solution. In contrast, the SAT-based approach is designed to solve the decision problem of whether a solution with a given length exists. An iterative search is required to determine a minimum solution length using a SAT-based approach. However, with increasing complexity, quantified by the minimum solution length, the SAT-based approach outperforms A*. We also compared the different approaches to the decision problem, where A* again performed best for the largest number of puzzles. Here, again, SAT supersedes A* for higher complexities, albeit with a lower crossing point.
fulltext_available: false
fulltext_source: "none"
created: "2026-10-26T16:00:09.367608"
---

# Solving Flood-It Puzzles: A Comparison of Tailored A* Search with Declarative Solver Approaches

## Abstract

We present an optimized approach for finding minimal move sequences to solve Flood-It puzzles using A* search and compare it with approaches using SAT, Integer Programming, and Constraint Programming solvers. The performance of A* search is considerably improved by using an appropriate heuristic and sophisticated equivalences of game states to limit the search space. Each aspect is systematically evaluated, providing insights that generalize to other problems. By comparing the best variant of each approach, the A* search is the fastest in finding a minimal solution in about 75 % of the Flood-It instances tested. This result is in line with our expectation since A* specifically looks for a minimum solution. In contrast, the SAT-based approach is designed to solve the decision problem of whether a solution with a given length exists. An iterative search is required to determine a minimum solution length using a SAT-based approach. However, with increasing complexity, quantified by the minimum solution length, the SAT-based approach outperforms A*. We also compared the different approaches to the decision problem, where A* again performed best for the largest number of puzzles. Here, again, SAT supersedes A* for higher complexities, albeit with a lower crossing point.

## Links

- arXiv: [arXiv:2610.31100v1](https://arxiv.org/abs/2610.31100v1)
- URL: [Link](https://arxiv.org/abs/2610.31100v1)

## Faculty

- [[berlin-bccn/faculty#benjamin-blankertz|Benjamin Blankertz]]
