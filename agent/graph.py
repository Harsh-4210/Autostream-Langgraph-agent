from langgraph.graph import StateGraph, END
from typing import Literal

from agent.state import AgentState
from agent.intent import detect_intent
from agent.rag import build_rag
from agent.tools import mock_lead_capture

# Initialize RAG chain once
rag_chain = build_rag()

def classify_node(state: AgentState):
    """
    Node 1: Classify user intent (Greeting, Inquiry, High Intent).
    Only runs if we are not already locked into a high-intent flow.
    """
    user_message = state["messages"][-1]
    
    # If we are already mid-capture, keep the intent as 'high_intent'
    # so the router sends us back to the lead capture node.
    if state.get("intent") == "high_intent":
        return state

    detected_intent = detect_intent(user_message)
    state["intent"] = detected_intent
    return state

def rag_node(state: AgentState):
    """
    Node 2: Handle product inquiries using RAG.
    """
    user_message = state["messages"][-1]
    result = rag_chain.invoke(user_message)
    
    # Append the AI response to history (optional, but good for context)
    # Here we just print it as per your original request pattern
    print(f"Agent: {result.content}")
    return state

def greeting_node(state: AgentState):
    """
    Node 3: Simple Greeting Response.
    """
    print("Agent: Hi! How can I help you with AutoStream today?")
    return state

def lead_capture_node(state: AgentState):
    """
    Node 4: High Intent Handler (Slot Filling).
    This node manages the state of the lead capture conversation.
    """
    user_message = state["messages"][-1]

    # --- SLOT FILLING LOGIC ---
    # We assume the user's *current* message is the answer to the *previous* question
    # unless we haven't started asking yet.
    
    # 1. Capture Name
    if not state.get("name"):
        # If we haven't asked for name yet (this is the first high-intent turn)
        # We don't save the current message (which was likely "I want to buy") as the name.
        # We just ask the question.
        # BUT, to track "have we asked?", we can check if this is the immediate switch.
        pass 
    elif not state.get("name_captured"):
        # The user just responded to "What is your name?"
        state["name"] = user_message
        state["name_captured"] = True # Helper flag
        
    # 2. Capture Email (only if name is done)
    elif not state.get("email"):
        pass
    elif not state.get("email_captured"):
        state["email"] = user_message
        state["email_captured"] = True

    # 3. Capture Platform (only if email is done)
    elif not state.get("platform"):
        pass
    elif not state.get("platform_captured"):
        state["platform"] = user_message
        state["platform_captured"] = True

    # --- QUESTION LOGIC ---
    # Now check what is still missing and ask for it
    
    if not state.get("name"):
        print("Agent: Great! Let's get you set up. May I know your name?")
        # We define a temporary flag in the state to know we are waiting for a name next
        # (In a real app, we'd use a more complex conversation stack, but this suffices)
        state["name"] = "waiting" # Placeholder to signal we are "in process"
        # Note: In the NEXT turn, 'name' will be "waiting", so we enter the capture block above.
        # This is a simple state machine trick for this assignment.
        state["name_captured"] = False
        return state

    if not state.get("email"):
        print(f"Agent: Thanks {state['name']}. What is your email address?")
        state["email"] = "waiting"
        state["email_captured"] = False
        return state

    if not state.get("platform"):
        print("Agent: Got it. Finally, which platform do you create content on?")
        state["platform"] = "waiting"
        state["platform_captured"] = False
        return state

    # --- FINAL EXECUTION ---
    # If we are here, we have everything (and it's not "waiting")
    if state.get("platform_captured"):
        mock_lead_capture(state["name"], state["email"], state["platform"])
        # Reset intent to allow normal conversation to resume (optional)
        state["intent"] = None 
        state["name"] = None
        state["email"] = None
        state["platform"] = None
        # Reset helper flags
        state["name_captured"] = False
        state["email_captured"] = False
        state["platform_captured"] = False
        
    return state

def router(state: AgentState) -> Literal["greeting", "rag", "high_intent"]:
    """
    Determines which node to visit next based on intent.
    """
    intent = state.get("intent")
    if intent == "greeting":
        return "greeting"
    elif intent == "high_intent":
        return "high_intent"
    else:
        return "rag"

def build_graph():
    graph = StateGraph(AgentState)

    # Add Nodes
    graph.add_node("classify", classify_node)
    graph.add_node("greeting", greeting_node)
    graph.add_node("rag", rag_node)
    graph.add_node("high_intent", lead_capture_node)

    # Set Entry Point
    graph.set_entry_point("classify")

    # Add Conditional Edges
    graph.add_conditional_edges(
        "classify",
        router,
        {
            "greeting": "greeting",
            "rag": "rag",
            "high_intent": "high_intent"
        }
    )

    # Add Edges to END (Wait for next user input)
    graph.add_edge("greeting", END)
    graph.add_edge("rag", END)
    graph.add_edge("high_intent", END)

    return graph.compile()