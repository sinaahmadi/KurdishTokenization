#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Sina Ahmadi (ahmadi.sina@outlook.com)

"""
	A script to convert Kurdish lexicons in raw text (a lemma per line) into a JSON file suitable for the Kurdish Lnaguage Processing Toolkit
	More information at https://github.com/sinaahmadi/klpt
"""

import sys
sys.path.append('../klpt')
from klpt.transliterator import Transliterator
import json

# transliterator for the Latin to Arabic script for Sorani (ckb)
ckb_trans = Transliterator("Sorani", "Latin", "Arabic")

def create_compounds(s):
	# generate all the possible combinations of the composing subtokens of the compound word
	# - are to be replaced by spaces or removed
	# e.g. pel-û-po -> pel û po, pelû po, pel ûpo, pelûpo
	# e.g. parêz-kirdin -> parêz kirdin, parêzkirdin
    head, _, rest = s.partition('-')
    if len(rest) == 0:
        yield head
    else:
        for c in create_compounds(rest):
            yield f'{head}-{c}'
            yield f'{head} {c}'


lexicon_dir = {"ckb": "/Users/sina/My_GitHub/KurdishTokenization/dicts/lexicon_ckb_latin.lex", "kmr": "/Users/sina/My_GitHub/KurdishTokenization/dicts/lexicon_kmr_latin.lex"}

for dialect in lexicon_dir:
	json_lexicon, json_lexicon_arab = dict(), dict()
	with open(lexicon_dir[dialect]) as f:
		lexicon_enteries = f.read().split("\n") 

	for lemma in lexicon_enteries[6:]:# skip the copyright description
		if "-" not in lemma:
			# no word form to be added
			if dialect == "ckb":
				# Arabic and Latin scripts
				for script in ["arab", "latn"]:
					if script == "arab":
						# transliterate the lemma
						json_lexicon_arab[ckb_trans.transliterate(lemma)] = []
					else:
						json_lexicon[lemma] = []
			else:
				json_lexicon[lemma] = [] 
		else:
			# the lemma is a compound word.
			# Create all the possible compounds and insert as the value of the lemma in the JSON file
			if dialect == "ckb":
				# Arabic and Latin scripts
				for script in ["arab", "latn"]:
					if script == "arab":
						# transliterate the lemma and replace û with w for the sake of correct transliteration to avoid "ئاخرئووئۆخر" or "ئاخرئوو ئۆخر" cases
						trans_lemma = lemma.replace("-û-", "-w-")
						trans_lemma = ckb_trans.transliterate(trans_lemma.replace("-", " ")) # for a correct transliteration
						lemma_forms = [j for j in [i.replace("-", "") for i in create_compounds(trans_lemma.replace(" ", "-"))] if j != trans_lemma.replace(" ", "-")]

						# consider another case for conjuction û where û should be transliterated by وو
						trans_lemma_modified = ckb_trans.transliterate(lemma.replace("-û-", "û-").replace("-", " "))
						lemma_forms.extend([j for j in [i.replace("-", "") for i in create_compounds(trans_lemma_modified.replace(" ", "-"))] if j != trans_lemma_modified.replace(" ", "-")])

						json_lexicon_arab[trans_lemma.replace(" ", "-")] = {"token_forms": list(set(lemma_forms))}
					else:
						# Sorani-Latin
						lemma_forms = [j for j in [i.replace("-", "") for i in create_compounds(lemma)] if j != lemma]
						json_lexicon[lemma] = {"token_forms": lemma_forms}
			else:
				# Kuramanji-Latin
				lemma_forms = [j for j in [i.replace("-", "") for i in create_compounds(lemma)] if j != lemma]
				json_lexicon[lemma] = {"token_forms": lemma_forms}

	# Save JSON files
	if dialect == "ckb":
		with open("/Users/sina/My_GitHub/KurdishTokenization/dicts/lexicon_ckb_latn.json", "w") as f_json:
			json.dump({"Copyright": lexicon_enteries[0:5], "Lexicon": json_lexicon}, f_json, indent=4, sort_keys=True)
		with open("/Users/sina/My_GitHub/KurdishTokenization/dicts/lexicon_ckb_arab.json", "w") as f_json:
			json.dump({"Copyright": lexicon_enteries[0:5], "Lexicon": json_lexicon_arab}, f_json, indent=4, sort_keys=True)
	else:
		with open("/Users/sina/My_GitHub/KurdishTokenization/dicts/lexicon_kmr_latn.json", "w") as f_json:
			json.dump({"Copyright": lexicon_enteries[0:5], "Lexicon": json_lexicon}, f_json, indent=4, sort_keys=True)



# make sure output is saved in UTF-8
# تە'کید-کردنەوە