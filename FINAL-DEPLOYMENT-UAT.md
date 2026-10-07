# GORUT OUTBREAK AI v98 — FINAL DEPLOYMENT & UAT

## Status
Feature development is frozen at v98. This release is intended for deployment/UAT, not further feature expansion.

## 1. Supabase setup
1. Create a Supabase project.
2. Run SQL files in order: `001_initial_schema.sql` through `009_v98_response_management.sql`.
3. Do not run `service_role` keys in the browser.
4. Enable Email/Password authentication for staff accounts.
5. Populate `facilities` with the official Gorontalo Utara facility master.
6. Populate `profiles` for each test account with the correct role and facility.
7. Verify RLS before any real patient data is entered.

## 2. Browser configuration
Copy `backend-config.example.js` to `backend-config.js` and set:
- `url`: Supabase project URL
- `anonKey`: public anon/publishable key
- `enabled`: `true`

Never place a Supabase `service_role` key in this file.

## 3. Initial master data
Minimum production master data:
- Dinas Kesehatan Kabupaten Gorontalo Utara
- 15 Puskesmas
- Rumah sakit/unit pelapor yang digunakan SKDR
- TGC/surveilans users
- official population denominators
- validated administrative GIS boundary GeoJSON

## 4. UAT accounts
Create at least six test identities:
- Admin
- Surveilans
- Puskesmas A
- Rumah Sakit
- TGC
- Viewer

## 5. Mandatory UAT cases
### A. Authentication
- Login succeeds with valid account.
- Invalid password is rejected.
- Logout destroys session.
- Role is loaded from `profiles`.

### B. Facility isolation
- Puskesmas A cannot read another facility's operational records.
- Viewer cannot read raw patient-level records.
- Admin/Surveilans can access district operational records.

### C. SKDR workflow
Create test alert and verify:
`Alert Baru → Terverifikasi → PE Dibuka → Respons → Selesai`.

Confirm workflow history is retained.

### D. PE/KLB
Create investigation from a test alert. Confirm:
- `source_alert_id` is populated.
- facility scope is retained.
- status changes are visible.

### E. Response management
Create a response action and test:
`Baru → Verifikasi → Ditugaskan → Intervensi → Monitoring → Selesai`.
Confirm PIC, deadline and history.

### F. GIS
Upload only validated official GeoJSON. Confirm:
- name matching works;
- denominator is required for IR;
- missing denominator is not treated as zero population;
- public view contains aggregate information only.

### G. Public dashboard
Confirm no public route exposes:
- patient name;
- phone number;
- address of individual;
- individual contact data;
- individual clinical record.

## 6. Production go/no-go
GO only when all six roles pass UAT, RLS isolation is verified, master facilities are correct, and GIS/population sources are validated.

Until then, use synthetic/test data only.
