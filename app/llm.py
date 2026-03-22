from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

def ask_llm(context, question):
    prompt = f"""
Answer only using the context below.

Context:
{context}

Question:
{question}
"""

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=1024,
        stream=True
    )

    final_answer = ""

    for chunk in completion:
        if not chunk.choices:
            continue

        delta = chunk.choices[0].delta

        if delta.content:
            print(delta.content, end="", flush=True)
            final_answer += delta.content

    print()
    return final_answer