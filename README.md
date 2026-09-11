# WEVJ Dubai EV Charging Siting — Reproducibility Archive

This repository supports the published article:

**Ghassan Malkawi, Azmi Alazzam, Ahmed Abdelaziz Elsayed, Asem Omari, Said Badreddine, Bakeel Hussein, Mohammed Alhagyan, and Abdelrahman Altigani (2026).**  
**“An Interaction-Aware NI-EA Framework for EV Charging-Station Siting: Source-Conditioned Robust Candidate Sets and Bounded Spatial Evidence in Dubai.”**  
*World Electric Vehicle Journal*, **17**(8), 411.  
DOI: https://doi.org/10.3390/wevj17080411

Published: **6 August 2026**.

## Purpose

This repository is the public companion for the published paper. Its primary reproducibility claim is **reported-output verification**: it is intended to make the released, reuse-safe screening and robustness outputs easier to inspect, cite, and verify against the Version of Record.

The published article explicitly distinguishes this from complete regeneration from all retained raw source layers. A separate raw-source regeneration step would be required before the workflow could be described as fully reproducible from those raw source layers.

The study is a **public-data screening and robustness-audit study**. It is **not** demand validation, feeder-capacity validation, power-flow analysis, financial feasibility analysis, construction approval, or a final deployment plan.

## Published result anchors

Any reproduced or verified output should preserve the published result state:

- Admitted candidate/amenity records: **7,410**
- Inside-boundary candidates: **5,097**
- Baseline leader: **S1421 / Boonmax**
- Official-DEWA coordinate-source leader: **S3473**
- Necessary top-15 core: **12 candidates**
- Possible top-15 envelope: **18 candidates**
- TOPSIS top-15 overlap with baseline NI-EA: **0/15**
- Road-network top-15 overlap with baseline NI-EA: **14/15**
- Official-DEWA top-15 overlap with baseline NI-EA: **13/15**

These values are verification targets, not parameters to be re-estimated.

## Release verification status

The final publisher-facing supplementary ZIP supplied for this archive was checked before preparing the first GitHub/Zenodo release candidate.

- Original supplementary ZIP integrity: **PASS**
- Original static SHA-256 manifest: **89/89 PASS**
- Published reported-output verifier: **54 PASS / 0 FAIL**
- Public-safe release-candidate verifier: **54 PASS / 0 FAIL**
- Public-safe CSV coordinate-column scan: **PASS**

For the GitHub/Zenodo public companion, two publisher-facing files are not re-published: a candidate-level transit-context file containing latitude/longitude fields and an internal source-bound reconstruction script containing absolute local paths and dependencies on controlled/raw inputs. Aggregate transit summaries and the public reported-output verifier remain included. This is a packaging-only filter and does not alter any published result, score, rank, weight, model structure, or conclusion. Details and hashes are recorded in `release/`.

## Repository structure

- `data/` — documentation for reuse-safe derived data and redistribution boundaries.
- `results/` — published verification targets and reported-output checks.
- `reproducibility/` — release instructions and the reproducibility boundary.
- `release/` — release-candidate verification notes and package hashes.
- `CITATION.cff` — citation metadata for GitHub.
- `.zenodo.json` — metadata prepared for Zenodo archiving.

## Data and redistribution boundary

The article uses public-data-derived and author-generated outputs. The public GitHub/Zenodo companion is restricted to reuse-safe derived outputs, verification material, and bounded summaries.

Raw third-party exports or coordinate archives whose licensing or platform terms may restrict redistribution should **not** be copied into this repository merely for convenience. Where redistribution is not appropriate, this repository documents the source, date, role, and retrieval route instead.

The official article and its publisher-hosted Supplementary Materials remain the authoritative scientific record.

## Citation

Please cite the published article when using the scientific method or results. Once the first GitHub release is archived by Zenodo, the Zenodo DOI may additionally be cited when referring specifically to this archived reproducibility package.

## Versioning

The first archival release is tagged `v1.0.0` only after the verified public-safe package is present in the repository. Later releases should document repository or packaging changes without altering the published scientific results unless a documented correction is issued by the authors or publisher.
