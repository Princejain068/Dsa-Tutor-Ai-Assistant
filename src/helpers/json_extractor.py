import re

def extract_json(text: str):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if not match:
        return None
    return match.group(0)