#!/usr/bin/env python3
"""由 data/characters.json 重建 data/relations.json 並更新 meta.counts"""
import json
R='/home/claude/bible-atlas/'
C=json.load(open(R+'data/characters.json',encoding='utf-8'))
REL=[]; seen=set()
def add(a,b,k):
    key=(min(a,b),max(a,b),k) if k in('配偶','手足') else (a,b,k)
    if key in seen or a not in C or b not in C or a==b: return
    seen.add(key); REL.append({'s':a,'t':b,'k':k})
for cid,c in C.items():
    for p in c.get('parents') or []: add(p,cid,'父母')
    for p in c.get('children') or []: add(cid,p,'父母')
    for p in c.get('spouses') or []: add(cid,p,'配偶')
    for p in c.get('siblings') or []: add(cid,p,'手足')
    for p in c.get('killed') or []: add(cid,p,'殺害')
    for p in c.get('killed_by') or []: add(p,cid,'殺害')
    for p in c.get('mentor_of') or []: add(cid,p,'師徒')
json.dump(REL,open(R+'data/relations.json','w',encoding='utf-8'),ensure_ascii=False)
m=json.load(open(R+'data/meta.json',encoding='utf-8')); m['counts']['relations']=len(REL); m['counts']['characters']=len(C); m['counts']['artworks']=len(json.load(open(R+'data/artworks.json',encoding='utf-8')))
json.dump(m,open(R+'data/meta.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('relations',len(REL))
