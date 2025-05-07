#!/usr/bin/env python3

import requests
import json
import time
import threading
from pynput.keyboard import Controller
import tkinter as tk
from tkinter import messagebox

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "qwen2.5-coder:1.5b-base"

keyboard = Controller()

def generate_and_type(prompt, model, done_event):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": model, "prompt": prompt, "stream": True},
            stream=True,
        )

        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    text = data["response"]
                    for char in text:
                        keyboard.type(char)
                        time.sleep(0.01)
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        done_event.set()

def on_submit():
    prompt = prompt_entry.get()
    model = model_entry.get().strip()
    if not prompt:
        messagebox.showwarning("Input Required", "Please enter a prompt.")
        return
    if not model:
        messagebox.showwarning("Model Required", "Please enter a model name.")
        return

    root.withdraw()
    done_event = threading.Event()

    threading.Thread(target=generate_and_type, args=(prompt, model, done_event), daemon=True).start()

    def check_done():
        if done_event.is_set():
            root.deiconify()
            messagebox.showinfo("Done", "Typing complete.")
        else:
            root.after(500, check_done)

    check_done()

def on_clear():
    prompt_entry.delete(0, tk.END)

# Tkinter setup
root = tk.Tk()
root.title("Ollama Typing Prompt")

# Model entry
tk.Label(root, text="Model to use:").pack(pady=(10, 0))
model_entry = tk.Entry(root, width=50)
model_entry.insert(0, DEFAULT_MODEL)
model_entry.pack(padx=10, pady=5)

# Prompt input
tk.Label(root, text="Enter your prompt:").pack(pady=(10, 0))
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack(padx=10, pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

submit_btn = tk.Button(button_frame, text="Submit and Type", command=on_submit)
submit_btn.pack(side=tk.LEFT, padx=5)

clear_btn = tk.Button(button_frame, text="Clear Prompt", command=on_clear)
clear_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()
