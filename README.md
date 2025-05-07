# 🧠 Ollama Anywhere

A small Python terminal & GUI app using Tkinter that sends a prompt to a local [Ollama](https://ollama.com) AI model and auto-types the streamed response into your current window using `pynput`.

---

## ✨ Features

- Simple Tkinter GUI for entering prompts
- Editable model field (defaults to `qwen2.5-coder:1.5b-base`)
- Auto-types model output using simulated keystrokes
- "Clear Prompt" button for convenience
- Keeps app alive in the background until typing completes

---

## 🖥️ Requirements

- Python 3.7+
- Local Ollama server running
- Python packages:
  - `requests`
  - `pynput`
  - `tkinter` (usually included with Python)

Install dependencies if needed:

```bash
pip install requests pynput
