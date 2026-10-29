import torch
from transformers import AutoTokenizer, AutoModel

sentences = ["Natural language processing is interesting.",
             "NLP is useful in artificial intelligence."]

for name in ["bert-base-uncased", "gpt2"]:
    tokenizer = AutoTokenizer.from_pretrained(name)
    model = AutoModel.from_pretrained(name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    batch = tokenizer(sentences, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        hidden = model(**batch).last_hidden_state
    mask = batch["attention_mask"].unsqueeze(-1).expand(hidden.size()).float()
    vectors = (hidden * mask).sum(1) / mask.sum(1).clamp(min=1e-9)
    print(name, "embedding shape:", tuple(vectors.shape))
    print("First vector (first 8 values):", vectors[0][:8].tolist())
