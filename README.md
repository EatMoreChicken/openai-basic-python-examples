# Basic OpenAI Python Examples

This repository provides example setups for using the OpenAI API with Python. While it is recommended to use the `openai` Python package, these examples include using the `requests` library directly for those who prefer it.

Below are various scripts demonstrating different ways to interact with the OpenAI API.

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
|✨| [openai-library-structured-output-pydantic.py](https://github.com/EatMoreChicken/openai-basic-python-example/blob/main/openai-library-structured-output-pydantic.py) | An example of using the OpenAI library with structured output using Pydantic. (I think this is the easiest way to use structured output.) |
|| [openai-library-structured-output-json.py](https://github.com/EatMoreChicken/openai-basic-python-example/blob/main/openai-library-structured-output-json.py) | An example of using the OpenAI library with structured output using JSON. |
|| [openai-library-streaming.py](https://github.com/EatMoreChicken/openai-basic-python-example/blob/main/openai-library-streaming.py) | An example of using the OpenAI library with streaming. 🔰 Work in Progress|
|| [openai-library-tool-use.py](https://github.com/EatMoreChicken/openai-basic-python-example/blob/main/openai-library-tool-use.py) | An example of using the OpenAI library with tool use. 🔰 Work in Progress|

## Contributing

Obviously the OpenAI documentation is vast and is likely the best way to learn how to use the API. However, I hope these examples can help you get started quickly. If you have any suggestions, improvements, or new examples, feel free to contribute or open an issue. 🙂