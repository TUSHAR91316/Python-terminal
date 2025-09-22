import os
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from commands import *
from ai_parser import parse_natural_language

COMMANDS = {
    "pwd": pwd,
    "ls": ls,
    "cd": cd,
    "mkdir": mkdir,
    "rm": rm,
    "cpu": cpu_usage,
    "mem": memory_usage,
    "ps": list_processes
}

def execute_command(user_input):
    parts = user_input.strip().split()
    if not parts:
        return ""
    
    cmd = parts[0]
    args = parts[1:]
    
    if cmd in COMMANDS:
        try:
            return COMMANDS[cmd](*args)
        except TypeError:
            return f"Error: Invalid arguments for '{cmd}'"
    else:
        return parse_natural_language(user_input)

def main():
    print("Python Terminal. Type 'exit' to quit.")
    history = InMemoryHistory()
    session = PromptSession(history=history)
    
    while True:
        try:
            user_input = session.prompt(f"{os.getcwd()}$ ")
            if user_input.lower() == "exit":
                break
            output = execute_command(user_input)
            print(output)
        except KeyboardInterrupt:
            print("\nExiting terminal.")
            break

if __name__ == "__main__":
    main()
