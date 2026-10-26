#!/usr/bin/env python3
"""Static test library validator. Requires only Python 3 stdlib."""
import json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
errors=[]; warnings=[]
def fail(msg): errors.append(msg)
def check(condition,msg):
    if not condition:fail(msg)
def read_json(path):
    try:return json.loads(path.read_text(encoding='utf8'))
    except Exception as e:fail(f'Invalid / missing JSON: {path.relative_to(ROOT)}: {e}');return {}
def exists(path):
    try:return path.is_file() and path.resolve().is_relative_to(ROOT.resolve())
    except:return False
catalog=read_json(ROOT/'data/catalog.json')
check(catalog.get('schemaVersion')==1,'Catalog schemaVersion must equal 1')
check(isinstance(catalog.get('tests'),list),'Catalog tests must be an array')
ids=set(); total_q=0
source=read_json(ROOT/'data/source_extracted.json')
source_questions={q['id']:q for q in source.get('questions',[]) if 'id' in q}
source_passages={p['id']:p for p in source.get('passages',[]) if 'id' in p}
for entry in catalog.get('tests',[]):
    tid=entry.get('id');prefix=str(tid)
    check(isinstance(tid,str) and bool(re.fullmatch('[a-z0-9-]+',tid)),f'Bad test ID: {tid}')
    check(tid not in ids,f'Duplicate test ID: {tid}');ids.add(tid)
    relative=entry.get('path','')
    check(bool(re.fullmatch(r'data/tests/[a-zA-Z0-9-]+\.json',relative)),f'Unsafe or missing path for {tid}')
    path=ROOT/relative
    if not exists(path):fail(f'Missing test file {relative}');continue
    test=read_json(path)
    check(test.get('schemaVersion')==1, f'{tid}: schemaVersion unsupported')
    check(test.get('id')==tid,f'{tid}: file ID differs from catalog ID')
    check(isinstance(test.get('title'),str) and test['title'].strip(),f'{tid}: title missing')
    check(test.get('questionCount')==len(test.get('questions',[]))==entry.get('questionCount'),f'{tid}: question-count mismatch')
    check(test.get('source',{}).get('file'),f'{tid}: missing source document record')
    questions=test.get('questions',[])
    passageIds=set()
    for p in test.get('passages',[]):
        pid=p.get('id');check(pid not in passageIds,f'{tid}: duplicate passage ID {pid}');passageIds.add(pid)
        check(p.get('title') and p.get('original') and p.get('translationId'),f'{tid}: missing passage title / source / translation {pid}')
        if pid in source_passages:check(p.get('original')==source_passages[pid].get('original'),f'{tid}: passage original changed {pid}')
        for key in ['images','assets']:
            for filename in p.get(key,[]):
                check(isinstance(filename,str) and filename.startswith('assets/tests/') and exists(ROOT/filename),f'{tid}: missing or unsafe asset {filename}')
    qids=set(); numbers=set(); graded=0
    for q in questions:
        name=f'{tid} q{q.get("number", "?")}'
        qid=q.get('id');n=q.get('number')
        check(qid not in qids,f'{name}: duplicate question ID {qid}');qids.add(qid)
        check(n not in numbers,f'{name}: duplicate question number {n}');numbers.add(n)
        check(q.get('type') in ('single','multiple','category'),f'{name}: unsupported type {q.get("type")}')
        check(q.get('passageId') in passageIds,f'{name}: missing passage reference {q.get("passageId")}')
        check(bool(q.get('page')) and isinstance(q.get('page'),int),f'{name}: original page absent')
        check(bool(q.get('prompt')),f'{name}: missing prompt')
        check(bool(q.get('explanationId')) and len(q.get('explanationId',''))>=50,f'{name}: missing / too-short explanation')
        check(q.get('answerProvenance') in ('independently-derived','supplied','official','unresolved'),f'{name}: missing key provenance')
        trans=q.get('translationId',{})
        check(bool(trans.get('prompt')),f'{name}: missing prompt translation')
        options=q.get('options',[])
        idsOfOptions=[opt.get('id') for opt in options]
        check(idsOfOptions==list('ABCDE')[:len(options)] and 3<=len(options)<=5,f'{name}: option ids invalid')
        check(bool(all(opt.get('text') for opt in options)),f'{name}: empty option text')
        check(isinstance(trans.get('options'),dict) and set(trans.get('options',{}))==set(idsOfOptions) and all(trans.get('options',{}).values()),f'{name}: translation missing for option')
        check(isinstance(q.get('optionReasonId'),dict) and set(q.get('optionReasonId',{}))==set(idsOfOptions) and all(q.get('optionReasonId',{}).values()),f'{name}: missing per-option reasons')
        if qid in source_questions:
            original=source_questions[qid]
            check(q.get('prompt')==original.get('prompt'),f'{name}: prompt differs from PDF')
            check(q.get('options')==original.get('options'),f'{name}: choices differ from PDF')
            check(q.get('type')==original.get('type'),f'{name}: question type differs from inventory')
        else:
            warnings.append(f'{name}: no baseline text for PDF fidelity comparison (expected for future tests)')
        for ev in q.get('evidence',[]):
            passage=next((p for p in test['passages'] if p['id']==q.get('passageId')),None)
            check(bool(ev.get('quote')) and passage is not None and ev.get('quote','') in passage.get('original',''),f'{name}: evidence is not verbatim in referenced passage')
        check(bool(q.get('evidence')),f'{name}: missing source evidence')
        if q.get('graded'):
            graded+=1
            answer=q.get('answer')
            if q.get('type')=='single':
                check(isinstance(answer,list) and len(answer)==1 and answer[0] in idsOfOptions,f'{name}: invalid single-answer key')
            elif q.get('type')=='multiple':
                check(isinstance(answer,list) and bool(answer) and len(set(answer))==len(answer) and set(answer)<=set(idsOfOptions),f'{name}: invalid multiple-answer key')
                check(q.get('scoring')=='exact-set',f'{name}: incorrect multiple-answer scoring')
            elif q.get('type')=='category':
                categories={c['id'] for c in q.get('categories',[])}
                check(isinstance(answer,dict) and set(answer)==set(idsOfOptions) and set(answer.values())<=categories,f'{name}: invalid category key')
                check(q.get('scoring')=='all-rows-correct',f'{name}: incorrect category scoring')
        else:
            check(q.get('answer') is None and q.get('answerProvenance')=='unresolved',f'{name}: unresolved question must not be gradeable')
            check(bool(q.get('sourceIssue')),f'{name}: unresolved question requires source note')
    check(len(numbers)==len(questions),f'{tid}: duplicate numbering')
    check(entry.get('gradedCount')==graded,f'{tid}: incorrect catalog graded count')
    total_q+=len(questions)
# First test exact inventory, but don't constrain future added tests.
base=next((entry for entry in catalog.get('tests',[]) if entry.get('id')=='tka-eng-to03-elephant-study-labuan-bajo'),None)
if base:
    test=read_json(ROOT/base['path'])
    check([q['number'] for q in test['questions']]==list(range(1,21)),'First test: missing / reordered original question numbers')
    check(len(test['passages'])==5,'First test: expected five original passages')
    check([q['id'] for q in test['questions']]==[q['id'] for q in source.get('questions',[])],'First test: source inventory mismatch')
for name in ['index.html','test.html','results.html','css/style.css','js/home.js','js/test.js','js/results.js','js/scoring.js','js/storage.js','assets/favicon.svg']:
    check(exists(ROOT/name),f'Missing required site file: {name}')
print(f'Validated {len(ids)} tests, {total_q} questions; {len(errors)} errors, {len(warnings)} warnings')
for w in warnings:print('WARNING:',w)
for err in errors:print('ERROR:',err)
sys.exit(1 if errors else 0)
