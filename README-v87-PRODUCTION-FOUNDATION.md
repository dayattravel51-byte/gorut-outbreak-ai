# GORUT OUTBREAK AI v87 — Production Foundation

This package is based on v86 and prepares the application for a free initial deployment using GitHub Pages + Supabase Free.

## What changed
- Added PWA manifest for the main app.
- Added a production-oriented Supabase schema under `supabase/`.
- Added browser-safe backend configuration example.
- Kept the v86  separate from production data.
- Kept local/offline storage as a fallback while remote sync is implemented.

## Current limitation
The database schema is prepared, but the existing UI is not yet fully converted to remote CRUD. The next development step is the sync/auth adapter.

## Free deployment target
- Frontend: GitHub Pages
- Database/Auth: Supabase Free
- Maps: Leaflet + OpenStreetMap
- Charts: Chart.js

## Safety
Do not upload credentials, service-role keys, patient exports, or private health information to a public Git repository.
