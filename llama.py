import httpx
from config.config import config
class LlamaClient:
    def __init__(self):
        self.client = httpx.AsyncClient(base_url=config.OLLAMA_BASE_URL,timeout=420)

    async def generate(self, prompt: str, max_tokens: int = 100):
        response = await self.client.post("/api/generate", json={"prompt": prompt, "model": "llama3.2", "stream": False,"options": {
            "num_predict": max_tokens
        }})
        response.raise_for_status()
        return response.json()