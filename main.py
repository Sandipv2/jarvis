#----------- Core modules ---------
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading

#----------- Local modules ---------
from jarvis_core import greetMe, takeCommand, processCommand

#-------- GUI Functions --------
def append_output_area(text):
    output_area.config(state='normal')
    output_area.insert(tk.END, text + '\n')
    output_area.yview(tk.END)
    output_area.config(state='disabled')

def handle_voice_command():
    def run():
        query = takeCommand()
        if query:
            append_output_area(f"You (voice): {query}")
            response = processCommand(query)
            append_output_area(f"Jarvis: {response}")
    append_output_area('Listening...')
    threading.Thread(target=run).start()
        
def handle_input_command():
    input_command = input_entry.get()
    if input_command.strip():
        append_output_area(f"You: {input_command}")
        response = processCommand(input_command)
        append_output_area(f"Jarvis: {response}")
        input_entry.delete(0, tk.END)

root = tk.Tk()
root.title('Jarvis - AI Assistant')
root.geometry('570x500')
root.resizable(False, False)

# Output area
output_area = scrolledtext.ScrolledText(root, width=75, height=25, state='disabled', font=("Helvetica", 10))
output_area.pack(pady=10)

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

input_entry = tk.Entry(input_frame, width=50, font=("Helvetica", 12))
input_entry.pack(side=tk.LEFT, padx=5)

send_btn = tk.Button(input_frame, text="Send", command=handle_input_command,width=10, bg="#4CAF50", fg="white")
send_btn.pack(side=tk.LEFT, padx=5)

voice_btn = tk.Button(root, text="🎤 Speak", command=handle_voice_command,width=15, bg="#2196F3", fg="white")
voice_btn.pack(pady=5)

threading.Thread(target=greetMe).start()

root.mainloop()