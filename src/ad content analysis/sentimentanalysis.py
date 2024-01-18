from transformers import BertTokenizer, BertModel, pipeline
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')


def preprocess_text(text):
    inputs = tokenizer(text, return_tensors="pt",
                       truncation=True, max_length=512)
    return inputs


def get_bert_embeddings(text):
    inputs = preprocess_text(text)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state


nlp = pipeline("sentiment-analysis",
               model="distilbert-base-uncased-finetuned-sst-2-english")
result = nlp("Get a Sports Car for mere 100$")
print(result)
