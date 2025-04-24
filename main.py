from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os
from differential import DifferentialDiagnosis
from intake_agent import IntakeAgent

os.environ["OPENAI_API_KEY"] = os.getenv('SIMPLE_CHAT_BOT_API_KEY')

class MedicalBot:
    def __init__(self):
        self.intake_agent = IntakeAgent()
        self.differential = DifferentialDiagnosis()
        self.conversation_history = ""
        self.in_differential = False
        self.differential_result = None
        
    def process_input(self, user_input):
        """
        Process user input and return appropriate response based on the current state.
        
        Args:
            user_input (str): Input from the user
            
        Returns:
            str: Response to show to the user
        """
        if not self.in_differential:
            # In intake phase
            response, should_start_differential = self.intake_agent.conduct_intake(
                user_input, 
                self.conversation_history
            )
            
            if self.conversation_history:
                self.conversation_history += f"\nPatient: {user_input}\nAgent: {response}"
            else:
                self.conversation_history = f"Patient: {user_input}\nAgent: {response}"
            
            if should_start_differential:
                self.in_differential = True
                print("\nStarting differential diagnosis. The doctors will now discuss your case:")
                print("-" * 50)
                
                doctors_conversation, final_analysis = self.differential.conduct_differential(self.conversation_history)
                
                # Print each message from the doctors' conversation with a delay
                for message in doctors_conversation:
                    print(message)
                    print("-" * 50)
                
                print("\nFinal Analysis:")
                print("-" * 50)
                print(final_analysis)
                print("-" * 50)
                
                self.differential_result = f"Doctors' Discussion:\n" + "\n".join(doctors_conversation) + "\n\nFinal Analysis:\n" + final_analysis
                return "The differential diagnosis is complete. You can continue asking questions, and I'll show you the analysis again if needed."
            
            return response
        else:
            # Differential is complete, return the stored result
            return "The differential diagnosis has been completed. Here's the analysis again:\n\n" + self.differential_result

def main():
    bot = MedicalBot()
    print("Welcome to the Medical Assistant. Please describe your symptoms.")
    print("(Type 'quit', 'exit', or 'bye' to end the conversation)")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            break
            
        response = bot.process_input(user_input)
        print("\nBot:", response)

if __name__ == "__main__":
    main() 