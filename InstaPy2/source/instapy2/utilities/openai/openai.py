from .completions import Completions

class OpenAI:
    def set_api_key(self, api_key: str):
        self.completions = Completions(api_key=api_key)