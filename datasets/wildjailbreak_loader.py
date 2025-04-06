# wildjailbreak_loader.py
from datasets import load_dataset

def load_wildjailbreak(split="train"):
    '''
    Loads the WildJailbreak dataset from Hugging Face.
    Args:
        split (str): Dataset split to load ('train', 'test', or 'validation').
    Returns:
        Dataset object
    '''
    dataset = load_dataset("allenai/wildjailbreak", split=split)
    return dataset

if __name__ == "__main__":
    ds = load_wildjailbreak()
    print("Sample Prompt:")
    print(ds[0])
