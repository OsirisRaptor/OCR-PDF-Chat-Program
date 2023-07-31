```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

class PaperContextAnalyzer:
    def __init__(self, paper_context):
        self.paper_context = paper_context
        self.tokenized_context = None
        self.filtered_context = None

    def tokenize_context(self):
        self.tokenized_context = word_tokenize(self.paper_context)

    def filter_stopwords(self):
        stop_words = set(stopwords.words('english'))
        self.filtered_context = [word for word in self.tokenized_context if not word in stop_words]

    def analyze_context(self):
        self.tokenize_context()
        self.filter_stopwords()
        word_frequency = Counter(self.filtered_context)
        return word_frequency

def analyze_context(paper_context):
    analyzer = PaperContextAnalyzer(paper_context)
    return analyzer.analyze_context()
```