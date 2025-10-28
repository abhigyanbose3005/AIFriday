import re

def validate_input(user_input):
    # Guardrail 1: Check for empty input
    if not user_input.strip():
        return False, "Input cannot be empty."

    # Guardrail 2: Check for profanity (simple example)
    banned_words = ["badword1", "badword2"]
    if any(word in user_input.lower() for word in banned_words):
        return False, "Inappropriate language is not allowed."

    # Guardrail 3: Check for prompt injection attempts
    if re.search(r"(ignore previous|pretend to be|you are now)", user_input, re.IGNORECASE):
        return False, "Input contains unsafe instructions."

    # Guardrail 4: Limit input length
    if len(user_input) > 500:
        return False, "Input is too long. Please keep it under 500 characters."

    return True, "Input is valid."
	

user_input = input("Enter your question: ")
is_valid, message = validate_input(user_input)

if is_valid:
    # Proceed with AI model
    print("Processing:", user_input)
else:
    print("Validation failed:", message)
