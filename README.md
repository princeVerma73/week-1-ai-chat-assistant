# 🤖 AI Chat Assistant

A simple AI Chat Assistant built using **Google Gemini API** and **Streamlit**. This project was developed as part of my **Week 1 Generative AI Internship**.

---
## 🚀 Features

- 💬 Interactive AI Chat Interface
- 🧠 Conversation Memory
- ⚡ Google Gemini 2.5 Flash Integration
- 🛡️ Error Handling
- 🔐 Secure API Key Management using `.env`
- 🗑️ Clear Chat Button
- 📌 Sidebar with Project Information
- 🎨 Clean and Responsive Streamlit UI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- python-dotenv

---

## 📂 Project Structure

```
week-1-ai-chat-assistant/
│
├── chat.py            # Backend (Gemini API)
├── Frontend.py        # Streamlit Frontend
├── .env.example       # Environment Variables Example
├── .gitignore
├── requirements.txt
└── README.md
```
---

## ⚙️ Installation

### Clone Repository
```bash
git clone https://github.com/princeVerma73/week-1-ai-chat-assistant.git

cd week-1-ai-chat-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add your Gemini API key.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run Frontend.py
```

---

## 📸 Features Demonstrated

- AI Question Answering
- Conversation Memory
- Streamlit Chat Interface
- Error Handling
- Sidebar Information
- Clear Chat Functionality

---

## 📈 Future Improvements

- Chat Session API
- Multiple LLM Support
- Chat Export
- Theme Customization
- Deployment on Streamlit Cloud

---

## 👨‍💻 Developer

**Prince Verma**

B.Tech CSE | IIIT Bhagalpur

GitHub: https://github.com/princeVerma73

---

⭐ If you like this project, consider giving it a star.