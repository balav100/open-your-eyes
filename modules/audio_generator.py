from gtts import gTTS
import os


def generate_audio(text):

    text = text[:3000]

    tts = gTTS(
        text=text,
        lang='en'
    )

    audio_path = os.path.join(
        "audio",
        "book_audio.mp3"
    )

    tts.save(audio_path)

    return audio_path