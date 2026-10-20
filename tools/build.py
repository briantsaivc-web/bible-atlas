#!/usr/bin/env python3
"""由 /home/claude/bible/work/out 的來源檔合併出 data/*.json（v1）"""
import json,glob,os
R='/home/claude/bible-atlas/'; O='/home/claude/bible/work/out/'
L=lambda f:json.load(open(O+f,encoding='utf-8'))
sl={s['id']:s for s in L('story_list.json')}
ST=[]
for f in sorted(glob.glob(O+'stories_part*.json')):
    d=json.load(open(f,encoding='utf-8')); ST+=d
ST.sort(key=lambda s:sl[s['id']]['n'])
CH=L('characters.json')
cy=L('cycles.json')
COL={'creation':'#4a6fa5','patriarchs':'#b0894a','exodus':'#a8553f','judges':'#6f7f3d','kings':'#7b4a8c','prophets':'#2f5d62','wisdom':'#c2a24a','apocrypha':'#8a6a4f','nativity':'#d0b25a','ministry':'#3d5a8c','parables':'#7d8f4a','passion':'#8c2f3a','resurrection':'#c9a227','acts':'#9a5b32','revelation':'#5b3a7a'}
cycles=[]
for k,v in sorted(cy.items(),key=lambda kv:kv[1]['order']):
    cycles.append({'id':k,'zh':v['zh'],'en':v['en'],'desc':v['desc'],'order':v['order'],'color':COL[k],'count':sum(1 for s in ST if s['cycle']==k)})
A=L('atlas_cands.json')
first={}
for a in A:
    if not a.get('generic') and a['cands']: first.setdefault(a['cands'][0],[]).append(a['id'])
for s in ST:
    s['n']=sl[s['id']]['n']; s['art']=first.get(s['id'],[]); s['art_why']={}
    if s['art']: s['art_provisional']=True
ART=[]
by={s['id']:s for s in ST}
for a in A:
    b={k:v for k,v in a.items() if k!='cands'}
    if not a.get('generic'):
        ch=[]
        for sid in a['cands'][:1]:
            for c in by[sid]['chars']:
                if c not in ch: ch.append(c)
        b['chars']=ch
    else: b['chars']=[]
    ART.append(b)
ids={a['id'] for a in ART}
assert all(x in ids for s in ST for x in s['art'])
os.makedirs(R+'data',exist_ok=True)
J=lambda n,d,**k:json.dump(d,open(R+'data/'+n+'.json','w',encoding='utf-8'),ensure_ascii=False,**k)
J('stories',ST); J('characters',CH); J('artworks',ART)
J('meta',{'version':'v1','updated':'2026-10-20','cycles':cycles,'counts':{'stories':len(ST),'characters':len(CH),'artworks':len(ART)}},indent=1)
print(len(ST),len(CH),len(ART),sum(1 for s in ST if s['art']))
