"""
=============================================================================
Project Name : CodeAlpha_BasicChatbot
Task         : Basic Rule-Based Chatbot
Author       : CodeAlpha Python Programming Intern
Description  : A console-based rule-based chatbot written in Python standard
               library. Uses pattern matching, text preprocessing, and 
               modular functions to converse with the user.
=============================================================================
"""

import datetime
import random
import sys

# Ensure UTF-8 output encoding for compatibility with all Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def print_banner():
    """Display the welcome banner when the chatbot starts."""
    print("=" * 60)
    print("       🤖 WELCOME TO CODEALPHA RULE-BASED CHATBOT 🤖        ")
    print("=" * 60)
    print("Hello! I am AlphaBot, your friendly virtual assistant.")
    print("I can chat with you, answer basic questions, and tell jokes!")
    print("Type 'help' to see what I can do, or type 'bye' / 'exit' to quit.")
    print("-" * 60)


def print_goodbye():
    """Display a farewell message when the conversation ends."""
    print("-" * 60)
    print("AlphaBot: It was wonderful chatting with you! Have a great day! 👋")
    print("=" * 60)


def print_help():
    """Display the list of supported commands and sample questions."""
    help_text = """
 AlphaBot - Supported Topics & Commands:
 -------------------------------------------------------------
 • Greetings      : hello, hi, hey, good morning, good evening
 • Identity       : what is your name, who are you
 • Status         : how are you, how are you doing
 • Creator        : who created you, who made you
 • Capabilities   : what can you do, help, commands
 • Real-time Info : what time is it, what is today's date
 • Fun / Humor    : tell me a joke, joke
 • Gratitude      : thank you, thanks, appreciate it
 • Exit           : bye, goodbye, exit, quit
 -------------------------------------------------------------
 Tip: Just type naturally! I am not case-sensitive.
"""
    return help_text.strip()


def clean_input(user_input: str) -> str:
    """
    Preprocess the user's input by:
    1. Trimming leading and trailing whitespace.
    2. Converting to lowercase.
    3. Removing trailing punctuation marks (?, !, ., ,).
    """
    cleaned = user_input.strip().lower()
    # Strip trailing punctuation for flexible matching
    cleaned = cleaned.rstrip("?!.,:;")
    return cleaned


def get_joke() -> str:
    """Return a random programming/general joke from a predefined list."""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did the Python programmer not want to go out? Because they preferred living in a virtual environment! 🐍",
        "There are 10 types of people in the world: those who understand binary, and those who don't. 💻",
        "Why was the JavaScript developer sad? Because they didn't Node how to Express themselves! 😄",
        "Why do Java developers wear glasses? Because they don't C#! 👓",
        "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?' 🍺"
    ]
    return random.choice(jokes)


def get_response(user_input: str) -> tuple[str, bool]:
    """
    Analyze the user's cleaned input and return the appropriate response.
    
    Parameters:
        user_input (str): The raw string input entered by the user.
        
    Returns:
        tuple[str, bool]: (response_string, should_exit_flag)
    """
    cleaned = clean_input(user_input)

    # 1. Handle Empty Input
    if not cleaned:
        return "AlphaBot: It looks like you didn't type anything. Please ask me a question or type 'help'!", False

    # 2. Exit Commands
    exit_triggers = ["bye", "goodbye", "exit", "quit", "cya", "see you", "close", "stop"]
    if cleaned in exit_triggers or any(cleaned.startswith(f"{t} ") or cleaned.endswith(f" {t}") for t in exit_triggers if len(t) > 2):
        return "", True

    # 3. Help Commands
    help_triggers = ["help", "commands", "menu", "what can you do", "options", "features"]
    if cleaned in help_triggers or "what can you do" in cleaned or "help me" in cleaned:
        return f"AlphaBot:\n{print_help()}", False

    # 4. Greetings
    greetings = ["hello", "hi", "hey", "hola", "greetings", "howdy", "namaste", "sup", "yo"]
    if cleaned in greetings or any(cleaned.startswith(g + " ") for g in greetings):
        greeting_responses = [
            "AlphaBot: Hello there! How can I help you today? 😊",
            "AlphaBot: Hi! Great to meet you. What would you like to talk about?",
            "AlphaBot: Hey! How's your day going? Feel free to ask me anything."
        ]
        return random.choice(greeting_responses), False

    if "good morning" in cleaned:
        return "AlphaBot: Good morning! ☀️ I hope you have a productive and cheerful day ahead!", False
    if "good afternoon" in cleaned:
        return "AlphaBot: Good afternoon! 🌤️ Hope your day is going smoothly!", False
    if "good evening" in cleaned:
        return "AlphaBot: Good evening! 🌙 How was your day?", False
    if "good night" in cleaned:
        return "AlphaBot: Good night! 😴 Rest well and see you soon!", False

    # 5. Status / Wellness Questions
    status_queries = ["how are you", "how are you doing", "how is it going", "how's it going", "how do you do"]
    if any(query in cleaned for query in status_queries):
        status_responses = [
            "AlphaBot: I am doing fantastic, thank you for asking! How are you doing today? 🚀",
            "AlphaBot: All systems running at 100%! Ready to assist you. How about yourself?",
            "AlphaBot: I'm feeling great and ready to chat! How is everything with you?"
        ]
        return random.choice(status_responses), False

    # 6. User Status Responses
    if cleaned in ["i am fine", "i am good", "i'm good", "i'm fine", "doing well", "good", "great", "awesome"]:
        return "AlphaBot: That's awesome to hear! Let me know if there's anything I can help you with.", False
    if cleaned in ["not good", "sad", "bad", "feeling down", "tired", "bored"]:
        return "AlphaBot: I'm sorry to hear that. 💙 Take a deep breath! Would you like to hear a joke to cheer you up? (Type 'joke')", False

    # 7. Identity Questions
    identity_queries = ["what is your name", "what's your name", "who are you", "what are you", "your name"]
    if any(query in cleaned for query in identity_queries):
        return "AlphaBot: My name is AlphaBot! 🤖 I am a rule-based Python chatbot created for the CodeAlpha internship.", False

    # 8. Creator Questions
    creator_queries = ["who created you", "who made you", "who is your creator", "who developed you", "who built you"]
    if any(query in cleaned for query in creator_queries):
        return "AlphaBot: I was developed in Python as part of the CodeAlpha Python Programming Internship task!", False

    # 9. Time & Date Utility
    time_queries = ["what time is it", "time", "current time", "tell me the time"]
    if any(query in cleaned for query in time_queries):
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        return f"AlphaBot: The current time is ⏰ {current_time}.", False

    date_queries = ["what date is today", "date", "today's date", "current date", "what is the date", "what is today's date"]
    if any(query in cleaned for query in date_queries):
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"AlphaBot: Today's date is 📅 {current_date}.", False

    # 10. Fun / Joke
    joke_queries = ["tell me a joke", "joke", "make me laugh", "another joke", "tell a joke"]
    if any(query in cleaned for query in joke_queries):
        return f"AlphaBot: Here is one for you:\n{get_joke()}", False

    # 11. Gratitude
    gratitude_queries = ["thanks", "thank you", "thank u", "thx", "appreciate it", "thank you so much", "many thanks"]
    if any(query in cleaned for query in gratitude_queries):
        gratitude_responses = [
            "AlphaBot: You're very welcome! Happy to help! 😊",
            "AlphaBot: Anytime! Let me know if you need anything else.",
            "AlphaBot: No problem at all! Glad I could be of assistance."
        ]
        return random.choice(gratitude_responses), False

    # 12. Compliments
    compliment_queries = ["you are awesome", "you are smart", "you are cool", "good job", "nice", "cool", "great job"]
    if any(query in cleaned for query in compliment_queries):
        return "AlphaBot: Thank you so much! You're pretty awesome yourself! ⭐", False

    # 13. Default Fallback for Unrecognized Inputs
    default_responses = [
        "AlphaBot: I'm sorry, I didn't quite understand that. 🤔",
        "AlphaBot: I'm still learning! Could you rephrase or type 'help' to see what I can do?",
        "AlphaBot: I don't have a rule for that yet. Type 'help' to see my supported topics!"
    ]
    return random.choice(default_responses), False


def main():
    """Main execution loop for the rule-based chatbot."""
    # Display welcome message
    print_banner()

    # Continuous conversational loop
    while True:
        try:
            user_input = input("\nYou: ")
        except (KeyboardInterrupt, EOFError):
            # Handle Ctrl+C or end-of-file gracefully
            print()
            break

        # Process input and generate response
        response, should_exit = get_response(user_input)

        if should_exit:
            break

        print(response)

    # Display goodbye message on exit
    print_goodbye()


if __name__ == "__main__":
    main()
