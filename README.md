# WEVJ Dubai EV Charging Siting — Reproducibility Archive

[![Zenodo v1.0.0 DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22713999.svg)](https://doi.org/10.5281/zenodo.22713999)

This repository supports the published article:

**Ghassan Malkawi, Azmi Alazzam, Ahmed Abdelaziz Elsayed, Asem Omari, Said Badreddine, Bakeel Hussein, Mohammed Alhagyan, and Abdelrahman Altigani (2026).**  
**“An Interaction-Aware NI-EA Framework for EV Charging-Station Siting: Source-Conditioned Robust Candidate Sets and Bounded Spatial Evidence in Dubai.”**  
*World Electric Vehicle Journal*, **17**(8), 411.  
Article DOI: https://doi.org/10.3390/wevj17080411  
Archived v1.0.0 reproducibility DOI: https://doi.org/10.5281/zenodo.22713999  
Current GitHub release prepared here: **v1.1.0 — Dubai Open-Data Source Extension**

Published article: **6 August 2026**.

## Purpose

This repository is the public companion for the published paper. Its primary reproducibility claim remains **reported-output verification**: the released, reuse-safe screening and robustness outputs can be inspected and verified against the Version of Record.

Version **v1.1.0** adds a bounded source-traceability extension for selected reuse-safe Dubai government open-data layers. It does not convert the archive into complete raw-layer regeneration, and it does not alter the published scientific results.

The study remains a **public-data screening and robustness-audit study**. It is **not** demand validation, feeder-capacity validation, power-flow analysis, financial feasibility analysis, construction approval, or a final deployment plan.

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

## v1.0.0 reported-output verification

The first public archival release preserved the publisher-facing verification boundary.

- Original supplementary ZIP integrity: **PASS**
- Original static SHA-256 manifest: **89/89 PASS**
- Published reported-output verifier: **54 PASS / 0 FAIL**
- Public-safe release-candidate verifier: **54 PASS / 0 FAIL**
- Public-safe CSV coordinate-column scan: **PASS**

Two publisher-facing files were not re-published in v1.0.0: a candidate-level transit-context file containing latitude/longitude fields and an internal source-bound reconstruction script containing absolute local paths and dependencies on controlled/raw inputs. This was a packaging-only filter and did not alter any reported result.

## v1.1.0 Dubai open-data source extension

The source extension adds only material that passed the current provenance and redistribution gate:

- **RTA Public Transportation Stations** retained open-data snapshot — **137 rows**.
- **Population by Community** retained open-data snapshot — **1,130 rows**.
- Deterministic one-row-per-stop derivative of the retained **RTA Bus Stop Details** audit snapshot — **4,505 unique integer stop IDs**, with **no missing coordinates**.
- Exact transformation script for the bus-stop derivative.
- Attribution, source-admission, redistribution, QA, and SHA-256 records.

RC1 package SHA-256 before release:

`51811ad32fb7ee111d35dea9279cafed75a8d770f899c77dd73f503b13728353`

The following remain held, excluded, or link-only: raw Google-derived material; the mixed-source 7,410-record candidate acquisition archive; historical DEWA raw charger coordinates whose exact retained bytes were not recovered; historical Dubai Municipality community KML whose exact retained bytes were not recovered; Metro/Tram historical KML snapshots with unresolved file-level resource provenance; parking/estimated-population/population-cluster snapshots whose exact retained resource identity remains unresolved; and the large Geofabrik PBF, which remains link-only under ODbL.

## Repository structure

- `data/` — documentation for reuse-safe derived data and redistribution boundaries.
- `results/` — published verification targets and reported-output checks.
- `reproducibility/` — verification instructions and claim boundary.
- `release/` — v1.0.0 release package and verification notes.
- `source_extension_v1.1.0/` — v1.1.0 source-admission, licence, QA, and release-candidate material.
- `CITATION.cff` — citation metadata.
- `.zenodo.json` — metadata used for Zenodo archiving.

## Data and redistribution boundary

The article uses public-data-derived and author-generated outputs. Public releases are restricted to reuse-safe outputs and source files whose redistribution basis and provenance are sufficiently documented.

Raw third-party exports or coordinate archives whose licensing or platform terms may restrict redistribution are not copied into the archive merely for convenience. Where redistribution is not appropriate, the archive records source identity, role, retrieval route, and the applicable HOLD or LINK-ONLY status.

The published article and its publisher-hosted Supplementary Materials remain the authoritative scientific record.

## Citation

Please cite the published article when using the scientific method or results:

**Malkawi, G.; Alazzam, A.; Elsayed, A.A.; Omari, A.; Badreddine, S.; Hussein, B.; Alhagyan, M.; Altigani, A. (2026).** “An Interaction-Aware NI-EA Framework for EV Charging-Station Siting: Source-Conditioned Robust Candidate Sets and Bounded Spatial Evidence in Dubai.” *World Electric Vehicle Journal*, **17**(8), 411. https://doi.org/10.3390/wevj17080411

When referring specifically to a reproducibility archive version, additionally cite the corresponding Zenodo version record. The v1.0.0 DOI is `10.5281/zenodo.22713999`; the v1.1.0 version DOI is recorded after Zenodo archives the GitHub v1.1.0 release.

## Versioning

- `v1.0.0` — public-safe reported-output verification archive.
- `v1.1.0` — selected Dubai open-data source-traceability extension.

Versioning documents packaging and reproducibility-surface changes. It does not alter the published scientific results unless a documented correction is issued by the authors or publisher.
