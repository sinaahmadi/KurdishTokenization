# -*- coding: utf-8 -*-
# August 4, 2020 - Sina Ahmadi

from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import corpus_bleu
import json


def create_MWE_lexicons():
	# extract MWE from the two lexicons and save them
	MWE_ckb, MWE_kmr = list(), list()
	with open("dicts/lexicon_ckb_arab.json", "r") as f:
		for headword in json.load(f)["Lexicon"]:
			if "-" in headword:
				MWE_ckb.append(headword)

	with open("dicts/lexicon_kmr_latn.json", "r") as f:
		for headword in json.load(f)["Lexicon"]:
			if "-" in headword:
				MWE_kmr.append(headword)

	with open("dicts/lexicon_ckb_arab_MWE.lex", "w") as fw:
		fw.write("\n".join(MWE_ckb))

	with open("dicts/lexicon_kmr_latn_MWE.lex", "w") as fw:
		fw.write("\n".join(MWE_kmr))

def calculate_accuracy(reference_tokens, candidate_tokens):
	# Number of identical tokens in the reference and candidate divided by the whole number of tokens in the reference
	all_matches, all_tokens = 0, 0
	for i in range(len(reference_tokens)):
		all_matches += sum(x == y for x, y in zip(reference_tokens[i].split(), candidate_tokens[i].split()))
		all_tokens += len(reference_tokens[i].split())
	return all_matches * 100 / all_tokens


def calculate_MWE_accuracy(reference_tokens, candidate_tokens):
	# Number of "exact" matches between reference MWEs and the candidates
	all_matches, all_tokens = 0, 0
	for i in range(len(reference_tokens)):
		if reference_tokens[i] == candidate_tokens[i]:
			all_matches += 1

	return all_matches * 100 / len(reference_tokens)


gold_standard_files = {"ckb": "data/annotated_corpus_ckb.txt",
						"kmr": "data/annotated_copus_kmr.txt"}

gold_standard_mwe_files = {"ckb": "data/lexicon_ckb_arab_MWE.lex",
							"kmr": "data/lexicon_kmr_latn_MWE.lex"}

model_outputs = {
	"ckb": [
		"experiments/ckb/ckb_sentences_ckb_bpe_4000.txt", 
		"experiments/ckb/ckb_sentences_ckb_bpe_8000.txt", 
		"experiments/ckb/ckb_sentences_ckb_bpe_16000.txt", 
		"experiments/ckb/ckb_sentences_ckb_bpe_32000.txt", 
		"experiments/ckb/ckb_sentences_ckb_unigram_4000.txt", 
		"experiments/ckb/ckb_sentences_ckb_unigram_8000.txt", 
		"experiments/ckb/ckb_sentences_ckb_unigram_16000.txt", 
		"experiments/ckb/ckb_sentences_ckb_unigram_32000.txt", 
		"experiments/ckb/ckb_sentences_ckb_word_4000.txt", 
		"experiments/ckb/ckb_sentences_ckb_word_8000.txt", 
		"experiments/ckb/ckb_sentences_ckb_word_16000.txt", 
		"experiments/ckb/ckb_sentences_ckb_word_32000.txt", 
		"experiments/ckb/ckb_sentences_ckb_wordpiece_4000.txt", 
		"experiments/ckb/ckb_sentences_ckb_wordpiece_8000.txt", 
		"experiments/ckb/ckb_sentences_ckb_wordpiece_16000.txt", 
		"experiments/ckb/ckb_sentences_ckb_wordpiece_32000.txt", 
		"experiments/ckb/ckb_sentences_WordPunct.txt",
		"experiments/ckb_sentences_klpt.txt"
	],
	"kmr": [
		"experiments/kmr/kmr_sentences_kmr_bpe_4000.txt", 
		"experiments/kmr/kmr_sentences_kmr_bpe_8000.txt", 
		"experiments/kmr/kmr_sentences_kmr_bpe_16000.txt", 
		"experiments/kmr/kmr_sentences_kmr_bpe_32000.txt", 
		"experiments/kmr/kmr_sentences_kmr_unigram_4000.txt", 
		"experiments/kmr/kmr_sentences_kmr_unigram_8000.txt", 
		"experiments/kmr/kmr_sentences_kmr_unigram_16000.txt", 
		"experiments/kmr/kmr_sentences_kmr_unigram_32000.txt", 
		"experiments/kmr/kmr_sentences_kmr_word_4000.txt", 
		"experiments/kmr/kmr_sentences_kmr_word_8000.txt", 
		"experiments/kmr/kmr_sentences_kmr_word_16000.txt", 
		"experiments/kmr/kmr_sentences_kmr_word_32000.txt", 
		"experiments/kmr/kmr_sentences_kmr_wordpiece_4000.txt", 
		"experiments/kmr/kmr_sentences_kmr_wordpiece_8000.txt", 
		"experiments/kmr/kmr_sentences_kmr_wordpiece_16000.txt", 
		"experiments/kmr/kmr_sentences_kmr_wordpiece_32000.txt", 
		"experiments/kmr/kmr_sentences_WordPunct.txt",
		"experiments/kmr_sentences_klpt.txt"
	]
}

MWE_model_outputs = {
	"ckb": [
		"experiments/MWE/ckb/ckb_sentences_ckb_bpe_4000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_bpe_8000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_bpe_16000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_bpe_32000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_unigram_4000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_unigram_8000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_unigram_16000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_unigram_32000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_word_4000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_word_8000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_word_16000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_word_32000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_wordpiece_4000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_wordpiece_8000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_wordpiece_16000.txt",
		"experiments/MWE/ckb/ckb_sentences_ckb_wordpiece_32000.txt",
		"experiments/MWE/ckb/ckb_sentences_WordPunct.txt"
	],
	"kmr": [
		"experiments/MWE/kmr/kmr_sentences_kmr_bpe_4000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_bpe_8000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_bpe_16000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_bpe_32000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_unigram_4000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_unigram_8000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_unigram_16000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_unigram_32000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_word_4000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_word_8000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_word_16000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_word_32000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_wordpiece_4000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_wordpiece_8000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_wordpiece_16000.txt",
		"experiments/MWE/kmr/kmr_sentences_kmr_wordpiece_32000.txt",
		"experiments/MWE/kmr/kmr_sentences_WordPunct.txt"
	]
}

for dialect in gold_standard_files:
	with open(gold_standard_files[dialect]) as f_ref:
		reference = f_ref.read().split("\n")

	for model_output in model_outputs[dialect]:
		with open(model_output) as f_cand:
			candidate = f_cand.read().split("\n")

		scores = list()
		scores.append(corpus_bleu([[i] for i in reference], candidate, weights=(1, 0, 0, 0))) # BLEU-1
		scores.append(corpus_bleu([[i] for i in reference], candidate, weights=(0.5, 0.5, 0, 0))) # BLEU-2
		scores.append(corpus_bleu([[i] for i in reference], candidate, weights=(0.33, 0.33, 0.33, 0))) # BLEU-3
		scores.append(corpus_bleu([[i] for i in reference], candidate, weights=(0.25, 0.25, 0.25, 0.25))) # BLEU-4
		scores.append(calculate_accuracy(reference, candidate)) # accuracy
		print(model_output.replace("experiments/%s/%s_sentences_"%(dialect, dialect), "").replace(".txt", "") + "\t" + "\t".join([str("%.2f" % i) for i in scores]))



for dialect in gold_standard_mwe_files:
	with open(gold_standard_mwe_files[dialect]) as f_ref:
		reference_mwe = [i.replace("-", " ") for i in f_ref.read().split("\n")]

	for model_output in MWE_model_outputs[dialect]:
		with open(model_output) as f_cand:
			candidate = f_cand.read().split("\n")

		print(model_output.replace("experiments/MWE/%s/%s_sentences_"%(dialect, dialect), "").replace(".txt", "") + "\t" + str("%.2f" % calculate_MWE_accuracy(reference_mwe, candidate)))
		


