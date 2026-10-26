import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {isComplete,evaluate,scoreTest,prettyAnswer,officialAnswer} from '../js/scoring.js';
const data=JSON.parse(fs.readFileSync(new URL('../data/tests/tka-eng-to03.json',import.meta.url),'utf8'));
const q=n=>data.questions.find(x=>x.number===n);
test('full inventory 20 questions and source preserved',()=>{assert.equal(data.questions.length,20);assert.equal(data.passages.length,5);assert.deepEqual(data.questions.map(x=>x.number),Array.from({length:20},(_,i)=>i+1));});
test('single-select correct, incorrect, unanswered, unresolved',()=>{assert.equal(evaluate(q(1),'B'),'correct');assert.equal(evaluate(q(1),'A'),'incorrect');assert.equal(evaluate(q(1),undefined),'unanswered');assert.equal(evaluate(q(4),'A'),'unresolved');assert.equal(evaluate(q(5),'D'),'unresolved');});
test('multiple exact set and no partial credit',()=>{assert.equal(evaluate(q(11),['A','B','E']),'correct');assert.equal(evaluate(q(11),['E','A','B']),'correct');assert.equal(evaluate(q(11),['A','B']),'incorrect');assert.equal(evaluate(q(11),['A','B','C','E']),'incorrect');assert.equal(evaluate(q(11),[]),'unanswered');});
test('category requires every row; all-rows-correct scoring',()=>{assert.equal(evaluate(q(18),{A:'Yes',B:'Yes',C:'No'}),'correct');assert.equal(evaluate(q(18),{A:'Yes',B:'No',C:'No'}),'incorrect');assert.equal(evaluate(q(18),{A:'Yes',B:'Yes'}),'unanswered');assert.equal(evaluate(q(19),{A:'No',B:'Yes',C:'Yes'}),'unresolved');assert.equal(isComplete(q(18),{A:'Yes',B:'Yes'}),false);});
test('unanswered gradeable questions count against denominator while unresolved excluded',()=>{const m=scoreTest(data,{});assert.equal(m.gradable,17);assert.equal(m.unresolved,3);assert.equal(m.unanswered,17);assert.equal(m.answered,0);assert.equal(m.percentage,0);});
test('perfect verified set scores 100%, including category questions',()=>{
 const answers=Object.fromEntries(data.questions.filter(x=>x.graded).map(x=>[x.id,x.type==='single'?x.answer[0]:x.type==='multiple'?[...x.answer]:{...x.answer}]));
 const m=scoreTest(data,answers);assert.equal(m.percentage,100);assert.equal(m.correct,17);assert.equal(m.unresolved,3);assert.equal(m.answered,17);
});
test('one incorrect exact-set multi-answer lowers points by exactly one',()=>{
 const answers=Object.fromEntries(data.questions.filter(x=>x.graded).map(x=>[x.id,x.type==='single'?x.answer[0]:x.type==='multiple'?[...x.answer]:{...x.answer}]));
 answers.q11=['A','B'];const m=scoreTest(data,answers);assert.equal(m.correct,16);assert.equal(m.incorrect,1);assert.equal(m.percentage,Math.round(16/17*100));
});
test('current gradeable source issues are documented and not silently replaced',()=>{assert.equal(q(8).options[2].text,q(8).options[4].text);assert.equal(q(10).graded,true);assert.equal(q(4).answer,null);assert.equal(q(19).answer,null);assert.equal(q(20).answer.C,'Yes');});
test('answer labels visible and faithfully summarized',()=>{assert.equal(prettyAnswer(q(11),['B','A','E']),'A, B, E');assert.equal(officialAnswer(q(20)),'A: Ya · B: Tidak · C: Ya');assert.equal(officialAnswer(q(4)),'Belum terverifikasi');});
