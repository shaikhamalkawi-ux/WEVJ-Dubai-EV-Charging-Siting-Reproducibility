# v1.1.0 Dubai Open-Data Source Extension

Status: **RELEASED on GitHub — 12 September 2026**.

GitHub release: `v1.1.0`

This extension adds a source-by-source licence and provenance layer for selected Dubai government open-data inputs used as contextual or source-reconciliation evidence in the published WEVJ study.

It does **not** change the published manuscript, scores, rankings, weights, model structure, datasets used for the Version of Record, or conclusions.

## Scientific boundary

The study remains a public-data screening and robustness-audit study. This extension must not be described as demand validation, feeder-capacity validation, power-flow analysis, financial feasibility, construction approval, or a final deployment plan.

## Admission rule

A raw or source-layer file enters the public source extension only when all of the following are locked:

1. exact source dataset and issuing authority;
2. public/open classification on the source platform;
3. applicable reuse licence or other explicit redistribution basis;
4. exact downloaded file name and SHA-256;
5. download/access date;
6. no third-party content or personal/private data outside the provider's open-data grant;
7. attribution statement;
8. role in the paper documented without expanding the claim boundary.

Anything not satisfying every gate remains **HOLD**, **LINK-ONLY**, or **EXCLUDED**.

The released package contains the admitted RTA Public Transportation Stations snapshot, Population by Community snapshot, the deterministic 4,505-stop bus-stop derivative, and the associated transformation/provenance/QA records. See `SOURCE_LICENSE_REGISTER.csv`, `REDISTRIBUTION_MATRIX.csv`, `ATTRIBUTION.md`, and `RELEASE_CANDIDATE_v1.1.0.md`.
