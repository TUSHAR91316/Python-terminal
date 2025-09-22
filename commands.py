import os
import shutil
import psutil

# ------------------------
# FILE & DIRECTORY OPERATIONS
# ------------------------

def pwd():
    return os.getcwd()

def ls(path="."):
    try:
        return "\n".join(os.listdir(path))
    except FileNotFoundError:
        return f"Error: Path '{path}' does not exist."

def cd(path):
    try:
        os.chdir(path)
        return f"Changed directory to {os.getcwd()}"
    except FileNotFoundError:
        return f"Error: Path '{path}' does not exist."

def mkdir(path):
    try:
        os.mkdir(path)
        return f"Directory '{path}' created."
    except FileExistsError:
        return f"Error: Directory '{path}' already exists."

def rm(path):
    if os.path.isdir(path):
        try:
            shutil.rmtree(path)
            return f"Directory '{path}' removed."
        except Exception as e:
            return f"Error: {e}"
    elif os.path.isfile(path):
        try:
            os.remove(path)
            return f"File '{path}' removed."
        except Exception as e:
            return f"Error: {e}"
    else:
        return f"Error: '{path}' does not exist."

# ------------------------
# SYSTEM MONITORING
# ------------------------

def cpu_usage():
    return f"CPU Usage: {psutil.cpu_percent()}%"

def memory_usage():
    mem = psutil.virtual_memory()
    return f"Memory Usage: {mem.percent}% ({mem.used/1024**2:.2f}MB/{mem.total/1024**2:.2f}MB)"

def list_processes():
    processes = [p.info for p in psutil.process_iter(['pid', 'name'])]
    return "\n".join([f"{p['pid']}: {p['name']}" for p in processes])
