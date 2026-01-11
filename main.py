from dotenv import load_dotenv
load_dotenv()

from agent.graph import build_graph

# Build the Graph
graph = build_graph()

# Initial state
state = {
    "messages": [],
    "intent": None,
    "name": None, 
    "email": None, 
    "platform": None,
    "name_captured": False,
    "email_captured": False,
    "platform_captured": False
}

print("\nAutoStream Conversational Agent")
print("Type 'exit' to quit\n")

while True:
    try:
        user_input = input("You: ").strip()
        if not user_input:
            continue
            
        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        # Pass user message to state
        state["messages"].append(user_input)

        # Run the graph
        # The graph returns the updated state
        result = graph.invoke(state)
        
        # Update our local state with the result for the next loop
        state = result

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")