from app.agent import build_graph

graph = build_graph()

state = {
    "messages": [],
    "intent": "",
    "name": "",
    "email": "",
    "platform": "",
    "stage": ""   # 👈 IMPORTANT
}

print("AutoStream AI Agent (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # 🚨 If in lead collection → treat input as slot value
    if state.get("stage") == "lead_collection":

        if not state.get("name"):
            state["name"] = user_input

        elif not state.get("email"):
            state["email"] = user_input

        elif not state.get("platform"):
            state["platform"] = user_input

    else:
        state["messages"].append(user_input)

    # Run agent
    state = graph.invoke(state)

    print("Bot:", state["messages"][-1])