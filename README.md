readme = """# 🧠 AI Resume Screener

A fine-tuned DistilBERT model that classifies resumes into 43 job categories with **88% accuracy**.

## 🚀 Live Demo
👉 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/Musadiq7860/resume-screener)

## 📊 Model Performance
| Metric | Score |
|--------|-------|
| Test Accuracy | 88% |
| Macro F1 | 0.87 |
| Training Epochs | 3 |
| Categories | 43 |

**Best categories:** Civil Engineer (0.98), SAP Developer (0.98), Aviation (0.97)

## 🛠️ Tech Stack
- **Model:** distilbert-base-uncased (fine-tuned)
- **Dataset:** [resume-atlas](https://huggingface.co/datasets/ahmedheakl/resume-atlas) — 13,389 resumes
- **Framework:** PyTorch + HuggingFace Transformers
- **UI:** Gradio
- **Deployment:** HuggingFace Spaces

## 📁 Project Structure
```
resume-screener/
├── app.py                    # Gradio app
├── requirements.txt          # Dependencies
└── cv-resume-screener.ipynb  # Training notebook
```

## ⚙️ Run Locally
```bash
pip install -r requirements.txt
python app.py
```

## 🤗 Model on HuggingFace
👉 [Musadiq7860/resume-screener](https://huggingface.co/Musadiq7860/resume-screener)

## 📌 Job Categories (Sample)
Data Science, Software Engineer, React Developer, DevOps, Civil Engineer,
Aviation, SAP Developer, HR, Marketing, Accountant, and 33 more...

## 👤 Author
**Muhammad Mussadiq** — [GitHub](https://github.com/Musadiq7860) · [HuggingFace](https://huggingface.co/Musadiq7860)
"""

with open("README.md", "w") as f:
    f.write(readme)

os.system("git add README.md")
os.system('git commit -m "Add README"')
os.system("git push")
print("✅ README pushed")
