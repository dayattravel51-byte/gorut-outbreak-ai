# Deployment v29

## Checklist production
- [ ] Supabase project production
- [ ] Auth email/password atau provider resmi
- [ ] SQL v29 dijalankan
- [ ] RLS diuji sebagai user biasa dan admin
- [ ] Admin role ditetapkan pada profiles
- [ ] `backend-config.js` tidak berisi service_role key
- [ ] HTTPS aktif
- [ ] Domain production
- [ ] Backup database
- [ ] Uji registrasi -> payment reference -> admin verification -> 7 day access
- [ ] Uji expired access
- [ ] Uji admin bypass
- [ ] Uji isolasi data antar akun
- [ ] Uji delete record dan audit/logging sesuai kebijakan

## Security rule
Jangan menaruh Supabase `service_role` key di browser. Hanya anon/publishable key yang boleh digunakan frontend.
