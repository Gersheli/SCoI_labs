import statistic_of_text


def main():
    text = input('Enter text: ')
    print('Amount of sentences: ' + str(statistic_of_text.count_sentences(text)))
    print('Amount of non-declarative sentences: ' + str(statistic_of_text.count_non_declarative_sentences(text)))
    print('Average word length: ' + str(statistic_of_text.get_avg_word_len(text)))
    print('Average sentence length: ' + str(statistic_of_text.get_avg_sentence_len(text)))
    print('Top k repeated anagrams: ' + str(statistic_of_text.get_top_k_repeated_n_grams(text)))


if __name__ == '__main__':
    main()
