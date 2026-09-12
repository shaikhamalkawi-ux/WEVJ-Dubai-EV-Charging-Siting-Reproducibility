# v1.1.0 release-candidate preparation

Status: **RC1 PREPARATION — NOT RELEASED**.

The source-extension candidate preserves the published WEVJ paper and all reported scientific results. It adds only public-source traceability material that passed the current redistribution/provenance gate.

## Candidate payload

The existing package `packages/WEVJ_Dubai_OpenData_SourceExtension_v1.1.0_PREP.zip` is internally self-consistent and contains:

- RTA Public Transportation Stations retained open-data snapshot — 137 rows.
- Population by Community retained open-data snapshot — 1,130 rows.
- Deterministic one-row-per-stop RTA bus-stop derivative — 4,505 stops, no missing coordinates.
- The exact transformation script reproducing that derivative.
- Attribution, provenance and SHA-256 records.

Package SHA-256: `94202eb94d5691987d220ff44dbfdb008dfaeca7c7b271ff57b2120513b554d8`.

## RC1 gates

PASS:
- ZIP integrity.
- Internal SHA manifest verification.
- RTA station row count = 137.
- Population-by-community row count = 1,130.
- Bus-stop derivative row count = 4,505 unique integer `stop_id` values.
- Bus-stop derivative missing-coordinate count = 0.
- Transformation script reproduces derivative SHA-256 `3f1a47bf5b1608f22f414035fabb6d47d1081aaae8bf07397866cf7c47f6306e` exactly from the retained raw audit snapshot.
- No Google-derived raw material, no mixed 7,410-candidate raw archive, no DEWA raw coordinate export, no community KML, and no Geofabrik PBF are included.

HOLD:
- Parking Spaces Per Zone.
- Estimated Population by Community.
- Population Cluster.
- Metro/Tram historical KML snapshots.
- Historical DEWA raw charger snapshot.
- Historical Dubai Municipality community KML.

## Scientific lock

No score, ranking, weight, model structure, dataset definition, or conclusion is changed. The source extension supports source traceability and partial source-to-output regeneration only; it is not observed-demand validation, feeder-capacity validation, power-flow analysis, financial feasibility analysis, construction approval, or a final deployment plan.

Do not publish `v1.1.0` or create a new Zenodo version until the author explicitly approves the release candidate.
