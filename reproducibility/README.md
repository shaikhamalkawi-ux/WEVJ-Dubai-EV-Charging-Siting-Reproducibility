# Reproducibility release guidance

Before creating the first archival GitHub/Zenodo release:

1. Compare every public file against the final published Supplementary Materials.
2. Include only reuse-safe derived tables, documented verifier scripts, and source/ontology metadata that are consistent with the Version of Record.
3. Exclude restricted third-party raw exports and sensitive or licence-incompatible coordinate archives.
4. Run the reported-output verifier and confirm the published anchors documented in `results/README.md`.
5. Create GitHub release tag `v1.0.0` only after the above checks pass.
6. Let Zenodo archive that GitHub release and mint the repository DOI.
7. Add the final Zenodo DOI back to this README and to citation metadata in a packaging-only update; do not alter the published scientific results.

## Scientific boundary

This archive supports a public-data candidate screening and robustness audit. It must not be described as observed-demand validation, feeder-capacity validation, financial feasibility, power-flow analysis, construction approval, or a final deployment plan.
