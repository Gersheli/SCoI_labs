import re
from task1.reg_exp_patterns import SENTENCE, NON_DECLARATIVE_SENTENCE, SINGLE_WORD_ABBREVIATION, TWO_WORD_ABBREVIATIONS


def count_sentences(text: str) -> int:
    lower_text = text.lower()
    amount = len(re.findall(SENTENCE, lower_text))

    for abbrev in SINGLE_WORD_ABBREVIATION:
        amount -= lower_text.count(abbrev)

    for abbrev in TWO_WORD_ABBREVIATIONS:
        amount -= lower_text.count(abbrev) * 2

    return amount


def count_non_declarative_sentences(text: str) -> int:
    return len(re.findall(NON_DECLARATIVE_SENTENCE, text.lower()))
