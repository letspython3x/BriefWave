"""ChatGPT service for interacting with the OpenAI API."""

from openai import OpenAI

class ChatGPTClient:
    """Responsible for interacting with the OpenAI ChatGPT API to generate summaries."""
   
    def __init__(self, api_key: str, model: str):
        """Initialize the ChatGPT client with API key and model."""
   
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate_summary(self, prompt: str) -> str:
        """Uses the ChatGPT API to generate a summary based on the given prompt."""

        if not prompt:
            raise ValueError("No prompt provided for summarization.")

        print("Sending request to ChatGPT for summary generation...")
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates concise summaries."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            summary = response.choices[0].message.content
            print("ChatGPT summary generation successful.")
            return summary
        except Exception as e:
            print(f"Error generating summary: {e}")
            raise Exception(f"Failed to get summary from ChatGPT: {str(e)}")
