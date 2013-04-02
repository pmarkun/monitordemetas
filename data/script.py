# -*- coding: utf-8 -*-
from lxml.html import parse
import re
import json
import csvkit

soup =  parse("metasaberto.html").getroot()

metas = []
for m in soup.cssselect("li"):
	meta = {}
	meta['meta_numero'], meta['meta'] = re.search("Meta ([0-9]{1,3}) - (.*)",m.text_content().strip(u"\uf0b7")).groups(1)
	meta['objetivo_numero'], meta['objetivo'] =  re.search("Objetivo ([0-9]{1,2}) - (.*)", m.getparent().getprevious().getprevious().text_content()).groups(1)
	metas.append(meta)

for m in metas:
	m['meta_numero'] = int(m['meta_numero'])
	m['objetivo_numero'] = int(m['objetivo_numero'])
	if m['objetivo_numero'] in range(1,12):
		
		m['eixo_numero'] = 1
		m['eixo'] = u'Compromisso com os direitos sociais e civis'
	elif m['objetivo_numero'] in range(12, 20):
		m['eixo'] = u'Desenvolvimento econômico sustentável com redução das desigualdades'
		m['eixo_numero'] = 2
	elif m['objetivo_numero'] in range(19, 22):
		m['eixo'] = u'Gestão descentralizada, participativa e transparente'
		m['eixo_numero'] = 3

jason = open("metasaberto-sp.json", "w")
jason.write(json.dumps(metas, indent=4, separators=(',', ': ')))
jason.close()

cessev = csvkit.CSVKitDictWriter(open("metasaberto-sp.csv", "w"), metas[0].keys())
cessev.writeheader()
cessev.writerows(metas)