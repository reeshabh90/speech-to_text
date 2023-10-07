from google.cloud import speech
from google.oauth2 import service_account
import io

def speech_to_text(
    config: speech.RecognitionConfig,
    audio: speech.RecognitionAudio,
) -> speech.RecognizeResponse:
    client_file = 'YOUR Config File'
    credentials = service_account.Credentials.from_service_account_file(client_file)
    client = speech.SpeechClient(credentials=credentials)

    # Synchronous speech recognition request
    response = client.recognize(config=config, audio=audio)

    return response


def print_response(response: speech.RecognizeResponse):
    for result in response.results:
        print_result(result)


def print_result(result: speech.SpeechRecognitionResult):
    best_alternative = result.alternatives[0]
    print("-" * 80)
    print(f"language_code: {result.language_code}")
    print(f"transcript:    {best_alternative.transcript}")
    print(f"confidence:    {best_alternative.confidence:.0%}")


config = speech.RecognitionConfig(
    language_code="en",
)
audio = speech.RecognitionAudio(
    uri="gs://cloud-samples-data/speech/brooklyn_bridge.flac",
)

# audio_file = './AudioFile/LLMINtro-converted.mp3'
# with io.open(audio_file, 'rb') as f:
#     content = f.read()
#     audio = speech.RecognitionAudio(content)

response = speech_to_text(config, audio)
print_response(response)