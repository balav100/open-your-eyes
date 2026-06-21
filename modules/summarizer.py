from transformers import pipeline

# Load summarization pipeline
summarizer_pipeline = pipeline(
    task="summarization",
    model="facebook/bart-large-cnn"
)


def summarize_text(text):

    # limit very large inputs
    text = text[:2000]

    # generate summary
    summary = summarizer_pipeline(
        text,
        max_length=150,
        min_length=50,
        do_sample=False
    )

    return summary[0]["summary_text"]