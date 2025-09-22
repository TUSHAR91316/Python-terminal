import re
import shutil
from commands import mkdir, rm, cd

def parse_natural_language(query):
    query = query.lower()
    
    # Create folder
    if "create" in query and "folder" in query:
        folder_name = re.search(r"called (\w+)", query)
        if folder_name:
            return mkdir(folder_name.group(1))
    
    # Move file
    if "move" in query and "into" in query:
        parts = re.findall(r"(\w+\.\w+|\w+)", query)
        if len(parts) >= 2:
            src = parts[0]
            dst = parts[-1]
            try:
                shutil.move(src, dst)
                return f"Moved {src} into {dst}"
            except Exception as e:
                return f"Error: {e}"
    
    # Delete folder/file
    if "delete" in query or "remove" in query:
        target = re.search(r"(file|folder) (\w+)", query)
        if target:
            return rm(target.group(2))
    
    return "Sorry, could not understand the command."
