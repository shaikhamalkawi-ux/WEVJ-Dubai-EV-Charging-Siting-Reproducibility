# Old-library recovery audit — v1.1.0 source-extension preparation

Date: 2026-09-12

## Scope

This audit searched retained WEVJ/NI-EA project libraries and historical packages for exact source bytes that could strengthen public reproducibility without changing the published scientific results or claim boundary. Packages checked included Phase14, Phase29A, Phase31/31B, SourceConditioned, SubmissionReady, preservation/QA, boundary-lock, and DEWA-document collections.

## Exact snapshots recovered

- RTA Public Transportation Stations: 137 rows; SHA-256 `d0c8f689f12904b1944260ec456ecbecb3a827c6760cc4256973c64acf67ea6b`.
- Dubai Statistics Population by Community: 1,130 rows; SHA-256 `d6d4cc288de5a66c6aba054b486f998f495aba0471c33b3071e458a0d2bdd8d1`.
- RTA Bus Stop Details raw audit snapshot: 451,712 rows / 4,505 unique non-null stop IDs; SHA-256 `dcd1ebab4a583c782e4e657993237581b446f2e9bedf35c3fc3ace53edbbbe57`.
- RTA Parking Spaces Per Zone: 84 rows; SHA-256 `e368bd1ccaf9ca168e3ea044fdd113d247425cc19c11d079ed4bc7e6d7981e2a` — HOLD pending exact Data Dubai retained-resource identity/version.
- Estimated Population by Community: 1,578 rows; SHA-256 `67e4bdfb276acfe2821cabe7ba190709667b336134355d61b7b778bd153b9d00` — HOLD pending exact resource identity.
- Population Cluster: SHA-256 `9db1c3aea4bbb8d1fdeb0a338b24bcfa31306d68eaa86e0a2bffbdf53429031c` — HOLD pending exact resource identity.
- RTA Metro Stations CSV: 55 rows; SHA-256 `b1d2de46106ab9707ec07c700ae809629d4b4fba91eb6138ee46a900c09cd4d5` — auxiliary only.
- RTA Metro GIS KML: 56 point features; SHA-256 `ce4e69c6503c0fd40c8da4c15c662f800731434fb064b3b11a876f4f10428e24` — HOLD pending exact historical KML resource identity.
- RTA Tram KML: 11 point features; SHA-256 `f90dc6aceb486b3706cefdd246d81f7b72be36e6fc4157c5027ffdc2d2e8cdbe` — HOLD pending exact historical KML resource identity.

## Derived public-prep layer

The retained RTA bus-stop snapshot was reduced deterministically to one latest-report row per integer `stop_id`. The derivative has 4,505 rows, no missing coordinates, and SHA-256 `3f1a47bf5b1608f22f414035fabb6d47d1081aaae8bf07397866cf7c47f6306e`. The transformation script is preserved in `scripts/derive_current_bus_stops.py`.

## Exact historical source identities found but bytes not recovered

- DEWA EV Green Charger study snapshot: historical verified SHA-256 `2a881f803e5642ae03fe09f4f737c2d0506b175f46b9ca6a4bd9bd275a3ea526`, 335 records, 304 unique exact coordinates. The exact raw CSV was not found in the preserved WEVJ packages or DEWA-document archive. A newer portal export must not be substituted for this study snapshot.
- Dubai Municipality community KML: source identity `dm_community-open`; historical inspection recorded 224 polygons. Exact retained bytes were not recovered, so no boundary KML is redistributed.

## Intentionally excluded or link-only

- `phase5_combined_charger_layer_dewa_google_osm.csv`: excluded because it mixes DEWA, Google and OSM provenance.
- Mixed raw 7,410 candidate/amenity acquisition archive: HOLD pending row-level redistribution provenance.
- Google Maps / Places / Geocoding raw outputs: DO NOT REDISTRIBUTE.
- Geofabrik `gcc-states-260619.osm.pbf`: LINK-ONLY with source URL, snapshot date, checksum and ODbL attribution.

## Automated official-URL recovery test

A hash-gated GitHub Actions recovery was tested for the two clearly admitted official snapshots. The workflow was designed to commit a file only if the current portal bytes exactly matched the retained study SHA-256. Dubai Pulse download endpoints timed out from the hosted GitHub runner, so the workflow failed safely and committed no substitute data. This is treated as a source-access failure, not as evidence that the datasets are unavailable.

## Prepared package

A local PREP archive was built and integrity-tested:

`WEVJ_Dubai_OpenData_SourceExtension_v1.1.0_PREP.zip`

SHA-256: `94202eb94d5691987d220ff44dbfdb008dfaeca7c7b271ff57b2120513b554d8`

It contains only the two exact retained open-data snapshots, the deterministic bus-stop derivative, transformation script, attribution, provenance and SHA manifest. It is not a Zenodo release and not yet a final v1.1.0 payload.

## Scientific lock

No score, ranking, weight, model structure, published dataset definition, or conclusion was changed. The paper remains a public-data screening and robustness-audit study, not demand validation, feeder-capacity validation, power-flow analysis, financial feasibility analysis, construction approval, or a final deployment plan.
