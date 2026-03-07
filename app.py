
import gradio as gr
import torch
import pickle
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from huggingface_hub import hf_hub_download

model_name = "Musadiq7860/resume-screener"
tokenizer  = AutoTokenizer.from_pretrained(model_name)
model      = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

le_path = hf_hub_download(repo_id=model_name, filename="label_encoder.pkl")
with open(le_path, "rb") as f:
    le = pickle.load(f)

def predict(text):
    if not text.strip():
        return "Please enter some resume text."
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        probs   = outputs.logits.softmax(dim=-1)
        top3    = probs.topk(3)

    results = ""
    for i, (prob, idx) in enumerate(zip(top3.values[0], top3.indices[0])):
        label = le.inverse_transform([idx.item()])[0]
        results += f"#{i+1} {label}: {prob.item()*100:.1f}%\n"
    return results.strip()

gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=10, placeholder="Paste resume text here..."),
    outputs=gr.Textbox(label="Top 3 Matching Job Categories"),
    title="AI Resume Screener",
    description="Paste a resume and get top 3 matching job categories."
).launch()
