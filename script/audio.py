import torch
from TTS.api import TTS


def audio(map):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # Init TTS
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    tts.tts_to_file(text= map
                    , speaker_wav="../assets/trump.mp3", language="en", file_path="output.wav")