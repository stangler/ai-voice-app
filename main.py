from TTS.api import TTS

# XTTS v2 モデルを GPU にロード
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")

# 音声生成
tts.tts_to_file(
    text="これはXTTSによる日本語音声合成です。",
    speaker_wav="voice_sample.wav",
    file_path="output.wav"
)
