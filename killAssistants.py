import os
from openai import OpenAI

# Set your OpenAI API key
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# List all assistants
response = client.beta.assistants.list()

# Get the list of assistants
assistants = response.data

# Delete all assistants except the last one
for assistant in assistants[:-1]:
    client.beta.assistants.delete(assistant.id)

# if __name__ == "__main__":
#     main()