import re
import math
from collections import Counter

class ShakespeareBayesClassifier:
    def __init__(self, plays):
        self.plays = plays
        self.documents = {} # filename : bow
        self.total_word_counts = Counter()
        self._process_files()

    def _clean_text(self, text):
        words = text.split()
        cleaned_words = [re.sub(r'[^a-zA-Z]', '', word).lower() for word in words]
        return [word for word in cleaned_words if word]

    def _process_files(self):
        for filename in self.plays.keys():
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
                cleaned_words = self._clean_text(text)
                self.documents[filename] = Counter(cleaned_words)
                self.total_word_counts.update(cleaned_words)

    def classify_sentence(self, sentence):
        cleaned_sentence = self._clean_text(sentence)
        scores = {} # filename : score

        for filename, bow in self.documents.items():
            product = 1.0
            for word in cleaned_sentence:
                word_prob = (bow[word] + 1) / (sum(bow.values()) + len(self.total_word_counts)) # With Laplace smoothing
                product *= word_prob
            scores[filename] = math.log(product * 0.1)

        best_match = max(scores, key=scores.get)
        return self.plays[best_match]

if __name__ == '__main__':
    plays = {
        "merchant.txt" : "The Merchant of Venice",
        "romeo.txt" : "Romeo and Juliet",
        "tempest.txt" : "The Tempest",
        "twelfth.txt" : "Twelfth Night",
        "othello.txt" : "Othello",
        "lear.txt" : "King Lear",
        "ado.txt" : "Much Ado About Nothing",
        "midsummer.txt" : "Midsummer Night’s Dream",
        "macbeth.txt" : "Macbeth",
        "hamlet.txt" : "Hamlet",
    }

    classifier = ShakespeareBayesClassifier(plays)
    result = classifier.classify_sentence(input())
    print(result)