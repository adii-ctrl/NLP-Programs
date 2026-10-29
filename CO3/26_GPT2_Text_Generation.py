from transformers import AutoTokenizer, AutoModelForCausalLM

name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(name)
model = AutoModelForCausalLM.from_pretrained(name)
prompt = "Natural language processing helps computers"
inputs = tokenizer(prompt, return_tensors="pt")
output = model.generate(**inputs, max_new_tokens=60, do_sample=True,
                        temperature=0.8, top_p=0.9,
                        pad_token_id=tokenizer.eos_token_id)
print(tokenizer.decode(output[0], skip_special_tokens=True))
