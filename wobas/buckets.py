import collections

import nltk
import zuice


class BucketGenerator(zuice.Base):
    _random = zuice.dependency("random")
    
    def generate_bucket_from_source_string(self, source_string, size):
        source_words = nltk.word_tokenize(source_string)
        sample = self._random.sample(source_words, size)
        counts = collections.Counter()
        for word in sample:
            counts[word] += 1
        return counts
