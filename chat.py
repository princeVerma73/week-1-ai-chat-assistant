# backend: chat.py

import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Read API Key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Create Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0.5
)

# Prompt Template
prompt_template = PromptTemplate(
    input_variables=["conversation"],

    template="""
You are a professional AI Customer Support Assistant.

Your responsibilities:
- Answer customer queries politely.
- Help with orders, refunds, payments, shipping and account-related questions.
- Be friendly, professional and concise.
- If you don't know the answer, politely say you don't know.
- Never make up information.

Conversation:
{conversation}

Customer Support Assistant:
"""
)

# Generate AI Response 
def generate_response(messages: list[dict]) -> str:
    """
    Generate AI response using LangChain PromptTemplate.
    """
    try:

        # Convert chat history into conversation
        conversation = ""

        for message in messages:

            if message["role"] == "user":
                conversation += f"Customer: {message['content']}\n"

            else:
                conversation += f"Assistant: {message['content']}\n"

        # Create final prompt
        final_prompt = prompt_template.format(
            conversation=conversation
        )

        # Generate response
        response = llm.invoke(final_prompt)

        return response.content

    except Exception as e:
        print(e)
        return (
            "Sorry, I'm unable to process your request right now. "
            "Please try again later."
        )