# Basic OpenAI Python Example

This is an example setup for using the OpenAI API with Python and the `requests` library. Using the `openai` Python package is recommended, but this example is for those who prefer to use `requests` directly.

## Setting the Environment Variable

| OS/Shell | Command |
| --- | --- |
| Windows CMD | `set OPENAI_API_KEY='your_api_key_here'` |
| Windows PowerShell | `$Env:OPENAI_API_KEY='your_api_key_here'` |
| Linux (bash) | `export OPENAI_API_KEY='your_api_key_here'` |

Replace `your_api_key_here` with your actual OpenAI API key.

After setting the environment variable, you can run the Python script in the same terminal session.

## Scripts

|| Script Name | Description |
|-| --- | --- |
|| [requests-openai-api.py](https://github.com/EatMoreChicken/openai-basic-python-example/blob/main/requests-openai-api.py) | A basic example of using the OpenAI API with the `requests` library. |
|| [openai-library-generic.py](https://github.com/EatMoreChicken/openai-basic-python-example/blob/main/openai-library-generic.py) | A generic example of using the OpenAI library. |
|✨| [openai-library-structured-output-pydantic.py](https://github.com/EatMoreChicken/openai-basic-python-example/blob/main/openai-library-structured-output-pydantic.py) | An example of using the OpenAI library with structured output using Pydantic. (I think this is the easiest |way to use structured output.) |
|| [openai-library-structured-output-json.py](https://github.com/EatMoreChicken/openai-basic-python-example/blob/main/openai-library-structured-output-json.py) | An example of using the OpenAI library with structured output using JSON. |