from openai import OpenAI
class ChatAgent:
    def __init__(self): 
        self.client = OpenAI()
        self.conversation_history = []
        self.system_prompt = None  # This will be set in the subclass
        self.response = None

        # Moved the call to add_to_conversation to ensure system_prompt can be overridden
        if self.system_prompt:
            self.add_to_conversation({
                'role': 'system',
                'content': self.system_prompt
            })

    def add_to_conversation(self, message): 
        self.conversation_history.append(message)

    def step(self, transcription):
        self.add_to_conversation({
            'role': 'user',
            'content': transcription
        })

        response = self.client.chat.completions.create(
            model='gpt-4',
            messages=self.conversation_history,
        )
        self.response = response

    def get_response(self): 
        if self.response:
            # Assuming response structure is correct; adjust according to the actual API response
            return self.response.choices[0].message.content

class MedicalScribeAgent(ChatAgent): 
    def __init__(self): 
        super().__init__()  # Initialize the base class
        self.system_prompt = '''
        You are a helpful medical scribe and you will organise the transcription given to you in the following format. 
        You will rely strictly on the provided text, without including external information.
        History of Present Illness (HPI)
        (insert relevant data)
        ED Course: 
        (insert relevant data)
        Initial Orders Include: (insert relevant data)
        Medications given: (insert relevant data)
        '''

        # This will now add the correct system_prompt to the conversation history
        self.add_to_conversation({
            'role': 'system',
            'content': self.system_prompt
        })

# Note: Ensure that 'client' is properly defined and accessible

class conversationFormattingAgent(ChatAgent): 
    def  __init__(self):
        super().__init__()
        self.system_prompt =  '''
        You are a helpful tool that organises a given transcription from a doctor's consultation with a patient into the following conversation format. 
        You will rely strictly on the provided text, wihtout including external information.
        Doctor: (insert relevant data)
        Patient: (insert relevant data)
        Doctor: (insert relevant data)
        Patient: (insert relevant data)
        Doctor: (insert relevant data)
        Patient: (insert relevant data)
        and so on...
        '''
        self.add_to_conversation({
            'role': 'system',
            'content': self.system_prompt
        })
