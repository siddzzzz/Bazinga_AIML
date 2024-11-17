import google.generativeai as genai
import time

# Set up API key
API_KEY = "AIzaSyBGrFOkNt0qgnNezVhhmdpjdtUIp9PfqIk"  # Replace with your actual Gemini API key
genai.configure(api_key=API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-8b")
chat = model.start_chat(history=[])
user_input = f"What is a resume"
# Function to generate a response from a user prompt
def get_gemini_response(prompt):
    retries = 3  # Number of retries
    delay = 5    # Delay in seconds between retries

    # Retry logic for handling API quota or other transient errors
    for attempt in range(retries):
        try:
            # Send the prompt to the Gemini API
            response = chat.send_message(prompt, stream=False)
            return response.text
        except Exception as e:
            if "ResourceExhausted" in str(e):
                print(f"Resource exhausted. Retrying in {delay} seconds... (Attempt {attempt + 1})")
                time.sleep(delay)
            else:
                print(f"Error: {e}")
                break  # Exit the loop on non-quota-related errors
    return "Failed to generate a response after multiple attempts."
