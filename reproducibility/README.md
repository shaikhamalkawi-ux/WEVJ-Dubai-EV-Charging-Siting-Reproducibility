# Reproducibility release guidance

Before creating the first archival GitHub/Zenodo release:

1. Compare every public file against the final published Supplementary Materials.
2. Include only reuse-safe derived tables, documented verifier scripts, and source/ontology metadata that are consistent with the Version of Record.
3. Exclude restricted third-party raw exports and licence-incompatible coordinate archives.
4. Run the reported-output verifier from the supplementary-package root and confirm the published anchors documented in `results/README.md`.
5. The final production-QA state recorded for the published supplementary package was **54 PASS / 0 FAIL**; the release payload should reproduce that verifier state before archival.
6. Create GitHub release tag `v1.0.0` only after the above checks pass.
7. Let Zenodo archive that GitHub release and mint the repository DOI.
8. Add the final Zenodo DOI back to the repository citation metadata in a packaging-only update; do not alter the published scientific results.

## Reproducibility boundary

The Version of Record supports **reported-output verification** from the released supplementary material. It does not claim complete end-to-end regeneration from every retained raw third-party source layer; a separate raw-source regeneration step would be required for that stronger claim.

## Scientific boundary

This archive supports a public-data candidate screening and robustness audit. It must not be described as observed-demand validation, feeder-capacity validation, financial feasibility, power-flow analysis, construction approval, or a final deployment plan.
