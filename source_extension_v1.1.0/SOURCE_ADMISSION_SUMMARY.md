# v1.1.0 source-admission summary

**Status: PREPARATION ONLY. No v1.1.0 release has been created and nothing on `v1.0.0` has been altered.**

This note records the current evidence state for a possible Dubai open-data source extension. `ADMIT` below means *technically/source-provenance admissible for the future package after the remaining licence/attribution gates are closed*; it is not a legal opinion and it does not expand the scientific claims of the paper.

## Governing reuse evidence

- Dubai Law No. (26) of 2015 defines Open Data and requires government data providers to disseminate Open Data under the competent authority's standards and policies.
- The current Dubai Pulse **Open Data Licence** states that use of information offered under that licence is governed by its terms. The licence is retained as the general reuse instrument for Data Dubai/Dubai Pulse open datasets.
- Dataset-specific metadata still controls where it is more restrictive or where resource provenance is unresolved.

Official licence: https://www.dubaipulse.gov.ae/docs/DDE%20_%20DRAFT_Open_Data%20Licence_LONG_Form_English%203.pdf

## Current source state

### Source identity + retained bytes locked

1. **RTA Public Transportation Stations** — `ADMIT-HASH-LOCKED`
   - retained SHA-256: `d0c8f689f12904b1944260ec456ecbecb3a827c6760cc4256973c64acf67ea6b`
   - 137 rows
   - role: descriptive urban-accessibility context only.

2. **RTA Bus Stop Details** — `ADMIT-HASH-LOCKED-DERIVATIVE-PREFERRED`
   - raw retained SHA-256: `dcd1ebab4a583c782e4e657993237581b446f2e9bedf35c3fc3ace53edbbbe57`
   - raw rows: 451,712; unique non-null stop IDs: 4,505
   - exact official dataset identity: `rta_bus_stop_details-open`
   - a deterministic one-row-per-stop derivative has been prepared and QA-checked; its SHA-256 is `d2e919d9d6ec5f5f561dcb48a14647002f169308ae7a7cd95264a5dbf58b13d6`.
   - the raw 67 MB snapshot is not planned for GitHub; the compact derivative is preferred after the final licence gate.

3. **Population by Community** — `ADMIT-HASH-LOCKED`
   - retained SHA-256: `d6d4cc288de5a66c6aba054b486f998f495aba0471c33b3071e458a0d2bdd8d1`
   - 1,130 rows
   - role: descriptive community/population enrichment only; not demand validation.

### Source identity locked; one byte/resource gate remains

4. **DEWA EV Green Charger raw export**
   - prior exact retained-file SHA-256: `2a881f803e5642ae03fe09f4f737c2d0506b175f46b9ca6a4bd9bd275a3ea526`
   - 335 records; 304 unique exact coordinates in the prior verified snapshot
   - official dataset page: `dewa_ev_green_charger-open`, classified Open Data
   - the current dataset metadata itself displays `License: notspecified`; therefore the final public package will preserve the Dubai Open Data Licence as the general reuse basis and will not publish this file until its retained bytes are re-hashed in the release workspace.

5. **Dubai Municipality Community polygons**
   - official source identity: `dm_community-open`
   - prior inspection: 224 polygons
   - exact retained KML SHA-256 still needs to be locked before redistribution.

### Hash locked; exact retained resource URL/version still held

6. **Number of Parking Spaces Per Zone**
   - SHA-256: `e368bd1ccaf9ca168e3ea044fdd113d247425cc19c11d079ed4bc7e6d7981e2a`
   - 84 rows
   - Open status is confirmed; the exact Data Dubai resource URL for this retained snapshot is still required.

7. **Estimated Population by Community**
   - SHA-256: `67e4bdfb276acfe2821cabe7ba190709667b336134355d61b7b778bd153b9d00`
   - 1,578 rows
   - portal listing is Open; exact dataset/resource identity remains to be locked.

8. **Population Cluster**
   - SHA-256: `9db1c3aea4bbb8d1fdeb0a338b24bcfa31306d68eaa86e0a2bffbdf53429031c`
   - exact dataset/resource identity remains to be locked.

9. **RTA Tram Stations retained KML**
   - SHA-256: `f90dc6aceb486b3706cefdd246d81f7b72be36e6fc4157c5027ffdc2d2e8cdbe`
   - 11 points
   - official dataset is Open, but the current portal exposes a CSV resource; the retained KML version remains on HOLD until its exact official resource/version is resolved.

### Intentionally not redistributed

10. **Geofabrik GCC OSM PBF** — `LINK-ONLY`; retain source URL/snapshot/checksum and ODbL attribution rather than duplicating the large file.
11. **Google Maps / Places / Geocoding raw outputs** — `DO-NOT-REDISTRIBUTE`.
12. **Mixed raw 7,410-candidate archive** — `HOLD-PROVENANCE-AUDIT` until row-level source provenance excludes restricted third-party content.

## Scientific boundary

None of these source-package changes modifies the Version of Record or any published score, ranking, weight, model structure, dataset definition, or conclusion. The source extension, if eventually released, supports stronger public source traceability and partial source-to-output regeneration. It does **not** establish observed charging demand, feeder capacity, power-flow feasibility, financial feasibility, construction approval, or a final deployment plan.
