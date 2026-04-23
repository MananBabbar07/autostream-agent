from langgraph.graph import StateGraph, END
from app.intent import classify_intent
from app.rag import retrieve_answer
from app.tools import mock_lead_capture
from app.state import AgentState
from app.prompts import GREETING_RESPONSE

# Step 1: Detect intent
def detect_intent(state: AgentState):
    user_input = state["messages"][-1]
    state["intent"] = classify_intent(user_input)
    return state

# Step 2: Handle inquiries via RAG
def handle_query(state: AgentState):
    response = retrieve_answer(state["messages"][-1])
    state["messages"].append(response)
    return state

# Step 3: Lead capture flow
def handle_lead(state):

    state["stage"] = "lead_collection"

    # Step 1: Name
    if not state.get("name"):
        state["messages"].append("Sure! Can I have your name?")
        return state

    # Step 2: Email
    if not state.get("email"):
        state["messages"].append("Great, what's your email?")
        return state

    # ✅ Validate email ONLY after it's entered
    if "@" not in state["email"] or "." not in state["email"]:
        state["messages"].append("Please enter a valid email address.")
        state["email"] = ""   # reset so user re-enters
        return state

    # Step 3: Platform
    if not state.get("platform"):
        state["messages"].append("Which platform do you create content on?")
        return state

    # ✅ Tool execution
    mock_lead_capture(state["name"], state["email"], state["platform"])

    state["messages"].append("You're all set! 🚀 We'll contact you soon.")
    state["stage"] = ""  # reset

    return state

# Step 4: Routing
def router(state: AgentState):

    # 🚨 If already collecting lead → STAY there
    if state.get("stage") == "lead_collection":
        return "lead"

    if state["intent"] == "greeting":
        state["messages"].append(GREETING_RESPONSE)
        return END

    if state["intent"] == "inquiry":
        return "query"

    if state["intent"] == "high_intent":
        state["stage"] = "lead_collection"   # 👈 lock state
        return "lead"

    return END

# Build graph
def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("intent", detect_intent)
    builder.add_node("query", handle_query)
    builder.add_node("lead", handle_lead)

    builder.set_entry_point("intent")

    builder.add_conditional_edges(
        "intent",
        router,
        {
            "query": "query",
            "lead": "lead",
            END: END
        }
    )

    builder.add_edge("query", END)
    builder.add_edge("lead", END)

    return builder.compile()