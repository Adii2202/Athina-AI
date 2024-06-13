import os
import numpy as np

from rag.AIVoiceAssistant import AIVoiceAssistant

DEFAULT_MODEL_SIZE = "medium"
DEFAULT_CHUNK_LENGTH = 10

ai_assistant = AIVoiceAssistant()

def main():
    
    model_size = DEFAULT_MODEL_SIZE + ".en"
    customer_input_transcription = ""

    try:
        while True:
            # Get text input from the user
            transcription = input("")
            
            # Add customer input to transcript
            customer_input_transcription += "Customer: " + transcription + "\n"

            # Process customer input and get response from AI assistant
            output = ai_assistant.interact_with_llm(customer_input_transcription)
            if output:
                output = output.lstrip()
                print("AI Assistant: {}".format(output))

    
    except KeyboardInterrupt:
        print("\nStopping...")

if __name__ == "__main__":
    main()
