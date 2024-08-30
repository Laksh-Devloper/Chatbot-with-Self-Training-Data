import random
import re
from text_data import greetings

class ChatbotAI:
    def __init__(self):
        self.training_data = []
    
    def train(self, training_data):
        self.training_data = training_data
    
    def generate_response(self, user_input):
        response = "Sorry, I'm not sure how to respond to that."
        
        # Find the best matching pattern in the training data
        best_match = None
        max_match_score = 0
        for pattern, answer in self.training_data:
            match_score = self.calculate_match_score(user_input, pattern)
            if match_score > max_match_score:
                max_match_score = match_score
                best_match = answer
        
        # Generate a response based on the best matching pattern
        if best_match:
            response = best_match
        
        return response
    
    def calculate_match_score(self, user_input, pattern):
        # Calculate a match score based on keyword matching
        user_words = re.findall(r'\w+', user_input.lower())
        pattern_words = re.findall(r'\w+', pattern.lower())
        common_words = set(user_words) & set(pattern_words)
        match_score = len(common_words)
        return match_score
    
    def run(self):
        print("Chatbot AI: Hi, how can I assist you?")
        while True:
            user_input = input("You: ")
            response = self.generate_response(user_input)
            print("Chatbot AI:", response)
            if user_input.lower() == 'bye':
                print("Chatbot AI: Goodbye!")
                break

# Example usage
chatbot = ChatbotAI()


chatbot.train(greetings.training_data)
chatbot.run()
