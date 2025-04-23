from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os
from agent import Agent

os.environ["OPENAI_API_KEY"] = os.getenv('SIMPLE_CHAT_BOT_API_KEY')

def chat_with_bot():
    # Initialize our agent with a friendly personality
    agent = Agent(personality="You are a doctor who is very friendly and helpful. Your job is to help the user with their health concerns. You should be very friendly and helpful and provide a lot of information.")
    
    print("Welcome to the chat bot!")
    print("Commands:")
    print("  'quit' - Exit the chat")
    print("  'history' - Show conversation history")
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'history':
            print("\nConversation History:")
            print(agent.get_conversation_history())
            continue
        
        response = agent.generate_response(user_input)
        print("\nBot:", response)

if __name__ == "__main__":
    chat_with_bot() 