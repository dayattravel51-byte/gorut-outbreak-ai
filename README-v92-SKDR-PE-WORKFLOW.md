# GORUT OUTBREAK AI v92 — SKDR → PE/KLB Workflow

v92 menghubungkan alur operasional alert SKDR dengan verifikasi, pembukaan PE, respons, dan penutupan.

## Workflow
1. Alert Baru
2. Terverifikasi
3. PE Dibuka
4. Respons Berjalan
5. Selesai

Setiap perpindahan tahap di browser dicatat pada `workflowEvents`. Jika Supabase aktif, aplikasi mencoba mencatat transisi melalui RPC `transition_alert()` dan tabel `workflow_events`.

## Supabase
Jalankan SQL secara berurutan:
- `001_initial_schema.sql`
- `002_facility_rls_hardening.sql`
- `003_v91_command_center.sql`
- `004_v92_skrd_pe_workflow.sql`

## Catatan
Workflow membantu mengorganisasi respons dan tidak menetapkan KLB/wabah secara otomatis. Keputusan epidemiologis tetap dilakukan oleh tim yang berwenang berdasarkan definisi kasus, pedoman, dan investigasi lapangan.
