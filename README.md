# AutoStream Agent — Social-to-Lead Conversational AI

> Built as part of ServiceHive GenAI Intern Assignment (Inflx Agent Simulation)

A production-style GenAI agent that converts social conversations into qualified leads using **intent classification**, **RAG-based knowledge retrieval**, and **stateful multi-turn dialogue** — a minimal simulation of systems like ServiceHive's Inflx.

---

## Demo

📽️ [Watch the Demo →](https://drive.google.com/file/d/1U3Z3mYb9LdJvOzaiC3GfeTpJ_obqdk7S/view?usp=sharing)

---

## Overview

AutoStream Agent simulates a real-world lead generation assistant for AutoStream, a fictional SaaS platform for automated video editing.

The agent understands user intent, answers product queries using a knowledge base, detects high-intent buyers, and captures lead information — all within a smooth, multi-turn conversation.

---

## Agent Reasoning & Flow

The agent is designed as a **stateful multi-step workflow**, not a simple chatbot. Each turn passes through a deliberate pipeline:

```
User Input
    │
    ▼
[1] Intent Detection        ← LLM classifies: Greeting / Inquiry / High-Intent
    │
    ▼
[2] Knowledge Retrieval     ← RAG pulls grounded answers from local knowledge base
    │
    ▼
[3] Response Generation     ← LLM responds using retrieved context
    │
    ▼
[4] Intent Shift Detection  ← monitors for transition: inquiry → high intent
    │
    ▼
[5] Lead Qualification      ← collects Name, Email, Platform sequentially
    │
    ▼
[6] Controlled Tool Execution ← fires ONLY after all fields confirmed
```

### Step 1 — Intent Detection

User input is classified into one of three intents using structured LLM prompting:

- **Greeting** — casual opener, no product interest yet
- **Product Inquiry** — questions about features, pricing, plans
- **High-Intent Lead** — signals readiness to try, subscribe, or buy

LLM-based classification (over keyword matching) handles varied phrasing robustly — "I wanna give this a shot" is correctly read as high intent.

### Step 2 — Knowledge Retrieval (RAG)

For product-related queries, the agent retrieves grounded answers from a local JSON knowledge base before generating a response. This prevents hallucination on specific product details like pricing tiers, feature limits, and policies.

Retrieval is scoped to three domains:
- Pricing plans
- Product features
- Company policies

### Step 3 — Response Generation

The LLM generates a response using the retrieved context as its grounding source, not raw training memory. This ensures accurate, consistent answers regardless of how the question is phrased.

### Step 4 — Intent Shift Detection

After each agent response, the system re-evaluates whether the user's intent has shifted. A transition from "Inquiry" to "High-Intent" triggers the lead qualification stage automatically — the agent doesn't require the user to explicitly say "sign me up."

### Step 5 — Lead Qualification

Once high intent is detected, the agent collects three required fields in sequence:

- Name
- Email
- Creator Platform

Each field is confirmed before requesting the next. The agent handles interruptions and re-asks gracefully if a field is missing or ambiguous.

### Step 6 — Controlled Tool Execution

The lead capture function is triggered **only after all three fields are collected and confirmed**. There are no partial submissions or premature tool calls.

```python
def mock_lead_capture(name, email, platform):
    print(f"Lead captured: {name} | {email} | {platform}")
```

This sequencing is enforced by the LangGraph workflow state — not ad-hoc conditionals.

---

## Example Conversation

```
User:   Hi, tell me about your pricing.

Agent:  We offer two plans:
        • Basic: $29/month — 10 videos, 720p
        • Pro:   $79/month — Unlimited videos, 4K, AI captions

User:   That sounds great. I want to try the Pro plan for my YouTube channel.

Agent:  Awesome! Could you share your name?

User:   Manan

Agent:  Thanks Manan! What's your email address?

User:   manan@gmail.com

Agent:  Got it. Which platform do you primarily create on?

User:   YouTube

✅ Lead captured: Manan | manan@gmail.com | YouTube
```

---

## Architecture

| Component | Role |
|-----------|------|
| LLM | Intent classification and response generation |
| LangGraph | Stateful multi-step agent workflow with stage transitions |
| RAG Pipeline | Grounds responses in local knowledge base, prevents hallucination |
| Memory / State | Tracks intent, collected fields, and conversation stage across turns |
| Tool Layer | Executes lead capture after all required fields are confirmed |

---

## Features

### Intent Detection
Classifies user messages using structured LLM prompting — flexible over rigid rule-based logic, handles varied phrasing naturally.

### RAG-Based Knowledge Retrieval
Retrieves grounded answers from a local JSON knowledge base before responding. Prevents hallucination on pricing, features, and policies.

### Stateful Conversation Handling
LangGraph maintains full conversation state across turns — current intent, collected fields, and conversation stage — enabling clean transitions from inquiry to qualification to lead capture.

### Controlled Tool Execution
Lead capture fires only after all required fields (name, email, platform) are collected and confirmed. No partial data, no early exits.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.9+ |
| Agent Framework | LangChain / LangGraph |
| LLM | GPT / Gemini / Claude |
| Knowledge Base | JSON (local) |
| Deployment (concept) | WhatsApp Business API / Twilio |

---

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/MananBabbar07/autostream-agent
cd autostream-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the agent
python main.py
```

---

## Design Decisions

**LLM-based intent detection over keyword matching** — handles varied user phrasing ("I'm interested", "let's go", "sign me up") without brittle rule maintenance.

**LangGraph for stateful workflow** — enforces stage transitions cleanly (greeting → inquiry → qualification → capture) without spaghetti conditionals. State is explicit, not implicit.

**RAG for knowledge grounding** — retrieval from a structured knowledge base ensures product answers are accurate and consistent, not hallucinated from LLM memory.

**Delayed tool execution** — lead capture is triggered only after all required fields are confirmed. Enforced at the workflow level, not as an afterthought.

---

## WhatsApp Deployment (Concept)

To deploy this agent on WhatsApp:

1. Set up WhatsApp Business API (or Twilio's WhatsApp integration)
2. Configure a webhook to receive incoming messages
3. Route messages to the agent backend
4. Use the user's phone number as the session key for state management
5. Send agent responses back via the API

This enables real-time conversational lead generation at scale on messaging platforms.

---

## Project Structure

```
autostream-agent/
├── main.py               # Entry point
├── agent/
│   ├── graph.py          # LangGraph workflow definition
│   ├── intent.py         # Intent detection logic
│   ├── retriever.py      # RAG pipeline
│   └── tools.py          # Lead capture tool
├── knowledge_base/
│   └── data.json         # Pricing, features, policies
├── requirements.txt
└── README.md
```

---

## Future Improvements

- Fine-tuned intent classifier for higher accuracy
- Vector embeddings (FAISS / Pinecone) for improved RAG retrieval
- Real CRM API integration for lead storage
- REST API deployment (FastAPI / Flask)
- Conversation analytics dashboard

---

## Author

**Manan Babbar**  
[GitHub](https://github.com/MananBabbar07) · [LinkedIn](https://www.linkedin.com/in/manan-babbar-2809091ab/)

---

*This project is for educational and demonstration purposes.*
