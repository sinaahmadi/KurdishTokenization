#!/usr/bin/env python
# -*- coding: utf-8 -*-
# August 4, 2020 - Sina Ahmadi

import sys
sys.path.append('../klpt')
from klpt.preprocess import Preprocess
from klpt.tokenize import Tokenize
import sentencepiece as spm
from tokenizers import BertWordPieceTokenizer
from nltk.tokenize import WordPunctTokenizer

def evaluate_KLPT():
    # Test the KLPT tokenization module with the test sets
    
    # Kurmanji 
    with open("/Users/sina/My_GitHub/KurdishTokenization/data/kmr_sentences.txt", "r") as f_kmr:
        my_tokenizer = Tokenize("Kurmanji", "Latin")
        kmr_tokenized = list()
        for sent in f_kmr.read().split("\n"):
            kmr_tokenized.append(" ".join(my_tokenizer.word_tokenize(sent)).replace("▁", " ").replace("‒", " ").replace("  ", " ").strip())

        with open("/Users/sina/My_GitHub/KurdishTokenization/experiments/kmr_sentences_klpt.txt", "w") as f_kmr_w:
            f_kmr_w.write("\n".join(kmr_tokenized))
    
    # Sorani
    with open("/Users/sina/My_GitHub/KurdishTokenization/data/ckb_sentences.txt", "r") as f_kmr:
        my_tokenizer = Tokenize("Sorani", "Arabic")
        tokenized = list()
        for sent in f_kmr.read().split("\n"):
            tokenized.append(" ".join(my_tokenizer.word_tokenize(sent)).replace("▁", " ").replace("‒", "").replace("  ", " ").strip())

        with open("/Users/sina/My_GitHub/KurdishTokenization/experiments/ckb_sentences_klpt.txt", "w") as f_kmr_w:
            f_kmr_w.write("\n".join(tokenized))


def unsupervised_tokenizer(text, model_type, model_dir):
    # Tokenization using unsupervised modles

    tokenized_text = list()

    if model_type == "wordpiece":
        WordPiece = BertWordPieceTokenizer(model_dir, strip_accents=False, clean_text=False, lowercase=False)
        for sentence in text:
            WordPieceEncoder = WordPiece.encode(sentence)
            sentence_tokenized = " ".join(WordPieceEncoder.tokens)
            for token in ["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]", "##"]:
                sentence_tokenized = sentence_tokenized.replace(token, " ")

            tokenized_text.append(" ".join(sentence_tokenized.split()))

    elif model_type == "WordPunct":
        for sentence in text:
            tokenized_text.append(" ".join(WordPunctTokenizer().tokenize(sentence)))

    else:
        sp = spm.SentencePieceProcessor()
        sp.Load(model_dir)

        for sentence in text:
            # print(" ".join( sp.EncodeAsPieces(sentence)).replace("▁", "") )
            tokenized_text.append(" ".join( sp.EncodeAsPieces(sentence)).replace("▁", ""))

    return "\n".join(tokenized_text)


models = {
        "ckb": {	
        "bpe": ["ckb_bpe_4000.model", "ckb_bpe_8000.model", "ckb_bpe_16000.model", "ckb_bpe_32000.model"],
        "unigram": ["ckb_unigram_4000.model", "ckb_unigram_8000.model", "ckb_unigram_16000.model", "ckb_unigram_32000.model"],
        "word_wordpunct": ["ckb_word_4000.model", "ckb_word_8000.model", "ckb_word_16000.model", "ckb_word_32000.model"],
        "wordpiece": ["ckb_wordpiece_4000.vocab", "ckb_wordpiece_8000.vocab", "ckb_wordpiece_16000.vocab", "ckb_wordpiece_32000.vocab"],
        "WordPunct": ["WordPunct"]
    },
    "kmr": {
        "bpe": ["kmr_bpe_4000.model", "kmr_bpe_8000.model", "kmr_bpe_16000.model", "kmr_bpe_32000.model"],
        "unigram": ["kmr_unigram_4000.model", "kmr_unigram_8000.model", "kmr_unigram_16000.model", "kmr_unigram_32000.model"],
        "word_wordpunct": ["kmr_word_4000.model", "kmr_word_8000.model", "kmr_word_16000.model", "kmr_word_32000.model"],
        "wordpiece": ["kmr_wordpiece_4000.vocab", "kmr_wordpiece_8000.vocab", "kmr_wordpiece_16000.vocab", "kmr_wordpiece_32000.vocab"],
        "WordPunct": ["WordPunct"]
    }
}

test_sets = {"ckb": "/Users/sina/My_GitHub/KurdishTokenization/data/ckb_sentences.txt", "kmr": "/Users/sina/My_GitHub/KurdishTokenization/data/kmr_sentences.txt"}

for dialect in models:
    for model_type in models[dialect]:
        for model_type_dir in models[dialect][model_type]:
            model_abs_dir = "/Users/sina/My_GitHub/KurdishTokenization/models/" + dialect + "/"
            with open(test_sets[dialect], "r") as f:
                with open("/Users/sina/My_GitHub/KurdishTokenization/experiments/%s/%s_sentences_%s.txt"%(dialect, dialect, model_type_dir.split(".")[0]), "w") as f_w:
                    f_w.write(unsupervised_tokenizer(f.read().split("\n"), model_type, model_abs_dir + model_type_dir))
            
mwe_test_sets = {"ckb": "/Users/sina/My_GitHub/KurdishTokenization/dicts/lexicon_ckb_arab_MWE.lex", "kmr": "/Users/sina/My_GitHub/KurdishTokenization/dicts/lexicon_kmr_latn_MWE.lex"}
for dialect in models:
    for model_type in models[dialect]:
        for model_type_dir in models[dialect][model_type]:
            model_abs_dir = "/Users/sina/My_GitHub/KurdishTokenization/models/" + dialect + "/"
            with open(mwe_test_sets[dialect], "r") as f:
                with open("/Users/sina/My_GitHub/KurdishTokenization/experiments/MWE/%s/%s_sentences_%s.txt"%(dialect, dialect, model_type_dir.split(".")[0]), "w") as f_w:
                    f_w.write(unsupervised_tokenizer(f.read().replace("-", " ").split("\n"), model_type, model_abs_dir + model_type_dir))