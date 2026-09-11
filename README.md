# WEVJ Dubai EV Charging Siting — Reproducibility Archive

This repository supports the published article:

**Ghassan Malkawi, Azmi Alazzam, Ahmed Abdelaziz Elsayed, Asem Omari, Said Badreddine, Bakeel Hussein, Mohammed Alhagyan, and Abdelrahman Altigani (2026).**  
**“An Interaction-Aware NI-EA Framework for EV Charging-Station Siting: Source-Conditioned Robust Candidate Sets and Bounded Spatial Evidence in Dubai.”**  
*World Electric Vehicle Journal*, **17**(8), 411.  
DOI: https://doi.org/10.3390/wevj17080411

Published: **6 August 2026**.

## Purpose

This repository is the public reproducibility companion for the published paper. It is intended to make the reported screening and robustness outputs easier to inspect, cite, and reproduce without extending the claims beyond the published study.

The study is a **public-data screening and robustness-audit study**. It is **not** demand validation, feeder-capacity validation, power-flow analysis, financial feasibility analysis, construction approval, or a final deployment plan.

## Published result anchors

Any reproduced output should preserve the published result state:

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

## Repository structure

- `data/` — documentation for reuse-safe derived data and redistribution boundaries.
- `results/` — documentation for published verification targets and reported-output checks.
- `reproducibility/` — instructions and scope for the reproducibility archive.
- `CITATION.cff` — citation metadata for GitHub.
- `.zenodo.json` — metadata prepared for Zenodo archiving.

Additional reuse-safe supplementary files and verifier scripts can be added here only when they are confirmed to match the final published supplementary package.

## Data and redistribution boundary

The article uses public-data-derived and author-generated outputs. The published Supplementary Materials provide reuse-safe derived tables, scenario/rank diagnostics, sensitivity summaries, source/date/unit documentation, and reproducibility material.

Raw third-party exports or coordinate archives whose licensing or platform terms may restrict redistribution should **not** be copied into this repository merely for convenience. Where redistribution is not appropriate, this repository should document the source, date, role, and retrieval route instead.

The official article and its Supplementary Materials remain the authoritative scientific record.

## Citation

Please cite the published article when using the scientific method or results. Once the GitHub release is archived by Zenodo, the Zenodo DOI may additionally be cited for the archived reproducibility package.

## Versioning

The first archival release should be tagged `v1.0.0` only after the repository contents have been checked against the final published Supplementary Materials. Later releases should document repository or packaging changes without altering the published scientific results unless a documented correction is issued by the authors/publisher.
