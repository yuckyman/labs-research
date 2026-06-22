---
title: "Distributed \Delta -Coloring Plays Hide-and-Seek"
authors:
  - "Alkida Balliu"
  - "Sebastian Brandt"
  - "Fabian Kuhn"
  - "Dennis Olivetti"
year: 2026
journal: "Journal of the ACM"
doi: "10.1145/3819817"
url: "https://doi.org/10.1145/3819817"
lab: "berlin-bccn"
faculty:
  - "Stephan Brandt"
tags:
  - "publication"
  - "berlin-bccn"
abstract: |
  <jats:p>
                      We prove several new tight or near-tight distributed lower bounds for classic symmetry breaking problems in graphs. As a basic tool, we first provide a new insightful proof that any deterministic distributed algorithm that computes a
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Delta</jats:tex-math>
                      </jats:inline-formula>
                      -coloring on
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Delta</jats:tex-math>
                      </jats:inline-formula>
                      -regular trees requires
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Omega (\\log _\\Delta n)</jats:tex-math>
                      </jats:inline-formula>
                      rounds and any randomized such algorithm requires
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Omega (\\log _\\Delta \\log n)</jats:tex-math>
                      </jats:inline-formula>
                      rounds. We prove this by showing that a natural relaxation of the
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Delta</jats:tex-math>
                      </jats:inline-formula>
                      -coloring problem is a fixed point in the round elimination framework.
                    </jats:p>
                    <jats:p>
                      As a first application, we show that our
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Delta</jats:tex-math>
                      </jats:inline-formula>
                      -coloring lower bound proof directly extends to arbdefective colorings. An arbdefective
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">c</jats:tex-math>
                      </jats:inline-formula>
                      -coloring of a graph
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">G=(V,E)</jats:tex-math>
                      </jats:inline-formula>
                      is given by a
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">c</jats:tex-math>
                      </jats:inline-formula>
                      -coloring of
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">V</jats:tex-math>
                      </jats:inline-formula>
                      and an orientation of
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">E</jats:tex-math>
                      </jats:inline-formula>
                      , where the arbdefect of a color
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">i</jats:tex-math>
                      </jats:inline-formula>
                      is the maximum number of monochromatic outgoing edges of any node of color
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">i</jats:tex-math>
                      </jats:inline-formula>
                      . We exactly characterize which variants of the arbdefective coloring problem can be solved in
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">O(f(\\Delta) + \\log ^*n)</jats:tex-math>
                      </jats:inline-formula>
                      rounds, for some function
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">f</jats:tex-math>
                      </jats:inline-formula>
                      , and which of them instead require
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Omega (\\log _\\Delta n)</jats:tex-math>
                      </jats:inline-formula>
                      rounds for deterministic algorithms and
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Omega (\\log _\\Delta \\log n)</jats:tex-math>
                      </jats:inline-formula>
                      rounds for randomized ones.
                    </jats:p>
                    <jats:p>
                      As a second application, which we see as our main contribution, we use the structure of the fixed point as a building block to prove lower bounds as a function of
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Delta</jats:tex-math>
                      </jats:inline-formula>
                      for problems that, in some sense, are
                      <jats:italic toggle="yes">much easier</jats:italic>
                      than
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Delta</jats:tex-math>
                      </jats:inline-formula>
                      -coloring, as they can be solved in
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">O(\\log ^* n)</jats:tex-math>
                      </jats:inline-formula>
                      deterministic rounds in bounded-degree graphs. More specifically, we prove lower bounds as a function of
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Delta</jats:tex-math>
                      </jats:inline-formula>
                      for a large class of distributed symmetry breaking problems, which can all be solved by a simple sequential greedy algorithm. For example, we obtain novel results for the fundamental problem of computing a
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">(2,\\beta)</jats:tex-math>
                      </jats:inline-formula>
                      -ruling set, i.e., for computing an independent set
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">S\\subseteq V</jats:tex-math>
                      </jats:inline-formula>
                      such that every node
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">v\\in V</jats:tex-math>
                      </jats:inline-formula>
                      is within distance
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\le \\beta</jats:tex-math>
                      </jats:inline-formula>
                      of some node in
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">S</jats:tex-math>
                      </jats:inline-formula>
                      . We in particular show that
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Omega (\\beta \\Delta ^{1/\\beta })</jats:tex-math>
                      </jats:inline-formula>
                      rounds are needed even if initially an
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">O(\\Delta)</jats:tex-math>
                      </jats:inline-formula>
                      -coloring of the graph is given. With an initial
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">O(\\Delta)</jats:tex-math>
                      </jats:inline-formula>
                      -coloring, this lower bound is tight and without, it still nearly matches the existing
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">O(\\beta \\Delta ^{2/(\\beta +1)}+\\log ^* n)</jats:tex-math>
                      </jats:inline-formula>
                      upper bound. The new
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">(2,\\beta)</jats:tex-math>
                      </jats:inline-formula>
                      -ruling set lower bound is an exponential improvement over the best existing lower bound for the problem, which was proven in [FOCS ’20]. As a special case of the lower bound, we also obtain a tight linear-in-
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Delta</jats:tex-math>
                      </jats:inline-formula>
                      lower bound for computing a maximal independent set (MIS) in trees. While such an MIS lower bound was known for general graphs, the best previous MIS lower bounds for trees was
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Omega (\\log \\Delta)</jats:tex-math>
                      </jats:inline-formula>
                      . Our lower bound even applies to a much more general family of problems that allows for almost arbitrary combinations of natural constraints from coloring problems, orientation problems, and independent set problems, and provides a single unified proof for known and new lower bound results for these types of problems.
                    </jats:p>
                    <jats:p>
                      All of our lower bounds as a function of
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Delta</jats:tex-math>
                      </jats:inline-formula>
                      also imply substantial lower bounds as a function of
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">n</jats:tex-math>
                      </jats:inline-formula>
                      . For instance, we obtain that the maximal independent set problem, on trees, requires
                      <jats:inline-formula content-type="math/tex">
                        <jats:tex-math notation="LaTeX" version="MathJaX">\\Omega (\\log n / \\log \\log n)</jats:tex-math>
                      </jats:inline-formula>
                      rounds for deterministic algorithms, which is tight.
                    </jats:p>
fulltext_available: false
fulltext_source: "none"
created: "2026-06-22T14:43:25.364245"
---

# Distributed  \Delta -Coloring Plays Hide-and-Seek

## Abstract

<jats:p>
                    We prove several new tight or near-tight distributed lower bounds for classic symmetry breaking problems in graphs. As a basic tool, we first provide a new insightful proof that any deterministic distributed algorithm that computes a
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Delta</jats:tex-math>
                    </jats:inline-formula>
                    -coloring on
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Delta</jats:tex-math>
                    </jats:inline-formula>
                    -regular trees requires
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Omega (\log _\Delta n)</jats:tex-math>
                    </jats:inline-formula>
                    rounds and any randomized such algorithm requires
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Omega (\log _\Delta \log n)</jats:tex-math>
                    </jats:inline-formula>
                    rounds. We prove this by showing that a natural relaxation of the
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Delta</jats:tex-math>
                    </jats:inline-formula>
                    -coloring problem is a fixed point in the round elimination framework.
                  </jats:p>
                  <jats:p>
                    As a first application, we show that our
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Delta</jats:tex-math>
                    </jats:inline-formula>
                    -coloring lower bound proof directly extends to arbdefective colorings. An arbdefective
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">c</jats:tex-math>
                    </jats:inline-formula>
                    -coloring of a graph
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">G=(V,E)</jats:tex-math>
                    </jats:inline-formula>
                    is given by a
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">c</jats:tex-math>
                    </jats:inline-formula>
                    -coloring of
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">V</jats:tex-math>
                    </jats:inline-formula>
                    and an orientation of
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">E</jats:tex-math>
                    </jats:inline-formula>
                    , where the arbdefect of a color
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">i</jats:tex-math>
                    </jats:inline-formula>
                    is the maximum number of monochromatic outgoing edges of any node of color
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">i</jats:tex-math>
                    </jats:inline-formula>
                    . We exactly characterize which variants of the arbdefective coloring problem can be solved in
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">O(f(\Delta) + \log ^*n)</jats:tex-math>
                    </jats:inline-formula>
                    rounds, for some function
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">f</jats:tex-math>
                    </jats:inline-formula>
                    , and which of them instead require
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Omega (\log _\Delta n)</jats:tex-math>
                    </jats:inline-formula>
                    rounds for deterministic algorithms and
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Omega (\log _\Delta \log n)</jats:tex-math>
                    </jats:inline-formula>
                    rounds for randomized ones.
                  </jats:p>
                  <jats:p>
                    As a second application, which we see as our main contribution, we use the structure of the fixed point as a building block to prove lower bounds as a function of
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Delta</jats:tex-math>
                    </jats:inline-formula>
                    for problems that, in some sense, are
                    <jats:italic toggle="yes">much easier</jats:italic>
                    than
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Delta</jats:tex-math>
                    </jats:inline-formula>
                    -coloring, as they can be solved in
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">O(\log ^* n)</jats:tex-math>
                    </jats:inline-formula>
                    deterministic rounds in bounded-degree graphs. More specifically, we prove lower bounds as a function of
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Delta</jats:tex-math>
                    </jats:inline-formula>
                    for a large class of distributed symmetry breaking problems, which can all be solved by a simple sequential greedy algorithm. For example, we obtain novel results for the fundamental problem of computing a
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">(2,\beta)</jats:tex-math>
                    </jats:inline-formula>
                    -ruling set, i.e., for computing an independent set
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">S\subseteq V</jats:tex-math>
                    </jats:inline-formula>
                    such that every node
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">v\in V</jats:tex-math>
                    </jats:inline-formula>
                    is within distance
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\le \beta</jats:tex-math>
                    </jats:inline-formula>
                    of some node in
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">S</jats:tex-math>
                    </jats:inline-formula>
                    . We in particular show that
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Omega (\beta \Delta ^{1/\beta })</jats:tex-math>
                    </jats:inline-formula>
                    rounds are needed even if initially an
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">O(\Delta)</jats:tex-math>
                    </jats:inline-formula>
                    -coloring of the graph is given. With an initial
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">O(\Delta)</jats:tex-math>
                    </jats:inline-formula>
                    -coloring, this lower bound is tight and without, it still nearly matches the existing
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">O(\beta \Delta ^{2/(\beta +1)}+\log ^* n)</jats:tex-math>
                    </jats:inline-formula>
                    upper bound. The new
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">(2,\beta)</jats:tex-math>
                    </jats:inline-formula>
                    -ruling set lower bound is an exponential improvement over the best existing lower bound for the problem, which was proven in [FOCS ’20]. As a special case of the lower bound, we also obtain a tight linear-in-
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Delta</jats:tex-math>
                    </jats:inline-formula>
                    lower bound for computing a maximal independent set (MIS) in trees. While such an MIS lower bound was known for general graphs, the best previous MIS lower bounds for trees was
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Omega (\log \Delta)</jats:tex-math>
                    </jats:inline-formula>
                    . Our lower bound even applies to a much more general family of problems that allows for almost arbitrary combinations of natural constraints from coloring problems, orientation problems, and independent set problems, and provides a single unified proof for known and new lower bound results for these types of problems.
                  </jats:p>
                  <jats:p>
                    All of our lower bounds as a function of
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Delta</jats:tex-math>
                    </jats:inline-formula>
                    also imply substantial lower bounds as a function of
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">n</jats:tex-math>
                    </jats:inline-formula>
                    . For instance, we obtain that the maximal independent set problem, on trees, requires
                    <jats:inline-formula content-type="math/tex">
                      <jats:tex-math notation="LaTeX" version="MathJaX">\Omega (\log n / \log \log n)</jats:tex-math>
                    </jats:inline-formula>
                    rounds for deterministic algorithms, which is tight.
                  </jats:p>

## Links

- DOI: [10.1145/3819817](https://doi.org/10.1145/3819817)
- URL: [Link](https://doi.org/10.1145/3819817)

## Faculty

- [[berlin-bccn/faculty#stephan-brandt|Stephan Brandt]]
