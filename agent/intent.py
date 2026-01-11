from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


# Deterministic intent classification
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

intent_prompt = PromptTemplate.from_template(
    """
You are an intent classification system.

Classify the user's message into ONE of the following intents:
- greeting
- product_inquiry
- high_intent

User message:
"{message}"

Respond with ONLY one of these words:
greeting, product_inquiry, high_intent
"""
)


def detect_intent(message: str) -> str:
    response = llm.invoke(intent_prompt.format(message=message))
    return response.content.strip().lower()
