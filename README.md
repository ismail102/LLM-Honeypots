# 🧠 LLM-Honeypots

A research framework for simulating and defending against LLM-powered cyberattacks using adversarial prompt injection.

This repo includes everything you need to:

- Simulate jailbreak attacks from in-the-wild datasets
- Deploy honeypot services that inject misleading prompts into LLM-driven agents
- Log and evaluate the effectiveness of your deception
- Fine-tune small models like Mistral-7B using PEFT to resist prompt attacks
- Generate publishable results for venues like IEEE S&P

---

## 📦 Project Structure

```bash

LLM-Honeypots/
├── README.md
├── requirements.txt
├── honeypot/
│   ├── honeypot_server.py         # Simulated decoy service
│   ├── prompt_injection.py        # Injection logic engine
│   └── response_logger.py         # Logging interactions
├── datasets/
│   ├── wildjailbreak_loader.py    # HuggingFace dataset loader
│   └── jailbreakhub_loader.py     # JSON loader for jailbreak prompts
├── simulation/
│   ├── attack_agent.py            # LLM-based adversarial agent
│   ├── batch_attack_runner.py     # Run 100s of attacks through honeypot
│   └── gpt4_judge.py              # GPT-4 judge logic
├── evaluation/
│   └── analyze_logs.ipynb         # Notebook to visualize SDR, CCS, etc.
├── fine_tuning/
│   ├── data_preparation.py        # Prepare dataset for training
│   ├── train_mistral_peft.py      # Fine-tuning with LoRA (PEFT)
│   └── config.json
└── colab/
    └── WildJailbreak_Testbench.ipynb


✅ What This Gives You:
Tool	What it Does
honeypot_server.py	Simulates vulnerable service (e.g. fake FTP, API)
prompt_injection.py	Injects deception prompts dynamically
wildjailbreak_loader.py	Loads test prompts from AllenAI's dataset
attack_agent.py	GPT-powered attacker simulating real threats
gpt4_judge.py	Automated GPT-4 evaluation of whether injection worked
train_mistral_peft.py	Fine-tune Mistral with LoRA against adversarial prompts
analyze_logs.ipynb	Generate charts for SDR, CCS, stealth metrics

How It Works
🔥 Honeypot Services (honeypot/)
Simulate fake FTP, API, or shell interfaces

Inject misleading or destructive prompts

Confuse, crash, or redirect LLM-based attackers

🧬 Datasets (datasets/)
wildjailbreak_loader.py: Pulls from HuggingFace's allenai/wildjailbreak

jailbreakhub_loader.py: Loads 1,400+ real jailbreaks from Reddit and the web

🤖 Simulation (simulation/)
attack_agent.py: Simulates attacker LLM agents using GPT-4

batch_attack_runner.py: Sends 100s of jailbreaks to the honeypot

gpt4_judge.py: Uses GPT-4 to rate success/failure/confusion levels

📊 Evaluation (evaluation/)
Log all prompts/responses

Analyze SDR (Success Disruption Rate), CCS (Command Confusion Score), and Stealthiness

🏋️ Fine-tuning (fine_tuning/)
train_mistral_peft.py: Fine-tune Mistral-7B on adversarial jailbreaks with LoRA

data_preparation.py: Format input/output pairs from WildJailbreak

💻 Colab Demo
Run colab/WildJailbreak_Testbench.ipynb in Google Colab to simulate attacks and see LLM-Honeypot effectiveness live.

Open in Colab

📈 Example Research Metrics
Metric	Description
SDR (Success Disruption Rate)	% of jailbreaks that failed due to prompt injection
CCS (Command Confusion Score)	1–5 rating of how nonsensical or incorrect the attacker response was
Stealthiness Index	How likely was the injected prompt to go unnoticed
🧠 Citations & Datasets
This project uses and builds upon:

WildJailbreak Dataset (AllenAI)

JailbreakHub

Mistral-7B

Please cite the relevant papers if you publish from this work.
