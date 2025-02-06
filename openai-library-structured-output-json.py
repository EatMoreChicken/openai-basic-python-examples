import os
import json
from openai import OpenAI
import datetime

# Function to retrieve the OpenAI API key from environment variables
def get_openai_settings():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("The OPENAI_API_KEY environment variable is not set.")
    return api_key

# Function to get movie details from OpenAI API in JSON format
def get_movie_details_json(prompt):
    client = OpenAI(api_key=api_key)

    # Define the JSON schema for the movie response
    json_schema = {
        "name": "movie_response",
        "schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "director": {"type": "string"},
                "release_year": {"type": "integer"}
            },
            "required": ["title", "director", "release_year"],
            "additionalProperties": False
        }
    }

    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # Ex. gpt-4o
        messages=[
            {"role": "system", "content": "Extract the movie details."},
            {"role": "user", "content": prompt},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": json_schema
        }
    )
    
    movie_json = json.loads(completion.choices[0].message.content)

    return movie_json

# Main script execution
if __name__ == '__main__':
    api_key = get_openai_settings()
    prompt = "Interstellar, directed by Christopher Nolan, was released in 2014."
    movie_json = get_movie_details_json(prompt)

    # Output the parsed movie details
    print(f"Movie Title: {movie_json['title']}")
    print(f"Director: {movie_json['director']}")
    print(f"Release Year: {movie_json['release_year']}")
    print(f"Years since release: {datetime.datetime.now().year - movie_json['release_year']}")
