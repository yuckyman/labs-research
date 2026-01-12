---
title: "Welterweight Go: Boxing, Structural Subtyping, and Generics"
authors:
  - "Raymond Hu"
  - "Julien Lange"
  - "Bernardo Toninho"
  - "Philip Wadler"
  - "Robert Griesemer"
  - "Keith Randall"
year: 2026
journal: "Proceedings of the ACM on Programming Languages"
doi: "10.1145/3776721"
url: "https://doi.org/10.1145/3776721"
lab: "radboud-university"
faculty:
  - "Floris de Lange"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  <jats:p>Go’s unique combination of structural subtyping between generics and types with non-uniform runtime representations presents significant challenges for formalising the language.  
  We introduce WG (Welterweight Go), a core model of Go that captures key features excluded by prior work, including underlying types, type constraints and type sets, and proposed new features, such as generic methods. We also develop LWG, a lower-level language that models Go’s runtime mechanisms, notably the distinction between raw struct values and interface values that carry runtime type information (RTTI).  
  We give a type-directed compilation from WG to LWG that demonstrates how the proposed features can be implemented while observing important design and implementation goals for Go: compatibility with separate compilation, and no runtime code generation. Unlike existing approaches based on static monomorphisation, our compilation strategy uses runtime type conversions and adaptor methods to handle the complex interactions between structural subtyping, generics, and Go’s runtime infrastructure.</jats:p>
fulltext_available: false
fulltext_source: "none"
created: "2026-01-12T09:36:08.597454"
---

# Welterweight Go: Boxing, Structural Subtyping, and Generics

## Abstract

<jats:p>Go’s unique combination of structural subtyping between generics and types with non-uniform runtime representations presents significant challenges for formalising the language.  
We introduce WG (Welterweight Go), a core model of Go that captures key features excluded by prior work, including underlying types, type constraints and type sets, and proposed new features, such as generic methods. We also develop LWG, a lower-level language that models Go’s runtime mechanisms, notably the distinction between raw struct values and interface values that carry runtime type information (RTTI).  
We give a type-directed compilation from WG to LWG that demonstrates how the proposed features can be implemented while observing important design and implementation goals for Go: compatibility with separate compilation, and no runtime code generation. Unlike existing approaches based on static monomorphisation, our compilation strategy uses runtime type conversions and adaptor methods to handle the complex interactions between structural subtyping, generics, and Go’s runtime infrastructure.</jats:p>

## Links

- DOI: [10.1145/3776721](https://doi.org/10.1145/3776721)
- URL: [Link](https://doi.org/10.1145/3776721)

## Faculty

- [[radboud-university/faculty#floris-de-lange|Floris de Lange]]
