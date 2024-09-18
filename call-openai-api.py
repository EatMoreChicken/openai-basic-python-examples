import os
import requests

# Function to get Open AI settings
def get_openai_settings():
    # Get the OpenAI API key from an environment variable
    api_key = os.getenv('OPENAI_API_KEY')

    # Check if the API key is set
    if not api_key:
        raise ValueError("The OPENAI_API_KEY environment variable is not set")

    return api_key

# Function to get a response from the OpenAI API
def get_openai_response(prompt):
    # Define the API endpoint and request headers
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Define the request data, this is where your prompt goes
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    # Make a POST request to the OpenAI API
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the message content from the response
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
        return None

if __name__ == '__main__':

    # Get the OpenAI API key
    api_key = get_openai_settings()

    # Define a prompt for the chat
    prompt = "What is the capital of France?"

    # Get a response from the OpenAI API
    response = get_openai_response(prompt)

    # Print the response
    if response:
        print(response)
