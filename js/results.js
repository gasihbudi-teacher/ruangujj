import {escapeHtml,paragraphs,loadTest,urlParam,$,niceDate} from './common.js';
import {scoreTest,evaluate,prettyAnswer,officialAnswer} from './scoring.js';
import {attempts,getAttempt,downloadBackup} from './storage.js';
let test,attempt,filter='all';
const terms={correct:'Benar',incorrect:'Perlu dipelajari',unanswered:'Belum dijawab',unresolved:'Belum dapat dinilai'};
function optionReview(q,answer){
  return q.options.map(o=>{
    const selected=q.type==='single'?answer===o.id:q.type==='multiple'?Array.isArray(answer)&&answer.includes(o.id):answer?.[o.id];
    const correct=q.graded?(q.type==='category'?q.answer[o.id]:q.answer.includes(o.id)):null;
    const label=q.type==='category'?`Pilihanmu: ${selected===undefined?'kosong':selected==='Yes'?'Ya':'Tidak'}${correct!=null?` · Rujukan: ${correct==='Yes'?'Ya':'Tidak'}`:''}`:selected?'Kamu pilih ini':'';
    const marked=q.graded&&(q.type==='category'?selected===correct:(selected && correct));
    const wrong=q.graded&&(q.type==='category'?selected!==correct:(selected&&!correct));
    return `<div class="review-option ${marked?'right':wrong?'wrong':''}"><div class="review-option-top"><strong>${o.id}.</strong><div><p>${escapeHtml(o.text)}</p><p class="review-translation">${escapeHtml(q.translationId.options[o.id])}</p>${label?`<span class="mini-tag">${escapeHtml(label)}</span>`:''}</div>${marked?'<b class="opt-marker">✓</b>':wrong?'<b class="opt-marker">✕</b>':''}</div><p class="review-reason">${escapeHtml(q.optionReasonId[o.id])}</p></div>`;
  }).join('');
}
function reviewCard(q) {
  const value=attempt.responses[q.id], status=evaluate(q,value), passage=test.passages.find(p=>p.id===q.passageId);
  const badge=status==='correct'?'is-correct':status==='unresolved'?'is-unresolved':'is-wrong';
  return `<article class="review-card" data-status="${status}"><details ${status==='incorrect'?'open':''}><summary><span class="review-num">${String(q.number).padStart(2,'0')}</span><span class="review-question-title">${escapeHtml(q.prompt)}<small>${escapeHtml(passage.title)} · sumber hlm. ${q.page}</small></span><span class="status-label ${badge}">${terms[status]}</span><span class="expander">⌄</span></summary><div class="review-body"><div class="review-answer-grid"><div><p class="overline">JAWABANMU</p><strong>${escapeHtml(prettyAnswer(q,value))}</strong></div><div><p class="overline">RUJUKAN (BUKAN KUNCI RESMI)</p><strong>${escapeHtml(officialAnswer(q))}</strong></div></div><div class="explanation-panel"><p class="overline">PEMBAHASAN BAHASA INDONESIA</p><p>${escapeHtml(q.explanationId)}</p>${q.sourceIssue?`<div class="source-issue"><strong>Catatan editorial</strong><p>${escapeHtml(q.sourceIssue)}</p></div>`:''}</div><div class="review-subheading">Pilihan dan penjelasan</div>${optionReview(q,value)}<div class="evidence-panel"><h4>Bukti dari bacaan</h4>${q.evidence.map(e=>`<blockquote>${escapeHtml(e.quote)}</blockquote>`).join('')}<p class="small-note">Kutipan berasal dari teks asli. Penarikan kesimpulan dijelaskan dalam pembahasan, bukan bagian dari kutipan.</p></div><details class="reading-expansion"><summary>Lihat teks bacaan utuh & terjemahan Indonesia</summary><div class="reading-expansion-columns"><div><h4>${escapeHtml(passage.title)} · English</h4>${paragraphs(passage.original)}</div><div><h4>Terjemahan bahasa Indonesia</h4>${paragraphs(passage.translationId)}</div></div></details>${q.vocabulary?.length?`<details class="vocabulary-expansion"><summary>Kosakata pendukung (${q.vocabulary.length})</summary>${q.vocabulary.map(([a,b])=>`<p><b>${escapeHtml(a)}</b> — ${escapeHtml(b)}</p>`).join('')}</details>`:''}</div></details></article>`;
}
function renderReview(){
 const items=test.questions.filter(q=>{
   const s=evaluate(q,attempt.responses[q.id]);
   if(filter==='incorrect')return s==='incorrect'||s==='unanswered';
   if(filter==='unresolved')return s==='unresolved';
   return true;
 });
 $('#review-list').innerHTML=items.length?items.map(reviewCard).join(''):'<p class="empty-state">Tidak ada soal pada kategori ini. Bagus!</p>';
}
async function init(){
 try {
  const id=urlParam('id');if(!id)throw new Error('ID tes belum tersedia.');
  test=await loadTest(id);
  const attemptId=urlParam('attempt'); attempt=attemptId?getAttempt(id,attemptId):attempts(id)[0];
  if(!attempt)throw new Error('Hasil tidak ditemukan di browser ini. Riwayat disimpan secara lokal; impor cadangan dari perangkat lama jika tersedia.');
  const metrics=attempt.metrics||scoreTest(test,attempt.responses);
  document.title=`Hasil ${test.title} — Ruang Uji`;
  $('#results-error').classList.add('hidden');$('#results-content').classList.remove('hidden');
  $('#results-title').textContent=test.title;
  $('#score-value').textContent=metrics.percentage==null?'—':`${metrics.percentage}%`;
  $('#score-headline').textContent=`${metrics.correct} dari ${metrics.gradable} soal bernilai dijawab benar`;
  $('#score-detail').textContent=`${metrics.answered} dari ${metrics.total} soal dijawab · ${niceDate(attempt.submittedAt)} · ${attempt.mode==='practice'?'Mode Latihan':'Mode Tes'}`;
  $('#metric-correct').textContent=metrics.correct;
  $('#metric-wrong').textContent=metrics.incorrect+metrics.unanswered;
  $('#metric-unresolved').textContent=metrics.unresolved;
  if(attempt.contentRevision!==test.contentRevision){
    const flag=document.createElement('div');flag.className='notice';flag.textContent='⚠ Data konten telah diperbarui sejak hasil ini disimpan. Skor di atas adalah skor saat pengerjaan; pembahasan di bawah mengikuti konten saat ini.';document.querySelector('.results-actions').before(flag);
  }
  $('#retake-link').href=`test.html?id=${encodeURIComponent(id)}&mode=${attempt.mode==='test'?'test':'practice'}`;
  $('#export-from-results').addEventListener('click',downloadBackup);
  document.querySelectorAll('.review-filters button').forEach(btn=>btn.addEventListener('click',()=>{
    filter=btn.dataset.filter;document.querySelectorAll('.review-filters button').forEach(b=>{b.classList.toggle('active',b===btn);b.setAttribute('aria-pressed',String(b===btn));});renderReview();
  }));renderReview();
 }catch(e){$('#results-error').className='error-banner';$('#results-error').innerHTML=`Tidak dapat membuka hasil: ${escapeHtml(e.message)} <a href="index.html">Kembali ke koleksi</a>`;}
}
init();
