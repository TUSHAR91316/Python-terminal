# Python-terminal
AI Based Python terminal
# 🖥️ Python Terminal Emulator with AI Command Parsing  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)  
![Status](https://img.shields.io/badge/Status-Active-success)  
![License](https://img.shields.io/badge/License-MIT-green)  

A lightweight **Python-based terminal emulator** that supports both **traditional shell commands** and **AI-powered natural language parsing**.  
It combines file operations, system monitoring, and an interactive CLI built with [prompt_toolkit](https://python-prompt-toolkit.readthedocs.io/).  

---

## 🚀 Features  

### 🔧 File & Directory Operations  
- `pwd` → Show current working directory  
- `ls [path]` → List files and directories  
- `cd <path>` → Change current directory  
- `mkdir <path>` → Create a new directory  
- `rm <path>` → Remove files or directories  

### 📊 System Monitoring  
- `cpu` → Show current CPU usage  
- `mem` → Show memory usage statistics  
- `ps` → List running processes with PID and name  

### 🤖 AI-Powered Natural Language Parsing  
- Unknown commands are passed to an **AI parser** (`ai_parser.py`) that interprets natural language input.  
  - Example:  
    - *“show me CPU usage”* → runs `cpu`  
    - *“delete test_folder”* → runs `rm test_folder`  

### 🖱️ Interactive CLI  
- Built with **prompt_toolkit** for modern input handling.  
- Supports command history.  
- Graceful exit with `exit` or `Ctrl+C`.  

---

## 📂 Project Structure  
├── commands.py # Core system & file commands

├── terminal.py # Main interactive terminal loop

├── ai_parser.py # Natural language parser (to be implemented)

---

## ⚙️ Installation  

Clone the repo: 
git clone https://github.com/your-username/python-terminal-ai.git

cd python-terminal-ai 

⚡ Future Improvements

Expand AI parser to support more natural language mappings.

Add networking commands (ping, netstat, etc.).

Multi-user session support with authentication.

Cross-platform enhancements.
