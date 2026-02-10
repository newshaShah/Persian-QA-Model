# PQuAD: Persian Question Answering Model 

[![Hugging Face Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-yellow)](https://huggingface.co/newsha/PQuAD)
[![Paper](https://img.shields.io/badge/ScienceDirect-Read%20Paper-orange)](https://www.sciencedirect.com/science/article/abs/pii/S0885230823000050)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

**PQuAD** is a Persian Question Answering model fine-tuned on the **PQuAD Dataset**.
The model is based on **[ParsBERT](https://github.com/hooshvare/parsbert)** and achieves state-of-the-art results in extractive QA tasks for the Persian language.

This project utilizes the dataset introduced in the paper **"PQuAD: A Persian Question Answering Dataset"**.

🔗 **View Live Model:** [huggingface.co/newsha/PQuAD](https://huggingface.co/newsha/PQuAD)

---

## 🚀 Features
- **Dataset:** Trained on PQuAD (Persian Question Answering Dataset)
- **Base Architecture:** ParsBERT (v2.0)
- **Task:** Extractive Question Answering
- **Language:** Persian (Farsi)

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

# 1. Load the model
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

## 📄 Citation

If you use this model or the PQuAD dataset in your research, please cite the original paper:

```bibtex
@article{PQuAD2023,
  title = {PQuAD: A Persian Question Answering Dataset},
  journal = {Computer Speech & Language},
  volume = {81},
  year = {2023},
  doi = {10.1016/j.csl.2023.101505},
  url = {https://www.sciencedirect.com/science/article/abs/pii/S0885230823000050}
}
```

## 🎓 Credits
- **University:** Amirkabir University of Technology (Tehran Polytechnic)
- **Base Model:** ParsBERT by Hooshvare Lab

---
*Maintained by Newsha*
