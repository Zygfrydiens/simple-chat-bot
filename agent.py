from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

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
        
        # Initialize conversation memory
        self.conversation_history = [self.system_message]
    
    def generate_response(self, query):
        """
        Generate a response to a given query, maintaining conversation history.
        
        Args:
            query (str): The input query/message
            
        Returns:
            str: The agent's response
        """
        # Add user's message to conversation history
        user_message = HumanMessage(content=query)
        self.conversation_history.append(user_message)
        
        try:
            # Generate response using full conversation history
            response = self.llm.invoke(self.conversation_history)
            
            # Add agent's response to conversation history
            ai_message = AIMessage(content=response.content)
            self.conversation_history.append(ai_message)
            
            return response.content
        except Exception as e:
            error_message = f"Error generating response: {str(e)}"
            # Remove the user's message if there was an error
            self.conversation_history.pop()
            return error_message
    
    def get_conversation_history(self):
        """
        Get the full conversation history as a formatted string.
        
        Returns:
            str: Formatted conversation history
        """
        history = []
        for message in self.conversation_history[1:]:  # Skip the system message
            if isinstance(message, HumanMessage):
                history.append(f"User: {message.content}")
            elif isinstance(message, AIMessage):
                history.append(f"Bot: {message.content}")
        return "\n".join(history) 