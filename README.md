# AI Customer Support Assistant

A professional customer-support chat app built with Streamlit, LangChain, and Google Gemini. It retains the familiar Week 1 chat experience while adding a dedicated support prompt for orders, delivery, refunds, payments, accounts, and escalation guidance.

## Features

- Professional, safety-conscious customer support responses
- Gemini via LangChain's `ChatGoogleGenerativeAI`
- `PromptTemplate` for consistent support behavior
- Conversation history held in Streamlit session state
- Sidebar with capabilities and a clear-chat action
- Loading spinner and friendly failure message

## Project structure

```
Frontend.py       # Streamlit chat interface
chat.py           # LangChain + Gemini backend
.env.example      # API-key template
requirements.txt  # Dependencies
requirements-support.txt  # LangChain and Gemini packages
```

## Setup

1. Create and activate a virtual environment.

   ```powershell
   py -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies.

   ```powershell
   pip install -r requirements-support.txt
   ```

3. Copy `.env.example` to `.env`, then add your Google AI Studio key.

   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. Start the app.

   ```powershell
   streamlit run Frontend.py
   ```

Open `http://localhost:8501` in your browser.

## Backend flow

`Streamlit chat history → PromptTemplate → ChatGoogleGenerativeAI → professional support response`

The assistant does not make claims about real order, payment, or account data. It requests the necessary non-sensitive details or guides the customer to human support when needed.
