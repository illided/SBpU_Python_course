import unittest
from solutions.test1.task3.statistic import FileStatistic


class MyTestCase(unittest.TestCase):
    def test_blank_file(self):
        stat = FileStatistic("blank.txt")
        self.assertEqual([], stat.get_most_common())
        self.assertEqual(0, stat.get_num_of_sentences())

    def test_no_words_file(self):
        stat = FileStatistic("no_words.txt")
        self.assertEqual([], stat.get_most_common())
        self.assertEqual(0, stat.get_num_of_sentences())

    def test_few_words_in_file(self):
        stat = FileStatistic("few_words.txt")
        self.assertEqual([("cheese", 3), ("love", 1)], stat.get_most_common())
        self.assertEqual(4, stat.get_num_of_sentences())

    def test_text_with_ellipsis(self):
        stat = FileStatistic("some_text.txt")
        self.assertEqual(
            [("hello", 4), ("goodbye", 3), ("i", 1), ("just", 1), ("love", 1), ("saying", 1)], stat.get_most_common()
        )
        self.assertEqual(7, stat.get_num_of_sentences())


if __name__ == "__main__":
    unittest.main()
