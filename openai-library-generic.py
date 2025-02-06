import os
from openai import OpenAI

# Function to retrieve the OpenAI API key from environment variables
def get_openai_settings():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("The OPENAI_API_KEY environment variable is not set")
    return api_key

# Function to interact with OpenAI's API and get a response
def get_openai_response(prompt):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

# Main script execution
if __name__ == '__main__':
    api_key = get_openai_settings()
    prompt = "What is the capital of France?"
    response = get_openai_response(prompt)
    if response:
        print(response)