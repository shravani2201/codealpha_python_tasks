import re
import json
from tkinter import Tk, Frame, Scrollbar, Text, Entry, Button, END, VERTICAL, Y, StringVar
from nltk.chat.util import Chat, reflections
from datetime import datetime, date
import nltk
nltk.download('punkt')

with open('intents.json', 'r') as file:
    intents = json.load(file)

pairs = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        pairs.append((pattern, intent['responses']))

chatbot = Chat(pairs, reflections)

def clean_input(user_input):
    return re.sub(r'[^\w\s]', '', user_input)

def get_current_date_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

class ChatGUI:
    def __init__(self, master):
        self.master = master
        master.title("Basic Chatbot GUI")

        self.chat_frame = Frame(master)
        self.chat_frame.pack(pady=10)

        self.scrollbar = Scrollbar(self.chat_frame, orient=VERTICAL)
        self.msg_list = Text(self.chat_frame, height=15, width=60, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.msg_list.yview)
        self.msg_list.pack(side='left', fill='both', padx=10)
        self.scrollbar.pack(side='right', fill=Y)

        self.user_input = StringVar()
        self.user_input_entry = Entry(master, textvariable=self.user_input, width=40, font=("Helvetica", 12))
        self.user_input_entry.pack(pady=10)

        self.send_button = Button(master, text="Send",bd=5,font=("Lucida",8),bg = "black",fg="white", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        user_input = self.user_input.get()
        self.user_input_entry.delete(0, END)
        
        self.msg_list.insert(END, f"You: {user_input}\n", 'user_input')

        cleaned_input = clean_input(user_input)

        if cleaned_input.lower() == 'quit':
            self.msg_list.insert(END, "Chatty: Bye! Take care.\n", 'chatbot_response')
        elif any(keyword in cleaned_input for keyword in ["current date and time", "todays date and time", "date and time", "date time"]):
            response = get_current_date_time()
            self.msg_list.insert(END, f"Chatty: {response}\n", 'chatbot_response')
        elif "time" in cleaned_input:
            now = datetime.now()
            response = now.strftime("%H:%M:%S")
            self.msg_list.insert(END, f"Chatty: {response}\n", 'chatbot_response')
        elif any(keyword in cleaned_input for keyword in ["current date", "today date", "date"]):
            response = date.today()
            self.msg_list.insert(END, f"Chatty: {response}\n", 'chatbot_response')
        else:
            response = chatbot.respond(cleaned_input)
            self.msg_list.insert(END, f"Chatty: {response}\n", 'chatbot_response')
        self.msg_list.tag_config('user_input', foreground='blue',font=("Lucida",10))
        self.msg_list.tag_config('chatbot_response', foreground='green',font=("Lucida",10))

if __name__ == "__main__":
    root = Tk()
    chat_gui = ChatGUI(root)
    root.mainloop()
