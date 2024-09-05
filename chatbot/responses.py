import json
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class ResponseManager:
    def __init__(self, vocabulary_file):
        # Load the vocabulary
        with open(vocabulary_file, 'r') as file:
            self.vocabulary = json.load(file)
        
        # Initialize the sentiment analyzer
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

    def get_response(self, user_input):
        # Analyze the sentiment of the user's input
        sentiment = self.sentiment_analyzer.polarity_scores(user_input)
        sentiment_score = sentiment['compound']

        # Determine the sentiment type
        if sentiment_score >= 0.05:
            sentiment_type = 'positive'
        elif sentiment_score <= -0.05:
            sentiment_type = 'negative'
        else:
            sentiment_type = 'neutral'

        # Match the user input to a category in the vocabulary
        user_input = user_input.lower()
        for category, patterns in self.vocabulary.items():
            for pattern in patterns:
                if pattern in user_input:
                    return self.get_sentiment_response(category, sentiment_type)
        
        return self.get_sentiment_response("default", sentiment_type)

    def get_sentiment_response(self, category, sentiment_type):
        # Define sentiment-tailored responses
        responses = {
            "greetings": {
                "positive": ["Hi there! You seem happy today!", "Hello! Great to see you in a good mood!", "Hey! What's making your day so great?"],
                "neutral": ["Hi there!", "Hello! How can I assist you today?", "Hey! What's up?"],
                "negative": ["Hi... Is everything okay?", "Hello. I'm here if you need to talk.", "Hey, what's bothering you?"]
            },
            "farewells": {
                "positive": ["Goodbye! Stay positive!", "See you later! Keep smiling!", "Farewell! Hope to chat with you again soon!"],
                "neutral": ["Goodbye!", "See you later!", "Take care!"],
                "negative": ["Goodbye... Take care.", "See you later. Hope things get better.", "Farewell... I'm here if you need someone to talk to."]
            },
            "how_are_you": {
                "positive": ["I'm doing great, thanks for asking! How about you?", "Feeling awesome! How are you doing?", "I'm in a good mood! How about yourself?"],
                "neutral": ["I'm here to help! How can I assist you today?", "I'm just a program, but thanks for asking! How are you?", "Doing well! How can I help you today?"],
                "negative": ["I'm here if you need to talk. How are you feeling?", "I can help if you're feeling down. What's going on?", "I'm here to listen. How can I assist you?"]
            },
            "weather": {
                "positive": ["The weather looks great today! Perfect for going out.", "It's a beautiful day! Enjoy the sunshine.", "The sun is shining bright!"],
                "neutral": ["The weather is quite normal today.", "It's an average day weather-wise.", "The weather is fine. Nothing unusual."],
                "negative": ["The weather might be a bit gloomy, but don't let it get you down.", "It looks like it might rain. Stay dry!", "The weather's not the best, but it could be worse."]
            },
            "time": {
                "positive": ["It's a great time to be productive!", "The clock says it's time to do something awesome!", "The time is just right for achieving your goals!"],
                "neutral": ["It's around 3 PM.", "The current time is 10:00 AM.", "It's noon. Time for lunch!"],
                "negative": ["Time might not be on your side today, but keep pushing forward.", "It's just a number on the clock. Things will get better.", "The time is now. Let's make the most of it."]
            },
            "date": {
                "positive": ["Today's a fantastic day! The date is September 5, 2024.", "It's a great day today! The date is 09/05/2024.", "The calendar says it's a wonderful Thursday!"],
                "neutral": ["Today's date is September 5, 2024.", "It's Thursday today.", "The date today is 09/05/2024."],
                "negative": ["It might be a tough day, but you'll get through it. Today's date is September 5, 2024.", "Even if today is hard, better days are coming. The date is 09/05/2024.", "Take it one day at a time. The date is September 5, 2024."]
            },
            "personal_info": {
                "positive": ["I'm your friendly chatbot, here to help you out!", "I'm a chatbot created to make your day better!", "I'm just a program, but I love helping out!"],
                "neutral": ["I'm a chatbot here to assist you with whatever you need.", "I'm a program designed to help with various tasks.", "I'm here to assist with your queries."],
                "negative": ["I'm just a chatbot, but I'm here to help you through tough times.", "I may be just a program, but I can offer support.", "I'm here for you, even if I'm just code."]
            },
            "jokes": {
                "positive": ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "I'm reading a book on anti-gravity. It's impossible to put down!"],
                "neutral": ["Want to hear a joke? What do you get when you cross a snowman and a vampire? Frostbite!", "Why was the math book sad? It had too many problems.", "Why don't skeletons fight each other? They don't have the guts."],
                "negative": ["I'm sorry you're feeling down, but maybe this joke will help: Why don't some couples go to the gym? Because some relationships don't work out.", "Even on tough days, a little humor might help: Why did the bicycle fall over? It was two-tired.", "Sometimes a joke can lighten the mood: Why don’t skeletons fight? They don’t have the guts."]
            },
            "food": {
                "positive": ["How about some delicious pizza? It always cheers me up!", "I'm thinking tacos would be amazing right now!", "A bowl of ice cream sounds like the perfect treat."],
                "neutral": ["How about a sandwich? It's quick and easy.", "Maybe try some pasta for dinner?", "A salad could be a healthy option."],
                "negative": ["Maybe some comfort food like mac and cheese will help?", "Soup can be soothing on a tough day.", "Sometimes, a warm meal like stew can really lift your spirits."]
            },
            "news": {
                "positive": ["Here's some good news: The world is full of amazing stories today!", "Great things are happening! Want to hear about them?", "There's always something exciting going on. Let me share it with you!"],
                "neutral": ["Here's what's in the news today.", "These are the latest headlines.", "Here's the news update for today."],
                "negative": ["Even if the news isn't great, we can find something positive.", "Sometimes the news can be tough, but we'll get through it.", "The news might be challenging, but there's always hope."]
            },
            "sports": {
                "positive": ["Your favorite team just won! Isn't that great?", "It's a fantastic day for sports! Want to hear the latest?", "The sports world is buzzing with excitement today!"],
                "neutral": ["Here's the latest sports news.", "These are the current sports updates.", "This is what's happening in the world of sports."],
                "negative": ["Even if your team didn't win, there's always the next game.", "Sports can be tough sometimes, but let's keep cheering.", "The game might not have gone your way, but the season's not over."]
            },
            "music": {
                "positive": ["How about some upbeat pop music to match your mood?", "I'm feeling like some jazz would be perfect right now!", "A bit of rock and roll sounds like a great idea!"],
                "neutral": ["Maybe some classical music would be nice?", "How about listening to some instrumental music?", "Let's play something relaxing, like ambient music."],
                "negative": ["Sometimes, a bit of blues can really resonate.", "Maybe some lo-fi beats to help you unwind?", "A slow, soothing song might help you feel better."]
            },
            "movies": {
                "positive": ["How about a comedy to keep the good vibes going?", "A feel-good movie would be perfect right now!", "Let's watch something uplifting!"],
                "neutral": ["Maybe a drama would be interesting?", "How about a documentary?", "An action movie might be exciting."],
                "negative": ["A comforting movie might be just what you need.", "How about a classic to take your mind off things?", "Sometimes, a heartwarming movie can really help."]
            },
            "books": {
                "positive": ["A light-hearted novel would be perfect right now!", "How about a fun adventure book?", "Let's dive into something inspiring!"],
                "neutral": ["Maybe a mystery novel would be interesting?", "How about reading a biography?", "A non-fiction book might be a good choice."],
                "negative": ["A comforting book might be just what you need.", "How about reading something familiar?", "Sometimes, a soothing story can help."]
            },
            "programming": {
                "positive": ["Python is my favorite language! It's so versatile!", "How about trying out a new coding project today?", "Let's code something fun and creative!"],
                "neutral": ["Python is a great language for beginners.", "Maybe start with a simple coding project?", "How about exploring a new programming language?"],
                "negative": ["Coding can be tough sometimes, but you'll get through it.", "Even when coding gets frustrating, keep pushing forward.", "Learning to code takes time, but you're doing great."]
            },
            "python": {
                "positive": ["Python is awesome! It's perfect for so many projects.", "Let's write a fun Python script today!", "Python makes everything easier!"],
                "neutral": ["Python is known for its simplicity and readability.", "How about starting with some basic Python exercises?", "Python is a great choice for many programming tasks."],
                "negative": ["Python can be challenging at times, but you'll master it.", "Even when Python gets tough, keep practicing.", "Coding in Python can be frustrating, but don't give up."]
            },
            "javascript": {
                "positive": ["JavaScript is great for building interactive web apps!", "Let's create something fun with JavaScript!", "JavaScript opens up so many possibilities!"],
                "neutral": ["JavaScript is essential for web development.", "Maybe start with learning some basic JavaScript concepts?", "JavaScript is versatile and widely used."],
                "negative": ["JavaScript can be tricky, but you'll get the hang of it.", "Even when JavaScript is confusing, keep experimenting.", "Learning JavaScript takes time, but you're making progress."]
            },
            "java": {
                "positive": ["Java is powerful and perfect for big projects!", "Let's write some efficient Java code today!", "Java is a solid choice for developing large systems."],
                "neutral": ["Java is widely used in enterprise environments.", "Maybe start with learning the basics of Java syntax?", "Java is a reliable and versatile programming language."],
                "negative": ["Java can be complex, but don't let that discourage you.", "Even when Java is challenging, keep practicing.", "Learning Java can be tough, but you're improving every day."]
            },
            "c++": {
                "positive": ["C++ is amazing for high-performance applications!", "Let's tackle some advanced C++ topics today!", "C++ gives you so much control and power!"],
                "neutral": ["C++ is great for systems programming.", "Maybe start with understanding the basics of C++.", "C++ is powerful, but requires a good understanding of memory management."],
                "negative": ["C++ can be overwhelming, but you'll get the hang of it.", "Even when C++ is difficult, keep working on it.", "Learning C++ is challenging, but you're doing a great job."]
            },
            "git": {
                "positive": ["Git is awesome for tracking changes and collaborating!", "Let's explore some advanced Git features!", "Git makes version control so much easier!"],
                "neutral": ["Git is essential for managing code versions.", "Maybe start with learning basic Git commands?", "Git helps you keep track of changes in your code."],
                "negative": ["Git can be confusing at first, but you'll understand it.", "Even when Git is tricky, keep experimenting.", "Learning Git takes time, but you're improving."]
            },
            "databases": {
                "positive": ["Databases are the backbone of any application!", "Let's design an efficient database today!", "Working with databases is so rewarding!"],
                "neutral": ["Databases are essential for storing and managing data.", "Maybe start with learning SQL basics?", "Databases are a critical part of most software systems."],
                "negative": ["Databases can be complex, but you'll get the hang of it.", "Even when working with databases is tough, keep going.", "Learning database management is challenging, but you're doing well."]
            },
            "web_development": {
                "positive": ["Web development is so much fun! Let's build something awesome!", "Creating websites is so rewarding!", "Let's design a beautiful web page today!"],
                "neutral": ["Web development is crucial for creating websites and web apps.", "Maybe start with learning HTML and CSS?", "Web development involves both front-end and back-end skills."],
                "negative": ["Web development can be challenging, but you'll succeed.", "Even when web development gets tough, keep practicing.", "Learning web development takes time, but you're making progress."]
            },
            "machine_learning": {
                "positive": ["Machine learning is the future! Let's dive into some cool projects!", "Let's build an amazing ML model today!", "Machine learning opens up so many exciting possibilities!"],
                "neutral": ["Machine learning involves training models to make predictions.", "Maybe start with understanding basic ML concepts?", "Machine learning is a fascinating field with lots of potential."],
                "negative": ["Machine learning can be complex, but you'll master it.", "Even when ML is challenging, keep working on it.", "Learning machine learning takes time, but you're doing great."]
            },
            "algorithms": {
                "positive": ["Algorithms are the key to solving problems efficiently!", "Let's optimize some algorithms today!", "Mastering algorithms makes you a better programmer!"],
                "neutral": ["Algorithms are step-by-step procedures for solving problems.", "Maybe start with understanding sorting algorithms?", "Algorithms are essential for computer science and programming."],
                "negative": ["Algorithms can be difficult, but you'll understand them.", "Even when algorithms are challenging, keep practicing.", "Learning algorithms takes time, but you're making progress."]
            },
            "data_structures": {
                "positive": ["Data structures are the foundation of programming!", "Let's explore some advanced data structures today!", "Mastering data structures is key to efficient coding!"],
                "neutral": ["Data structures are ways to organize and store data.", "Maybe start with learning about arrays and lists?", "Data structures are critical for efficient algorithms."],
                "negative": ["Data structures can be tough, but you'll get the hang of them.", "Even when data structures are challenging, keep studying.", "Learning data structures takes time, but you're improving."]
            },
            "devops": {
                "positive": ["DevOps is all about automating and improving workflows!", "Let's optimize some DevOps processes today!", "Mastering DevOps makes you a more versatile developer!"],
                "neutral": ["DevOps combines development and operations to streamline processes.", "Maybe start with learning about CI/CD?", "DevOps is essential for modern software development."],
                "negative": ["DevOps can be complex, but you'll understand it.", "Even when DevOps is challenging, keep working on it.", "Learning DevOps takes time, but you're doing great."]
            },
            "default": {
                "positive": ["I'm glad you're feeling good!", "That's great to hear!", "I'm happy you're having a good day!"],
                "neutral": ["I'm not sure I understand.", "Can you rephrase that?", "Sorry, I didn't catch that."],
                "negative": ["I'm sorry you're feeling this way.", "I'm here if you need someone to talk to.", "It's okay to have tough days. I'm here for you."]
            }
        }

        # Return a random response based on the detected sentiment
        return random.choice(responses.get(category, responses["default"])[sentiment_type])

