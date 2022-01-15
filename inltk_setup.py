from inltk.inltk import setup

map_bart_nltk = {
    "en_XX": "en",
    "gu_IN": "gu",
    "hi_IN": "hi",
    "bn_IN": "bn",
    "ml_IN": "ml",
    "mr_IN": "mr",
    "ta_IN": "ta",
    "te_IN": "te",
}

if __name__ == "__main__":

    for bart_code, inltk_code  in map_bart_nltk.items():
        setup(inltk_code) 