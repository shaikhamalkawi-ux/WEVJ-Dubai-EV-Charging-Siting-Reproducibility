# RTA bus-stop derivative QA

Source snapshot: `bus_stop_details_2026-04-29_11-28-32_1.csv`

Source SHA-256: `dcd1ebab4a583c782e4e657993237581b446f2e9bedf35c3fc3ace53edbbbe57`

Official dataset identity: `rta_bus_stop_details-open` (Roads and Transport Authority, Data Dubai / Dubai Pulse).

## Source audit

- Raw rows: **451,712**
- Unique non-null `stop_id`: **4,505**
- Null `stop_id` rows: **1**
- Rows with a missing longitude or latitude: **1**
- `report_date` range: **2020-07-13 to 2026-03-29**

## Derivation rule

For each non-null `stop_id`, retain the rows at that stop's maximum `report_date`. At that latest report date, the following fields were checked for within-stop invariance across route rows: stop name, street name, longitude, latitude, bus-stop type, timetable-panel flag, MUPI flag, RTPI flag, last-survey date, valid-from date, and valid-until date.

**QA result: zero stop IDs had conflicting values in any of those checked fields at their latest report date.**

The derivative therefore emits one representative row per stop, plus the number of distinct routes and the number of source rows present at the latest report date.

## Derived file audit

Prepared file: `rta_bus_stops_current_stop_level_derived_2026-04-29.csv`

- Rows: **4,505**
- Unique stop IDs: **4,505**
- Missing coordinate rows: **0**
- SHA-256: `d2e919d9d6ec5f5f561dcb48a14647002f169308ae7a7cd95264a5dbf58b13d6`

The derivative is **not yet committed to the public preparation branch**. It will be added only after the source-licence admission gate is closed. This processing is for descriptive transit/access context only and does not introduce a new NI-EA criterion or demand-validation claim.
