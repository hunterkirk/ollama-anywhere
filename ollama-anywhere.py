#!/usr/bin/env python3

import requests
import json
import time
from pynput.keyboard import Controller
import tkinter as tk

window = tk.Tk()


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5-coder:1.5b-base"

keyboard = Controller()

prompt = input("Enter your prompt: ")
print("Select destination")
time.sleep(2)

response = requests.post(
    OLLAMA_URL,
    json={"model": MODEL, "prompt": prompt, "stream": True},
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
