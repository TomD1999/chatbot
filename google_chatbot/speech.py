"""Synthesizes speech from the input string of text."""
from google.cloud import texttospeech
from pydub import AudioSegment
from pydub.playback import play


class SpeechGenerator:
    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()
        self.voice = texttospeech.VoiceSelectionParams(
            language_code="en-GB",
            name="en-GB-News-H",
        )
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16,
            speaking_rate=1
        )

    def generate_speech(self,words):
            
        input_text = texttospeech.SynthesisInput(text=words)


        response = self.client.synthesize_speech(
            request={"input": input_text, "voice": self.voice, "audio_config": self.audio_config}
        )

        # The response's audio_content is binary.
        with open("output.wav", "wb") as out:
            out.write(response.audio_content)
        
        audio = AudioSegment.from_wav("output.wav")
        play(audio)



