# AutoStream AI Agent 🤖

This is a conversational AI agent built for **AutoStream** (a fictional SaaS platform) as part of the ServiceHive Machine Learning Internship assignment.

## 🚀 Features
- **Intent Recognition:** Classifies users into Greeting, Product Inquiry, or High-Intent Leads.
- **RAG (Retrieval-Augmented Generation):** Answers pricing and policy questions using a local knowledge base (FAISS + LangChain).
- **Lead Capture:** Identifies high-intent users and intelligently collects Name, Email, and Platform details using slot-filling logic.
- **State Management:** Uses **LangGraph** to maintain conversation context and handle interruptions.

## 🛠️ Tech Stack
- **Framework:** LangChain & LangGraph
- **LLM:** OpenAI GPT-4o-mini
- **Vector Store:** FAISS (CPU)
- **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)

## 🏃‍♂️ How to Run Locally
1. **Clone the repository**
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Setup Environment:** Create a `.env` file with `OPENAI_API_KEY=your_key_here`
4. **Run:** `python main.py`

---

## 🏗️ Architecture Explanation
**Why LangGraph?**
I chose **LangGraph** over a linear chain because this agent requires cyclic state management. The conversation often needs to loop back (e.g., asking for missing details) while retaining context. LangGraph allows for a "Router" node that dynamically directs the flow between RAG retrieval and the Lead Capture state machine based on user intent.

**State Management:**
The agent uses a typed `AgentState` dictionary to persist the conversation history and slot-filling variables (`name`, `email`, `platform`). This ensures that if a user interrupts the flow, the agent "remembers" which data points are still missing.

## 📱 WhatsApp Integration Strategy
To deploy this agent on WhatsApp, I would use the **Meta Cloud API** with a **FastAPI** webhook.
1. **Webhook:** A `POST` endpoint receives messages from WhatsApp.
2. **Persistence:** I would use LangGraph's `Checkpointer` (backed by Postgres or SQLite) to map the WhatsApp phone number to a specific `thread_id`. This ensures the agent remembers the user's state across multiple messages.
3. **Response:** The agent's text response is sent back via the WhatsApp API `messages` endpoint.