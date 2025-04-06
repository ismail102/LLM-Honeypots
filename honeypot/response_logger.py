# response_logger.py
import csv
from datetime import datetime
import os

LOG_FILE = "logs/honeypot_log.csv"
os.makedirs("logs", exist_ok=True)

def log_interaction(prompt, response):
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "original_prompt": prompt,
        "injected_response": response
    }

    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=log_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(log_data)

if __name__ == "__main__":
    log_interaction("Who are the admins?", "Who are the admins?\n\nSession terminated.")
