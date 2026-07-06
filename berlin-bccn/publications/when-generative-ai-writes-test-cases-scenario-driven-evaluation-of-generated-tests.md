---
title: "When Generative AI Writes Test Cases: Scenario-Driven Evaluation of Generated Tests"
authors:
  - "Baris Ardic"
  - "Idil Isil Yildirim"
  - "Carolin Brandt"
  - "Andy Zaidman"
year: 2026
doi: "10.21203/rs.3.rs-9238547/v1"
url: "https://doi.org/10.21203/rs.3.rs-9238547/v1"
lab: "berlin-bccn"
faculty:
  - "Stephan Brandt"
tags:
  - "publication"
  - "berlin-bccn"
abstract: |
  <title>Abstract</title>
                  <p>
                    Software developers increasingly turn to Generative AI (GenAI) to generate unit tests. Moreover, they can interact with GenAI in different ways, e.g., directly prompting to generate a test suite or asking for higher-level test scenarios.However, we lack the means to compare the effectiveness of these strategies.Commonly used metrics, e.g., coverage or pass@k, give limited insight into the effectiveness of a test suite.They do not fully capture which higher-level
                    <italic>test scenarios</italic>
                    are exercised by the test suite. In this paper, we present a scenario-driven evaluation methodology to compare automatically generated test suites and human-written test suites.We compare three interaction strategies for GenAI in terms of recovery of expected behavior, duplication, and additional (previously absent) scenarios.For this, we assemble a dataset of 15 Java methods with manually written tests. Then, we generate test suites with GenAI using distinct prompting strategies, and quantitatively and qualitatively analyze over 1800 tests.We show that direct prompts to generate whole test suites recover more of the manual scenarios but yield more duplicate tests.Ideate–then–implement prompts produce smaller suites with fewer duplicates, and ideate-only prompts surface more additional scenarios that can be selectively implemented later.In-depth manual analysis of the failing generated tests shows that most are straightforward to repair, while a smaller portion reflects behavioral misunderstandings between the method and generated tests.
                  </p>
fulltext_available: false
fulltext_source: "none"
created: "2026-07-06T12:51:10.102724"
---

# When Generative AI Writes Test Cases: Scenario-Driven Evaluation of Generated Tests

## Abstract

<title>Abstract</title>
                <p>
                  Software developers increasingly turn to Generative AI (GenAI) to generate unit tests. Moreover, they can interact with GenAI in different ways, e.g., directly prompting to generate a test suite or asking for higher-level test scenarios.However, we lack the means to compare the effectiveness of these strategies.Commonly used metrics, e.g., coverage or pass@k, give limited insight into the effectiveness of a test suite.They do not fully capture which higher-level
                  <italic>test scenarios</italic>
                  are exercised by the test suite. In this paper, we present a scenario-driven evaluation methodology to compare automatically generated test suites and human-written test suites.We compare three interaction strategies for GenAI in terms of recovery of expected behavior, duplication, and additional (previously absent) scenarios.For this, we assemble a dataset of 15 Java methods with manually written tests. Then, we generate test suites with GenAI using distinct prompting strategies, and quantitatively and qualitatively analyze over 1800 tests.We show that direct prompts to generate whole test suites recover more of the manual scenarios but yield more duplicate tests.Ideate–then–implement prompts produce smaller suites with fewer duplicates, and ideate-only prompts surface more additional scenarios that can be selectively implemented later.In-depth manual analysis of the failing generated tests shows that most are straightforward to repair, while a smaller portion reflects behavioral misunderstandings between the method and generated tests.
                </p>

## Links

- DOI: [10.21203/rs.3.rs-9238547/v1](https://doi.org/10.21203/rs.3.rs-9238547/v1)
- URL: [Link](https://doi.org/10.21203/rs.3.rs-9238547/v1)

## Faculty

- [[berlin-bccn/faculty#stephan-brandt|Stephan Brandt]]
