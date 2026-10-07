from pathlib import Path
p=Path('/mnt/data/v78-work/index.html')
s=p.read_text(encoding='utf-8')
# Replace old v77 demography CSS block with v78 compact no-scroll CSS and add mobile field styles.
old="""/* Demography table: deliberately wide, readable numeric entry cells, horizontal scroll. */
#v72DemographyCard{overflow:hidden!important}#v72DemographyCard>div[style*=\"overflow:auto\"]{overflow-x:auto!important;overflow-y:auto!important;border:1px solid #dfe7ef;border-radius:12px;background:#fff;box-shadow:inset 0 1px 0 #fff}#v72DemographyCard .report-table{min-width:1540px;table-layout:fixed}#v72DemographyCard .report-table th,#v72DemographyCard .report-table td{white-space:nowrap;vertical-align:middle;padding:9px 10px}#v72DemographyCard .report-table th:nth-child(1){width:55px}#v72DemographyCard .report-table th:nth-child(2){width:145px}#v72DemographyCard .report-table th:nth-child(3){width:165px}#v72DemographyCard .report-table th:nth-child(4){width:170px}#v72DemographyCard .report-table th:nth-child(5),#v72DemographyCard .report-table th:nth-child(6),#v72DemographyCard .report-table th:nth-child(7),#v72DemographyCard .report-table th:nth-child(8){width:125px}#v72DemographyCard .report-table th:nth-child(9){width:120px}#v72DemographyCard .report-table th:nth-child(10),#v72DemographyCard .report-table th:nth-child(11){width:145px}#v72DemographyCard .report-table th:nth-child(12){width:145px}#v72DemographyCard .report-table th:nth-child(13){width:220px}#v72DemographyCard .report-table input{width:100%;min-width:105px;height:40px;padding:8px 10px;font-size:14px;font-variant-numeric:tabular-nums;background:#fbfdff}#v72DemographyCard .report-table td:nth-child(5) input,#v72DemographyCard .report-table td:nth-child(6) input,#v72DemographyCard .report-table td:nth-child(7) input,#v72DemographyCard .report-table td:nth-child(8) input{min-width:110px}#v72DemographyCard .report-table td:nth-child(9) input{min-width:105px}#v72DemographyCard .report-table td:nth-child(10) input,#v72DemographyCard .report-table td:nth-child(11) input{min-width:125px}#v72DemographyCard .report-table th{position:sticky;top:0;background:#f4f8fc;z-index:3}#v72DemographyCard .report-table td:nth-child(-n+4){background:#fbfdff}#v72DemographyCard .report-table tr:hover td{background:#f7fbff}#v72DemographyCard .badge{white-space:nowrap}
"""
if old not in s:
    raise SystemExit('old CSS block not found')
new="""/* v78 — Demography compact table: no horizontal scroll, no Catatan/Status columns. */
#v72DemographyCard{overflow:hidden!important}
#v72DemographyCard>div[style*=\"overflow:auto\"]{overflow:hidden!important;border:1px solid #dfe7ef;border-radius:12px;background:#fff;box-shadow:inset 0 1px 0 #fff}
#v72DemographyCard .report-table{width:100%!important;min-width:0!important;table-layout:fixed;border-collapse:separate;border-spacing:0}
#v72DemographyCard .report-table th,#v72DemographyCard .report-table td{white-space:normal;vertical-align:middle;padding:8px 7px}
#v72DemographyCard .report-table th{position:sticky;top:0;background:#f4f8fc;z-index:3;font-size:13px;line-height:1.15}
#v72DemographyCard .report-table td{font-size:13px}
#v72DemographyCard .report-table th:nth-child(1){width:4%}
#v72DemographyCard .report-table th:nth-child(2){width:10%}
#v72DemographyCard .report-table th:nth-child(3){width:12%}
#v72DemographyCard .report-table th:nth-child(4){width:13%}
#v72DemographyCard .report-table th:nth-child(5){width:11%}
#v72DemographyCard .report-table th:nth-child(6){width:10%}
#v72DemographyCard .report-table th:nth-child(7){width:10%}
#v72DemographyCard .report-table th:nth-child(8){width:8%}
#v72DemographyCard .report-table th:nth-child(9){width:8%}
#v72DemographyCard .report-table th:nth-child(10){width:7%}
#v72DemographyCard .report-table th:nth-child(11){width:7%}
#v72DemographyCard .report-table input{box-sizing:border-box;width:100%;min-width:0!important;height:44px;padding:8px 7px;font-size:15px;font-weight:600;font-variant-numeric:tabular-nums;background:#fbfdff;text-align:right;border:1px solid #cbd7e5;border-radius:10px}
#v72DemographyCard .report-table td:nth-child(10) input,#v72DemographyCard .report-table td:nth-child(11) input{text-align:center;font-size:13px}
#v72DemographyCard .report-table td:nth-child(-n+4){background:#fbfdff}
#v72DemographyCard .report-table tr:hover td{background:#f7fbff}
#v72DemographyCard .report-table td:nth-child(2),#v72DemographyCard .report-table td:nth-child(3),#v72DemographyCard .report-table td:nth-child(4){word-break:break-word}
#v72DemographyCard .v78-no-scroll-note{display:flex;align-items:center;gap:8px;margin-top:8px;font-size:12px;color:#52606d}
/* v78 — Mobile field form */
.v78-mobile-field{display:none}
.v78-mobile-field .mobile-hero{background:linear-gradient(135deg,#f5fbff,#f2fffc);border:1px solid #d8e8f2;border-radius:18px;padding:16px;box-shadow:0 10px 28px rgba(16,42,67,.06)}
.v78-mobile-field .mobile-hero h2{margin:0 0 5px;font-size:22px}
.v78-mobile-field .mobile-hero p{margin:0;color:#52606d;font-size:13px;line-height:1.45}
.v78-mobile-field .mobile-step{display:flex;align-items:center;gap:10px;margin:14px 0 8px;font-weight:800;font-size:13px;color:#243b53}
.v78-mobile-field .mobile-step span{display:inline-flex;width:26px;height:26px;align-items:center;justify-content:center;border-radius:50%;background:#1769aa;color:#fff;font-size:12px}
.v78-mobile-field .mobile-card{background:#fff;border:1px solid #e1e8f0;border-radius:16px;padding:14px;margin-top:12px;box-shadow:0 8px 22px rgba(16,42,67,.05)}
.v78-mobile-field .mobile-field{margin-top:11px}.v78-mobile-field .mobile-field label{display:block;font-size:12px;font-weight:800;color:#52606d;margin-bottom:6px}.v78-mobile-field input,.v78-mobile-field select,.v78-mobile-field textarea{width:100%;box-sizing:border-box;min-height:48px;border:1px solid #cbd7e5;border-radius:12px;background:#fbfdff;padding:11px 12px;font-size:16px!important;color:#172b4d}.v78-mobile-field textarea{min-height:96px;resize:vertical}.v78-mobile-field input:focus,.v78-mobile-field select:focus,.v78-mobile-field textarea:focus{outline:3px solid rgba(23,105,170,.12);border-color:#1769aa;background:#fff}.v78-mobile-field .gps-row{display:grid;grid-template-columns:1fr 1fr;gap:8px}.v78-mobile-field .gps-btn{width:100%;min-height:48px;border:0;border-radius:12px;background:#1769aa;color:#fff;font-weight:800;font-size:14px}.v78-mobile-field .save-btn{width:100%;min-height:54px;border:0;border-radius:14px;background:linear-gradient(135deg,#0b8f8b,#1769aa);color:#fff;font-size:16px;font-weight:900;box-shadow:0 10px 22px rgba(23,105,170,.2)}.v78-mobile-field .draft-btn{width:100%;min-height:48px;border:1px solid #cbd7e5;border-radius:12px;background:#fff;color:#243b53;font-weight:800}.v78-mobile-field .status-pill{display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border-radius:999px;background:#eef4f8;font-size:12px;font-weight:800;color:#52606d}.v78-mobile-field .photo-preview{width:100%;max-height:180px;object-fit:cover;border-radius:12px;margin-top:8px;display:none}.v78-mobile-field .offline-note{font-size:12px;color:#52606d;line-height:1.45}.v78-mobile-field .required::after{content:' *';color:#b42318}
@media(max-width:800px){
  .v78-mobile-field{display:block}
  #lapangan>.card:first-child,#lapangan>#fieldDashboard,#lapangan>.card:last-child{display:none!important}
  #v72DemographyCard>div[style*="overflow:auto"]{overflow:hidden!important}
  #v72DemographyCard .report-table{font-size:11px}
  #v72DemographyCard .report-table th,#v72DemographyCard .report-table td{padding:5px 3px}
  #v72DemographyCard .report-table input{height:38px;padding:5px 3px;font-size:12px!important;border-radius:7px}
  #v72DemographyCard .report-table th:nth-child(2),#v72DemographyCard .report-table th:nth-child(3),#v72DemographyCard .report-table th:nth-child(4){width:auto}
}
@media(min-width:801px){#v78MobileField{display:none!important}}
"""
s=s.replace(old,new)
# Change sidebar label only, keep page id.
s=s.replace('<button onclick="page(\'lapangan\',this)">📱 Lapangan</button>','<button onclick="page(\'lapangan\',this)">📱 Formulir Lapangan</button>')
p.write_text(s,encoding='utf-8')

p=Path('/mnt/data/v78-work/app.js')
s=p.read_text(encoding='utf-8')
marker='/* ==================== v77 — PREMIUM DASHBOARD + DATA ENTRY UX ==================== */'
if marker not in s: raise SystemExit('v77 marker missing')
# Append v78 after v77 block (end of file).
append=r'''

/* ==================== v78 — COMPACT DEMOGRAPHY + MOBILE FIELD FORM ==================== */
(function(){
  const V='v78';
  const E=id=>document.getElementById(id);
  const esc78=v=>typeof esc==='function'?esc(v):String(v??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
  const KEY='gorut-demography-v72-village';
  const DRAFT='gorut-field-mobile-draft-v78';
  const master=window.GORUT_VILLAGE_MASTER_V69?.data||[];
  const villages=master.flatMap(g=>(g.desa||[]).map(d=>({puskesmas:g.puskesmas,kec:g.kec,desa:d})));
  const vByName=name=>villages.find(x=>String(x.desa).toLowerCase()===String(name||'').toLowerCase());
  function year(){return Number(E('demoYearV49')?.value)||new Date().getFullYear()}
  function load(){try{return JSON.parse(localStorage.getItem(KEY)||'null')||{years:{},meta:{}}}catch(e){return {years:{},meta:{}}}}
  function rows(y){const d=load(),saved=d.years?.[String(y)]||{};return villages.map(r=>({...r,population:'',male:'',female:'',households:'',areaKm2:'',lat:'',lng:'',note:'',...(saved[`${r.puskesmas}||${r.desa}`]||{}),puskesmas:r.puskesmas,kec:r.kec,desa:r.desa}))}
  function valid(r){const p=Number(r.population),m=Number(r.male),f=Number(r.female);return p>0&&m>=0&&f>=0&&Math.abs(m+f-p)<0.001}
  function renderCompact(){
    const host=E('demoMasterV66');if(!host)return;
    const card=E('v72DemographyCard');if(!card)return;
    const table=card.querySelector('.report-table');if(!table)return;
    const wrap=table.closest('div[style*="overflow:auto"]');if(wrap){wrap.style.overflow='hidden';wrap.style.overflowX='hidden';wrap.style.overflowY='hidden'}
    const thead=table.querySelector('thead tr');
    if(thead){thead.innerHTML='<th>No.</th><th>Kecamatan</th><th>Puskesmas</th><th>Desa</th><th>Penduduk</th><th>Laki-laki</th><th>Perempuan</th><th>KK</th><th>Luas<br>km²</th><th>Latitude</th><th>Longitude</th>';}
    const body=E('v72Rows');if(!body)return;
    const oldRows=rows(year());
    const q=(E('v72Search')?.value||'').toLowerCase().trim(),k=E('v72Kec')?.value||'',p=E('v72Pkm')?.value||'';
    const arr=oldRows.map((r,i)=>({...r,_i:i})).filter(r=>(!k||r.kec===k)&&(!p||r.puskesmas===p)&&(!q||`${r.kec} ${r.puskesmas} ${r.desa}`.toLowerCase().includes(q)));
    body.innerHTML=arr.map((r,n)=>`<tr><td>${n+1}</td><td>${esc78(r.kec)}</td><td><b>${esc78(r.puskesmas)}</b></td><td><b>${esc78(r.desa)}</b></td><td><input aria-label="Penduduk ${esc78(r.desa)}" data-v72="population" data-i="${r._i}" type="number" min="0" inputmode="numeric" value="${esc78(r.population)}"></td><td><input aria-label="Laki-laki ${esc78(r.desa)}" data-v72="male" data-i="${r._i}" type="number" min="0" inputmode="numeric" value="${esc78(r.male)}"></td><td><input aria-label="Perempuan ${esc78(r.desa)}" data-v72="female" data-i="${r._i}" type="number" min="0" inputmode="numeric" value="${esc78(r.female)}"></td><td><input aria-label="KK ${esc78(r.desa)}" data-v72="households" data-i="${r._i}" type="number" min="0" inputmode="numeric" value="${esc78(r.households)}"></td><td><input aria-label="Luas km2 ${esc78(r.desa)}" data-v72="areaKm2" data-i="${r._i}" type="number" min="0" step="any" inputmode="decimal" value="${esc78(r.areaKm2)}"></td><td><input aria-label="Latitude ${esc78(r.desa)}" data-v72="lat" data-i="${r._i}" type="number" step="any" inputmode="decimal" value="${esc78(r.lat)}"></td><td><input aria-label="Longitude ${esc78(r.desa)}" data-v72="lng" data-i="${r._i}" type="number" step="any" inputmode="decimal" value="${esc78(r.lng)}"></td></tr>`).join('')||'<tr><td colspan="11"><div class="notice">Tidak ada desa yang cocok dengan filter.</div></td></tr>';
    if(!card.querySelector('.v78-no-scroll-note')){const n=document.createElement('div');n.className='v78-no-scroll-note';n.innerHTML='✓ <span>Mode ringkas aktif. Catatan dan status denominator tidak ditampilkan; validasi denominator tetap dihitung otomatis oleh sistem.</span>';table.parentElement.appendChild(n)}
  }
  function saveCompact(){
    const y=year(),rs=rows(y);
    document.querySelectorAll('[data-v72]').forEach(el=>{const i=Number(el.dataset.i);if(rs[i])rs[i][el.dataset.v72]=el.value});
    const d=load();d.years=d.years||{};d.meta=d.meta||{};d.years[String(y)]={};rs.forEach(r=>d.years[String(y)][`${r.puskesmas}||${r.desa}`]={...r});d.meta[String(y)]={...(d.meta?.[String(y)]||{}),structure:'1 baris per desa · v78 compact'};
    localStorage.setItem(KEY,JSON.stringify(d));
    if(typeof window.renderDemographyV49==='function'){try{window.renderDemographyV49()}catch(e){}}
    renderCompact();
    alert(`Demografi desa ${y} berhasil disimpan: ${rs.length} desa.`);
  }
  window.renderDemographyVillageV72=renderCompact;
  window.saveDemographyV72=saveCompact;
  window.saveDemographyV66=saveCompact;

  function optionList(){return villages.map(v=>`<option value="${esc78(v.desa)}">${esc78(v.desa)} — ${esc78(v.puskesmas)}</option>`).join('')}
  function caseOptions(){return (db.cases||[]).filter(c=>!db.active||String(c.investigationId)===String(db.active)).map(c=>`<option value="${esc78(c.id)}">${esc78(c.id)} — ${esc78(c.name||'Tanpa nama')}</option>`).join('')}
  function contactOptions(){return (db.contacts||[]).filter(c=>!db.active||String(c.investigationId)===String(db.active)).map(c=>`<option value="${esc78(c.id)}">${esc78(c.id)} — ${esc78(c.name||'Tanpa nama')}</option>`).join('')}
  function getDraft(){try{return JSON.parse(localStorage.getItem(DRAFT)||'null')}catch(e){return null}}
  function setVal(id,v){const e=E(id);if(e)e.value=v??''}
  function renderMobileField(){
    const sec=E('lapangan');if(!sec)return;
    let host=E('v78MobileField');if(!host){host=document.createElement('div');host.id='v78MobileField';host.className='v78-mobile-field';sec.insertBefore(host,sec.firstElementChild)}
    const investigations=(db.investigations||[]);
    host.innerHTML=`<div class="mobile-hero"><div class="eyebrow">FIELD RESPONSE · MOBILE</div><h2>📱 Formulir Lapangan</h2><p>Pengisian cepat untuk petugas di HP. Data disimpan di perangkat terlebih dahulu dan dapat dilanjutkan saat koneksi tersedia.</p><div style="margin-top:10px"><span class="status-pill" id="v78NetStatus">● Memeriksa koneksi…</span></div></div>
      <div class="mobile-card"><div class="mobile-step"><span>1</span> Kegiatan lapangan</div>
        <div class="mobile-field"><label class="required">Investigasi aktif</label><select id="mFieldInv"><option value="">Pilih investigasi</option>${investigations.map(i=>`<option value="${esc78(i.id)}">${esc78(i.name||i.id)} — ${esc78(diseases[i.disease]?.name||i.disease||'')}</option>`).join('')}</select></div>
        <div class="mobile-field"><label class="required">Jenis kegiatan</label><select id="mFieldActivity"><option>Kunjungan kasus</option><option>Wawancara kontak</option><option>Verifikasi lokasi</option><option>Pengambilan spesimen</option><option>Survei lingkungan</option><option>Investigasi aktif</option><option>Pelacakan kontak</option></select></div>
        <div class="mobile-field"><label class="required">Tanggal & waktu</label><input id="mFieldDate" type="datetime-local"></div>
        <div class="mobile-field"><label>Petugas</label><input id="mFieldOfficer" placeholder="Nama/inisial petugas"></div>
      </div>
      <div class="mobile-card"><div class="mobile-step"><span>2</span> Lokasi</div>
        <div class="mobile-field"><label class="required">Desa/Kelurahan</label><select id="mFieldVillage"><option value="">Pilih desa</option>${optionList()}</select></div>
        <div class="mobile-field"><label>Puskesmas</label><input id="mFieldPkm" readonly placeholder="Otomatis dari desa"></div>
        <div class="mobile-field"><label>Kecamatan</label><input id="mFieldKec" readonly placeholder="Otomatis dari desa"></div>
        <div class="mobile-field"><label>Koordinat GPS</label><div class="gps-row"><input id="mFieldLat" inputmode="decimal" placeholder="Latitude"><input id="mFieldLng" inputmode="decimal" placeholder="Longitude"></div><button class="gps-btn" type="button" style="margin-top:8px" onclick="getMobileGPS()">📍 Ambil lokasi GPS</button><div id="mFieldGpsStatus" class="small" style="margin-top:6px">GPS belum diambil.</div></div>
        <div class="mobile-field"><label>Alamat/lokasi detail</label><textarea id="mFieldLocation" placeholder="Dusun, rumah, sekolah, pasar, fasilitas kesehatan, atau lokasi kejadian"></textarea></div>
      </div>
      <div class="mobile-card"><div class="mobile-step"><span>3</span> Subjek & keterkaitan</div>
        <div class="mobile-field"><label>Nama/ID subjek</label><input id="mFieldSubject" placeholder="Gunakan ID/inisial bila perlu"></div>
        <div class="mobile-field"><label>Kasus terkait</label><select id="mFieldCase"><option value="">Tidak terkait kasus tertentu</option>${caseOptions()}</select></div>
        <div class="mobile-field"><label>Kontak terkait</label><select id="mFieldContact"><option value="">Tidak terkait kontak tertentu</option>${contactOptions()}</select></div>
      </div>
      <div class="mobile-card"><div class="mobile-step"><span>4</span> Temuan & respons</div>
        <div class="mobile-field"><label class="required">Temuan utama</label><textarea id="mFieldFinding" placeholder="Apa yang ditemukan di lapangan?"></textarea></div>
        <div class="mobile-field"><label>Tindakan/intervensi</label><textarea id="mFieldAction" placeholder="Edukasi, isolasi, rujukan, pengambilan spesimen, PSN, komunikasi risiko, dll."></textarea></div>
        <div class="mobile-field"><label>Foto lapangan</label><input id="mFieldPhoto" type="file" accept="image/*" capture="environment"><img id="mFieldPreview" class="photo-preview" alt="Pratinjau foto lapangan"></div>
      </div>
      <div class="mobile-card"><div class="mobile-step"><span>5</span> Simpan</div><div class="offline-note">💾 <b>Offline-first:</b> jika internet tidak tersedia, data tetap disimpan di perangkat. Sinkronisasi dapat dilakukan setelah koneksi tersedia.</div><div style="display:grid;gap:9px;margin-top:12px"><button class="save-btn" type="button" onclick="saveMobileFieldVisit()">✓ Simpan Kunjungan Lapangan</button><button class="draft-btn" type="button" onclick="saveMobileFieldDraft()">📝 Simpan sebagai Draft</button><button class="draft-btn" type="button" onclick="clearMobileFieldForm()">↺ Bersihkan Formulir</button></div><div id="mFieldSaveStatus" class="small" style="margin-top:10px"></div></div>`;
    const inv=E('mFieldInv');if(inv&&db.active)inv.value=db.active;
    const dt=E('mFieldDate');if(dt&&!dt.value)dt.value=new Date(Date.now()-new Date().getTimezoneOffset()*60000).toISOString().slice(0,16);
    const draft=getDraft();if(draft)fillDraft(draft);
    E('mFieldVillage')?.addEventListener('change',()=>{const v=vByName(E('mFieldVillage').value);setVal('mFieldPkm',v?.puskesmas||'');setVal('mFieldKec',v?.kec||'');});
    E('mFieldPhoto')?.addEventListener('change',()=>{const f=E('mFieldPhoto')?.files?.[0],img=E('mFieldPreview');if(!f||!img){if(img)img.style.display='none';return}const u=URL.createObjectURL(f);img.src=u;img.style.display='block';img.onload=()=>URL.revokeObjectURL(u)});
    updateNetStatus();
  }
  function readMobilePhoto(){return new Promise(resolve=>{const f=E('mFieldPhoto')?.files?.[0];if(!f)return resolve(null);const r=new FileReader();r.onload=()=>resolve(r.result);r.onerror=()=>resolve(null);r.readAsDataURL(f)})}
  function mobileData(){const v=vByName(E('mFieldVillage')?.value||'');return {investigationId:E('mFieldInv')?.value||db.active||'',activity:E('mFieldActivity')?.value||'',subject:E('mFieldSubject')?.value||'',caseId:E('mFieldCase')?.value||'',contactId:E('mFieldContact')?.value||'',date:E('mFieldDate')?.value||new Date().toISOString().slice(0,16),officer:E('mFieldOfficer')?.value||'',desa:v?.desa||'',puskesmas:v?.puskesmas||'',kec:v?.kec||'',lat:E('mFieldLat')?.value||'',lng:E('mFieldLng')?.value||'',location:E('mFieldLocation')?.value||'',finding:E('mFieldFinding')?.value||'',action:E('mFieldAction')?.value||''}}
  function fillDraft(d){Object.entries(d||{}).forEach(([k,v])=>setVal(k,v));const v=E('mFieldVillage')?.value? vByName(E('mFieldVillage').value):null;if(v){setVal('mFieldPkm',v.puskesmas);setVal('mFieldKec',v.kec)}}
  window.saveMobileFieldDraft=function(){const d=mobileData();localStorage.setItem(DRAFT,JSON.stringify(d));if(E('mFieldSaveStatus'))E('mFieldSaveStatus').textContent='✓ Draft tersimpan di perangkat.'}
  window.clearMobileFieldForm=function(){localStorage.removeItem(DRAFT);renderMobileField();if(E('mFieldSaveStatus'))E('mFieldSaveStatus').textContent='Formulir dibersihkan.'}
  window.getMobileGPS=function(){const s=E('mFieldGpsStatus');if(!navigator.geolocation){if(s)s.textContent='GPS tidak didukung perangkat ini.';return}if(s)s.textContent='GPS sedang mengambil lokasi…';navigator.geolocation.getCurrentPosition(pos=>{setVal('mFieldLat',pos.coords.latitude.toFixed(6));setVal('mFieldLng',pos.coords.longitude.toFixed(6));if(s)s.textContent=`✓ GPS diperoleh · akurasi ±${Math.round(pos.coords.accuracy||0)} m`},e=>{if(s)s.textContent='GPS gagal: '+e.message},{enableHighAccuracy:true,timeout:15000,maximumAge:30000})}
  window.saveMobileFieldVisit=async function(){
    const d=mobileData();
    if(!d.investigationId)return alert('Pilih investigasi aktif terlebih dahulu.');
    if(!d.desa)return alert('Pilih Desa/Kelurahan terlebih dahulu.');
    if(!d.finding)return alert('Isi Temuan utama terlebih dahulu.');
    const photo=await readMobilePhoto();
    const o={id:'MFV'+Date.now(),...d,photo,syncStatus:'pending',source:'mobile-field-v78',createdAt:new Date().toISOString()};
    db.fieldVisits=db.fieldVisits||[];db.fieldVisits.push(o);
    if(typeof queueSync==='function')queueSync('field_visits');
    save();localStorage.removeItem(DRAFT);
    if(E('mFieldSaveStatus'))E('mFieldSaveStatus').textContent='✓ Kunjungan tersimpan di perangkat dan masuk antrean sinkronisasi.';
    if(typeof fieldVisits==='function')try{fieldVisits()}catch(e){}
    renderMobileField();
    if(E('mFieldSaveStatus'))E('mFieldSaveStatus').textContent='✓ Kunjungan tersimpan. Siap untuk kunjungan berikutnya.';
  };
  function updateNetStatus(){const e=E('v78NetStatus');if(!e)return;e.textContent=navigator.onLine?'● Online · data tetap disimpan lokal':'● Offline · data disimpan di perangkat';e.style.background=navigator.onLine?'#e8f7ef':'#fff4e5';e.style.color=navigator.onLine?'#176b45':'#8a4b08'}
  window.addEventListener('online',updateNetStatus);window.addEventListener('offline',updateNetStatus);
  function inject(){renderCompact();renderMobileField()}
  const oldPage=window.page;window.page=function(id,b){const r=typeof oldPage==='function'?oldPage.apply(this,arguments):undefined;setTimeout(()=>{if(id==='demografi')renderCompact();if(id==='lapangan')renderMobileField()},180);return r};
  setTimeout(inject,1800);
  window.GORUT_V78={version:V,features:['compact demography without horizontal scroll','removed Catatan and Status Denominator from visible table','larger numeric inputs','mobile-first field response form','GPS capture','village-to-puskesmas-kecamatan mapping','offline draft','offline-first field visit storage','photo capture']};
})();
'''
s += append
p.write_text(s,encoding='utf-8')
