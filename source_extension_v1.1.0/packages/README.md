# v1.1.0 package staging

No public `v1.1.0` release has been created from this directory, and `v1.0.0` / Zenodo DOI `10.5281/zenodo.22713999` remain unchanged.

## Current release candidate

The exact verified RC1 binary is now present on the preparation branch:

- `WEVJ_Dubai_OpenData_SourceExtension_v1.1.0_RC1.zip`
- size: `135405` bytes
- SHA-256: `51811ad32fb7ee111d35dea9279cafed75a8d770f899c77dd73f503b13728353`
- Git blob SHA: `d53543f35d8844f240047dfd3a9d8d97e1f8ccf8`

The remote Git blob SHA matches the locally computed Git blob SHA for the verified RC1 binary, confirming byte-for-byte identity with the locally tested package.

RC1 contains only material that passed the current source/provenance gate:

- RTA Public Transportation Stations retained snapshot — 137 rows.
- Population by Community retained snapshot — 1,130 rows.
- Deterministic RTA bus-stop derivative — 4,505 unique integer stop IDs with no missing coordinates.
- Exact transformation script.
- Attribution, provenance, redistribution matrix, QA results and SHA-256 manifest.

The following remain excluded or held: raw Google-derived material; the mixed-source 7,410-candidate archive; historical DEWA raw charger coordinates whose exact retained bytes were not recovered; historical Dubai Municipality community KML whose exact retained bytes were not recovered; Metro/Tram historical KML snapshots with unresolved file-level resource provenance; parking/estimated-population/population-cluster snapshots with unresolved exact retained resource identity; and the large Geofabrik PBF, which remains link-only under ODbL.

Do not create the public GitHub/Zenodo `v1.1.0` release until author approval.

No published scientific score, rank, weight, model structure, dataset definition, or conclusion is changed by this source-extension work.
