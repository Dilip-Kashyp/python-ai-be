import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def AI(query):
    query = 'prompt:'+query+r'you have to act as a  boy  and answer the question. answer length should be accoriding to the question'
    try:
        generation_config = {
            "temperature": 0.5,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 512,
            "response_mime_type": "text/plain",
        }
        
        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
        )

        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(query)
        cleaned_response = response.text.replace('\n', ' ')
        print(cleaned_response)
        return cleaned_response

    except:
        return "Error in AI function, please try again"
        


