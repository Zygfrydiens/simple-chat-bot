from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

os.environ["OPENAI_API_KEY"] = os.getenv('SIMPLE_CHAT_BOT_API_KEY')

llm = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-3.5-turbo"
)

def test_chat():
    try:
        messages = [
            HumanMessage(content="What is the capital of France?")
        ]
        response = llm.invoke(messages)
        print("Bot's response:", response.content)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def chat_with_bot():
    print("Welcome to the chat bot! Type 'quit' to exit.")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        try:
            messages = [HumanMessage(content=user_input)]
            response = llm.invoke(messages)
            print("\nBot:", response.content)
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    chat_with_bot() 