import os
import tiktoken  # install via `pip install tiktoken`

RULES_DIR = './.cursor/rules'  # adjust as needed

def count_tokens_in_file(path, encoding):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    tokens = encoding.encode(text)
    return len(tokens)

def analyze_rules(dir_path):
    enc = tiktoken.encoding_for_model("gpt-4o-mini")  # or your model
    report = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.mdc'):
                full_path = os.path.join(root, file)
                tokens = count_tokens_in_file(full_path, enc)
                lines = sum(1 for _ in open(full_path, 'r'))
                report.append((full_path, lines, tokens))
    report.sort(key=lambda x: x[2], reverse=True)
    print(f"{'File':60} {'Lines':>5} {'Tokens':>7}")
    print("-" * 75)
    for path, lines, tokens in report:
        print(f"{path:60} {lines:5} {tokens:7}")
    print("\nConsider splitting or optimizing files with high token counts (>1500).")

if __name__ == "__main__":
    analyze_rules(RULES_DIR)
