from edge_tts import Communicate


class TTS:
    def __init__(self, voice="en-IN-NeerjaExpressiveNeural", rate="+0%", volume="+0%"):
        self.voice = voice
        self.rate = rate
        self.volume = volume

    async def synthesize(self, text, output_path):
        communicate = Communicate(text, self.voice, rate=self.rate, volume=self.volume)
        await communicate.save(output_path)
