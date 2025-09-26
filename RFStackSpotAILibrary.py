from stackclient.client import StackSpotAgentClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

class RFStackSpotAILibrary:
    def __init__(self):
        self.client = None
        self.agent_id = None
        self.instructions = None
        self.history = []

    def set_credentials(self): # muda de IA pra IA
        self.client = StackSpotAgentClient(
            realm = os.getenv("STACKSPOT_REALM"),
            # precisar gerar na conta stackspot
            client_id = os.getenv("STACKSPOT_CLIENT_ID"),
            client_secret = os.getenv("STACKSPOT_CLIENT_SECRET"),
            # obter da interface
            agent_id = os.getenv("STACKSPOT_AGENT_ID")
        )
        self.agent_id = os.getenv("STACKSPOT_AGENT_ID")

    def set_instructions(self, instructions):
        self.instructions = instructions

    def send_message(self, message):
        prompt = f"{self.instructions}\n{message}" if self.instructions else message
        response = self.client.call_agent(prompt)
        return response

