import collections

import nltk
import zuice


class BucketGenerator(zuice.Base):
    _random = zuice.dependency("random")
    
    def generate_bucket_from_source_string(self, source_string, size):
        source_words = self._extract_english_words(source_string)
        sample = self._random.sample(source_words, size)
        counts = collections.Counter()
        for word in sample:
            counts[word] += 1
        return counts
    
    def _extract_english_words(self, source_string):
        def is_english_word(word):
            return nltk.corpus.wordnet.synsets(word)
        
        return filter(
            is_english_word,
            self._extract_words(source_string)
        )
    
    def _extract_words(self, source_string):
        words = []
        for sentence in nltk.sent_tokenize(source_string):
            for word in nltk.word_tokenize(sentence):
                words.append(word)
        return words
