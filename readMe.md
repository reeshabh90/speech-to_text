# Speech to Text Translation

This code snippet demonstrates how to use the Google Cloud Speech-to-Text and Translation APIs to transcribe and translate audio files.

## Prerequisites

1. Python 3.x installed on your machine.
2. Google Cloud Speech-to-Text and Translation APIs enabled.
3. Service account credentials JSON file ( `speech-to-text-demo.json` ) obtained from the Google Cloud Console.

## Setup

1. Install the required Python packages by running the following command:
pip install google-cloud-speech google-cloud-translate
2. Replace  `'Your Audio URI'`  in the code with the URI of your audio file. Alternatively, you can uncomment the  `audio_file`  section and provide the local path to the audio file.

3. Ensure that the audio file format is supported by the Speech-to-Text API (e.g., FLAC, WAV, etc.). Adjust the  `config`  parameters (encoding, sample rate, etc.) according to your audio file specifications.

## Usage

1. Run the script using the command:
python your_script_name.py
2. The script will transcribe the audio file and display the results in the console.

3. It will also translate the transcriptions to the target language (in this case, French) using the Google Cloud Translation API.

4. The translated text, along with the detected source language, will be printed in the console.

## Note

- Make sure you have the necessary permissions and quota to use the Google Cloud APIs.
- Refer to the official Google Cloud documentation for detailed information on the Speech-to-Text and Translation APIs.