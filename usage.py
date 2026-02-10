from transformers import pipeline

def ask_question(context, question):
    print("Loading model from Hugging Face... (newsha/PQuAD)")
    # Load the model directly from your Hugging Face hub
    qa_pipeline = pipeline("question-answering", model="newsha/PQuAD")
    
    # Get prediction
    result = qa_pipeline(question=question, context=context)
    return result

if __name__ == "__main__":
    # Example Context (متن نمونه)
    context_text = """
    دانشگاه صنعتی امیرکبیر یکی از با‌سابقه‌ترین دانشگاه‌های فنی ایران است 
    که در سال ۱۳۳۷ در تهران تأسیس شد. این دانشگاه قبلاً پلی‌تکنیک تهران نام داشت.
    """
    
    # Example Question (سوال نمونه)
    question_text = "دانشگاه امیرکبیر در چه سالی تأسیس شد؟"
    
    print("-" * 40)
    print(f"Context: {context_text.strip()}")
    print(f"Question: {question_text}")
    print("-" * 40)

    # Run the model
    answer = ask_question(context_text, question_text)
    
    print(f"Answer: {answer['answer']}")
    print(f"Confidence Score: {answer['score']:.4f}")
    print("-" * 40)
