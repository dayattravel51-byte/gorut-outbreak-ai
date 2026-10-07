# GORUT-OUTBREAK AI v13

v13 adds an operational **Chain of Transmission** module and extends the investigation map with field-visit locations.

## New modules
- Chain of Transmission page
- Case/contact relationship visualization
- Linked-case relationship support (`linkedCaseId` locally; metadata in backend)
- Transmission-link entry form
- JSON export of investigation chain
- GIS map now displays case markers and field-visit points
- Backend sync for contacts and field visits using the existing Supabase schema

## Interpretation safeguard
A contact relationship is an epidemiological investigation link, not automatically proof of transmission. Investigators should establish temporal, spatial and exposure evidence according to the applicable disease investigation guidance.

## Offline-first
All new chain and field-visit records are stored locally first. Backend sync is attempted only when a configured Supabase backend and authenticated user are available.

## Production status
Still a development prototype. Do not deploy as an official registry without security review, privacy controls, validated instruments, server-side audit logging, tested synchronization/conflict handling, and statistical/epidemiological validation.
