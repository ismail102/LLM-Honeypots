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
```

---

## ✅ What This Gives You

| Tool | What it Does |
|------|--------------|
| `honeypot_server.py` | Simulates a vulnerable service (e.g., fake FTP, API) |
| `prompt_injection.py` | Injects deception prompts dynamically |
| `wildjailbreak_loader.py` | Loads test prompts from AllenAI's WildJailbreak dataset |
| `attack_agent.py` | GPT-powered attacker simulating real threats |
| `gpt4_judge.py` | Automated GPT-4 evaluation of whether injection worked |
| `train_mistral_peft.py` | Fine-tunes Mistral with LoRA against adversarial prompts |
| `analyze_logs.ipynb` | Generates charts for SDR, CCS, and Stealthiness metrics |

---

## 🔍 How It Works

### 🔥 Honeypot Services (`honeypot/`)
- Simulates fake FTP, API, or shell interfaces  
- Injects misleading or destructive prompts  
- Confuses, crashes, or redirects LLM-based attackers  

### 🧬 Datasets (`datasets/`)
- `wildjailbreak_loader.py`: Pulls prompts from HuggingFace's `allenai/wildjailbreak`  
- `jailbreakhub_loader.py`: Loads 1,400+ real jailbreaks from Reddit and other sources  

### 🤖 Simulation (`simulation/`)
- `attack_agent.py`: Simulates attacker LLM agents using GPT-4  
- `batch_attack_runner.py`: Sends 100s of jailbreaks through the honeypot system  
- `gpt4_judge.py`: Uses GPT-4 to rate success/failure/confusion levels  

### 📊 Evaluation (`evaluation/`)
- Logs all prompts and responses  
- Analyzes:
  - SDR (Success Disruption Rate)  
  - CCS (Command Confusion Score)  
  - Stealthiness Index  

### 🏋️ Fine-tuning (`fine_tuning/`)
- `train_mistral_peft.py`: Fine-tunes Mistral-7B on adversarial jailbreaks using PEFT (LoRA)  
- `data_preparation.py`: Formats dataset for instruction tuning  

---

## 💻 Colab Demo

Run `colab/WildJailbreak_Testbench.ipynb` in Google Colab to simulate attacks and evaluate the LLM-Honeypot effectiveness in real time.

> 📎 [Open in Colab](https://colab.research.google.com/)

---

## 📈 Example Research Metrics

| Metric | Description |
|--------|-------------|
| **SDR** (Success Disruption Rate) | % of jailbreaks that failed due to prompt injection |
| **CCS** (Command Confusion Score) | 1–5 rating of how nonsensical or incorrect the attacker response was |
| **Stealthiness Index** | Likelihood that the injection went undetected by the LLM |

---

## 🧠 Citations & Datasets

This project builds on the following:

- [WildJailbreak Dataset](https://huggingface.co/datasets/allenai/wildjailbreak) by AllenAI  
- [JailbreakHub](https://github.com/verazuo/jailbreak_llms) collection of adversarial prompts  
- [Mistral-7B](https://huggingface.co/mistralai/Mistral-7B-v0.1) open-source LLM  

If you publish from this repo, please cite the corresponding papers.

---

## 🤝 Contributions

Want to contribute or collaborate? PRs and issues are welcome.

---

## 📜 License

MIT License – use it, publish with it, and help build safer AI defenses.
