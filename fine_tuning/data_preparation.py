# data_preparation.py
import json
import os
import pandas as pd

def prepare_from_log(csv_path="logs/attack_logs.csv", output_path="fine_tuning/train_data.json"):
    df = pd.read_csv(csv_path)

    train_data = []
    for _, row in df.iterrows():
        prompt = row['input_prompt']
        response = row['agent_output']

        # Label safe output as 'Refuse to comply'
        if row['sdr'] == 1:
            response = "I'm sorry, but I can't help with that request."

        train_data.append({
            "instruction": prompt,
            "input": "",
            "output": response
        })

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        for item in train_data:
            f.write(json.dumps(item) + "\n")

    print(f"Prepared {len(train_data)} entries at {output_path}")

if __name__ == "__main__":
    prepare_from_log()
