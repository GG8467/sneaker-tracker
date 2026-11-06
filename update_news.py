#!/usr/bin/env python3
"""Collect public Google News RSS headlines; not verified release/raffle dates."""
import datetime as dt
import email.utils
import json
import pathlib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parents[1]
QUERIES=[('発売ニュース','NIKE スニーカー 発売日 新作'),('抽選ニュース','NIKE スニーカー 抽選 応募 atmos SNKRS')]
items=[]
seen=set()
for category,query in QUERIES:
    url='https://news.google.com/rss/search?'+urllib.parse.urlencode({'q':query,'hl':'ja','gl':'JP','ceid':'JP:ja'})
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; SneakerTracker/1.0)'})
        with urllib.request.urlopen(req,timeout=20) as response:
            root=ET.fromstring(response.read(2_000_000))
        for node in root.findall('./channel/item')[:20]:
            title=(node.findtext('title') or '').strip()
            link=(node.findtext('link') or '').strip()
            source=(node.findtext('source') or '').strip()
            date=(node.findtext('pubDate') or '').strip()
            if not title or not link or link in seen:continue
            parsed=urllib.parse.urlparse(link)
            if parsed.scheme!='https':continue
            seen.add(link)
            try: published=email.utils.parsedate_to_datetime(date).isoformat()
            except (TypeError,ValueError):published=''
            items.append({'title':title[:240],'url':link,'source':source[:100],'published':published,'category':category})
    except Exception as exc:
        print(f'Could not fetch {category}: {exc}')
if not items:
    raise SystemExit('No new feed results; preserve existing file')
items.sort(key=lambda x:x['published'],reverse=True)
payload={'updated_at':dt.datetime.now(dt.timezone.utc).isoformat(),'items':items[:40]}
(ROOT/'data/news.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Saved',len(payload['items']),'articles')
