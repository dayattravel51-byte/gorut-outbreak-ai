# GORUT-OUTBREAK AI v28 — Deployment Production

## 1. Frontend
- Host static files on a provider with HTTPS.
- `backend-config.js` must contain only the Supabase project URL and public anon/publishable key.
- Never put `service_role` or secret API keys in `backend-config.js`.

Example:
```js
window.GORUT_BACKEND = {
  enabled: true,
  url: 'https://YOUR-PROJECT.supabase.co',
  anonKey: 'YOUR-PUBLISHABLE-OR-ANON-KEY'
};
```

## 2. Supabase database
Run, in order:
1. `supabase-schema.sql`
2. Review RLS policies in the Supabase dashboard.
3. Confirm `registration_requests`, `subscriptions`, `audit_log`, `my_access_status` and functions exist.

## 3. Authentication
Enable Email provider in Supabase Auth. Use email verification according to the deployment policy.

## 4. Admin
Create the admin account through Supabase Auth, then set its profile role to one of:
- `admin_kabupaten`
- `admin_provinsi`
- `admin_pusat`

Do not expose service-role credentials in browser code.

## 5. Premium registration flow
1. User creates an account in **Registrasi Akses 7 Hari**.
2. User transfers Rp30.000 to BNI 0599687726 a.n. Hidayat.
3. User confirms through WhatsApp 082290150334.
4. Admin verifies the transfer independently.
5. Admin activates the registration from the server-side admin panel.
6. PostgreSQL sets `starts_at = now()` and `expires_at = now() + 7 days`.
7. User can enter only while the subscription is active.

## 6. Offline/demo
The localStorage path remains for training/demo/offline scenarios. It is not a security boundary and must not be used as the production subscription authority.

## 7. Before commercial launch
- Test RLS with two different users.
- Confirm user A cannot read/write user B's cases, contacts, specimens or investigations.
- Test expiry using a controlled test subscription.
- Test admin activation and audit log.
- Configure database backups and recovery.
- Configure HTTPS, domain, CSP, and secure headers.
- Minimize personally identifiable information and define retention policy.
- Conduct privacy/security review before operational epidemiological data is uploaded.
