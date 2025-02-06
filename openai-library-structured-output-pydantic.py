import os
from pydantic import BaseModel
from openai import OpenAI
import datetime

# Function to retrieve the OpenAI API key from environment variables
def get_openai_settings():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("The OPENAI_API_KEY environment variable is not set.")
    return api_key

# Function to get movie details from OpenAI API
def get_movie_details(prompt):
    client = OpenAI(api_key=api_key)

    # Define the Movie model
    class Movie(BaseModel):
        title: str
        director: str
        release_year: int

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini", # Ex. gpt-4o
        messages=[
            {"role": "system", "content": "Extract the movie details."},
            {"role": "user", "content": prompt},
        ],
        response_format=Movie,
    )

    return completion.choices[0].message.parsed

# Main script execution
if __name__ == '__main__':
    api_key = get_openai_settings()
    prompt = "Interstellar, directed by Christopher Nolan, was released in 2014."
    movie = get_movie_details(prompt)

    print(f"Movie Title: {movie.title}")
    print(f"Director: {movie.director}")
    print(f"Release Year: {movie.release_year}")
    print(f"Years since release: {datetime.datetime.now().year - movie.release_year}")
