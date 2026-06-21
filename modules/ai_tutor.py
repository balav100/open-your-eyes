from transformers import pipeline
from modules.braille_converter import text_to_braille

tutor_pipeline = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)


def ask_ai_tutor(question):

    prompt = f"""
    Explain clearly for a visually impaired student:

    {question}
    """

    response = tutor_pipeline(
        prompt,
        max_length=200,
        do_sample=True
    )

    return response[0]["generated_text"]


def explain_chapter(text, question):
    """
    Explain a chapter based on user question and return both 
    text and braille explanations
    """
    prompt = f"""
    Based on this text:
    {text}
    
    Please answer this question clearly for a visually impaired student:
    {question}
    """

    response = tutor_pipeline(
        prompt,
        max_length=200,
        do_sample=True
    )

    explanation = response[0]["generated_text"]
    braille_explanation = text_to_braille(explanation)

    return explanation, braille_explanation