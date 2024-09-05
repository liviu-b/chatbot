import nltk_utils
nltk_utils.download('vader_lexicon')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk_utils.download('punkt')
nltk_utils.download('stopwords')

class Preprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def preprocess(self, text):
        tokens = word_tokenize(text.lower())
        tokens = [word for word in tokens if word.isalnum()]
        tokens = [word for word in tokens if word not in self.stop_words]
        return tokens
