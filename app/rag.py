import json
from app.llm import get_llm

llm = get_llm()

def load_knowledge():
    with open("data/knowledge_base.json") as f:
        return json.load(f)

def retrieve_answer(query):
    kb = load_knowledge()
    context = json.dumps(kb, indent=2)
    history = "\n".join(state["messages"][-3:])  # last 3 messages

    prompt = f"""
    You are an assistant for AutoStream.

    Conversation so far:
    {history}

    Context:
    {context}

    User question:
    {query}

    Answer helpfully.
    """

    return llm.invoke(prompt).content