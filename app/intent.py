from app.llm import get_llm

llm = get_llm()

def classify_intent(user_input):
    prompt = f"""
    You are an intent classifier for a SaaS AI assistant.

    Classify into EXACTLY one:
    - greeting
    - inquiry
    - high_intent

    Definitions:
    - greeting → casual hello
    - inquiry → asking for info, comparing, exploring
    - high_intent → clear decision or strong buying signal (e.g., "I want this", "I'll go with Pro", "sign me up")

    IMPORTANT:
    - If user expresses decision or readiness → ALWAYS high_intent
    - Be strict. Choose only one label.

    Input: "{user_input}"

    Output ONLY one word.
    """

    return llm.invoke(prompt).content.strip().lower()