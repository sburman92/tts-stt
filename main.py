import asyncio

from tts import TTS
from stt import STT
from llama import LlamaClient


async def main():
    stt = STT()
    tts = TTS()
    llama = LlamaClient()
    segments, info = stt.transcribe("sample.m4a")

    print(f"Detected language: {info.language} ({info.language_probability:.2f})")
    for segment in segments:
        prompt = segment.text
        print(f"{prompt}")
    llm_output=await llama.generate(prompt)
    print(f"LLM Output: {llm_output['response']}")
    await tts.synthesize(llm_output['response'], "output.mp3")
    print("output.mp3 Saved successfully!")


if __name__ == "__main__":
    asyncio.run(main())
