# 🎬 AutoStream Agent — Social-to-Lead Conversational AI

> A production-style GenAI agent that converts social conversations into qualified leads using intent detection, RAG-based knowledge retrieval, and stateful multi-turn dialogue.

---

## 🎥 Demo

📽️ **[Watch the Demo →](#)**  
*(Replace `#` with your Google Drive / YouTube link)*

---

## 📌 Overview

**AutoStream Agent** is a conversational AI system built for AutoStream — a fictional SaaS platform for automated video editing. It simulates a real-world lead generation assistant, similar to systems like ServiceHive's Inflx.

The agent understands user intent, answers product queries using a knowledge base, detects high-intent buyers, and captures lead information — all within a smooth, multi-turn conversation.

---

## 🧠 Problem Statement

Build a conversational AI agent that:

1. Identifies user **intent** from natural language
2. Answers queries accurately using **RAG** (Retrieval-Augmented Generation)
3. Detects **high-intent signals** in user messages
4. Collects user details and triggers **lead capture**

---

## 🏗️ Architecture

```
User Input
    │
    ▼
Intent Detection
    │
    ▼
Knowledge Retrieval (RAG)
    │
    ▼
Response Generation
    │
    ▼
Intent Shift Detection
    │
    ▼
Lead Qualification
    │
    ▼
Tool Execution (Lead Capture)
```

### Key Components

| Component | Role |
|-----------|------|
| **LLM** | Intent classification & response generation |
| **LangGraph** | Stateful multi-step agent workflow |
| **RAG Pipeline** | Grounds responses in local knowledge base |
| **Memory / State** | Tracks context across conversation turns |
| **Tool Layer** | Executes lead capture after all fields collected |

---

## ✨ Features

### 🎯 Intent Detection
Classifies user messages into:
- Greeting
- Product / price inquiry
- High-intent lead signal

Uses structured LLM prompting for flexibility over rigid rule-based logic.

---

### 📚 RAG-Based Knowledge Retrieval
- Local JSON knowledge base
- Retrieves grounded answers for:
  - Pricing plans
  - Product features
  - Company policies
- Prevents hallucinations and ensures accuracy

---

### 🔁 Stateful Conversation Handling
Maintains context across multiple turns, tracking:
- Current intent
- Collected user fields
- Conversation stage

Enables smooth transitions from query → qualification → lead capture.

---

### 📋 Lead Capture Tool (Controlled Execution)

Collects the following before triggering the tool:
- **Name**
- **Email**
- **Creator Platform**

```python
def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")
```

> ⚠️ Tool fires **only after all required fields are collected** — no premature triggers.

---

## 💬 Example Conversation

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

→ ✅ Lead captured: Manan | manan@gmail.com | YouTube
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.9+ |
| Agent Framework | LangChain / LangGraph |
| LLM | GPT / Gemini / Claude |
| Knowledge Base | JSON (local) |
| Deployment (concept) | WhatsApp Business API / Twilio |

---

## 🚀 Getting Started

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

## 🧩 Design Decisions

**LLM-based Intent Detection**  
Chosen over keyword matching to handle varied user phrasing robustly.

**LangGraph for Stateful Workflow**  
Enables multi-turn reasoning and controlled stage transitions without spaghetti logic.

**RAG for Knowledge Grounding**  
Retrieval from a structured knowledge base prevents hallucinations in product responses.

**Delayed Tool Execution**  
Lead capture is only triggered after all required fields are confirmed — no partial data, no early exits.

---

## 📲 WhatsApp Deployment (Concept)

To deploy this agent on WhatsApp:

1. Set up **WhatsApp Business API** (or Twilio's WhatsApp integration)
2. Configure a **webhook** to receive incoming messages
3. Route messages to the **agent backend**
4. Use the user's **phone number** as the session key
5. Send agent responses back via the API

This enables real-time conversational automation at scale on messaging platforms.

---

## 🔮 Future Improvements

- [ ] Fine-tuned intent classifier for higher accuracy
- [ ] Vector embeddings (e.g., FAISS / Pinecone) for improved RAG retrieval
- [ ] Real CRM API integration for lead storage
- [ ] REST API deployment (FastAPI / Flask)
- [ ] Conversation analytics dashboard

---

## 📁 Project Structure

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

## 👤 Author

**Manan Babbar**  
[GitHub](https://github.com/MananBabbar07) · [LinkedIn](#)

---

## 📄 License

This project is for educational and demonstration purposes.
