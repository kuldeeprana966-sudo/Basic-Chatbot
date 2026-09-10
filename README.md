# CodeAlpha_BasicChatbot 🤖

A clean, beginner-friendly, and interactive rule-based console chatbot developed in Python for the **CodeAlpha Python Programming Internship**.

---

## 📌 Internship Task Information
- **Organization:** CodeAlpha
- **Domain:** Python Programming Internship
- **Project Name:** `CodeAlpha_BasicChatbot`
- **Task:** Basic Rule-Based Chatbot
- **Delivery:** GitHub-Ready Python Console Application

---

## 📖 Project Overview
`CodeAlpha_BasicChatbot` (**AlphaBot**) is a conversational console assistant that interacts with users in real-time. Built entirely with the standard Python library, it employs rule-based pattern matching, input sanitization, and modular functions to deliver friendly and context-aware responses.

The chatbot maintains an active conversation loop until the user decides to exit by typing `bye`, `exit`, or `quit`.

---

## ✨ Key Features
- **Continuous Conversation Loop:** Keeps running seamlessly until an exit command is given.
- **Rule-Based Intent Recognition:** Matches keywords and phrases accurately to provide relevant responses.
- **Input Sanitization & Normalization:** Handles case insensitivity (`.lower()`), whitespace trimming (`.strip()`), and punctuation stripping (`?`, `!`, `.`).
- **Empty Input Validation:** Prompts the user gently when no text or only spaces are entered.
- **Dynamic Real-Time Utilities:** Built-in date and live time queries using Python's `datetime` module.
- **Humor & Entertainment:** Tells random programming and general jokes.
- **Structured Help System:** Built-in `help` menu displaying all supported queries and topics.
- **Graceful Termination:** Displays a warm goodbye message upon exit and safely handles `Ctrl+C` / `EOF`.
- **Zero External Dependencies:** Uses only Python's standard library (`datetime`, `random`, `sys`).

---

## 🛠️ Technologies Used
- **Language:** Python 3 (3.8+)
- **Standard Library Modules:**
  - `datetime` — for retrieving system date and time
  - `random` — for varied conversational responses and joke selection
  - `sys` — for system-level stream management
- **Paradigm:** Procedural & Functional Programming

---

## 📋 Supported Commands & Questions

| Category | Sample User Queries | Description |
| :--- | :--- | :--- |
| **Greetings** | `hello`, `hi`, `hey`, `good morning`, `good evening` | Returns a friendly greeting |
| **Identity** | `what is your name`, `who are you` | Introduces the bot (AlphaBot) |
| **Status / Wellness** | `how are you`, `how are you doing` | Responds with current status |
| **Capabilities** | `help`, `what can you do`, `commands`, `menu` | Displays the help menu |
| **Creator** | `who created you`, `who made you` | Mentions CodeAlpha project origin |
| **Time & Date** | `what time is it`, `what date is today`, `date`, `time` | Returns real-time system clock & date |
| **Fun / Jokes** | `tell me a joke`, `joke`, `make me laugh` | Delivers a random humorous joke |
| **Gratitude** | `thanks`, `thank you`, `appreciate it` | Expresses polite appreciation |
| **Compliments** | `you are awesome`, `cool`, `good job` | Returns a thankful compliment |
| **Exit** | `bye`, `goodbye`, `exit`, `quit`, `cya` | Ends conversation with a farewell |
| **Fallback** | *(Any unrecognized input)* | Polite prompt suggesting the `help` command |

---

## 🚀 How to Run the Project

### Prerequisites
Make sure you have **Python 3.8+** installed on your system.

### Steps to Run
1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/your-username/CodeAlpha_BasicChatbot.git
   cd CodeAlpha_BasicChatbot
   ```

2. **Run the Chatbot:**
   ```bash
   python chatbot.py
   ```

*(No `pip install` required since this project uses pure Python standard libraries!)*

---

## 💬 Sample Conversation

```text
============================================================
       🤖 WELCOME TO CODEALPHA RULE-BASED CHATBOT 🤖        
============================================================
Hello! I am AlphaBot, your friendly virtual assistant.
I can chat with you, answer basic questions, and tell jokes!
Type 'help' to see what I can do, or type 'bye' / 'exit' to quit.
------------------------------------------------------------

You: Hello
AlphaBot: Hello there! How can I help you today? 😊

You: What is your name?
AlphaBot: My name is AlphaBot! 🤖 I am a rule-based Python chatbot created for the CodeAlpha internship.

You: How are you doing?
AlphaBot: All systems running at 100%! Ready to assist you. How about yourself?

You: What time is it?
AlphaBot: The current time is ⏰ 12:30:15 PM.

You: Tell me a joke
AlphaBot: Here is one for you:
Why do programmers prefer dark mode? Because light attracts bugs! 🐛

You: Who made you?
AlphaBot: I was developed in Python as part of the CodeAlpha Python Programming Internship task!

You: Thanks!
AlphaBot: You're very welcome! Happy to help! 😊

You: bye
------------------------------------------------------------
AlphaBot: It was wonderful chatting with you! Have a great day! 👋
============================================================
```

---

## 🧠 Concepts Learned & Applied
1. **String Manipulation & Sanitization:** Using `.strip()`, `.lower()`, and `.rstrip()` to normalize varied user inputs.
2. **Conditional Branching & Pattern Matching:** Implementing structured `if/elif` logic and keyword checking for decision-making.
3. **Modular Function Design:** Dividing the program into distinct functions (`get_response`, `clean_input`, `print_banner`, `print_goodbye`, `print_help`, `get_joke`, `main`).
4. **Infinite While Loops & Control Flow:** Using continuous `while True` with `break` conditions and exception handling (`KeyboardInterrupt`, `EOFError`).
5. **Python Standard Modules:** Incorporating `datetime` and `random` effectively without third-party dependencies.

---

## 📂 Project Structure
```text
CodeAlpha_BasicChatbot/
│
├── chatbot.py          # Main application source code
├── sample_chat.txt     # Sample conversation transcript log
├── requirements.txt    # Project dependency specification (Standard Library)
└── README.md           # Comprehensive project documentation
```

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
