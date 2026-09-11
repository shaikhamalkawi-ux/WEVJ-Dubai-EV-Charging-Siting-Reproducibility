# v1.0.0 release preparation

This release candidate is a public-safe reproducibility companion for the published WEVJ article:

Ghassan Malkawi, Azmi Alazzam, Ahmed Abdelaziz Elsayed, Asem Omari, Said Badreddine, Bakeel Hussein, Mohammed Alhagyan, and Abdelrahman Altigani (2026), “An Interaction-Aware NI-EA Framework for EV Charging-Station Siting: Source-Conditioned Robust Candidate Sets and Bounded Spatial Evidence in Dubai,” World Electric Vehicle Journal 17(8), 411. DOI: 10.3390/wevj17080411.

## Verification completed

- Original final supplementary ZIP integrity: PASS.
- Original static SHA-256 manifest: 89/89 PASS.
- Published reported-output verifier: 54 PASS / 0 FAIL.
- Public-safe companion verifier after packaging filter: 54 PASS / 0 FAIL.
- Public-safe CSV coordinate-column scan: PASS (no lat/lon/latitude/longitude fields).

## Public-safe packaging filter

The published scientific results are unchanged. Two publisher-facing supplementary files are not re-published in this GitHub/Zenodo companion:

1. `robust_candidate_sets/candidate_transit_proximity_context.csv` because it contains candidate latitude/longitude fields, inconsistent with the coordinate-free redistribution boundary used for this public companion. Aggregate transit-proximity summaries are retained.
2. `robust_candidate_sets/run_analysis.py` because it is an internal source-bound reconstruction script with absolute local paths and controlled/raw-input dependencies. It is not Script S1, the public reported-output verifier.

The Version of Record and publisher-hosted Supplementary Materials remain authoritative. The GitHub/Zenodo package is an additional public-safe reproducibility archive and does not alter the paper.

## Scientific claim boundary

This is a public-data screening and robustness-audit study. It is not demand validation, feeder-capacity validation, power-flow analysis, financial feasibility analysis, construction approval, or a final deployment plan.
