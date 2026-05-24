from faster_whisper import WhisperModel
class STT:
    def __init__(self, model_size="small", device="cuda", compute_type="float16"):
        self.model = WhisperModel(model_size) 
    def transcribe(self, audio_path):
        segments, info = self.model.transcribe(audio_path)
        return segments, info