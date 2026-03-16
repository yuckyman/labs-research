---
title: "Souporcell3: Robust Demultiplexing for High-Donor Single-Cell RNA-seq Datasets"
authors:
  - "Minindu Weerakoon"
  - "Hai Vu"
  - "Reza Behboudi"
  - "Haynes Heaton"
year: 2026
journal: "Bioinformatics"
doi: "10.1093/bioinformatics/btag117"
url: "https://doi.org/10.1093/bioinformatics/btag117"
lab: "berlin-bccn"
faculty:
  - "John-Dylan Haynes"
tags:
  - "publication"
  - "berlin-bccn"
abstract: |
  <jats:title>Abstract</jats:title>
                    <jats:sec>
                      <jats:title>Motivation</jats:title>
                      <jats:p>Accurate demultiplexing of pooled single-cell RNA-seq (scRNA-seq) data is critical for large-scale studies. However, existing methods like vireo, while effective up to ∼16 donors, often struggle with poor clustering due to local optima as donor numbers rise. In high-donor scenarios, overlapping genotypes, a dense genotype space, and increased doublet formation make demultiplexing challenging, requiring methods that are robust to sparse, high-dimensional data and maintain reliable accuracy even as sample complexity grows.</jats:p>
                    </jats:sec>
                    <jats:sec>
                      <jats:title>Results</jats:title>
                      <jats:p>We present an enhanced version of souporcell capable of demultiplexing up to 64 donors. The method uses 10x merge for initialization, K-Harmonic Means for robust clustering, and iterative refinement with reinitialization of low-quality clusters and locking of high-quality ones. Compared to vireo, overclustered vireo, and the original souporcell, our approach completely eliminates incorrectly merged clusters and achieves consistently high Adjusted Rand Index (ARI) scores across various doublet rates, demonstrating improved accuracy and scalability.</jats:p>
                    </jats:sec>
                    <jats:sec>
                      <jats:title>Availability</jats:title>
                      <jats:p>Souporcell3 is freely available under the MIT open-source license at https://github.com/wheaton5/souporcell.</jats:p>
                    </jats:sec>
                    <jats:sec>
                      <jats:title>Supplementary information</jats:title>
                      <jats:p>Supplementary data are available at Bioinformatics online.</jats:p>
                    </jats:sec>
fulltext_available: false
fulltext_source: "none"
created: "2026-03-16T10:08:05.404234"
---

# Souporcell3: Robust Demultiplexing for High-Donor Single-Cell RNA-seq Datasets

## Abstract

<jats:title>Abstract</jats:title>
                  <jats:sec>
                    <jats:title>Motivation</jats:title>
                    <jats:p>Accurate demultiplexing of pooled single-cell RNA-seq (scRNA-seq) data is critical for large-scale studies. However, existing methods like vireo, while effective up to ∼16 donors, often struggle with poor clustering due to local optima as donor numbers rise. In high-donor scenarios, overlapping genotypes, a dense genotype space, and increased doublet formation make demultiplexing challenging, requiring methods that are robust to sparse, high-dimensional data and maintain reliable accuracy even as sample complexity grows.</jats:p>
                  </jats:sec>
                  <jats:sec>
                    <jats:title>Results</jats:title>
                    <jats:p>We present an enhanced version of souporcell capable of demultiplexing up to 64 donors. The method uses 10x merge for initialization, K-Harmonic Means for robust clustering, and iterative refinement with reinitialization of low-quality clusters and locking of high-quality ones. Compared to vireo, overclustered vireo, and the original souporcell, our approach completely eliminates incorrectly merged clusters and achieves consistently high Adjusted Rand Index (ARI) scores across various doublet rates, demonstrating improved accuracy and scalability.</jats:p>
                  </jats:sec>
                  <jats:sec>
                    <jats:title>Availability</jats:title>
                    <jats:p>Souporcell3 is freely available under the MIT open-source license at https://github.com/wheaton5/souporcell.</jats:p>
                  </jats:sec>
                  <jats:sec>
                    <jats:title>Supplementary information</jats:title>
                    <jats:p>Supplementary data are available at Bioinformatics online.</jats:p>
                  </jats:sec>

## Links

- DOI: [10.1093/bioinformatics/btag117](https://doi.org/10.1093/bioinformatics/btag117)
- URL: [Link](https://doi.org/10.1093/bioinformatics/btag117)

## Faculty

- [[berlin-bccn/faculty#john-dylan-haynes|John-Dylan Haynes]]
