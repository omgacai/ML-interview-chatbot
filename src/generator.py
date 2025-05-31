def generate_answer(query, context_chunks, max_tokens=7000):
    from openai import AzureOpenAI
    from src.config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, CHAT_DEPLOYMENT

    client = AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version="2023-05-15"
    )

    # Step 1: Truncate context if needed
    token_estimate = lambda text: len(text.split())  # rough estimate: 1 word ≈ 1 token
    combined = ""
    total_tokens = 0

    for chunk in context_chunks:
        chunk_tokens = token_estimate(chunk)
        if total_tokens + chunk_tokens > max_tokens:
            break
        combined += chunk + "\n\n"
        total_tokens += chunk_tokens

    # Step 2: Build prompt
    prompt = f"Context:\n{combined}\n\nQuestion: {query}\nAnswer:"

    # Step 3: Query LLM
    response = client.chat.completions.create(
        model=CHAT_DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()
