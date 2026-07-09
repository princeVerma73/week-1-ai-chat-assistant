#backend:
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

#read api key
api_key=os.getenv("GEMINI_API_KEY")
if not api_key:
    #print("API Key not found!")
    #exit()
    raise ValueError("GEMINI_API_KEY not found in .env file")

MODEL_NAME = "gemini-2.5-flash"

def create_client(): # will help in Switch to OpenAI. etc.
    return genai.Client(api_key=api_key)

client = create_client() 

# Generate AI Response with Conversation Memory
def generate_response(messages:list[dict])->str: #typeCast string input, output string
    """
    Send the complete conversation to Gemini
    and return the AI response.
    """
    
    try:  # error handling

         # Convert chat history into a single prompt
        prompt = ""
        for message in messages:
            if message["role"] == "user":
                prompt += f"User: {message['content']}\n"
            else:
                prompt += f"Assistant: {message['content']}\n"
                
        # Tell Gemini it's now the assistant's turn
        prompt += "Assistant:"

        response = client.models.generate_content( #Python tries to contact Gemini
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text
    
    except Exception as e:
        import traceback

        traceback.print_exc()

        return f"Error: {e}"