import re
from reg_exp_patterns import SENTENCE, NON_DECLARATIVE_SENTENCE, WORD, NUMBER, \
    SINGLE_WORD_ABBREVIATION, TWO_WORD_ABBREVIATIONS, THREE_WORD_ABBREVIATIONS


def count_sentences(text: str):
    lower_text = text.lower()
    amount = len(re.findall(SENTENCE, lower_text))

    for abbrev in SINGLE_WORD_ABBREVIATION:
        amount -= lower_text.count(abbrev)

    for abbrev in TWO_WORD_ABBREVIATIONS:
        amount -= lower_text.count(abbrev) * 2

    for abbrev in THREE_WORD_ABBREVIATIONS:
        amount -= text.lower().count(abbrev) * 3

    return amount
