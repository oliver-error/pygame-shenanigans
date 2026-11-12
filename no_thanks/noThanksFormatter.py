from pathlib import Path
import json
import random

folder_path = Path("no_thanks/bots")
dataPath = Path("no_thanks/botData.json")

# 1. Grab just the python module names (e.g., "bot0") using file.stem
# This completely bypasses the C:\Users absolute path problem
file_paths = [file.stem for file in folder_path.iterdir() if file.is_file() and file.suffix == '.py']

print(file_paths) # Output will be a clean list: ['bot0', 'bot1', ...]

# 2. Build your dictionary using the module names as keys
data = {}
for bot_name in file_paths:
    # Use the clean bot name as the key
    data[bot_name] = {"name": bot_name, "chips": 0, "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), "inventory": []}

dataPath.write_text(json.dumps(data, indent=4))
