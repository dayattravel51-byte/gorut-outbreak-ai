
/* ============================================================
   GORUT-OUTBREAK AI v97 — EARLY WARNING & RESPONSE ENGINE
   Transparent, non-validated operational screening. No automatic KLB.
   ============================================================ */
(function(){
  'use strict';
  const VERSION='v97';
  const E=id=>document.getElementById(id);
  const esc97=v=>typeof esc==='function'?esc(v):String(v??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
  const norm=s=>String(s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9]+/g,' ').trim();
  const invs=()=>db?.investigations||[];
  const cases=()=>db?.cases||[];
  const alerts=()=>db?.alerts||[];
  const specimens=()=>db?.specimens||[];
  const diseaseName=code=>(typeof diseases!=='undefined'&&diseases?.[code]?.name)||code||'Semua penyakit';
  const dt=v=>{const d=new Date(v);return isNaN(d)?null:new Date(d.getFullYear(),d.getMonth(),d.getDate())};
  const day0=d=>new Date(d.getFullYear(),d.getMonth(),d.getDate());
  const daysAgo=(d,n)=>{const x=new Date(d);x.setDate(x.getDate()-n);return x};
  const diseaseOfCase=c=>{const i=invs().find(x=>String(x.id)===String(c.investigationId));return c.disease||i?.disease||i?.disease_code||''};
  const diseaseFilter=()=>E('v97Disease')?.value||'';
  function eligibleCases(){const f=diseaseFilter();return cases().filter(c=>{const d=diseaseOfCase(c);return !f||String(d)===f}).map(c=>({...c,_d:dt(c.onset||c.onsetAt||c.createdAt)})).filter(c=>c._d);}
  function eligibleAlerts(){const f=diseaseFilter();return alerts().filter(a=>!f||String(a.disease||a.diseaseCode||'')===f).map(a=>({...a,_d:dt(a.alertDate||a.date||a.createdAt)})).filter(a=>a._d);}
  function eligibleInvs(){const f=diseaseFilter();return invs().filter(i=>!f||String(i.disease||i.disease_code||'')===f);}
  function populateDisease(){const s=E('v97Disease');if(!s)return;const cur=s.value, seen=new Set(), opts=[];invs().forEach(i=>{const d=i.disease||i.disease_code||'';if(d&&!seen.has(d)){seen.add(d);opts.push([d,diseaseName(d)])}});alerts().forEach(a=>{const d=a.disease||a.diseaseCode||'';if(d&&!seen.has(d)){seen.add(d);opts.push([d,diseaseName(d)])}});opts.sort((a,b)=>a[1].localeCompare(b[1]));s.innerHTML='<option value="">Semua penyakit</option>'+opts.map(x=>`<option value="${esc97(x[0])}">${esc97(x[1])}</option>`).join('');if(cur&&seen.has(cur))s.value=cur;}
  function calc(){
    const cs=eligibleCases(), as=eligibleAlerts(), today=cs.reduce((m,c)=>c._d>m?c._d:m,day0(new Date()));
    const latest=cs.filter(c=>c._d>=daysAgo(today,6)&&c._d<=today);
    const prev28=cs.filter(c=>c._d>=daysAgo(today,34)&&c._d<daysAgo(today,6));
    const prevWeeks=prev28.length/4;
    const growthPct=prevWeeks?((latest.length-prevWeeks)/prevWeeks*100):(latest.length?100:0);
    const trendScore=Math.min(35,Math.max(0,growthPct/100*35));
    const totalPop=(db?.demography||[]).reduce((s,r)=>s+(Number(r.population||r.penduduk)||0),0);
    const ir=totalPop?latest.length/totalPop*10000:null;
    const irScore=ir==null?0:Math.min(25,(ir/10)*25);
    const alert7=as.filter(a=>a._d>=daysAgo(today,6)&&a._d<=today).length;
    const alertScore=Math.min(20,alert7*4);
    const deaths=latest.filter(c=>String(c.outcome||'').toLowerCase().includes('meninggal')).length;
    const deathScore=Math.min(20,deaths*10);
    const score=Math.round(trendScore+irScore+alertScore+deathScore);
    const level=score>=75?'SANGAT TINGGI':score>=50?'TINGGI':score>=25?'SEDANG':'RENDAH';
    const pending=specimens().filter(s=>{const st=norm(s.status||'');const r=norm(s.result||'');return !r&&!['selesai','final','negatif','positif'].some(x=>st.includes(x));}).length;
    const openInv=eligibleInvs().filter(i=>!['selesai','ditutup'].includes(norm(i.status))).length;
    const quality={casesWithOnset:cs.length,alerts:as.length,population:totalPop};
    return {today,latest:latest.length,prevWeeks,growthPct,ir,alert7,deaths,pending,openInv,score,level,trendScore,irScore,alertScore,deathScore,quality};
  }
  function render(){
    populateDisease(); const a=calc(); window.V97_EARLY_WARNING=a;
    const sum=E('v97Summary'); if(sum)sum.innerHTML=`<div class="stat"><small>Early Warning Score</small><b>${a.score}/100</b><span>${a.level}</span></div><div class="stat"><small>Kasus 7 hari</small><b>${a.latest}</b><span>${a.growthPct>0?'+':''}${a.growthPct.toFixed(1)}% vs rerata mingguan</span></div><div class="stat"><small>Alert 7 hari</small><b>${a.alert7}</b><span>${a.openInv} investigasi terbuka</span></div><div class="stat"><small>Respons/Lab</small><b>${a.pending}</b><span>spesimen pending</span></div>`;
    const bar=E('v97ScoreBars');if(bar)bar.innerHTML=[['Tren kasus',a.trendScore,35],['Incidence Rate',a.irScore,25],['Alert SKDR',a.alertScore,20],['Kematian',a.deathScore,20]].map(x=>`<div style="margin:10px 0"><div style="display:flex;justify-content:space-between"><b>${x[0]}</b><span>${x[1].toFixed(1)} / ${x[2]}</span></div><div style="height:10px;background:#e5e7eb;border-radius:9px;overflow:hidden"><div style="height:100%;width:${Math.min(100,x[1]/x[2]*100)}%;background:#1677d2"></div></div></div>`).join('');
    const rec=E('v97Recommendation');if(rec){let t='';if(a.score>=75)t='Prioritas sangat tinggi: lakukan verifikasi lapangan dan telaah investigasi aktif segera.';else if(a.score>=50)t='Prioritas tinggi: lakukan review epidemiologis, validasi data dan kesiapan respons.';else if(a.score>=25)t='Prioritas sedang: pantau tren, kelengkapan pelaporan, dan sinyal SKDR.';else t='Prioritas rendah berdasarkan indikator yang tersedia; surveilans rutin tetap dilanjutkan.';rec.innerHTML=`<b>${t}</b><br><span class="small">Ini adalah screening operasional yang transparan, bukan skor tervalidasi untuk diagnosis, prediksi wabah, atau penetapan KLB.</span>`;}
    const gap=E('v97Gaps');if(gap)gap.innerHTML=`<table><tbody><tr><th>Spesimen pending</th><td>${a.pending}</td></tr><tr><th>Investigasi terbuka</th><td>${a.openInv}</td></tr><tr><th>Denominator penduduk</th><td>${a.quality.population.toLocaleString('id-ID')}</td></tr><tr><th>Data kasus dengan tanggal</th><td>${a.quality.casesWithOnset}</td></tr></tbody></table>`;
  }
  window.renderV97EarlyWarning=render;
  window.exportV97EarlyWarning=function(){const a=window.V97_EARLY_WARNING||calc();const rows=[['Indikator','Nilai'],['Score',a.score],['Level',a.level],['Kasus 7 hari',a.latest],['Pertumbuhan persen',a.growthPct],['IR per 10000',a.ir??''],['Alert 7 hari',a.alert7],['Kematian 7 hari',a.deaths],['Spesimen pending',a.pending],['Investigasi terbuka',a.openInv]];const csv=rows.map(r=>r.map(v=>'"'+String(v??'').replace(/"/g,'""')+'"').join(',')).join('\n');const u=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));const el=document.createElement('a');el.href=u;el.download='GORUT-v97-early-warning.csv';el.click();setTimeout(()=>URL.revokeObjectURL(u),500);};
  function injectDashboard(){const d=E('dashboard');if(!d||E('v97DashboardCard'))return;const c=document.createElement('div');c.id='v97DashboardCard';c.className='card';c.style.marginTop='14px';c.innerHTML=`<div class="toolbar" style="justify-content:space-between"><div><div class="eyebrow">EARLY WARNING & RESPONSE ENGINE · v97</div><h3 style="margin:3px 0">🚨 Prioritas Epidemiologi Mingguan</h3><div class="small">Screening transparan berbasis tren, IR, alert SKDR dan kematian. Bukan model prediksi tervalidasi dan tidak menetapkan KLB otomatis.</div></div><button class="primary" onclick="page('earlyWarning');setTimeout(renderV97EarlyWarning,80)">Buka Early Warning →</button></div><div id="v97DashMini" class="notice" style="margin-top:10px">Memuat indikator…</div>`;d.appendChild(c);const mini=E('v97DashMini');const a=calc();mini.innerHTML=`<b>Score ${a.score}/100 · ${a.level}</b> · ${a.latest} kasus/7 hari · ${a.alert7} alert/7 hari · ${a.pending} spesimen pending.`;}
  const oldPage=window.page;if(oldPage&&!window.__v97PagePatched){window.page=function(id,b){const r=oldPage.apply(this,arguments);if(id==='earlyWarning')setTimeout(render,60);if(id==='dashboard')setTimeout(injectDashboard,100);return r;};window.__v97PagePatched=true;}
  window.GORUT_V97={version:VERSION,features:['transparent early warning score','trend signal','incidence rate signal','SKDR alert burden','mortality signal','response gap dashboard','CSV export','no automatic KLB decision']};
  setTimeout(()=>{try{injectDashboard();populateDisease()}catch(e){}},1000);
})();
