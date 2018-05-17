import io
import os
#sets up my google cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='SpeechProject-a419123553f1.json'

# Transcribes the Speech file according to one of the Google models
# The options for model are: 
#	-default
# 	-video 
# 	-phone_call
# 	-command_and_search
def google_transcribe(speech_file, model):
    """Transcribe the given audio file synchronously with
    the selected model."""
    from google.cloud import speech_v1p1beta1 as speech
    client = speech.SpeechClient()

    with open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.types.RecognitionAudio(content=content)

	#configures the language, model and encoding. Additionally can specify the audio rate, profanity filter, etc.
    config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='en-US',
		model=model,
		enable_automatic_punctuation=True)

    response = client.recognize(config, audio)

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print('-' * 20)
        print(u'Transcript: {}'.format(alternative.transcript))
		

 
for file in os.listdir("audio"):
	print('-' * 100)
	print("File Name:")
	print(file)
	google_transcribe(os.path.join("audio", file), 'default')
	print('-' * 100)
	print("\n")