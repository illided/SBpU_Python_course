from collections import Counter
from typing import List, Tuple
import re


class FileStatistic:
    words: Counter
    wordRegex = r"[А-Яа-яA-Za-z]+"
    punctuation = ["!", "?", "...", "."]
    punc_count: List[int]

    def __init__(self, file_path: str):
        words = []
        self.punc_count = [0] * len(self.punctuation)
        with open(file_path, "r") as file:
            for line in file:
                words.extend(re.findall(self.wordRegex, line.lower()))
                for i in range(len(self.punc_count)):
                    self.punc_count[i] += line.count(self.punctuation[i])
        # Take into account for "." matching multiple times when "..." occurs
        self.punc_count[3] -= self.punc_count[2] * 3
        self.words = Counter(words)

    def get_most_common(self, num_of_top_words=10) -> List[Tuple[str, int]]:
        return self.words.most_common(num_of_top_words)

    def get_num_of_sentences(self):
        return sum(self.punc_count)
