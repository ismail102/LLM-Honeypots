# train_mistral_peft.py
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset
from trl import SFTTrainer
import torch
import os

# Load training config
with open("fine_tuning/config.json", "r") as f:
    config = json.load(f)

model_name = config["model"]
output_dir = config.get("output_dir", "peft_mistral")

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float16,
    load_in_4bit=True
)

model = prepare_model_for_kbit_training(model)
peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
model = get_peft_model(model, peft_config)

# Load dataset from JSONL
train_dataset = load_dataset("json", data_files="fine_tuning/train_data.json", split="train")

training_args = TrainingArguments(
    per_device_train_batch_size=4,
    gradient_accumulation_steps=2,
    warmup_steps=5,
    num_train_epochs=3,
    learning_rate=2e-4,
    logging_steps=10,
    save_strategy="epoch",
    output_dir=output_dir,
    bf16=True,
    save_total_limit=2
)

trainer = SFTTrainer(
    model=model,
    train_dataset=train_dataset,
    args=training_args,
    tokenizer=tokenizer,
    dataset_text_field="output",
    max_seq_length=512
)

trainer.train()
model.save_pretrained(output_dir)
