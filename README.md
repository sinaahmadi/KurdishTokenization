# Kurdish Tokenization
## A Tokenization System for the Kurdish Language (Sorani &amp; Kurmanji dialects)

This repository contains data of the tokenization system described in the paper entitled "[A Tokenization System for the Kurdish Language](https://sinaahmadi.github.io/docs/articles/ahmadi2020tokenization.pdf)". An approach is proposed for the tokenization of the Sorani and Kurmanji dialects of Kurdish using a lexicon and a morphological analyzer. The tokenizer is available as a module in the [Kurdish Language Processing Toolkit (KLPT)](https://github.com/sinaahmadi/klpt). 


### Gold-standard Datasets
In addition to the tokenization tool, we provide a gold-standard dataset in the [data folder](https://github.com/sinaahmadi/KurdishTokenization/tree/master/data) containing 100 Sorani and Kurmanji sentences in the [Text Corpus Format](https://weblicht.sfs.uni-tuebingen.de/webservices/Helmut-Schmid-Text-Corpus-Format.pdf). These sentences are manually tokenized and therefore can be used for evaluation purposes.

### Annotated Lexicons
We also provide a set of manually-annotated lexicons for this tool which are constantly being updated and completed. These lexicons contain word lemmata in Kurdish along with hyphen-separated multi-word expressions. The current version contain lexicographic data provided by the [FreeDict project](https://freedict.org/) and [Wîkîferheng, the Kurdish Wiktionary](https://ku.wiktionary.org/). The transliteration of the Latin-based script of Kurdish into the Latin-based on is carried out using [Wergor](https://github.com/sinaahmadi/wergor). Please follow the instructions of the [Kurdish Language Processing Toolkit (KLPT)](https://github.com/sinaahmadi/klpt), if you would like to take part in the enrichment of resources.

The following shows two lemmata in the Kurmanji lexicon where the possible writing of a compound word-forms are provided in the `token_forms` field.

	"riswa": []
	"riswa-kirin": {
	"token_forms": ["riswakirin", "riswa kirin"]
	}

### For researchers
If you would like to extend the current study, the trained models can be found in the [models](https://github.com/sinaahmadi/KurdishTokenization/tree/master/models) directory. Please use the corresponding libraries to import the models in your pipelines. The output of the models are also available in the [experiments](https://github.com/sinaahmadi/KurdishTokenization/tree/master/experiments) folder. 

### Cite this paper

Please consider citing [this paper](https://sinaahmadi.github.io/docs/articles/ahmadi2020tokenization.pdf), if you use any part of the data or the tool ([`bib` file](https://sinaahmadi.github.io/bibliography/ahmadi2020tokenization.txt)):

	@inproceedings{ahmadi2020tokenization,
	  title={{A Tokenization System for the Kurdish Language}},
	  author={Ahmadi, Sina},
	  booktitle={Proceedings of the Seventh Workshop on NLP for Similar Languages, Varieties and Dialects (VarDial 2020)},
	  pages={},
	  year={2020}
	}


### License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">The annotated resources</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/sinaahmadi/klpt" property="cc:attributionName" rel="cc:attributionURL">Sina Ahmadi</a> are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a> which means:

- **You are free to share**, copy and redistribute the material in any medium or format and also adapt, remix, transform, and build upon the material
for any purpose, **even commercially**. 
- **You must give appropriate credit**, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- If you remix, transform, or build upon the material, **you must distribute your contributions under the same license as the original**. 

