Here is the corrected and polished version of the README you provided. I have fixed the git command syntax error and slightly enhanced the WhatsApp section to better meet the technical requirements.

```markdown
# AutoStream – Social-to-Lead Agentic Workflow
### A GenAI-powered conversational agent built using LangGraph and RAG

## 📌 Overview
This project implements a GenAI-powered conversational AI agent for a fictional SaaS product called **AutoStream**, which provides automated video editing tools for content creators.

The agent simulates a real-world social-to-lead workflow, similar to ServiceHive’s Inflx platform. It is designed to handle product inquiries, identify high-intent users, and capture qualified leads using a controlled, stateful agentic workflow.

Unlike a simple chatbot, this system demonstrates intent reasoning, retrieval-augmented generation (RAG), state management, and tool execution.

## 🚀 Key Features

* **LLM-based Intent Detection**
    * Classifies user intent into greeting, product inquiry, or high-intent lead.
* **RAG-Powered Knowledge Retrieval**
    * Answers questions using a local Markdown knowledge base.
    * Prevents hallucinations by grounding responses in data.
* **Stateful Agent using LangGraph**
    * Maintains memory across multiple conversation turns.
    * Locks into lead-capture mode once high intent is detected.
* **Controlled Tool Execution**
    * Captures leads only after collecting: Name, Email, and Creator platform.
    * Prevents premature tool calls.
* **Production-Style Architecture**
    * Modular codebase with clear separation of concerns.

## 🧠 Tech Stack

* **Language:** Python 3.9+
* **Framework:** LangChain + LangGraph
* **LLM:** GPT-4o-mini
* **Embeddings:** Sentence-Transformers (local)
* **Vector Store:** FAISS
* **State Management:** LangGraph State
* **Environment Management:** python-dotenv

## 📂 Project Structure

```text
autostream-langgraph-agent/
├── agent/
│   ├── graph.py        # LangGraph workflow
│   ├── intent.py       # Intent detection logic
│   ├── rag.py          # RAG pipeline
│   ├── state.py        # Agent state schema
│   └── tools.py        # Mock lead capture tool
├── data/
│   └── knowledge_base.md
├── .env
├── main.py
├── requirements.txt
└── README.md

```

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone [https://github.com/Harsh-4210/Autostream-Langgraph-agent.git](https://github.com/Harsh-4210/Autostream-Langgraph-agent.git)
cd Autostream-Langgraph-agent

```

### 2️⃣ Create and Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt

```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here

```

### 5️⃣ Run the Agent

```bash
python main.py

```

## 💬 Example Interaction

```text
You: Hi
Agent: Hi! How can I help you with AutoStream today?
You: Tell me about your pricing
Agent: (Responds with Basic and Pro plan details)
You: That sounds good, I want to try the Pro plan for my YouTube channel
Agent: May I know your name?
You: Harsh
Agent: Please share your email address.
You: harsh@gmail.com
Agent: Which platform do you create content on?
You: YouTube
Lead captured successfully: Harsh, harsh@gmail.com, YouTube

```

## 🏗️ Architecture Explanation (≈200 Words)

This project uses **LangGraph** to implement a stateful, multi-turn conversational AI agent. LangGraph was chosen because it enables explicit state definition and deterministic workflow control, which are essential for real-world agentic systems.

The agent maintains a structured state that includes conversation history, detected intent, and lead details (name, email, platform). Intent detection is handled using an LLM-based classifier, allowing the agent to reason over natural language inputs rather than relying on brittle keyword rules.

For knowledge-based responses, the system implements a **Retrieval-Augmented Generation (RAG)** pipeline. A local Markdown knowledge base containing AutoStream pricing and policies is indexed using FAISS. Local sentence-transformer embeddings are used for retrieval to avoid external dependency during evaluation, while GPT-4o-mini is used as the primary LLM for reasoning and response generation.

Once high intent is detected, the agent transitions into a **lead qualification mode**. During this phase, intent re-detection is disabled, and the agent sequentially collects required user details. A mock lead capture tool is executed only after all required information is available, ensuring safe and controlled tool usage.

## 📲 WhatsApp Integration (Conceptual)

To integrate this agent with WhatsApp, incoming messages would be received using the **WhatsApp Cloud API** webhook. Each incoming message would be forwarded to a backend service (FastAPI/Flask) hosting the LangGraph agent.

Crucially, **session management** would be handled by mapping the user's WhatsApp phone number to a specific LangGraph `thread_id`. The state would be persisted in a database (e.g., PostgreSQL or Redis). When a new message arrives, the system retrieves the user's existing conversation state, processes the input, and sends the response back via the WhatsApp API, ensuring a continuous conversation flow.

## 🎥 Demo Video

The demo video (2–3 minutes) demonstrates:

* Pricing query handling using RAG
* High-intent detection
* Lead detail collection
* Successful lead capture via mock tool

## ⚠️ Known Notes

* Local embeddings are used to avoid OpenAI quota issues during evaluation.
* A deprecation warning from LangChain does not affect runtime or functionality.
* Tool execution is intentionally mocked as per assignment requirements.

## 🔮 Future Enhancements

* Persistent lead storage (database integration).
* Web or WhatsApp deployment.
* Dockerization.
* Admin dashboard for captured leads.

## 👤 Author

**Harsh Jain**
GitHub: [https://github.com/Harsh-4210](https://github.com/Harsh-4210)

```

```
