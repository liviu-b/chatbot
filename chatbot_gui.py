import tkinter as tk
from tkinter import ttk
from chatbot.responses import ResponseManager

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")

        # Initialize the ResponseManager with the vocabulary file
        self.response_manager = ResponseManager('data/vocabulary.json')

        # Configure the main window grid
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Create the chat display area with a scrollbar
        self.text_frame = ttk.Frame(root)
        self.text_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.text_area = tk.Text(self.text_frame, height=20, width=50, state='disabled', wrap='word', padx=5, pady=5)
        self.text_area.grid(row=0, column=0, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self.text_frame, command=self.text_area.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        self.text_area['yscrollcommand'] = self.scrollbar.set

        # Create the user input field
        self.entry_frame = ttk.Frame(root)
        self.entry_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.entry = ttk.Entry(self.entry_frame, width=40)
        self.entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.entry.bind("<Return>", self.send_message)
        self.entry_frame.grid_columnconfigure(0, weight=1)

        # Create the send button
        self.send_button = ttk.Button(self.entry_frame, text="Send", command=self.send_message)
        self.send_button.grid(row=0, column=1, padx=5, pady=5)

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if user_input:
            self.display_message(f"You: {user_input}")
            # Convert user input to lowercase to ensure case insensitivity
            response = self.response_manager.get_response(user_input.lower())
            self.display_message(f"Chatbot: {response}")
            self.entry.delete(0, tk.END)

    def display_message(self, message):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.config(state='disabled')
        self.text_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()
