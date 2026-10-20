# 聖經故事大全

副標：西洋繪畫與雕刻裡的聖經。365 則故事（舊約／次經／新約，15 個篇章）、264 位人物與關係圖、以及「看圖找故事」作品牆。看到一幅畫或一件雕刻，就能找到它背後的聖經故事。

靜態站（GitHub Pages），單頁應用、hash 路由，資料全在 `data/`。與「西洋藝術流派大全集」「西洋雕刻演進大全集」「希臘神話大全集」同架構。

## 結構
```
index.html            單頁應用：#home／#stories/<篇章>／#story/<id>／#chars/<類別>／#char/<id>／#graph/<id>／#gallery
lib/d3.min.js         d3（人物關係圖）
data/stories.json     365 則故事
data/characters.json  264 位人物（物件，key 為 id）
data/relations.json   由 characters 推導的關係邊
data/artworks.json    作品（繪畫與雕刻）
data/meta.json        版本、15 個篇章（含色碼）、計數
tools/build.py        由來源檔合併出 data/*.json
tools/relations.py    由 characters.json 重建 relations.json 與 meta.counts
```

## 資料欄位
- stories：`id, n, title, en, book, cycle, canon(ot/nt/apoc), chars[], hook, sections[{h,p[]}], ending, moral, summary, scripture(經文出處), context(背景), in_art(在藝術中如何辨認), art[](作品 id), art_why{}, art_provisional`
  - `art_provisional:true` 表示配圖為暫定（取候選清單第一個故事），之後會逐件精篩覆蓋。
- characters：`zh, en, cat, bio, parents, spouses, children, siblings, mentor_of, killed, killed_by, note`（關係欄位雙向）。
- relations：`s, t, k`，k 為 父母／配偶／手足／殺害／師徒。
- artworks：`id, site(p 繪畫／s 雕刻), wid, a, a_zh, t, z, y, mu, mat, img, thumb, src_url, wd_flag, kind, chars[], generic`。`generic:true` 為聖母、聖人、基督像等未對應單一故事的作品，由題名規則分類為 聖母與聖嬰／聖家族／聖人／基督像／聖殤。

## 資料來源與授權
- 故事、人物、篇章為本站撰寫。
- 圖檔取自姊妹站「西洋藝術流派大全集」「西洋雕刻演進大全集」，原圖皆為 Wikimedia Commons 公共領域作品，來源頁可從大圖視窗連回。
