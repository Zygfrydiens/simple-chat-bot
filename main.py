import openai
import langchain
import os

# Create a variable for the OpenAI API key using an environmental variable
openai_api_key = os.getenv('SIMPLE_CHAT_BOT_OPENAI_API_KEY')

if __name__ == "__main__":
    print("Hello, World!") 