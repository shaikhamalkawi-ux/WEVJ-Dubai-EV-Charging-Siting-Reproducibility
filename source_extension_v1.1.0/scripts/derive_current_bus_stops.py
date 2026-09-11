#!/usr/bin/env python3
"""Create a one-row-per-stop derivative from the retained RTA bus-stop snapshot.

This script is packaging/reproducibility support only. It does not alter the published
NI-EA score or ranking and does not convert bus-stop proximity into observed demand.

Rule
----
1. Parse report_date.
2. Remove the single row with null stop_id from the stop-level derivative.
3. For each stop_id, retain rows having that stop's maximum report_date.
4. Verify that stop-level identity, coordinates, facility fields and validity fields are
   invariant across route rows at that latest report date.
5. Emit one representative row per stop plus route_count_latest_report and
   source_rows_latest_report.

The retained raw snapshot used in the v1.1.0 preparation audit has 451,712 rows and
4,505 unique non-null stop IDs. The expected derivative has 4,505 rows and no missing
coordinates.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd

INVARIANT_FIELDS = [
    "stop_name",
    "street_name",
    "stop_location_longitude",
    "stop_location_latitude",
    "bus_stop_type",
    "time_table_panel",
    "mupi_available",
    "rtpi_available",
    "last_survey_date",
    "valid_from",
    "valid_until",
]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("input_csv", type=Path)
    p.add_argument("output_csv", type=Path)
    args = p.parse_args()

    df = pd.read_csv(args.input_csv, low_memory=False)
    required = {
        "report_date", "stop_id", "stop_name", "street_name", "route_name",
        "stop_location_longitude", "stop_location_latitude", "bus_stop_type",
        "time_table_panel", "mupi_available", "rtpi_available", "last_survey_date",
        "valid_from", "valid_until", "load_timestamp",
    }
    missing = required.difference(df.columns)
    if missing:
        raise SystemExit(f"Missing required columns: {sorted(missing)}")

    df["_report_date"] = pd.to_datetime(df["report_date"], errors="coerce")
    if df["_report_date"].isna().any():
        raise SystemExit("Unparseable report_date value(s) found")

    d = df.dropna(subset=["stop_id"]).copy()
    latest_date = d.groupby("stop_id")["_report_date"].transform("max")
    latest = d[d["_report_date"].eq(latest_date)].copy()

    violations = {}
    for field in INVARIANT_FIELDS:
        n = int((latest.groupby("stop_id")[field].nunique(dropna=True) > 1).sum())
        if n:
            violations[field] = n
    if violations:
        raise SystemExit(f"Latest-date stop-level invariance failed: {violations}")

    latest = latest.sort_values(["stop_id", "route_name"], na_position="last")
    first = latest.groupby("stop_id", as_index=False).first()
    route_count = (
        latest.groupby("stop_id")["route_name"]
        .nunique(dropna=True)
        .rename("route_count_latest_report")
        .reset_index()
    )
    source_rows = (
        latest.groupby("stop_id").size()
        .rename("source_rows_latest_report")
        .reset_index()
    )

    cols = [
        "stop_id", "stop_name", "street_name",
        "stop_location_longitude", "stop_location_latitude",
        "bus_stop_type", "time_table_panel", "mupi_available", "rtpi_available",
        "last_survey_date", "valid_from", "valid_until",
        "report_date", "load_timestamp",
    ]
    out = first[cols].merge(route_count, on="stop_id").merge(source_rows, on="stop_id")
    out = out.rename(columns={
        "report_date": "latest_report_date",
        "load_timestamp": "representative_load_timestamp",
    }).sort_values("stop_id").reset_index(drop=True)

    if len(out) != out["stop_id"].nunique():
        raise SystemExit("Output is not one row per stop_id")
    if out[["stop_location_longitude", "stop_location_latitude"]].isna().any(axis=1).any():
        raise SystemExit("Output contains missing coordinates")

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output_csv, index=False)
    print(f"PASS: wrote {len(out)} unique stop rows to {args.output_csv}")


if __name__ == "__main__":
    main()
