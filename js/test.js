import {escapeHtml,paragraphs,loadTest,urlParam,$,passageDisplay} from './common.js';
import {isComplete,evaluate,scoreTest,officialAnswer} from './scoring.js';
import {getDraft,setDraft,clearDraft,addAttempt} from './storage.js';
let test, mode, responses={}, checked=[], index=0, timerSeconds=0, timerLive=false, timerHandle;
const byId=id=>document.getElementById(id);
function activeQuestion(){return test.questions[index];}
function save(){return setDraft(test.id,mode,{responses,checked,index,timerSeconds,updatedAt:new Date().toISOString(),contentRevision:test.contentRevision});}
function setSaveMessage(ok){byId('autosave-msg').textContent=ok?'Tersimpan otomatis di perangkat ini.':'⚠ Penyimpanan lokal tidak tersedia. Cadangkan data bila memungkinkan.';}
function toggleTimer(){timerLive=!timerLive;byId('timer-button').setAttribute('aria-pressed',String(timerLive));renderTimer();if(timerLive) timerHandle=setInterval(()=>{timerSeconds++;renderTimer();if(timerSeconds%10===0)save();},1000);else{clearInterval(timerHandle);save();}}
function renderTimer(){const mm=String(Math.floor(timerSeconds/60)).padStart(2,'0'),ss=String(timerSeconds%60).padStart(2,'0');byId('timer-button').textContent=timerLive?`◷ Stopwatch opsional: ${mm}:${ss} · jeda`:`◷ Stopwatch opsional: ${timerSeconds?`${mm}:${ss} · lanjut`:'mati'}`;}
function renderPassage(){
  const p=test.passages.find(x=>x.id===activeQuestion().passageId);
  byId('passage-title').textContent=p.title;
  byId('passage-span').textContent=`Soal ${p.originalNumberRange} · sumber hlm. ${p.page}`;
  const savedScroll=byId('passage-body').scrollTop;
  byId('passage-body').innerHTML=passageDisplay(p);
  if(mode==='practice') byId('passage-controls').innerHTML=`<details class="passage-translation"><summary>🌐 Terjemahan bacaan (Indonesia)</summary>${passageDisplay(p,true)}</details>`;
  else byId('passage-controls').innerHTML='<p class="small-note">Terjemahan lengkap tersedia saat meninjau hasil.</p>';
  byId('passage-body').scrollTop=savedScroll;
  byId('dialog-passage-title').textContent=p.title;
  byId('dialog-passage-body').innerHTML=passageDisplay(p)+(mode==='practice'?`<details class="passage-translation"><summary>🌐 Tampilkan terjemahan Indonesia</summary>${passageDisplay(p,true)}</details>`:'');
}
function optionsHtml(q){
  const value=responses[q.id];
  if(q.type==='category') return q.options.map(row=>`<fieldset class="category-row"><legend><span class="option-label">${row.id}.</span> ${escapeHtml(row.text)}</legend><div class="category-choices">${q.categories.map(c=>`<label class="category-choice"><input type="radio" name="${q.id}-${row.id}" value="${c.id}" data-row="${row.id}" ${value?.[row.id]===c.id?'checked':''}><span>${escapeHtml(c.label)}</span></label>`).join('')}</div>${mode==='practice'?`<details class="inline-translation"><summary>Terjemahkan pernyataan ${row.id}</summary><p>${escapeHtml(q.translationId.options[row.id])}</p></details>`:''}</fieldset>`).join('');
  return q.options.map(opt=>`<label class="answer-option"><input type="${q.type==='single'?'radio':'checkbox'}" name="answer" value="${opt.id}" ${(q.type==='single'&&value===opt.id)||(q.type==='multiple'&&Array.isArray(value)&&value.includes(opt.id))?'checked':''}><span class="option-letter">${opt.id}</span><span class="option-text">${escapeHtml(opt.text)}${mode==='practice'?`<small class="option-translation" hidden>${escapeHtml(q.translationId.options[opt.id])}</small>`:''}</span><span class="option-check" aria-hidden="true"></span></label>`).join('');
}
function renderFeedback(q){
 const root=byId('practice-feedback');root.innerHTML='';
 if(mode!=='practice'||!checked.includes(q.id))return;
 const state=evaluate(q,responses[q.id]);
 const icon=state==='correct'?'✓':state==='unresolved'?'?':'✕', heading=state==='correct'?'Tepat!':state==='unresolved'?'Kunci belum pasti':'Yuk, pelajari alasannya';
 root.innerHTML=`<div class="feedback-box ${state}"><div class="feedback-heading"><strong>${icon} ${heading}</strong><span>${state==='unresolved'?'Tidak dinilai':`Jawaban rujukan: ${escapeHtml(officialAnswer(q))}`}</span></div><p>${escapeHtml(q.explanationId)}</p>${q.sourceIssue?`<p class="issue-text"><b>Catatan sumber:</b> ${escapeHtml(q.sourceIssue)}</p>`:''}<details><summary>Lihat bukti bacaan & alasan tiap opsi</summary><div class="evidence-items">${q.evidence.map(e=>`<blockquote>${escapeHtml(e.quote)}</blockquote>`).join('')}</div>${q.options.map(o=>`<p><b>${o.id}.</b> ${escapeHtml(q.optionReasonId[o.id])}</p>`).join('')}</details></div>`;
}
function renderQuestion(){
 const q=activeQuestion();
 byId('q-number').textContent=`SOAL ${String(q.number).padStart(2,'0')} / ${test.questionCount}`;
 const typelabel={single:'PILIH SATU',multiple:'PILIH SEMUA YANG BENAR',category:'PILIH YA / TIDAK PER BARIS'};
 byId('q-type').textContent=typelabel[q.type];
 byId('q-heading').textContent=q.prompt;
 byId('q-translation').innerHTML=mode==='practice'?`<details class="inline-translation question-translation"><summary>🌐 Terjemahkan pertanyaan & pilihan</summary><p>${escapeHtml(q.translationId.prompt)}</p>${q.type!=='category'?'<p class="small-note">Terjemahan setiap opsi dapat ditampilkan lewat tombol di bawah.</p><button type="button" class="small-button" id="toggle-option-translations">Tampilkan terjemahan opsi</button>':''}</details>`:'';
 byId('options').innerHTML=optionsHtml(q);

 const toggle=byId('toggle-option-translations');
 if(toggle)toggle.addEventListener('click',()=>{const elems=document.querySelectorAll('.option-translation');const newState=elems[0]?.hidden;elems.forEach(x=>x.hidden=!newState);toggle.textContent=newState?'Sembunyikan terjemahan opsi':'Tampilkan terjemahan opsi';});
 byId('check-answer').classList.toggle('hidden',mode!=='practice');
 byId('check-answer').disabled=!isComplete(q,responses[q.id]) || checked.includes(q.id);
 byId('check-answer').textContent=checked.includes(q.id)?'Sudah diperiksa ✓':'Periksa jawaban';
 renderFeedback(q);renderPassage();renderNavigation();
 byId('prev-q').disabled=index===0;
 byId('next-q').textContent=index===test.questions.length-1?'Kembali ke soal 1 ↺':'Berikutnya →';
 if(window.matchMedia('(max-width: 960px)').matches){byId('question-area').scrollIntoView({behavior:'instant',block:'start'});}
}
function handleChange(e){
 const q=activeQuestion();
 if(q.type==='single') responses[q.id]=e.target.value;
 else if(q.type==='multiple') responses[q.id]=[...document.querySelectorAll('#options input:checked')].map(x=>x.value);
 else {responses[q.id]=responses[q.id]&&typeof responses[q.id]==='object'?{...responses[q.id]}:{};responses[q.id][e.target.dataset.row]=e.target.value;}
 checked=checked.filter(x=>x!==q.id);
 setSaveMessage(save());
 byId('check-answer').disabled=!isComplete(q,responses[q.id]);
 byId('check-answer').textContent='Periksa jawaban';
 byId('practice-feedback').innerHTML='';
 renderNavigation();
}
function renderNavigation(){
 const complete=test.questions.filter(q=>isComplete(q,responses[q.id])).length;
 byId('progress-text').textContent=`${complete} dari ${test.questionCount} soal dijawab`;
 byId('progress-percent').textContent=`${Math.round(complete/test.questionCount*100)}% terisi`;
 byId('progress-fill').style.width=`${complete/test.questionCount*100}%`;
 byId('nav-numbers').innerHTML=test.questions.map((q,i)=>{
  const has=isComplete(q,responses[q.id]);return `<button type="button" class="nav-num ${has?'answered':''} ${i===index?'current':''}" data-index="${i}" ${i===index?'aria-current="step"':''} aria-label="Soal ${q.number}: ${has?'terjawab':'belum lengkap'}${i===index?', aktif':''}">${q.number}</button>`;
 }).join('');
 byId('nav-numbers').querySelectorAll('button').forEach(el=>el.addEventListener('click',()=>go(Number(el.dataset.index))));
}
function go(n){index=(n+test.questions.length)%test.questions.length;save();renderQuestion();}
function modal(show){byId('confirm-modal').classList.toggle('hidden',!show);if(show)byId('cancel-submit').focus();}
function beginSubmit(){
 const left=test.questions.filter(q=>!isComplete(q,responses[q.id])).length;
 byId('modal-desc').textContent=`${left?`${left} soal masih belum terjawab lengkap. `:''}Jawaban kosong pada soal yang dinilai akan dihitung belum benar. ${test.questions.filter(q=>!q.graded).length} soal berkunci belum pasti dikecualikan dari nilai. Lanjutkan?`;
 modal(true);
}
function finish(){
 const metrics=scoreTest(test,responses);
 const attempt={id:`${Date.now()}-${Math.random().toString(36).slice(2,10)}`, testId:test.id,mode,contentRevision:test.contentRevision,submittedAt:new Date().toISOString(),responses:JSON.parse(JSON.stringify(responses)),metrics};
 if(!addAttempt(test.id,attempt)) {alert('Penyimpanan lokal tidak tersedia. Hasil masih dapat dilihat, tetapi riwayat mungkin hilang setelah keluar.');}
 clearDraft(test.id,mode);clearInterval(timerHandle);
 window.location.href=`results.html?id=${encodeURIComponent(test.id)}&attempt=${encodeURIComponent(attempt.id)}`;
}
async function init(){
 try{
  const id=urlParam('id'),rawMode=urlParam('mode');mode=rawMode==='test'?'test':'practice';
  if(!id)throw new Error('ID tes belum diberikan. Pilih tes dari halaman koleksi.');
  test=await loadTest(id);
  document.title=`${test.title} — Ruang Uji`;
  byId('test-title').textContent=test.title;byId('test-subtitle').textContent=test.subtitle;
  byId('test-kicker').textContent=`${test.subject} · ${test.questionCount} soal · ${test.passages.length} bacaan`;
  byId('mode-label').textContent=mode==='practice'?'Mode Latihan':'Mode Tes';
  byId('test-mode-tag').textContent=mode==='practice'?'LATIHAN · TANPA BATAS WAKTU':'TES · JAWABAN DISEMBUNYIKAN';
  const draft=getDraft(test.id,mode);
  if(draft){responses=draft.responses||{};checked=mode==='practice'?(draft.checked||[]):[];index=Math.max(0,Math.min(test.questions.length-1,Number(draft.index)||0));timerSeconds=Number(draft.timerSeconds)||0;}
  byId('test-app').classList.remove('hidden');
  byId('check-answer').addEventListener('click',()=>{const q=activeQuestion();if(!isComplete(q,responses[q.id]))return;checked.push(q.id);save();renderQuestion();});
  byId('prev-q').addEventListener('click',()=>go(index-1));byId('next-q').addEventListener('click',()=>go(index+1));
  byId('submit-test').addEventListener('click',beginSubmit);
  byId('cancel-submit').addEventListener('click',()=>modal(false));byId('confirm-submit').addEventListener('click',finish);
  byId('confirm-modal').addEventListener('click',e=>{if(e.target===byId('confirm-modal'))modal(false);});
  document.addEventListener('keydown',e=>{if(e.key==='Escape')modal(false);});
  byId('timer-button').addEventListener('click',toggleTimer);
  byId('options').addEventListener('change',handleChange);
  byId('open-passage').addEventListener('click',()=>byId('passage-dialog').showModal());
  byId('close-passage').addEventListener('click',()=>byId('passage-dialog').close());
  renderTimer();renderQuestion();
 }catch(err){byId('app-error').className='error-banner';byId('app-error').innerHTML=`Gagal memuat tes: ${escapeHtml(err.message)}. <a href="index.html">Kembali ke koleksi</a>.`}
}
init();
