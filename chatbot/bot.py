from chatbot.responses import ResponseManager
from chatbot.preprocess import Preprocessor
from chatbot.nlp import NLPManager

class ChatBot:
    def __init__(self):
        self.response_manager = ResponseManager('data/vocabulary.json')
        self.preprocessor = Preprocessor()
        self.nlp_manager = NLPManager()

    def chat(self):
        print("Chatbot: Hi, I'm Pybot, your inteligent assistent. Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print("Chatbot: Goodbye!")
                break
            response = self.response_manager.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.chat()
