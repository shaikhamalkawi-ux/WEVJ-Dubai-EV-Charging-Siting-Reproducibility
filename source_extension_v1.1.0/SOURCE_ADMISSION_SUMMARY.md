# v1.1.0 source-admission summary

**Status: PREPARATION ONLY. No v1.1.0 release has been created and nothing on `v1.0.0` has been altered.**

This note records the evidence state for a possible Dubai open-data source extension. `ADMIT` means technically/source-provenance admissible for a future package after all stated gates are closed; it is not a legal opinion and it does not expand the scientific claims of the paper.

## Old-library recovery pass

The older WEVJ/NI-EA libraries and packages were searched again, including Phase14, Phase29A, Phase31/31B, SourceConditioned, SubmissionReady, and preservation/QA packages. This recovered several exact source snapshots and confirmed that the later public/submission packages intentionally omitted the raw DEWA coordinate export, Dubai community KML, Geofabrik PBF, and mixed source archives.

### Admitted or preparation-ready

1. **RTA Public Transportation Stations** — `ADMIT-HASH-LOCKED-PREP`
   - 137 rows
   - SHA-256 `d0c8f689f12904b1944260ec456ecbecb3a827c6760cc4256973c64acf67ea6b`
   - role: descriptive urban-accessibility context only.

2. **RTA Bus Stop Details derivative** — `ADMIT-DERIVED-HASH-LOCKED-PREP`
   - raw retained snapshot: 451,712 rows; 4,505 unique non-null stop IDs
   - raw SHA-256 `dcd1ebab4a583c782e4e657993237581b446f2e9bedf35c3fc3ace53edbbbe57`
   - public-prep derivative: one latest-report row per integer stop ID, 4,505 rows, no missing coordinates
   - derivative SHA-256 `3f1a47bf5b1608f22f414035fabb6d47d1081aaae8bf07397866cf7c47f6306e`
   - deterministic transformation script is committed on this branch.

3. **Population by Community** — `ADMIT-HASH-LOCKED-PREP`
   - 1,130 rows
   - SHA-256 `d6d4cc288de5a66c6aba054b486f998f495aba0471c33b3071e458a0d2bdd8d1`
   - official resource ID `bedb04be-66cf-4b66-a628-07e5c674a3af`
   - role: descriptive community/population context only, not demand validation.

A GitHub Actions workflow on this branch performs a strict hash gate for the two exact official portal snapshots above. It will refuse to commit a current portal download if the bytes no longer match the retained study snapshot.

### Recovered but still held

4. **Parking Spaces Per Zone** — 84 rows; SHA-256 `e368bd1ccaf9ca168e3ea044fdd113d247425cc19c11d079ed4bc7e6d7981e2a`. Open status is confirmed, but the exact Data Dubai resource identity/version for the retained snapshot is still required.

5. **Estimated Population by Community** — 1,578 rows; SHA-256 `67e4bdfb276acfe2821cabe7ba190709667b336134355d61b7b778bd153b9d00`. The captured portal listing says Open; exact resource identity remains unresolved.

6. **Population Cluster** — SHA-256 `9db1c3aea4bbb8d1fdeb0a338b24bcfa31306d68eaa86e0a2bffbdf53429031c`. The captured portal listing says Open; exact resource identity remains unresolved.

7. **Metro Stations CSV** — 55 rows; SHA-256 `b1d2de46106ab9707ec07c700ae809629d4b4fba91eb6138ee46a900c09cd4d5`. Retained as an auxiliary audit file; it is not needed for the core extension because the published source-context ontology uses the unified public-transport stations layer.

8. **Metro GIS KML** — 56 point features; SHA-256 `ce4e69c6503c0fd40c8da4c15c662f800731434fb064b3b11a876f4f10428e24`. Hold until exact historical KML resource/version is tied to the official portal.

9. **Tram Stations KML** — 11 points; SHA-256 `f90dc6aceb486b3706cefdd246d81f7b72be36e6fc4157c5027ffdc2d2e8cdbe`. Hold for the same historical-resource reason.

### Source identity/history known, exact retained bytes not recovered

10. **Official DEWA EV Green Charger source snapshot** — historical exact SHA-256 `2a881f803e5642ae03fe09f4f737c2d0506b175f46b9ca6a4bd9bd275a3ea526`, 335 records, 304 unique exact coordinates. Old WEVJ packages were searched again but the exact raw CSV bytes were not recovered. Do not substitute a newer portal export for the historical study snapshot.

11. **Dubai Municipality Community KML** — source identity `dm_community-open`; historical project inspection recorded 224 polygons. Exact retained KML bytes were not recovered from old WEVJ packages, so no boundary file is redistributed yet.

### Intentionally not redistributed

12. **Geofabrik GCC OSM PBF** — `LINK-ONLY`; historical study-source SHA-256 `02b0f40a26734cea4220ff928626e28ad95882d309a9eec08f3621a3b7f2f8c4`. Retain source URL/snapshot/checksum and ODbL attribution rather than duplicating the large file.
13. **Google Maps / Places / Geocoding raw outputs** — `DO-NOT-REDISTRIBUTE`.
14. **Mixed raw 7,410-candidate/source archive** — `HOLD-PROVENANCE-AUDIT`; it is not made public because row-level source provenance includes mixed acquisition sources. The published coordinate-free 5,097-candidate derived outputs remain the safe public layer.

## Scientific boundary

None of these source-package actions changes the Version of Record or any published score, ranking, weight, model structure, dataset definition, or conclusion. The source extension, if eventually released, supports stronger public source traceability and partial source-to-output regeneration. It does **not** establish observed charging demand, feeder capacity, power-flow feasibility, financial feasibility, construction approval, or a final deployment plan.
