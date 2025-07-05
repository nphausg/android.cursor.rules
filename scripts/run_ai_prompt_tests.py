import os
import openai

# Set your OpenAI API key as environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

TEST_PROMPTS_DIR = "./.cursor/tests"
MODEL_NAME = "gpt-4o-mini"  # adjust as needed

# Define simple expectations per test file, e.g.:
EXPECTED_KEYWORDS = {
    "frontend-react-hooks.test": ["cleanup", "useEffect"],
    "unit-test-bdd.test": ["given_", "when_", "then_"],
}

def load_test_prompts():
    prompts = {}
    for fname in os.listdir(TEST_PROMPTS_DIR):
        if fname.endswith(".test"):
            with open(os.path.join(TEST_PROMPTS_DIR, fname), "r", encoding="utf-8") as f:
                prompts[fname] = f.read()
    return prompts

def run_test(prompt_name, prompt_text):
    messages = [
        {"role": "system", "content": "You are a helpful coding assistant applying coding rules."},
        {"role": "user", "content": prompt_text},
    ]
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=messages,
        max_tokens=200,
        temperature=0.0,
    )
    return response.choices[0].message.content.lower()

def main():
    prompts = load_test_prompts()
    failed = False
    for name, prompt in prompts.items():
        print(f"Running test: {name}")
        output = run_test(name, prompt)
        expected_words = EXPECTED_KEYWORDS.get(name, [])
        missing = [word for word in expected_words if word not in output]
        if missing:
            print(f"❌ Test {name} failed. Missing expected keywords: {missing}")
            failed = True
        else:
            print(f"✅ Test {name} passed.")
    if failed:
        exit(1)

if __name__ == "__main__":
    main()
