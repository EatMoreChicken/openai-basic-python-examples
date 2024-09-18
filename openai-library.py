import os
from openai import OpenAI

# Function to get OpenAI settings
def get_openai_settings():
    # Get the OpenAI API key from an environment variable
    api_key = os.getenv('OPENAI_API_KEY')

    # Check if the API key is set
    if not api_key:
        raise ValueError("The OPENAI_API_KEY environment variable is not set")

    return api_key

# Function to get a response from the OpenAI API
def get_openai_response(prompt):
    # Create an OpenAI client
    client = OpenAI(api_key=api_key)

    # Make a request to the OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    # Return the message content from the response
    return response.choices[0].message.content

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