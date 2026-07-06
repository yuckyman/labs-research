---
title: |
  Seismo-Acoustic Meteoroid Observation Recording Database (SMORD): A Global Dataset and Deep-Learning Phase Picker for Meteoroid-Generated Air-to-Ground Coupled Seismic Waves
authors:
  - "Dario Eickhoff"
  - "Runa Ostermeier"
  - "Joachim Ritter"
year: 2026
journal: "Seismica"
doi: "10.26443/seismica.v5i2.2551"
url: "https://doi.org/10.26443/seismica.v5i2.2551"
lab: "berlin-bccn"
faculty:
  - "Petra Ritter"
tags:
  - "publication"
  - "berlin-bccn"
abstract: |
  <jats:p>Meteoroids impacting Earth's atmosphere generate acoustic waves that can couple into the ground and can be recorded by dense, globally distributed seismic networks. Thus, these records complement optical and radar observations, especially since seismic stations also operate in cloudy weather conditions and during daytime. However, open datasets that link meteoroid events to labeled seismic waveforms are scarce, limiting the development of automated detectors for meteoroid-induced seismo-acoustic signals. We introduce the Seismo-acoustic Meteoroid Observation Recording Database (SMORD), compiled by cross-referencing public meteoroid catalogs (International Meteor Organization fireball reports; NASA CNEOS fireball catalog) with seismic archives. Continuous waveforms are manually labeled for the first clear meteoroid-related onset of air-to-ground coupled seismic waves using a three-level pick-quality scheme. SMORD v1.0 contains 310 meteoroid events and 3,295 labeled arrivals across a global station set. Using SMORD labels, we train a PhaseNet picker in SeisBench with station-level splits and augmentation. On test data, the model achieves 91% precision and 94% recall at a 0.5 decision threshold (area-under-curve value 0.89), with median absolute timing error of 0.02~s (90% within c. ±0.3 s). We demonstrate automated onset detection and trajectory reconstruction for an April 2025 Adriatic fireball, highlighting the values of SMORD for rapid post-event analysis.</jats:p>
fulltext_available: false
fulltext_source: "none"
created: "2026-07-06T12:50:12.107474"
---

# Seismo-Acoustic Meteoroid Observation Recording Database (SMORD): A Global Dataset and Deep-Learning Phase Picker for Meteoroid-Generated Air-to-Ground Coupled Seismic Waves

## Abstract

<jats:p>Meteoroids impacting Earth's atmosphere generate acoustic waves that can couple into the ground and can be recorded by dense, globally distributed seismic networks. Thus, these records complement optical and radar observations, especially since seismic stations also operate in cloudy weather conditions and during daytime. However, open datasets that link meteoroid events to labeled seismic waveforms are scarce, limiting the development of automated detectors for meteoroid-induced seismo-acoustic signals. We introduce the Seismo-acoustic Meteoroid Observation Recording Database (SMORD), compiled by cross-referencing public meteoroid catalogs (International Meteor Organization fireball reports; NASA CNEOS fireball catalog) with seismic archives. Continuous waveforms are manually labeled for the first clear meteoroid-related onset of air-to-ground coupled seismic waves using a three-level pick-quality scheme. SMORD v1.0 contains 310 meteoroid events and 3,295 labeled arrivals across a global station set. Using SMORD labels, we train a PhaseNet picker in SeisBench with station-level splits and augmentation. On test data, the model achieves 91% precision and 94% recall at a 0.5 decision threshold (area-under-curve value 0.89), with median absolute timing error of 0.02~s (90% within c. ±0.3 s). We demonstrate automated onset detection and trajectory reconstruction for an April 2025 Adriatic fireball, highlighting the values of SMORD for rapid post-event analysis.</jats:p>

## Links

- DOI: [10.26443/seismica.v5i2.2551](https://doi.org/10.26443/seismica.v5i2.2551)
- URL: [Link](https://doi.org/10.26443/seismica.v5i2.2551)

## Faculty

- [[berlin-bccn/faculty#petra-ritter|Petra Ritter]]
