from datasets import load_dataset

# Load the dataset
dataset = load_dataset("HuggingFaceFW/fineweb-edu")

# Inspect the size of each split
for split in dataset.keys():
    print(f"Split: {split}")
    print(f"Number of examples: {len(dataset[split])}")
    print(f"Features: {dataset[split].features}")
