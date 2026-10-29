import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(name)
model = AutoModelForCausalLM.from_pretrained(name)
history = None
print("Type 'quit' to exit.")
while True:
    message = input("You: ").strip()
    if message.lower() in {"quit", "exit"}:
        break
    if not message:
        continue
    new = tokenizer.encode(message + tokenizer.eos_token, return_tensors="pt")
    inputs = torch.cat([history, new], dim=-1) if history is not None else new
    history = model.generate(inputs, max_new_tokens=80, do_sample=True,
                             top_p=0.92, temperature=0.8,
                             pad_token_id=tokenizer.eos_token_id)
    reply = tokenizer.decode(history[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    print("Bot:", reply)
