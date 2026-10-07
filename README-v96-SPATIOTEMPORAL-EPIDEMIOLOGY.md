# GORUT OUTBREAK AI v96 — Spatiotemporal Epidemiology Engine

Adds a time-place decision-support layer to the v95 GIS engine.

## Functions
- Compare latest 7/14/28-day case counts with the immediately preceding equal window.
- Weekly trend display.
- District/subdistrict increase signals.
- Hotspot ranking by change in counts.
- Disease filter.
- CSV export.
- Aggregate Supabase RPC `spatiotemporal_summary`.

## Epidemiological guardrails
- This is not a statistical outbreak detector.
- It does not declare KLB/wabah.
- Increased reporting can reflect improved completeness rather than true incidence.
- Interpretation should be checked against baseline, seasonality, case definition, reporting completeness, laboratory evidence and field verification.
