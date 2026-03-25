from TTS.api import TTS
import jaconv
import mojimoji


def preprocess_text(text):
    """
    日本語テキストを音声合成向けに前処理する
    """
    # 全角・半角の統一
    text = mojimoji.han_to_zen(text)

    # 英数字を全角に（読み上げが安定しやすい）
    text = mojimoji.han_to_zen(text, digit=False, ascii=False)

    # 必要に応じてカタカナをひらがなに変換（柔らかい印象に）
    # text = jaconv.kata2hira(text)

    return text


def add_pauses(text):
    """
    読み上げの間（ポーズ）を自然に入れる
    """
    # 文節ごとに「、」を入れる（例: 「おでぐちは、みぎがわです。」）
    # ここでは簡易的に既存の句読点を活かす形にする
    return text


# XTTS v2 モデルを GPU にロード
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")

# 元のテキスト
raw_text = "つぎは、しゅうてん、とうきょう。おでぐちは、みぎがわです。"

# 前処理を適用
processed_text = preprocess_text(raw_text)

print(f"元のテキスト: {raw_text}")
print(f"処理後テキスト: {processed_text}")

# 音声生成
tts.tts_to_file(
    text=processed_text,
    speaker_wav="voice_sample.wav",
    language="ja",
    file_path="output.wav",
    speed=0.95,      # 少しゆっくりめに
    temperature=0.7, # 安定性重視
)