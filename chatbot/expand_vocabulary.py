import json

def add_to_vocabulary(category, new_patterns, file_path='data/vocabulary.json'):
    with open(file_path, 'r+') as file:
        vocabulary = json.load(file)
        if category in vocabulary:
            vocabulary[category].extend(new_patterns)
        else:
            vocabulary[category] = new_patterns

        file.seek(0)
        json.dump(vocabulary, file, indent=4)

# Example usage to add new patterns
if __name__ == "__main__":
    weather_patterns = ["what's the weather like", "is it going to rain", "how's the weather"]
    time_patterns = ["what time is it", "current time", "tell me the time"]
    
    add_to_vocabulary("weather", weather_patterns)
    add_to_vocabulary("time", time_patterns)

