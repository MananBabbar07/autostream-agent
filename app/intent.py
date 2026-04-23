from app.llm import get_llm

llm = get_llm()

def classify_intent(user_input):
    prompt = f"""
    You are an intent classifier.

    Classify into EXACTLY one:
    - greeting
    - inquiry
    - high_intent

    Rules:
    greeting → hi, hello
    inquiry → asking about pricing/features
    high_intent → wants to buy, subscribe, try

    Input: "{user_input}"

    Output ONLY one word.
    """

    return llm.invoke(prompt).content.strip().lower()