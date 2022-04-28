import grpc
import riva_api.riva_nlp_pb2 as rnlp
import riva_api.riva_nlp_pb2_grpc as rnlp_srv

def dgx_enquire(queries):
    channel = grpc.insecure_channel("localhost:50051")
    riva_nlp = rnlp_srv.RivaLanguageUnderstandingStub(channel) 
    request = rnlp.TextClassRequest()
    request.model.model_name = "riva_text_classification_default"
    for query in queries:
        request.text.append(query)
    resp = riva_nlp.ClassifyText(request)
    return resp.results[0].labels[0].class_name
    
if __name__ == '__main__':
    dgx_enquire()
