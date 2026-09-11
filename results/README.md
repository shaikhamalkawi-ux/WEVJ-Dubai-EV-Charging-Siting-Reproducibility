# Published-result verification targets

The following values are locked to the published Version of Record and should be used as regression/verification targets for any public verifier added to this repository:

| Check | Published value |
|---|---:|
| Admitted candidate/amenity records | 7,410 |
| Inside-boundary candidates | 5,097 |
| Baseline leader | S1421 / Boonmax |
| Official-DEWA coordinate-source leader | S3473 |
| Necessary top-15 core | 12 |
| Possible top-15 envelope | 18 |
| TOPSIS top-15 overlap | 0/15 |
| Road-network top-15 overlap | 14/15 |
| Official-DEWA top-15 overlap | 13/15 |

A verifier should fail clearly if a calculation intended to reproduce the published state does not recover these anchors.

These checks verify the reported screening/robustness state only. They do not convert the candidate ranking into demand, feeder-capacity, financial-feasibility, power-flow, or construction evidence.
