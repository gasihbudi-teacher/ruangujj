/** Browser-local progress, namespaced separately from all other websites. */
const KEY = 'ruang-uji-progress-v1';
export const SCHEMA_VERSION = 1;
function fresh() { return {schemaVersion:SCHEMA_VERSION, drafts:{}, history:{}}; }
export function readState() {
  try {
    const raw = localStorage.getItem(KEY);
    const obj = raw ? JSON.parse(raw) : fresh();
    if (!obj || obj.schemaVersion !== SCHEMA_VERSION || !obj.drafts || !obj.history || Array.isArray(obj.drafts) || Array.isArray(obj.history)) return fresh();
    return obj;
  } catch { return fresh(); }
}
export function writeState(state) {
  try { localStorage.setItem(KEY, JSON.stringify(state)); return true; } catch { return false; }
}
export function draftKey(testId, mode) { return `${testId}:${mode}`; }
export function getDraft(testId,mode) { return readState().drafts[draftKey(testId,mode)] || null; }
export function setDraft(testId,mode,draft) { const obj=readState(); obj.drafts[draftKey(testId,mode)]=draft; return writeState(obj); }
export function clearDraft(testId,mode) { const obj=readState(); delete obj.drafts[draftKey(testId,mode)]; return writeState(obj); }
export function addAttempt(testId,attempt) { const obj=readState(); if(!Array.isArray(obj.history[testId]))obj.history[testId]=[]; obj.history[testId].unshift(attempt); return writeState(obj); }
export function attempts(testId) { const arr=readState().history[testId]; return Array.isArray(arr)?arr:[]; }
export function getAttempt(testId,id) { return attempts(testId).find(a=>a.id===id) || null; }
export function downloadBackup() {
  const data=JSON.stringify({...readState(),exportedAt:new Date().toISOString(),product:'Ruang Uji'},null,2);
  const blob=new Blob([data],{type:'application/json'}), url=URL.createObjectURL(blob), link=document.createElement('a');
  link.href=url;link.download=`ruang-uji-backup-${new Date().toISOString().slice(0,10)}.json`;link.click();
  setTimeout(()=>URL.revokeObjectURL(url),5000);
}
export function importBackup(text) {
  if (text.length > 8_000_000) throw new Error('Berkas terlalu besar (maksimal 8 MB).');
  let incoming;
  try { incoming=JSON.parse(text); } catch {throw new Error('Berkas bukan JSON yang valid.');}
  if (!incoming || incoming.schemaVersion!==SCHEMA_VERSION || !incoming.drafts || !incoming.history ||
      typeof incoming.drafts!=='object' || Array.isArray(incoming.drafts) || typeof incoming.history!=='object' || Array.isArray(incoming.history)) {
    throw new Error('Versi atau format cadangan tidak sesuai dengan Ruang Uji v1.');
  }
  for(const [id,entry] of Object.entries(incoming.drafts)) {
    if (!/^[a-zA-Z0-9-]+:(practice|test)$/.test(id) || !entry || typeof entry!=='object' || !entry.responses || typeof entry.responses!=='object' || Array.isArray(entry.responses)) throw new Error('Format draf cadangan tidak valid.');
  }
  for(const [id,entries] of Object.entries(incoming.history)) {
    if(!/^[a-zA-Z0-9-]+$/.test(id) || !Array.isArray(entries) || entries.some(a=>!a || typeof a.id!=='string' || !a.responses || typeof a.responses!=='object' || !a.submittedAt)) throw new Error('Riwayat hasil dalam cadangan tidak valid.');
  }
  const base=readState(); let imported=0;
  for(const [k,draft] of Object.entries(incoming.drafts)) {
    if(!(k in base.drafts) || (new Date(draft.updatedAt||0) > new Date(base.drafts[k]?.updatedAt||0))) {base.drafts[k]=draft; imported++;}
  }
  for(const [id,entries] of Object.entries(incoming.history)) {
    if(!Array.isArray(base.history[id])) base.history[id]=[];
    const ids=new Set(base.history[id].map(a=>a.id));
    for(const attempt of entries) if(!ids.has(attempt.id)) {base.history[id].push(attempt);ids.add(attempt.id);imported++;}
    base.history[id].sort((a,b)=>String(b.submittedAt).localeCompare(String(a.submittedAt)));
  }
  if(!writeState(base)) throw new Error('Browser menolak penyimpanan data (kuota atau mode privat).');
  return imported;
}
