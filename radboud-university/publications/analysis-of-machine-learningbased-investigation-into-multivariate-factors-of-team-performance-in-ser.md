---
title: |
  Analysis of Machine Learning–Based Investigation Into Multivariate Factors of Team Performance in Serious Games: Cross-Sectional Retrospective Study
authors:
  - "Gruyff Germain Abdul-Rahman"
  - "Freark de Lange"
  - "Andrej Zwitter"
  - "Noman Haleem"
year: 2026
journal: "JMIR Serious Games"
doi: "10.2196/83478"
url: "https://doi.org/10.2196/83478"
lab: "radboud-university"
faculty:
  - "Floris de Lange"
tags:
  - "publication"
  - "radboud-university"
abstract: |
  <jats:title>Abstract</jats:title>
                    <jats:sec sec-type="background">
                      <jats:title>Background</jats:title>
                      <jats:p>Serious games (SGs) are increasingly used to study and enhance team performance in organizational and educational settings. While prior research has explored leadership and communication as isolated factors, the multivariate interactions between behavioral indicators remain poorly understood. A deeper understanding of these relationships can reveal which behavioral and demographic factors most strongly predict successful outcomes, offering insights relevant to both scientific research and practical training design.</jats:p>
                    </jats:sec>
                    <jats:sec sec-type="objective">
                      <jats:title>Objective</jats:title>
                      <jats:p>This study aimed to develop machine learning (ML) models to predict team success in SGs. Specifically, it sought to identify the behavioral and demographic predictors that most strongly influence team performance outcomes.</jats:p>
                    </jats:sec>
                    <jats:sec sec-type="methods">
                      <jats:title>Methods</jats:title>
                      <jats:p>
                        This study used a cross-sectional retrospective design. Behavioral and demographic data were analyzed from 233 teams participating in escape room–based SGs delivered by JGM Serious eXperiences in The Netherlands. Teams of 2‐8 players (mean age 25.8 y; 53 all-male, 55 all-female, and 125 mixed-gender) were scored by trained observers across collaboration, communication, and leadership constructs using Likert-scale indicators. Exploratory data analysis compared winning (n=141) and losing teams (n=92) using descriptive statistics, Pearson correlations, and significance testing (independent-samples
                        <jats:italic>t</jats:italic>
                        tests and Mann-Whitney
                        <jats:italic>U</jats:italic>
                        tests). Mean differences were interpreted with 95% CIs. A total of 4 ML models: logistic regression, random forest, multilayer perceptron, and support vector classifier, were trained using 5-fold cross-validation (
                        <jats:italic>F</jats:italic>
                        <jats:sub>1</jats:sub>
                        -score). The best model was interpreted using SHAP (Shapley Additive Explanations).
                      </jats:p>
                    </jats:sec>
                    <jats:sec sec-type="results">
                      <jats:title>Results</jats:title>
                      <jats:p>
                        Winning teams scored higher on several behavioral constructs, but only 4: knowledge sharing, leadership, guidance, and extraversion, showed statistically significant differences between winners and losing teams. These effects were supported by 95% CIs, Shapiro-Wilk tests for normality, and Mann-Whitney
                        <jats:italic>U</jats:italic>
                        tests where assumptions were violated, indicating that only a subset of behavioral indicators meaningfully distinguishes successful teams. Among the ML models, logistic regression achieved the highest accuracy (88%), followed by multilayer perceptron (87%), random forest (87%), and support vector classifier (85%). SHAP analysis showed that gender composition and prior escape-room experience were the strongest demographic predictors of success, while “celebrating progress” (extern5) and “taking initiative when the team is stuck” (sturing5) were the most influential behavioral indicators.
                      </jats:p>
                    </jats:sec>
                    <jats:sec sec-type="conclusions">
                      <jats:title>Conclusions</jats:title>
                      <jats:p>This work demonstrates the usefulness of multivariate analysis in studying and understanding complex human behavior in SG environments as opposed to studying isolated behavioral indicators, often described in previous studies. The ML models developed using behavioral and demographic features of participating teams showed promising accuracies, and their interpretation led to unveiling a set of demographic and behavioral components as the most decisive factors leading to team success. This improved understanding of what makes a team win can be potentially translated into terms of improved productivity in business and organizational settings.</jats:p>
                    </jats:sec>
fulltext_available: false
fulltext_source: "none"
created: "2026-04-20T10:54:14.684283"
---

# Analysis of Machine Learning–Based Investigation Into Multivariate Factors of Team Performance in Serious Games: Cross-Sectional Retrospective Study

## Abstract

<jats:title>Abstract</jats:title>
                  <jats:sec sec-type="background">
                    <jats:title>Background</jats:title>
                    <jats:p>Serious games (SGs) are increasingly used to study and enhance team performance in organizational and educational settings. While prior research has explored leadership and communication as isolated factors, the multivariate interactions between behavioral indicators remain poorly understood. A deeper understanding of these relationships can reveal which behavioral and demographic factors most strongly predict successful outcomes, offering insights relevant to both scientific research and practical training design.</jats:p>
                  </jats:sec>
                  <jats:sec sec-type="objective">
                    <jats:title>Objective</jats:title>
                    <jats:p>This study aimed to develop machine learning (ML) models to predict team success in SGs. Specifically, it sought to identify the behavioral and demographic predictors that most strongly influence team performance outcomes.</jats:p>
                  </jats:sec>
                  <jats:sec sec-type="methods">
                    <jats:title>Methods</jats:title>
                    <jats:p>
                      This study used a cross-sectional retrospective design. Behavioral and demographic data were analyzed from 233 teams participating in escape room–based SGs delivered by JGM Serious eXperiences in The Netherlands. Teams of 2‐8 players (mean age 25.8 y; 53 all-male, 55 all-female, and 125 mixed-gender) were scored by trained observers across collaboration, communication, and leadership constructs using Likert-scale indicators. Exploratory data analysis compared winning (n=141) and losing teams (n=92) using descriptive statistics, Pearson correlations, and significance testing (independent-samples
                      <jats:italic>t</jats:italic>
                      tests and Mann-Whitney
                      <jats:italic>U</jats:italic>
                      tests). Mean differences were interpreted with 95% CIs. A total of 4 ML models: logistic regression, random forest, multilayer perceptron, and support vector classifier, were trained using 5-fold cross-validation (
                      <jats:italic>F</jats:italic>
                      <jats:sub>1</jats:sub>
                      -score). The best model was interpreted using SHAP (Shapley Additive Explanations).
                    </jats:p>
                  </jats:sec>
                  <jats:sec sec-type="results">
                    <jats:title>Results</jats:title>
                    <jats:p>
                      Winning teams scored higher on several behavioral constructs, but only 4: knowledge sharing, leadership, guidance, and extraversion, showed statistically significant differences between winners and losing teams. These effects were supported by 95% CIs, Shapiro-Wilk tests for normality, and Mann-Whitney
                      <jats:italic>U</jats:italic>
                      tests where assumptions were violated, indicating that only a subset of behavioral indicators meaningfully distinguishes successful teams. Among the ML models, logistic regression achieved the highest accuracy (88%), followed by multilayer perceptron (87%), random forest (87%), and support vector classifier (85%). SHAP analysis showed that gender composition and prior escape-room experience were the strongest demographic predictors of success, while “celebrating progress” (extern5) and “taking initiative when the team is stuck” (sturing5) were the most influential behavioral indicators.
                    </jats:p>
                  </jats:sec>
                  <jats:sec sec-type="conclusions">
                    <jats:title>Conclusions</jats:title>
                    <jats:p>This work demonstrates the usefulness of multivariate analysis in studying and understanding complex human behavior in SG environments as opposed to studying isolated behavioral indicators, often described in previous studies. The ML models developed using behavioral and demographic features of participating teams showed promising accuracies, and their interpretation led to unveiling a set of demographic and behavioral components as the most decisive factors leading to team success. This improved understanding of what makes a team win can be potentially translated into terms of improved productivity in business and organizational settings.</jats:p>
                  </jats:sec>

## Links

- DOI: [10.2196/83478](https://doi.org/10.2196/83478)
- URL: [Link](https://doi.org/10.2196/83478)

## Faculty

- [[radboud-university/faculty#floris-de-lange|Floris de Lange]]
