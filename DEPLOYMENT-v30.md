# Deployment v30 — Production Release Candidate

1. Deploy static files over HTTPS.
2. Configure Supabase URL + anon key in `backend-config.js` (never service-role key).
3. Run base schema, then `supabase-schema-v30.sql`.
4. Enable Supabase Auth and email confirmation as desired.
5. Create the first admin account, then set its profile role to `admin_pusat` or another admin role.
6. Test registration: signup → registration request → admin review → activate 7 days → user login → server-side access status.
7. Test expired subscription and ensure access is denied.
8. Test RLS with two ordinary accounts: each must only see its own records.
9. Test admin account: admin can manage all operational records.
10. Test delete actions and confirm records are removed only after confirmation.
11. Keep bank verification manual unless an official payment gateway/API is integrated.
12. Never expose Supabase service-role key in frontend code.
