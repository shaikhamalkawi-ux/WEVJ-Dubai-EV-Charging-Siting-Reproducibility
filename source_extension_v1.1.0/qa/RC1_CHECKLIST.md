# RC1 QA checklist

Date: 2026-09-12

- [x] v1.0.0 tag/release left unchanged.
- [x] Zenodo DOI 10.5281/zenodo.22713999 left unchanged.
- [x] Older WEVJ/NI-EA libraries searched for retained source bytes.
- [x] Exact hashes locked for admitted source snapshots.
- [x] RTA bus-stop derivative reproduced exactly by the committed transformation rule.
- [x] Restricted/mixed third-party raw layers excluded.
- [x] OpenStreetMap/Geofabrik large raw snapshot retained as link-only.
- [x] Published scientific anchors and claim boundary preserved.
- [x] RC1 ZIP integrity and internal manifest verified locally.
- [x] RC1 SHA-256 locked: `51811ad32fb7ee111d35dea9279cafed75a8d770f899c77dd73f503b13728353`.
- [x] Temporary fail-closed GitHub Actions tests removed from the preparation branch after audit.
- [x] Exact RC1 binary uploaded to `source_extension_v1.1.0/packages/` on the preparation branch.
- [x] Remote Git blob SHA `d53543f35d8844f240047dfd3a9d8d97e1f8ccf8` matches the locally computed Git blob SHA for the verified 135,405-byte RC1 binary, establishing byte-for-byte identity with the locally verified file.
- [ ] Author approval to publish v1.1.0.
- [ ] Create GitHub release/tag v1.1.0 only after author approval.
- [ ] Confirm Zenodo version DOI after GitHub release.
- [ ] Update main README/CITATION metadata with the new Zenodo version/concept DOI only after publication.
