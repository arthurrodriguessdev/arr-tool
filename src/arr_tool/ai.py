import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class ModelAI:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ.get('GROQ_API_KEY'),
            base_url=os.environ.get('GROQ_API_URL')
        )

    def generate_output(self, prompt):
        response = self.request(prompt)
        return response.output_text

    def request(self, prompt):
        return self.client.responses.create(
            input=prompt,
            model=os.environ.get('GROQ_API_MODEL')
        )