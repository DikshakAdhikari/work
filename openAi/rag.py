from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
from pinecone import Pinecone, ServerlessSpec

print(os.getenv("PINECONE_KEY"))

pc = Pinecone(api_key='YOUR_API_KEY')

client = OpenAI()

response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-3-small"
)

print(response.data[0].embedding)