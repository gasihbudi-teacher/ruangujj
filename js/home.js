import {loadJson,escapeHtml,$} from './common.js';
import {readState,downloadBackup,importBackup} from './storage.js';
let catalog=[];
function statusFor(id) {
  const state=readState(); const done=Array.isArray(state.history[id]) && state.history[id].length;
  const started=['practice','test'].some(mode=>{const d=state.drafts[`${id}:${mode}`];return d && Object.keys(d.responses||{}).length;});
  return done?'done':started?'started':'new';
}
function card(t) {
  const state=readState(), entries=state.history[t.id]||[], status=statusFor(t.id), draft=state.drafts[`${t.id}:practice`]||state.drafts[`${t.id}:test`];
  const phrases={new:'Belum dikerjakan',started:'Ada jawaban tersimpan',done:'Pernah selesai'};
  const meta=[t.exam,t.subject,`${t.questionCount} soal`,t.year||'Tahun tidak diketahui'].filter(Boolean);
  return `<article class="test-card"><div class="card-rail"><span class="pill">${escapeHtml(t.badge||'LATIHAN')}</span><span class="card-arrow" aria-hidden="true">↗</span></div><div class="card-icon" aria-hidden="true">A<span>✓</span></div><p class="overline">${escapeHtml(t.subject)}</p><h3>${escapeHtml(t.title)}</h3><p class="card-desc">${escapeHtml(t.subtitle||'')}</p><div class="tag-row">${meta.map(x=>`<span>${escapeHtml(x)}</span>`).join('')}</div><p class="card-status ${status}"><span class="status-dot"></span>${phrases[status]}${entries.length?` · ${entries.length} riwayat`:''}</p><div class="card-footer"><a class="button primary" href="test.html?id=${encodeURIComponent(t.id)}&mode=practice">${draft?'Lanjut / latihan':'Mulai latihan'} ↗</a><a class="text-link" href="test.html?id=${encodeURIComponent(t.id)}&mode=test">Mode Tes →</a></div>${entries.length?`<a class="results-link" href="results.html?id=${encodeURIComponent(t.id)}">Lihat hasil terakhir · ${entries[0].metrics?.percentage??'—'}%</a>`:''}<p class="card-disclaimer">${escapeHtml(t.verification)}</p></article>`;
}
function render() {
  const text=$('#search').value.toLocaleLowerCase('id'),filter=$('#status-filter').value;
  const filtered=catalog.filter(t=>`${t.title} ${t.subtitle} ${t.subject} ${t.exam} ${(t.topics||[]).join(' ')}`.toLocaleLowerCase('id').includes(text) && (filter==='all'||statusFor(t.id)===filter));
  $('#catalog').innerHTML=filtered.length?filtered.map(card).join(''):'<div class="empty-state"><h3>Tidak ada tes yang cocok</h3><p>Coba kata kunci lain atau pilih “Semua status”.</p></div>';
  $('#test-count').textContent=`${filtered.length} dari ${catalog.length} tes`;
}
async function init() {
  try {const data=await loadJson('data/catalog.json');catalog=data.tests.filter(x=>x.available);render();}
  catch(e){$('#catalog').innerHTML=`<p class="error-banner">Katalog tidak dapat dimuat: ${escapeHtml(e.message)}. Buka situs melalui server HTTP, bukan langsung lewat file://.</p>`;}
  $('#search').addEventListener('input',render);$('#status-filter').addEventListener('change',render);
  $('#export-backup').addEventListener('click',downloadBackup);
  $('#import-backup').addEventListener('change',async e=>{
    const f=e.target.files[0]; if(!f)return;
    try{const count=importBackup(await f.text());$('#backup-feedback').textContent=`Cadangan berhasil diimpor: ${count} data baru / diperbarui.`;render();}
    catch(err){$('#backup-feedback').textContent=`Impor gagal: ${err.message}`;}
    e.target.value='';
  });
  try{localStorage.setItem('ruang-uji-storage-check','ok');localStorage.removeItem('ruang-uji-storage-check');}
  catch{$('#storage-status').textContent='⚠ Penyimpanan browser tidak tersedia; progres tidak akan bertahan setelah halaman ditutup.';}
}
init();
