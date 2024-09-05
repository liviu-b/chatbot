import spacy

class NLPManager:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def process_text(self, text):
        return self.nlp(text)
