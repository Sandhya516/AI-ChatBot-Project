import tkinter as tk
from tkinter import scrolledtext
import random

# Chatbot responses
def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return random.choice(["Hello! 😊", "Hi there!", "Hey! How can I help you?"])

    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! 😊"

    elif "your name" in user_input:
        return "I'm your AI Assistant 🤖"

    elif "ai" in user_input:
        return "AI stands for Artificial Intelligence. It helps machines think and learn!"

    elif "python" in user_input:
        return "Python is a powerful programming language used in AI, web, and more. Example: FastAPI!"

    elif "api" in user_input:
        return "A modern, high-performance framework based on standard Python type hints for building and deploying AI and machine learning applications!"
  
    elif "ml" in user_input:
        return "ML stands for Machine Learning. It improves accuracy in predictions over time!"

    elif "bye" in user_input:
        return "Bye, Have a great day! 👋"

    else:
        return "Sorry, I didn't understand that. Can you try something else?"

# Send message
def send_message():
    user_text = entry_box.get()
    if user_text.strip() == "":
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_text + "\n")

    response = get_response(user_text)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")

    chat_area.config(state=tk.DISABLED)
    entry_box.delete(0, tk.END)

# GUI Setup
window = tk.Tk()
window.title("AI Chatbot")
window.geometry("400x500")

chat_area = scrolledtext.ScrolledText(window,wrap=tk.WORD,state=tk.DISABLED)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry_box = tk.Entry(window)
entry_box.pack(padx=10, pady=10, fill=tk.X)

send_button = tk.Button(window,text="Send",command=send_message)
send_button.pack(pady=5)

window.mainloop()
