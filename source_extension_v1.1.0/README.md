# v1.1.0 Dubai Open-Data Source Extension — preparation branch

Status: **PREP ONLY — no release has been created.**

This branch stages a source-by-source licence and provenance lock for selected Dubai government open-data layers used as contextual or source-reconciliation inputs in the published WEVJ study.

It does **not** change the published manuscript, scores, rankings, weights, model structure, datasets used for the Version of Record, or conclusions.

## Scientific boundary

The study remains a public-data screening and robustness-audit study. This extension must not be described as demand validation, feeder-capacity validation, power-flow analysis, financial feasibility, construction approval, or a final deployment plan.

## Admission rule

A raw or source-layer file may enter a future public v1.1.0 release only if all of the following are locked:

1. exact source dataset and issuing authority;
2. public/open classification on the source platform;
3. applicable reuse licence or other explicit redistribution basis;
4. exact downloaded file name and SHA-256;
5. download/access date;
6. no third-party content or personal/private data outside the provider's open-data grant;
7. attribution statement;
8. role in the paper documented without expanding the claim boundary.

Anything not satisfying every gate remains **HOLD** or **LINK-ONLY**.

See `SOURCE_LICENSE_REGISTER.csv` and `ATTRIBUTION.md`.
