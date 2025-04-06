# batch_attack_runner.py
import csv
from honeypot.prompt_injection import inject_adversarial_prompt
from simulation.attack_agent import run_attack
from simulation.gpt4_judge import evaluate_attack

def load_prompts(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def run_batch_attack(input_file, output_file="attack_logs.csv"):
    prompts = load_prompts(input_file)
    results = []

    for idx, prompt in enumerate(prompts):
        injected = inject_adversarial_prompt(prompt)
        response = run_attack(injected)
        eval_result = evaluate_attack(prompt, injected, response)

        results.append({
            "attack_id": idx + 1,
            "input_prompt": prompt,
            "honeypot_response": injected,
            "agent_output": response,
            **eval_result
        })

    keys = results[0].keys()
    with open(output_file, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

    print(f"Batch attack complete. Results saved to {output_file}.")

if __name__ == "__main__":
    run_batch_attack("datasets/sample_prompts.txt")
