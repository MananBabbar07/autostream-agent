import json
from app.llm import get_llm

llm = get_llm()

def load_knowledge():
    with open("data/knowledge_base.json") as f:
        return json.load(f)

def retrieve_answer(query):
    kb = load_knowledge()
    context = json.dumps(kb, indent=2)

    prompt = f"""
    You are an AI assistant for AutoStream (video editing SaaS).

    Answer ONLY using the given context.

    Context:
    {context}

    User Question:
    {query}

    Provide a clear, natural, helpful answer.
    """

    return llm.invoke(prompt).content