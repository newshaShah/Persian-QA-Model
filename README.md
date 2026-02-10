# PQuAD: Persian Question Answering Model 🇮🇷

[![Hugging Face Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-yellow)](https://huggingface.co/newsha/PQuAD)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

**PQuAD** is a state-of-the-art **Persian Question Answering (QA)** model.
It is built by fine-tuning **[ParsBERT](https://github.com/hooshvare/parsbert)** (the leading Persian BERT model) on a proprietary QA dataset.

This project was developed as part of a **BSc Thesis** at **Amirkabir University of Technology (Tehran Polytechnic)**.

🔗 **View Live Model:** [huggingface.co/newsha/PQuAD](https://huggingface.co/newsha/PQuAD)

---

## 🚀 Features
- **Architecture:** BERT-based (ParsBERT v2.0)
- **Task:** Extractive Question Answering (SQuAD style)
- **Language:** Persian (Farsi)
- **Framework:** PyTorch & Hugging Face Transformers

## 🛠 Installation

To use this model, you need to install the `transformers` library.

```bash
pip install -r requirements.txt
```

*(Or simply run `pip install transformers torch`)*

## 💻 Usage

You can use the model directly with the Hugging Face `pipeline`.
Copy the code below to run the model:

```python
from transformers import pipeline

# 1. Load the model (downloads automatically from Hugging Face)
qa_pipeline = pipeline("question-answering", model="newsha/PQuAD")

# 2. Define context and question
context = "دانشگاه صنعتی امیرکبیر یکی از با‌سابقه‌ترین دانشگاه‌های فنی ایران است که در سال ۱۳۳۷ در تهران تأسیس شد."
question = "دانشگاه امیرکبیر در چه سالی تأسیس شد؟"

# 3. Get the answer
result = qa_pipeline(question=question, context=context)

print(f"Answer: {result['answer']}")
print(f"Score: {result['score']:.4f}")
# Output: ۱۳۳۷
```

## 🎓 Citation & Credits
- **University:** Amirkabir University of Technology
- **Base Model:** [ParsBERT](https://huggingface.co/hooshvare/parsbert-base-uncased) by Hooshvare Lab

---
*Created by Newsha*
