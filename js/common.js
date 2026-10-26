export const $=sel=>document.querySelector(sel);
export const escapeHtml=(value='')=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export const paragraphs=(s='')=>String(s).split(/\n\s*\n/).filter(Boolean).map(p=>`<p>${escapeHtml(p).replace(/\n/g,'<br>')}</p>`).join('');
export const urlParam=name=>new URLSearchParams(location.search).get(name);
export async function loadJson(url) { const response=await fetch(url,{cache:'no-cache'}); if(!response.ok)throw new Error(`HTTP ${response.status}: ${url}`);return response.json(); }
export async function loadTest(id) {
  const catalog=await loadJson('data/catalog.json');
  const entry=catalog.tests.find(item=>item.id===id);
  if(!entry || !entry.available)throw new Error('Tes ini tidak tersedia dalam katalog.');
  const test=await loadJson(entry.path);
  if(test.id!==id || test.schemaVersion!==1)throw new Error('Data tes tidak sesuai katalog / versi skema.');
  return test;
}
export const labelMode=m=>m==='practice'?'Mode Latihan':'Mode Tes';
export const responseSummary=(n,total)=>`${n} dari ${total} soal terjawab`;
export function passageDisplay(p,showTranslation=false) {return `<div class="passage-copy">${paragraphs(showTranslation?p.translationId:p.original)}</div>`;}
export function niceDate(text) {try{return new Date(text).toLocaleString('id-ID',{dateStyle:'medium',timeStyle:'short'});}catch{return text;}}
