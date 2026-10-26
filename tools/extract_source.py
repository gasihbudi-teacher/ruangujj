#!/usr/bin/env python3
"""Source-preserving PDF extraction; developer utility. Run with the supplied PDF."""
import re,json,sys
from pathlib import Path
import fitz
pdf=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/103 TO 03 TKA ENG (Elephant, Study Session, Labuan Bajo).pdf')
pages=[page.get_text('text') for page in fitz.open(pdf)]
alltext='\n'.join(pages)
sections=list(re.finditer(r'The following text is for questions (\d+)[–-](\d+)\.',alltext))
if len(sections)!=5: raise RuntimeError(f'Expected 5 sections, got {len(sections)}')
def flatten(text):
    return re.sub(r'\s+',' ',text).strip()
def passages(text):
    raw=text.strip()
    paragraphs=re.split(r'\n\s*\n',raw)
    return '\n\n'.join(flatten(t) for t in paragraphs if flatten(t))
records=[]; inv=[]
for secidx,marker in enumerate(sections):
    start,end=map(int,marker.groups())
    chunk=alltext[marker.end():(sections[secidx+1].start() if secidx+1<len(sections) else len(alltext))]
    rx=re.compile(r'(?m)^('+ '|'.join(str(n) for n in range(start,end+1)) + r')\.\s')
    searchable=chunk[chunk.find('6. Based on the information'):] if start==6 else chunk
    offset=len(chunk)-len(searchable)
    qs=list(rx.finditer(searchable))
    if start==6: qs=[type('MatchProxy', (), {'group': (lambda self, n, val=x.group(1): val), 'start': (lambda self, pos=x.start()+offset: pos), 'end': (lambda self,pos=x.end()+offset: pos)})() for x in qs]
    if [int(m.group(1)) for m in qs]!=list(range(start,end+1)):
       raise RuntimeError(f'Question mismatch {start}-{end}: {[m.group(1) for m in qs]}')
    header=chunk[:qs[0].start()].strip()
    ps=re.split(r'\n\s*\n',header, maxsplit=1)
    title=flatten(ps[0]); body=passages(ps[1]) if len(ps)>1 else ''
    pid=f'passage-{secidx+1}'
    records.append({'id':pid,'title':title,'original':body,'originalNumberRange':f'{start}–{end}', 'startPage':alltext[:marker.start()].count('\n')})
    for ix,m in enumerate(qs):
       raw=chunk[m.end():qs[ix+1].start() if ix+1<len(qs) else len(chunk)].strip()
       # Source is parsed by option labels at start of a line (all question types)
       labels=list(re.finditer(r'(?m)^([A-E])\.\s',raw))
       prompt=flatten(raw[:labels[0].start()])
       expected=5 if start<18 else 3
       if len(labels)!=expected:
           raise RuntimeError(f'Question {m.group(1)} options expected {expected}, got {len(labels)}')
       choices=[flatten(raw[mt.end():labels[j+1].start() if j+1<len(labels) else len(raw)]) for j,mt in enumerate(labels)]
       if [x.group(1) for x in labels]!=list('ABCDE'[:expected]): raise RuntimeError('Option labels wrong')
       num=int(m.group(1))
       # Page of question start from overall text
       pos=alltext.find(chunk[m.start():m.end()]+raw[:min(20,len(raw))])
       # Find page using the unique question prefix, constrained to all page text
       page=next((pi+1 for pi,p in enumerate(pages) if (str(num)+'. '+prompt[:15]) in p),None)
       q={'id':f'q{num:02d}', 'number':num,'type':('single' if num<=10 else 'multiple' if num<=17 else 'category'), 'passageId':pid, 'page':page, 'prompt':prompt,'options':[{'id':chr(65+i),'text':txt} for i,txt in enumerate(choices)]}
       records.append(q)
       inv.append({'number':num,'id':q['id'],'page':page,'type':q['type'],'passage':title,'optionCount':len(choices)})
passages_=[x for x in records if 'original' in x]
questions=[x for x in records if 'prompt' in x]
assert len(questions)==20 and len(passages_)==5
out=Path(__file__).parent.parent
(out/'data/source_extracted.json').write_text(json.dumps({'passages':passages_,'questions':questions},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'docs/question-inventory.json').write_text(json.dumps(inv,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('extracted',len(questions),'questions',len(passages_),'passages')
for q in questions:
 print(q['number'],q['page'],q['type'],repr(q['prompt'][:65]),'A:',q['options'][0]['text'][:45])
