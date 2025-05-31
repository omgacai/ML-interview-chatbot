from openai import AzureOpenAI
from src.config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, EMBEDDING_DEPLOYMENT

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version="2023-05-15"
)

MAX_TOKENS_PER_INPUT = 7000 

def truncate_text(text, max_words=MAX_TOKENS_PER_INPUT):
    words = text.split()
    return " ".join(words[:max_words])

def embed_text(texts):
    cleaned_texts = [truncate_text(t) for t in texts]

    response = client.embeddings.create(
        input=cleaned_texts,
        model=EMBEDDING_DEPLOYMENT
    )
    return [record.embedding for record in response.data]
