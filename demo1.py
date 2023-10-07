import io
from google.oauth2 import service_account
from google.cloud import speech

client_file = 'YOUR Config FIle'
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

# Translate Text
def translate_text(target: str, text: str) -> dict:
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client(credentials=credentials)

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print("Text: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    return result


#Load the audio file
# audio_file = './AudioFile/LLMINtro-converted.wav'
# with io.open(audio_file, 'rb') as f:
#     content = f.read()
#     audio = speech.RecognitionAudio(content)

audio = speech.RecognitionAudio(
    # uri="gs://cloud-samples-data/speech/brooklyn_bridge.flac",
    uri= "Your Audio URI"
)


config = speech.RecognitionConfig(
        # encoding=speech.RecognitionConfig.AudioEncoding.FLAC,        
        encoding = 'LINEAR16',
        language_code = 'en-US',
        sample_rate_hertz = 44100,
        audio_channel_count = 2,
    )

# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)

for result in response.results:
    print(f"Transcript: {result.alternatives[0].transcript}")
    print(translate_text('fr', result.alternatives[0].transcript))


