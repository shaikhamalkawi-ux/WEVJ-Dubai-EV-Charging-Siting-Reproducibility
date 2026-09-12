# v1.1.0 release record

Status: **RELEASED ON GITHUB — 2026-09-12**.

The source extension preserves the published WEVJ paper and all reported scientific results. It adds only public-source traceability material that passed the redistribution/provenance gate.

## Release payload

GitHub tag/release: `v1.1.0`

Release asset:
`packages/WEVJ_Dubai_OpenData_SourceExtension_v1.1.0_RC1.zip`

- size: `135405` bytes
- SHA-256: `51811ad32fb7ee111d35dea9279cafed75a8d770f899c77dd73f503b13728353`
- Git blob SHA on the preparation branch: `d53543f35d8844f240047dfd3a9d8d97e1f8ccf8`

The GitHub release asset reports the same SHA-256 digest as the locally verified RC1 binary.

The package contains:

- RTA Public Transportation Stations retained open-data snapshot — 137 rows.
- Population by Community retained open-data snapshot — 1,130 rows.
- Deterministic one-row-per-stop RTA bus-stop derivative — 4,505 unique integer stop IDs, no missing coordinates.
- Exact transformation script reproducing the derivative.
- Attribution, provenance, redistribution matrix, QA and SHA-256 manifest records.

## Release gates

PASS:
- ZIP integrity.
- Internal SHA manifest verification.
- RTA station row count = 137.
- Population-by-community row count = 1,130.
- Bus-stop derivative row count = 4,505 unique integer `stop_id` values.
- Bus-stop derivative missing-coordinate count = 0.
- Transformation script reproduces derivative SHA-256 `3f1a47bf5b1608f22f414035fabb6d47d1081aaae8bf07397866cf7c47f6306e` exactly from the retained raw audit snapshot.
- Uploaded GitHub binary is byte-identical to the locally verified RC1 file.
- GitHub release asset digest equals the locked RC1 SHA-256.
- No Google-derived raw material, no mixed 7,410-candidate raw archive, no DEWA raw coordinate export, no community KML, and no Geofabrik PBF are included.
- Author approval to publish v1.1.0 received on 2026-09-12.

HOLD / excluded from this release:
- Parking Spaces Per Zone.
- Estimated Population by Community.
- Population Cluster.
- Metro/Tram historical KML snapshots.
- Historical DEWA raw charger snapshot.
- Historical Dubai Municipality community KML.
- Geofabrik GCC PBF remains link-only under ODbL.
- Google raw outputs and the mixed-source 7,410-candidate archive remain excluded.

## Scientific lock

No score, ranking, weight, model structure, dataset definition, or conclusion is changed. The source extension supports source traceability and partial source-to-output regeneration only; it is not observed-demand validation, feeder-capacity validation, power-flow analysis, financial feasibility analysis, construction approval, or a final deployment plan.

Zenodo version DOI: pending confirmation after GitHub-to-Zenodo archiving.
