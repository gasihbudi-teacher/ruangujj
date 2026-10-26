import test from 'node:test';
import assert from 'node:assert/strict';
import {SCHEMA_VERSION,readState,writeState,setDraft,getDraft,clearDraft,addAttempt,attempts,importBackup} from '../js/storage.js';
const memory=new Map();
globalThis.localStorage={getItem:key=>memory.has(key)?memory.get(key):null,setItem:(key,val)=>memory.set(key,val),removeItem:key=>memory.delete(key)};
function reset(){memory.clear();}
test('progress starts empty and uses v1 schema',()=>{reset();assert.deepEqual(readState(),{schemaVersion:SCHEMA_VERSION,drafts:{},history:{}});});
test('save and reload a draft separately per mode',()=>{
 reset();setDraft('example','practice',{responses:{q01:'B'},updatedAt:'2026-10-01'});
 setDraft('example','test',{responses:{q01:'A'},updatedAt:'2026-10-02'});
 assert.equal(getDraft('example','practice').responses.q01,'B');
 assert.equal(getDraft('example','test').responses.q01,'A');
 clearDraft('example','practice');assert.equal(getDraft('example','practice'),null);
 assert.equal(getDraft('example','test').responses.q01,'A');
});
test('addAttempt retains history and import merges without duplication',()=>{
 reset();addAttempt('example',{id:'original',submittedAt:'2026-10-01',responses:{q01:'B'}});
 const backup={schemaVersion:1,drafts:{'example:practice':{updatedAt:'2026-10-03',responses:{q01:'A'}}},history:{example:[{id:'original',submittedAt:'2026-10-01',responses:{q01:'B'}},{id:'new',submittedAt:'2026-10-02',responses:{q01:'A'}}]}};
 assert.equal(importBackup(JSON.stringify(backup)),2);
 assert.equal(attempts('example').length,2);
 assert.equal(attempts('example')[0].id,'new');
 assert.equal(importBackup(JSON.stringify(backup)),0);
 assert.equal(attempts('example').length,2);
});
test('import rejects incompatible and broken shape without data loss',()=>{
 reset();addAttempt('example',{id:'stored',submittedAt:'2026-10-01',responses:{}});
 assert.throws(()=>importBackup('{}'),/format/);
 assert.throws(()=>importBackup('{not json'),/JSON/);
 assert.throws(()=>importBackup(JSON.stringify({schemaVersion:3,drafts:{},history:{}})),/Versi/);
 assert.throws(()=>importBackup(JSON.stringify({schemaVersion:1,drafts:{},history:{'not allowed!':[]}})),/valid/);
 assert.equal(attempts('example').length,1);
});
