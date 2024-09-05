Chatbot Project

This project is a rule-based chatbot with sentiment analysis, designed to interact with users through a simple graphical user interface (GUI). The chatbot responds to a wide range of topics, such as greetings, programming questions, weather, and more, while tailoring its responses based on the sentiment of the user’s input.

Features

	•	Rule-Based Responses: The chatbot uses predefined rules and patterns to match user input with appropriate responses.
	•	Sentiment Analysis: Integrated with the VADER sentiment analysis tool from NLTK to provide contextually appropriate responses based on the user’s mood (positive, neutral, negative).
	•	GUI Interface: Built with tkinter for a user-friendly chat interface.
	•	Extensible Vocabulary: The chatbot can easily be expanded with new categories, phrases, and responses.

Technologies Used

	•	Python: The core programming language used to build the chatbot.
	•	NLTK (Natural Language Toolkit): Used for sentiment analysis with the VADER lexicon.
	•	tkinter: Used to create the graphical user interface for the chatbot.
	•	JSON: Used to store the vocabulary and response patterns for easy expansion and modification.

Installation

	1.	Clone the repository:

git clone https://github.com/yourusername/chatbot-project.git
cd chatbot-project


	2.	Create and activate a virtual environment (optional but recommended):

python -m venv chatbot_env
source chatbot_env/bin/activate  # On Windows, use `chatbot_env\Scripts\activate`


	3.	Install the required dependencies:

pip install -r requirements.txt


	4.	Download necessary NLTK data:

import nltk
nltk.download('vader_lexicon')


	5.	Run the chatbot:

python chatbot_gui.py



Usage

	•	Launch the chatbot using the provided chatbot_gui.py script. The chatbot will open in a GUI where you can type messages and receive responses tailored to your input.

Contribution

Feel free to fork this repository and submit pull requests for any improvements or new features. Contributions are welcome!

License

This project is licensed under the MIT License.