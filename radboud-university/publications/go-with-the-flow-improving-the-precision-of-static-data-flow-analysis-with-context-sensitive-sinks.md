---
title: "Go With the Flow: Improving the Precision of Static Data Flow Analysis with Context-Sensitive Sinks"
authors:
  - "Marc Miltenberger"
  - "Steven Arzt"
  - "Tim Lange"
year: 2026
journal: "ACM Transactions on Software Engineering and Methodology"
doi: "10.1145/3828165"
url: "https://doi.org/10.1145/3828165"
lab: "radboud-university"
faculty:
  - "Floris de Lange"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  <jats:p>Data flow analysis is widely used to detect security vulnerabilities and privacy leaks. As we show, the traditional model that tracks flows between API calls is insufficient. Calls to write methods on Java stream objects, for example, are only relevant in case the stream is derived from a network connection or publicly readable file. Writing to an in-memory byte stream, on the other hand, is irrelevant in a security analysis.</jats:p>
                    <jats:p>
                      In this paper, we introduce the notion of context-sensitive sinks. A method is only a sink, e.g., when the stream is obtained by calling another API method. To evaluate such conditions, a
                      <jats:italic toggle="yes">secondary flow</jats:italic>
                      to the sink is required. We propose a demanddriven backwards data flow algorithm that computes secondary flows in a scalable and precise manner. We implemented our approach
                      <jats:sc>River</jats:sc>
                      on top of FlowDroid. Our empirical evaluation on real-world apps from the Google Play Store shows that
                      <jats:sc>River</jats:sc>
                      can distinguish between different usages of streams, e.g., network connections, files, etc. and by doing so, reduce the number of false positives by 98% in comparison to FlowDroid while retaining precision and recall. Further,
                      <jats:sc>River</jats:sc>
                      only induces moderate overhead in computation time and memory.
                    </jats:p>
fulltext_available: false
fulltext_source: "none"
created: "2026-07-06T12:51:51.992785"
---

# Go With the Flow: Improving the Precision of Static Data Flow Analysis with Context-Sensitive Sinks

## Abstract

<jats:p>Data flow analysis is widely used to detect security vulnerabilities and privacy leaks. As we show, the traditional model that tracks flows between API calls is insufficient. Calls to write methods on Java stream objects, for example, are only relevant in case the stream is derived from a network connection or publicly readable file. Writing to an in-memory byte stream, on the other hand, is irrelevant in a security analysis.</jats:p>
                  <jats:p>
                    In this paper, we introduce the notion of context-sensitive sinks. A method is only a sink, e.g., when the stream is obtained by calling another API method. To evaluate such conditions, a
                    <jats:italic toggle="yes">secondary flow</jats:italic>
                    to the sink is required. We propose a demanddriven backwards data flow algorithm that computes secondary flows in a scalable and precise manner. We implemented our approach
                    <jats:sc>River</jats:sc>
                    on top of FlowDroid. Our empirical evaluation on real-world apps from the Google Play Store shows that
                    <jats:sc>River</jats:sc>
                    can distinguish between different usages of streams, e.g., network connections, files, etc. and by doing so, reduce the number of false positives by 98% in comparison to FlowDroid while retaining precision and recall. Further,
                    <jats:sc>River</jats:sc>
                    only induces moderate overhead in computation time and memory.
                  </jats:p>

## Links

- DOI: [10.1145/3828165](https://doi.org/10.1145/3828165)
- URL: [Link](https://doi.org/10.1145/3828165)

## Faculty

- [[radboud-university/faculty#floris-de-lange|Floris de Lange]]
