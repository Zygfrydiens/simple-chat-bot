from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

class Agent:
    def __init__(self, personality=None, temperature=0.7, model_name="gpt-3.5-turbo"):
        """
        Initialize an AI agent with a specific personality.
        
        Args:
            personality (str): The personality description for the agent
            temperature (float): Creativity level of the responses (0.0 to 1.0)
            model_name (str): The name of the LLM model to use
        """
        self.llm = ChatOpenAI(
            temperature=temperature,
            model_name=model_name
        )
        
        # Set default personality if none provided
        if personality is None:
            personality = "You are a helpful and friendly AI assistant."
        
        self.system_message = SystemMessage(content=personality)
    
    def generate_response(self, query):
        """
        Generate a response to a given query.
        
        Args:
            query (str): The input query/message
            
        Returns:
            str: The agent's response
        """
        messages = [
            self.system_message,
            HumanMessage(content=query)
        ]
        
        try:
            response = self.llm.invoke(messages)
            return response.content
        except Exception as e:
            return f"Error generating response: {str(e)}" 