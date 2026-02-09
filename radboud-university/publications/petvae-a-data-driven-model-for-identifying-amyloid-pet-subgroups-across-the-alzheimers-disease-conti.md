---
title: |
  petVAE: A Data-Driven Model for Identifying Amyloid PET Subgroups Across the Alzheimer’s Disease Continuum
authors:
  - "Arina A. Tagmazian"
  - "Claudia Schwarz"
  - "Catharina Lange"
  - "Esa Pitkänen"
  - "Eero Vuoksimaa"
  - ""
year: 2026
doi: "10.64898/2026.02.02.703218"
url: "https://doi.org/10.64898/2026.02.02.703218"
lab: "radboud-university"
faculty:
  - "Floris de Lange"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  <jats:title>Abstract</jats:title>
                  <jats:p>Amyloid-β (Aβ) PET imaging is a core biomarker and is considered sufficient for the biological diagnosis of Alzheimer’s disease (AD). However, it is typically reduced to a binary Aβ™/Aβ+ classification. In this study, we aimed to identify subgroups along the continuum of Aβ accumulation including subgroups within Aβ− and Aβ+.</jats:p>
                  <jats:p>
                    We used a total of 3,110 of Aβ PET scans from Alzheimer’s Disease Neuroimaging Initiative (ADNI) and Anti-Amyloid Treatment in Asymptomatic Alzheimer’s Disease (A4) datasets to develop
                    <jats:italic>petVAE</jats:italic>
                    , a 2D variational autoencoder model. The model accurately reconstructed Aβ PET scans without prior labeling or pre-selection based on scanner type or region of interest. Latent representations of scans extracted from the
                    <jats:italic>petVAE</jats:italic>
                    (11,648 latent features per scan) were used to visualize, analyze, and cluster the AD continuum. We identified the latent features most representative of the continuum, and clustering of PET scans using these features produced four clusters. Post-hoc characterization revealed that two clusters (Aβ-, Aβ-+) were predominantly Aβ negative and two (Aβ+, Aβ++) were predominantly Aβ positive.
                  </jats:p>
                  <jats:p>
                    All clusters differed significantly in standardized uptake value ratio (p &lt; 1.64×10
                    <jats:sup>−8</jats:sup>
                    ) and cerebrospinal fluid (CSF) Aβ (p &lt; 0.02), demonstrating petVAE’s ability to assign scans along the Aβ continuum. The clusters at the extremes of the continuum (Aβ-, Aβ++) resembled to the conventional Aβ negative and Aβ positive groups and differed significantly in cognitive performance, Apolipoprotein E (
                    <jats:italic>APOE</jats:italic>
                    ) ε4 prevalence, and Aβ, tau and phosphorylated tau CSF biomarkers (p &lt; 3×10
                    <jats:sup>−6</jats:sup>
                    ). The two intermediate clusters (Aβ-+, Aβ+) showed significantly higher odds of carrying at least one
                    <jats:italic>APOE</jats:italic>
                    ε4 allele compared with the Aβ-cluster (p &lt; 0.026). Participants in Aβ+ or Aβ++ clusters exhibited a significantly faster rate of progression to AD compared to Aβ-group (Hazard ratio = 2.42 and 9.43 for groups Aβ+ and Aβ++, respectively,
                    <jats:italic>p</jats:italic>
                    &lt; 1.17×10
                    <jats:sup>−7</jats:sup>
                    ).
                  </jats:p>
                  <jats:p>
                    Thus,
                    <jats:italic>petVAE</jats:italic>
                    was capable of reconstructing PET scans while also extracting latent features that effectively represented the AD continuum and defined biologically meaningful clusters. By capturing subtle Aβ-related changes in brain PET scans,
                    <jats:italic>petVAE</jats:italic>
                    -based classification enables the detection of preclinical AD stages and offers a new data-driven framework for studying disease progression.
                  </jats:p>
fulltext_available: false
fulltext_source: "none"
created: "2026-02-09T10:05:46.368361"
---

# petVAE: A Data-Driven Model for Identifying Amyloid PET Subgroups Across the Alzheimer’s Disease Continuum

## Abstract

<jats:title>Abstract</jats:title>
                <jats:p>Amyloid-β (Aβ) PET imaging is a core biomarker and is considered sufficient for the biological diagnosis of Alzheimer’s disease (AD). However, it is typically reduced to a binary Aβ™/Aβ+ classification. In this study, we aimed to identify subgroups along the continuum of Aβ accumulation including subgroups within Aβ− and Aβ+.</jats:p>
                <jats:p>
                  We used a total of 3,110 of Aβ PET scans from Alzheimer’s Disease Neuroimaging Initiative (ADNI) and Anti-Amyloid Treatment in Asymptomatic Alzheimer’s Disease (A4) datasets to develop
                  <jats:italic>petVAE</jats:italic>
                  , a 2D variational autoencoder model. The model accurately reconstructed Aβ PET scans without prior labeling or pre-selection based on scanner type or region of interest. Latent representations of scans extracted from the
                  <jats:italic>petVAE</jats:italic>
                  (11,648 latent features per scan) were used to visualize, analyze, and cluster the AD continuum. We identified the latent features most representative of the continuum, and clustering of PET scans using these features produced four clusters. Post-hoc characterization revealed that two clusters (Aβ-, Aβ-+) were predominantly Aβ negative and two (Aβ+, Aβ++) were predominantly Aβ positive.
                </jats:p>
                <jats:p>
                  All clusters differed significantly in standardized uptake value ratio (p &lt; 1.64×10
                  <jats:sup>−8</jats:sup>
                  ) and cerebrospinal fluid (CSF) Aβ (p &lt; 0.02), demonstrating petVAE’s ability to assign scans along the Aβ continuum. The clusters at the extremes of the continuum (Aβ-, Aβ++) resembled to the conventional Aβ negative and Aβ positive groups and differed significantly in cognitive performance, Apolipoprotein E (
                  <jats:italic>APOE</jats:italic>
                  ) ε4 prevalence, and Aβ, tau and phosphorylated tau CSF biomarkers (p &lt; 3×10
                  <jats:sup>−6</jats:sup>
                  ). The two intermediate clusters (Aβ-+, Aβ+) showed significantly higher odds of carrying at least one
                  <jats:italic>APOE</jats:italic>
                  ε4 allele compared with the Aβ-cluster (p &lt; 0.026). Participants in Aβ+ or Aβ++ clusters exhibited a significantly faster rate of progression to AD compared to Aβ-group (Hazard ratio = 2.42 and 9.43 for groups Aβ+ and Aβ++, respectively,
                  <jats:italic>p</jats:italic>
                  &lt; 1.17×10
                  <jats:sup>−7</jats:sup>
                  ).
                </jats:p>
                <jats:p>
                  Thus,
                  <jats:italic>petVAE</jats:italic>
                  was capable of reconstructing PET scans while also extracting latent features that effectively represented the AD continuum and defined biologically meaningful clusters. By capturing subtle Aβ-related changes in brain PET scans,
                  <jats:italic>petVAE</jats:italic>
                  -based classification enables the detection of preclinical AD stages and offers a new data-driven framework for studying disease progression.
                </jats:p>

## Links

- DOI: [10.64898/2026.02.02.703218](https://doi.org/10.64898/2026.02.02.703218)
- URL: [Link](https://doi.org/10.64898/2026.02.02.703218)

## Faculty

- [[radboud-university/faculty#floris-de-lange|Floris de Lange]]
