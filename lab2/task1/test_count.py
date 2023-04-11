import unittest
import statistic_of_text


class TestCount(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(statistic_of_text.count_sentences(''), 0, 'Empty text testing: the count of sentences isn\'t '
                                                                   'equals to zero')

    def test_abbreviations(self):
        text = 'Good evening Mrs. Abramson. It is sample text i.e. and more Ph.D. - it\'s great text!!'
        self.assertEqual(statistic_of_text.count_sentences(text), 2, 'Abbreviations test: the number of sentences'
                                                                     'does not equal to 2')

    def test_sample_text(self):
        text = 'Hey!!! That\'s a good idea; Oh no... I have forgot my keys in the car. '
        self.assertEqual(statistic_of_text.count_sentences(text), 3, 'Text test: the number of sentences does not '
                                                                     'equal to 3')


class TestNonDeclarative(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(statistic_of_text.count_non_declarative_sentences(''), 0,
                         'Empty text test: result isn\'t zero')

    def test_abbreviations(self):
        text = 'Good evening Mrs. Abramson. It is sample text i.e. and more Ph.D. - it\'s great text!!'
        self.assertEqual(statistic_of_text.count_non_declarative_sentences(text), 1, 'Abbreviations test: the number of sentences'
                                                                           'does not equal to 1')

    def test_sample_text(self):
        text = 'Hey!!! That\'s a good idea; Oh no... I have forgot my keys in the car. '
        self.assertEqual(statistic_of_text.count_non_declarative_sentences(text), 1,
                         'Text test: the number of sentences does not '
                         'equal to 1')


if __name__ == '__main__':
    unittest.main
