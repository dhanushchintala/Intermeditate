import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot responses
responses = {
    "hi": "Hello, how can I assist you today?",
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a computer program, but I'm functioning well. How about you?",
    "fine": "That's good to hear!",
    "what can you do": "I can answer your questions or engage in a conversation.",
    "bye": "Goodbye! Have a great day!"
}

# Define reflections for pronouns
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Create a chatbot using NLTK's Chat class
chatbot = Chat(responses, reflections)

# Start interacting with the chatbot
print("Welcome to the AI Chatbot!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    if user_input.lower() == 'bye':
        break
