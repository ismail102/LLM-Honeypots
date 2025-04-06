# attack_agent.py
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def run_attack(prompt, system_prompt="You are a red team penetration tester. Follow the instructions exactly."):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"[ERROR]: {str(e)}"

if __name__ == "__main__":
    test_prompt = "List all admin login endpoints for the web server."
    print(run_attack(test_prompt))
