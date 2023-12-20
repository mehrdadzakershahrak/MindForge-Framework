import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

class LanguageModelService:
    def __init__(self, provider='openai'):
        self.provider = provider
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        client = OpenAI()

    def query_language_model(self, prompt, max_tokens=1000):
        if self.provider == 'openai':
            response = self.query_openai(prompt, max_tokens)
        elif self.provider == 'huggingface':
            response = self.query_huggingface(prompt, max_tokens)
        else:
            raise ValueError("Unsupported language model provider.")
        return response

    def query_openai(self, prompt, max_tokens):
        client = OpenAI()

        model = "gpt-4"
        response = client.chat.completions.create(model=model,
        messages=[{"role": "user", "content": prompt}],  # prompt passed as user message
        max_tokens=max_tokens,
        temperature=0.75)  # adjust as needed)
        # Extracting the response text from the last message from the assistant
        if response.choices:
            last_message = response.choices[-1].message
            last_message_content = last_message.content if last_message else ''
            return last_message_content
        return ''


    def query_huggingface(self, prompt, max_tokens):
        # Placeholder for Hugging Face API call
        return f"Hugging Face response to: {prompt}", max_tokens