import os
import requests

# Function to retrieve the OpenAI API key from environment variables
def get_openai_settings():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key is missing.")
    return api_key

# Function to send a prompt to OpenAI API and get a response
def get_openai_response(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == '__main__':
    api_key = get_openai_settings()
    prompt = "What is the capital of France?"
    response = get_openai_response(prompt)
    if response:
        print(response)