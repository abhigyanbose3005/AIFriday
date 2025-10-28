import re

def validate_output(ai_output):
    # Guardrail 1: Check for empty or null output
    if not ai_output or not ai_output.strip():
        return False, "Output is empty."

    # Guardrail 2: Check for profanity or offensive content
    banned_words = ["badword1", "offensive_term"]
    if any(word in ai_output.lower() for word in banned_words):
        return False, "Output contains inappropriate content."

    # Guardrail 3: Check for hallucinated URLs or fake citations
    if re.search(r"https?://[^\s]+", ai_output) and "example.com" in ai_output:
        return False, "Output may contain fabricated links."

    # Guardrail 4: Check for unsupported instructions
    if "as an AI language model" in ai_output.lower():
        return False, "Output contains meta-AI disclaimers."

    return True, "Output is valid."


ai_response = "Visit https://example.com for more info."

is_valid, message = validate_output(ai_response)

if is_valid:
    print("✅ Safe to display:", ai_response)
else:
    print("❌ Blocked:", message)
