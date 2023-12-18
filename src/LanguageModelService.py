import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

class LanguageModelService:
    def __init__(self, provider='openai'):
        self.provider = provider
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

    def query_language_model(self, prompt, max_tokens=100):
        if self.provider == 'openai':
            response = self.query_openai(prompt, max_tokens)
        elif self.provider == 'huggingface':
            response = self.query_huggingface(prompt, max_tokens)
        else:
            raise ValueError("Unsupported language model provider.")
        return response

    def query_openai(self, prompt, max_tokens):
        openai.api_key = self.openai_api_key
        response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=max_tokens)
        return response.choices[0].text.strip(), response.usage.total_tokens

    def query_huggingface(self, prompt, max_tokens):
        # Placeholder for Hugging Face API call
        return f"Hugging Face response to: {prompt}", max_tokens