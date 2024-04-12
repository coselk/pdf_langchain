from transformers import AutoModel, AutoTokenizer
# from huggingface_hub import login
# login()
# list of sentences
sentences = ['今天是个好日子', '我有些饿了','想吃奶油面包']

# init model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('maidalun1020/bce-embedding-base_v1',trust_remote_code=True)
model = AutoModel.from_pretrained('maidalun1020/bce-embedding-base_v1',trust_remote_code=True)

device = 'cpu'  # if no GPU, set "cpu"
model.to(device)

# get inputs
inputs = tokenizer(sentences, padding=True, truncation=True, max_length=512, return_tensors="pt")
inputs_on_device = {k: v.to(device) for k, v in inputs.items()}

# get embeddings
outputs = model(**inputs_on_device, return_dict=True)
embeddings = outputs.last_hidden_state[:, 0]  # cls pooler
embeddings = embeddings / embeddings.norm(dim=1, keepdim=True)  # normalize

print(embeddings)
