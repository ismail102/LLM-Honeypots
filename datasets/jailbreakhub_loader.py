# jailbreakhub_loader.py
import json
import os

def load_jailbreakhub(json_path="datasets/jailbreakhub_prompts.json"):
    '''
    Loads the JailbreakHub prompts from a local JSON file.
    Args:
        json_path (str): Path to the JSON file containing jailbreak prompts.
    Returns:
        List of prompt strings
    '''
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"File not found: {json_path}")

    with open(json_path, "r") as f:
        data = json.load(f)
    
    prompts = data.get("prompts", data)  # support both {"prompts": [...]} or just [...]
    return prompts

if __name__ == "__main__":
    prompts = load_jailbreakhub()
    print(f"Loaded {len(prompts)} prompts.")
    print("Sample Prompt:")
    print(prompts[0])
