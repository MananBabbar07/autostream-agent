import json
from app.llm import get_llm

llm = get_llm()

def load_knowledge():
    with open("data/knowledge_base.json") as f:
        return json.load(f)

def retrieve_answer(query, messages):
    kb = load_knowledge()
    context = json.dumps(kb, indent=2)

    history = "\n".join(messages[-3:])  # last 3 messages

    prompt = f"""
    You are an AI assistant for AutoStream.

    Conversation so far:
    {history}

    Context:
    {context}

    User Question:
    {query}

    Answer clearly and helpfully.
    """

    return llm.invoke(prompt).content