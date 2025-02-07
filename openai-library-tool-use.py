import pytz
from datetime import datetime
from openai import OpenAI
import json
import os

# Function to retrieve the OpenAI API key from environment variables
def get_openai_settings():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("The OPENAI_API_KEY environment variable is not set.")
    return api_key

# Function to convert time from one timezone to another
def convert_time(input_time_str, from_tz_str, to_tz_str):
    input_time = datetime.strptime(input_time_str, "%I %p")  # Assuming time format is like "8 PM"
    from_tz = pytz.timezone(from_tz_str)
    to_tz = pytz.timezone(to_tz_str)
    
    localized_time = from_tz.localize(input_time)
    converted_time = localized_time.astimezone(to_tz)
    
    return converted_time.strftime("%I:%M %p")

# Function to interact with OpenAI API and process the result
def process_timezone_conversion(prompt):
    # OpenAI client initialization
    client = OpenAI(api_key=get_openai_settings())

    # Define tools for function calling (timezone conversion)
    tools = [{
        "type": "function",
        "function": {
            "name": "convert_time",
            "description": "Convert time from one timezone to another.",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_time_str": {"type": "string", "description": "Time in the format '8 PM'"},
                    "from_tz_str": {"type": "string", "description": "Timezone to convert from in the format 'America/New_York'"},
                    "to_tz_str": {"type": "string", "description": "Timezone to convert to in the format 'America/Chicago'"}
                },
                "required": ["input_time_str", "from_tz_str", "to_tz_str"],
                "additionalProperties": False
            },
            "strict": True
        }
    }]

    # User's input asking to convert time
    messages = [{"role": "user", "content": prompt}]

    # First API call to OpenAI
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
    )

    # Extract tool call and arguments from OpenAI's response
    tool_call = completion.choices[0].message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)

    # Call the function with the extracted arguments
    result = convert_time(args["input_time_str"], args["from_tz_str"], args["to_tz_str"])

    # Append the function call message and result to the messages list
    messages.append(completion.choices[0].message)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": str(result)
    })

    # Second API call with updated messages
    completion_2 = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
    )

    # Return the final result
    return completion_2.choices[0].message.content

# Main script execution
if __name__ == '__main__':
    prompt = "Convert 8 PM EST in CST."
    result = process_timezone_conversion(prompt)
    print(result)