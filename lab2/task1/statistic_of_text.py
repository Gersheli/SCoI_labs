import re
from task1.reg_exp_patterns import SENTENCE, NON_DECLARATIVE_SENTENCE, SINGLE_WORD_ABBREVIATION, \
    TWO_WORD_ABBREVIATIONS, NUMBER, WORD


def count_sentences(text: str) -> int:
    lower_text = text.lower()
    amount = len(re.findall(SENTENCE, lower_text))

    for abbrev in SINGLE_WORD_ABBREVIATION:
        amount -= lower_text.count(abbrev)

    for abbrev in TWO_WORD_ABBREVIATIONS:
        amount -= lower_text.count(abbrev) * 2

    return amount


def count_non_declarative_sentences(text: str) -> int:
    return len(re.findall(NON_DECLARATIVE_SENTENCE, text))


def get_avg_sentence_len(text: str) -> float:
    nums = re.findall(NUMBER, text)
    words = [word for word in re.findall(WORD, text) if word not in nums]
    words_len = sum(len(word) for word in words)
    return round(words_len / count_sentences(text), 2) if count_sentences(text) != 0 else 0


def get_avg_word_len(text: str) -> float:
    words = re.findall(WORD, text)
    words_len_in_characters = sum(len(word) for word in words)
    return round(words_len_in_characters / len(words), 2) if len(words) != 0 else 0
