# v1.1.0 package staging

No public `v1.1.0` release has been created from this directory, and `v1.0.0` / Zenodo DOI `10.5281/zenodo.22713999` remain unchanged.

## Current release candidate

A verified local release-candidate archive has been built after the old-library recovery and redistribution audit:

- `WEVJ_Dubai_OpenData_SourceExtension_v1.1.0_RC1.zip`
- SHA-256: `51811ad32fb7ee111d35dea9279cafed75a8d770f899c77dd73f503b13728353`

RC1 contains only material that passed the current source/provenance gate:

- RTA Public Transportation Stations retained snapshot — 137 rows.
- Population by Community retained snapshot — 1,130 rows.
- Deterministic RTA bus-stop derivative — 4,505 unique integer stop IDs with no missing coordinates.
- Exact transformation script.
- Attribution, provenance, redistribution matrix, QA results and SHA-256 manifest.

The following remain excluded or held: raw Google-derived material; the mixed-source 7,410-candidate archive; historical DEWA raw charger coordinates whose exact retained bytes were not recovered; historical Dubai Municipality community KML whose exact retained bytes were not recovered; Metro/Tram historical KML snapshots with unresolved file-level resource provenance; parking/estimated-population/population-cluster snapshots with unresolved exact retained resource identity; and the large Geofabrik PBF, which remains link-only under ODbL.

The binary RC1 is intentionally not represented here by an unverified placeholder. Upload it to this directory only after confirming its SHA-256 above. Do not place it on `main` and do not create a GitHub/Zenodo release until author approval.

No published scientific score, rank, weight, model structure, dataset definition, or conclusion is changed by this source-extension work.
