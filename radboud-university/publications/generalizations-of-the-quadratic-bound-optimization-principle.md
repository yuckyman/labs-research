---
title: "Generalizations of the quadratic bound optimization principle"
authors:
  - "Xun-Jian Li"
  - "Guo-Liang Tian"
  - "Hua Zhou"
  - "Kenneth Lange"
year: 2026
journal: "Proceedings of the National Academy of Sciences"
doi: "10.1073/pnas.2525320123"
url: "https://doi.org/10.1073/pnas.2525320123"
lab: "radboud-university"
faculty:
  - "Floris de Lange"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  <jats:p>
                      The quadratic bound (QB) principle proposed by Böhning and Lindsay in 1988 is an important special case of the majorization–minimization or minorization-maximization optimization principle. The quadratic upper-bound (QUB) principle is pertinent to minimization; the analogous quadratic lower-bound principle is pertinent to maximization. Unfortunately, in minimizing a loss
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mrow>
                            <mml:mi>f</mml:mi>
                            <mml:mo stretchy="false">(</mml:mo>
                            <mml:mrow>
                              <mml:mi mathvariant="bold-italic">θ</mml:mi>
                            </mml:mrow>
                            <mml:mo stretchy="false">)</mml:mo>
                          </mml:mrow>
                        </mml:math>
                      </jats:inline-formula>
                      , the QUB principle is limited by the difficulty of finding a constant positive definite matrix
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mrow>
                            <mml:mi mathvariant="bold-italic">B</mml:mi>
                          </mml:mrow>
                        </mml:math>
                      </jats:inline-formula>
                      such that
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mrow>
                            <mml:mrow>
                              <mml:mi mathvariant="bold-italic">B</mml:mi>
                            </mml:mrow>
                            <mml:mo>−</mml:mo>
                            <mml:msup>
                              <mml:mi>d</mml:mi>
                              <mml:mn>2</mml:mn>
                            </mml:msup>
                            <mml:mi>f</mml:mi>
                            <mml:mrow>
                              <mml:mo stretchy="false">(</mml:mo>
                              <mml:mrow>
                                <mml:mi mathvariant="bold-italic">θ</mml:mi>
                              </mml:mrow>
                              <mml:mo stretchy="false">)</mml:mo>
                            </mml:mrow>
                          </mml:mrow>
                        </mml:math>
                      </jats:inline-formula>
                      is positive semidefinite for all
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mrow>
                            <mml:mi mathvariant="bold-italic">θ</mml:mi>
                          </mml:mrow>
                        </mml:math>
                      </jats:inline-formula>
                      . This paper proposes a generalization of the QB principle that avoids this limitation. In particular, we construct QUB algorithms by replacing the matrix
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mrow>
                            <mml:mi mathvariant="bold-italic">B</mml:mi>
                          </mml:mrow>
                        </mml:math>
                      </jats:inline-formula>
                      by a continuous matrix-valued function
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mrow>
                            <mml:msub>
                              <mml:mi>B</mml:mi>
                              <mml:mi>n</mml:mi>
                            </mml:msub>
                            <mml:mrow>
                              <mml:mo stretchy="false">(</mml:mo>
                              <mml:mrow>
                                <mml:mi mathvariant="bold-italic">θ</mml:mi>
                              </mml:mrow>
                              <mml:mo stretchy="false">)</mml:mo>
                            </mml:mrow>
                          </mml:mrow>
                        </mml:math>
                      </jats:inline-formula>
                      that dominates the Hessian
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mrow>
                            <mml:msup>
                              <mml:mi>d</mml:mi>
                              <mml:mn>2</mml:mn>
                            </mml:msup>
                            <mml:mi>f</mml:mi>
                            <mml:mrow>
                              <mml:mo stretchy="false">(</mml:mo>
                              <mml:mrow>
                                <mml:mi mathvariant="bold-italic">θ</mml:mi>
                              </mml:mrow>
                              <mml:mo stretchy="false">)</mml:mo>
                            </mml:mrow>
                          </mml:mrow>
                        </mml:math>
                      </jats:inline-formula>
                      and depends on the both the current iterate
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:msub>
                            <mml:mrow>
                              <mml:mi mathvariant="bold-italic">θ</mml:mi>
                            </mml:mrow>
                            <mml:mi>n</mml:mi>
                          </mml:msub>
                        </mml:math>
                      </jats:inline-formula>
                      and the next potential iterate
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mrow>
                            <mml:mi mathvariant="bold-italic">θ</mml:mi>
                          </mml:mrow>
                        </mml:math>
                      </jats:inline-formula>
                      . In practice, we require
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mrow>
                            <mml:msub>
                              <mml:mi>B</mml:mi>
                              <mml:mi>n</mml:mi>
                            </mml:msub>
                            <mml:mrow>
                              <mml:mo stretchy="false">(</mml:mo>
                              <mml:mrow>
                                <mml:mi mathvariant="bold-italic">θ</mml:mi>
                              </mml:mrow>
                              <mml:mo stretchy="false">)</mml:mo>
                            </mml:mrow>
                          </mml:mrow>
                        </mml:math>
                      </jats:inline-formula>
                      to be diagonal with its diagonal entries separated in
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mrow>
                            <mml:mi mathvariant="bold-italic">θ</mml:mi>
                          </mml:mrow>
                        </mml:math>
                      </jats:inline-formula>
                      . In other words, the
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mi>i</mml:mi>
                        </mml:math>
                      </jats:inline-formula>
                      th diagonal entry of
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mrow>
                            <mml:msub>
                              <mml:mi>B</mml:mi>
                              <mml:mi>n</mml:mi>
                            </mml:msub>
                            <mml:mrow>
                              <mml:mo stretchy="false">(</mml:mo>
                              <mml:mrow>
                                <mml:mi mathvariant="bold-italic">θ</mml:mi>
                              </mml:mrow>
                              <mml:mo stretchy="false">)</mml:mo>
                            </mml:mrow>
                          </mml:mrow>
                        </mml:math>
                      </jats:inline-formula>
                      depends on
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mrow>
                            <mml:mi mathvariant="bold-italic">θ</mml:mi>
                          </mml:mrow>
                        </mml:math>
                      </jats:inline-formula>
                      only through its
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:mi>i</mml:mi>
                        </mml:math>
                      </jats:inline-formula>
                      th entry
                      <jats:inline-formula>
                        <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                          <mml:msub>
                            <mml:mi>θ</mml:mi>
                            <mml:mi>i</mml:mi>
                          </mml:msub>
                        </mml:math>
                      </jats:inline-formula>
                      . Theoretical analysis confirms that this class of generalized QB algorithms enjoys global convergence in favorable circumstances. For the scalar case, the tangency condition that the second derivative equals the bound function at the current point promotes superlinear convergence. Several numerical experiments implemented in Julia illustrate the power of the generalized QB principle.
                    </jats:p>
fulltext_available: false
fulltext_source: "none"
created: "2026-01-26T09:37:37.072939"
---

# Generalizations of the quadratic bound optimization principle

## Abstract

<jats:p>
                    The quadratic bound (QB) principle proposed by Böhning and Lindsay in 1988 is an important special case of the majorization–minimization or minorization-maximization optimization principle. The quadratic upper-bound (QUB) principle is pertinent to minimization; the analogous quadratic lower-bound principle is pertinent to maximization. Unfortunately, in minimizing a loss
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mrow>
                          <mml:mi>f</mml:mi>
                          <mml:mo stretchy="false">(</mml:mo>
                          <mml:mrow>
                            <mml:mi mathvariant="bold-italic">θ</mml:mi>
                          </mml:mrow>
                          <mml:mo stretchy="false">)</mml:mo>
                        </mml:mrow>
                      </mml:math>
                    </jats:inline-formula>
                    , the QUB principle is limited by the difficulty of finding a constant positive definite matrix
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mrow>
                          <mml:mi mathvariant="bold-italic">B</mml:mi>
                        </mml:mrow>
                      </mml:math>
                    </jats:inline-formula>
                    such that
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mrow>
                          <mml:mrow>
                            <mml:mi mathvariant="bold-italic">B</mml:mi>
                          </mml:mrow>
                          <mml:mo>−</mml:mo>
                          <mml:msup>
                            <mml:mi>d</mml:mi>
                            <mml:mn>2</mml:mn>
                          </mml:msup>
                          <mml:mi>f</mml:mi>
                          <mml:mrow>
                            <mml:mo stretchy="false">(</mml:mo>
                            <mml:mrow>
                              <mml:mi mathvariant="bold-italic">θ</mml:mi>
                            </mml:mrow>
                            <mml:mo stretchy="false">)</mml:mo>
                          </mml:mrow>
                        </mml:mrow>
                      </mml:math>
                    </jats:inline-formula>
                    is positive semidefinite for all
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mrow>
                          <mml:mi mathvariant="bold-italic">θ</mml:mi>
                        </mml:mrow>
                      </mml:math>
                    </jats:inline-formula>
                    . This paper proposes a generalization of the QB principle that avoids this limitation. In particular, we construct QUB algorithms by replacing the matrix
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mrow>
                          <mml:mi mathvariant="bold-italic">B</mml:mi>
                        </mml:mrow>
                      </mml:math>
                    </jats:inline-formula>
                    by a continuous matrix-valued function
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mrow>
                          <mml:msub>
                            <mml:mi>B</mml:mi>
                            <mml:mi>n</mml:mi>
                          </mml:msub>
                          <mml:mrow>
                            <mml:mo stretchy="false">(</mml:mo>
                            <mml:mrow>
                              <mml:mi mathvariant="bold-italic">θ</mml:mi>
                            </mml:mrow>
                            <mml:mo stretchy="false">)</mml:mo>
                          </mml:mrow>
                        </mml:mrow>
                      </mml:math>
                    </jats:inline-formula>
                    that dominates the Hessian
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mrow>
                          <mml:msup>
                            <mml:mi>d</mml:mi>
                            <mml:mn>2</mml:mn>
                          </mml:msup>
                          <mml:mi>f</mml:mi>
                          <mml:mrow>
                            <mml:mo stretchy="false">(</mml:mo>
                            <mml:mrow>
                              <mml:mi mathvariant="bold-italic">θ</mml:mi>
                            </mml:mrow>
                            <mml:mo stretchy="false">)</mml:mo>
                          </mml:mrow>
                        </mml:mrow>
                      </mml:math>
                    </jats:inline-formula>
                    and depends on the both the current iterate
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:msub>
                          <mml:mrow>
                            <mml:mi mathvariant="bold-italic">θ</mml:mi>
                          </mml:mrow>
                          <mml:mi>n</mml:mi>
                        </mml:msub>
                      </mml:math>
                    </jats:inline-formula>
                    and the next potential iterate
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mrow>
                          <mml:mi mathvariant="bold-italic">θ</mml:mi>
                        </mml:mrow>
                      </mml:math>
                    </jats:inline-formula>
                    . In practice, we require
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mrow>
                          <mml:msub>
                            <mml:mi>B</mml:mi>
                            <mml:mi>n</mml:mi>
                          </mml:msub>
                          <mml:mrow>
                            <mml:mo stretchy="false">(</mml:mo>
                            <mml:mrow>
                              <mml:mi mathvariant="bold-italic">θ</mml:mi>
                            </mml:mrow>
                            <mml:mo stretchy="false">)</mml:mo>
                          </mml:mrow>
                        </mml:mrow>
                      </mml:math>
                    </jats:inline-formula>
                    to be diagonal with its diagonal entries separated in
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mrow>
                          <mml:mi mathvariant="bold-italic">θ</mml:mi>
                        </mml:mrow>
                      </mml:math>
                    </jats:inline-formula>
                    . In other words, the
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mi>i</mml:mi>
                      </mml:math>
                    </jats:inline-formula>
                    th diagonal entry of
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mrow>
                          <mml:msub>
                            <mml:mi>B</mml:mi>
                            <mml:mi>n</mml:mi>
                          </mml:msub>
                          <mml:mrow>
                            <mml:mo stretchy="false">(</mml:mo>
                            <mml:mrow>
                              <mml:mi mathvariant="bold-italic">θ</mml:mi>
                            </mml:mrow>
                            <mml:mo stretchy="false">)</mml:mo>
                          </mml:mrow>
                        </mml:mrow>
                      </mml:math>
                    </jats:inline-formula>
                    depends on
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mrow>
                          <mml:mi mathvariant="bold-italic">θ</mml:mi>
                        </mml:mrow>
                      </mml:math>
                    </jats:inline-formula>
                    only through its
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:mi>i</mml:mi>
                      </mml:math>
                    </jats:inline-formula>
                    th entry
                    <jats:inline-formula>
                      <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline" overflow="scroll">
                        <mml:msub>
                          <mml:mi>θ</mml:mi>
                          <mml:mi>i</mml:mi>
                        </mml:msub>
                      </mml:math>
                    </jats:inline-formula>
                    . Theoretical analysis confirms that this class of generalized QB algorithms enjoys global convergence in favorable circumstances. For the scalar case, the tangency condition that the second derivative equals the bound function at the current point promotes superlinear convergence. Several numerical experiments implemented in Julia illustrate the power of the generalized QB principle.
                  </jats:p>

## Links

- DOI: [10.1073/pnas.2525320123](https://doi.org/10.1073/pnas.2525320123)
- URL: [Link](https://doi.org/10.1073/pnas.2525320123)

## Faculty

- [[radboud-university/faculty#floris-de-lange|Floris de Lange]]
