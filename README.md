# 🚀 AutoStream Conversational AI Agent

**ServiceHive – Inflx Assignment**

---

## 📌 Overview

This project implements a **stateful conversational AI agent** for a fictional SaaS product, **AutoStream**, which provides automated video editing tools.

The agent is designed to simulate a **real-world “Social-to-Lead” workflow**, where user conversations are intelligently converted into qualified leads.

Unlike basic chatbots, this agent:

* Understands user intent
* Retrieves grounded information using RAG
* Tracks multi-turn conversation state
* Collects structured lead data
* Executes backend actions (mock API)

---

## 🧠 Key Features

### ✅ Intent Classification

The agent classifies user input into:

* `greeting`
* `inquiry`
* `high_intent`
* `closing`

---

### ✅ RAG (Retrieval-Augmented Generation)

* Uses a **local JSON knowledge base**
* Ensures **grounded responses (no hallucination)**
* Includes pricing, features, and policies

---

### ✅ Stateful Conversation (LangGraph)

* Maintains memory across multiple turns
* Uses a structured `AgentState`
* Handles transitions between:

  * Inquiry flow
  * Lead collection flow

---

### ✅ Lead Capture (Tool Execution)

* Collects:

  * Name
  * Email
  * Platform
* Executes mock function:

```python
def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")
```

---

### ✅ Validation & Control

* Prevents premature tool execution
* Validates:

  * Email format
  * Platform selection (YouTube / Instagram / TikTok)
* Ensures deterministic flow

---

## 🏗️ Project Structure

```bash
autostream-agent/
├── app/
│   ├── agent.py        # LangGraph workflow (core logic)
│   ├── intent.py       # Intent classification
│   ├── rag.py          # RAG pipeline
│   ├── tools.py        # Lead capture tool
│   ├── state.py        # Conversation state schema
│   ├── prompts.py      # Prompt templates
│   ├── llm.py          # LLM initialization (.env based)
│
├── data/
│   └── knowledge_base.json   # Pricing + policies
│
├── main.py            # CLI entry point
├── requirements.txt   # Dependencies
├── README.md
├── .env               # API key (not committed)
├── .gitignore
```

---

## ⚙️ Tech Stack

* Python 3.9+
* LangChain
* LangGraph
* OpenAI GPT-4o-mini
* dotenv

---

## 🔑 Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd autostream-agent
```

---

### 2. Create Virtual Environment (recommended)

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add OpenAI API Key

Create a `.env` file in the root directory:

```bash
OPENAI_API_KEY=your_api_key_here
```

⚠️ Do NOT commit this file (already added to `.gitignore`)

---

## ▶️ Run the Project

```bash
python main.py
```

You will see:

```bash
AutoStream AI Agent (type 'exit' to quit)
```

---

## 💬 Example Conversation Flow

### Step 1 – Inquiry

```
You: Hi, tell me about pricing
```

### Step 2 – RAG Response

```
Bot: Basic plan is $29/month...
```

---

### Step 3 – High Intent

```
You: I’ll go with the Pro plan
```

---

### Step 4 – Lead Collection

```
Bot: What's your name?
You: Manan

Bot: What's your email?
You: manan@gmail.com

Bot: Which platform?
You: YouTube
```

---

### Step 5 – Tool Execution

```
Lead captured successfully: Manan, manan@gmail.com, YouTube
```

---

## 🔄 Agent Workflow

1. User input received
2. Intent classified using LLM
3. Routed via LangGraph:

   * Inquiry → RAG
   * High Intent → Lead Flow
4. Slot filling (name, email, platform)
5. Tool execution
6. Response returned

---

## 📲 WhatsApp Integration (Concept)

To integrate this agent with WhatsApp:

1. Use **Meta WhatsApp Cloud API**
2. Set up a **Webhook (Flask/FastAPI server)**
3. Incoming messages → sent to agent
4. Agent processes:

   * Intent
   * RAG
   * Tool execution
5. Response sent back via WhatsApp API
6. Store user state in Redis/DB for persistence

---

## 🧪 Evaluation Alignment

This project demonstrates:

* ✅ Agent reasoning & intent detection
* ✅ Correct RAG usage
* ✅ Clean state management
* ✅ Safe tool execution
* ✅ Real-world deployability

---

## 🧠 Design Decisions

* **LangGraph** used for deterministic workflow control
* **Centralized LLM config** via `.env` for security
* **Structured state** for multi-turn conversations
* **Prompt-constrained RAG** to reduce hallucination
* **Slot-filling logic** to ensure complete data before tool calls

---

## ⚠️ Notes

* No vector DB used → kept lightweight for assignment
* Designed for clarity and correctness over complexity
* Easily extendable to API / UI / production system

---

## 👨‍💻 Author

Manan

---
