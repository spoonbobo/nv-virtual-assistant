import grpc
import wave
import riva_api.riva_asr_pb2 as rasr
import riva_api.riva_asr_pb2_grpc as rasr_srv
import riva_api.riva_audio_pb2 as ra

def dgx_enquire_audio(wf, data):
    channel = grpc.insecure_channel("localhost:50051")
    client = rasr_srv.RivaSpeechRecognitionStub(channel)
    config = rasr.RecognitionConfig(
        encoding=ra.AudioEncoding.LINEAR_PCM,
        sample_rate_hertz=wf.getframerate(),
        language_code="en-US",
        max_alternatives=1,
        enable_automatic_punctuation=False,
        audio_channel_count=1
    )
    request = rasr.RecognizeRequest(config=config, audio=data)
    response = client.Recognize(request)
    return response.results[0].alternatives[0].transcript
    
if __name__ == '__main__':
    dgx_enquire_audio()
