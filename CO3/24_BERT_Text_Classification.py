from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer

model_name = "distilbert/distilbert-base-uncased"
texts = [
    "I loved this movie", "Amazing acting", "Excellent film", "Wonderful story",
    "I hated this movie", "Terrible acting", "Awful film", "Boring story",
    "Very enjoyable", "Very disappointing"
]
labels = [1, 1, 1, 1, 0, 0, 0, 0, 1, 0]
data = Dataset.from_dict({"text": texts, "label": labels}).train_test_split(test_size=0.2, seed=42)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=64)

data = data.map(tokenize, batched=True)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
args = TrainingArguments(output_dir="bert_results", num_train_epochs=2,
                         per_device_train_batch_size=2, per_device_eval_batch_size=2,
                         save_strategy="no", report_to="none")
trainer = Trainer(model=model, args=args, train_dataset=data["train"],
                  eval_dataset=data["test"], processing_class=tokenizer)
trainer.train()
print(trainer.evaluate())
