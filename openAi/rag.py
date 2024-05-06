from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
from pinecone import Pinecone, ServerlessSpec

print(os.getenv("PINECONE_KEY"))

pc = Pinecone(api_key='PINECONE_KEY')
print(pc)
client = OpenAI()


with open('health.txt', 'r') as file:
    file_contents = file.read()


embedding_result= client.embeddings.create(
  model="text-embedding-ada-002",
  input=file_contents,
  encoding_format="float"
)

final_embedding= embedding_result.data[0].embedding
print(final_embedding)

index = pc.Index("test")

index.upsert(
    vectors=[
        {"id": "vec1", "values": final_embedding }
    ],
    namespace="ns1"
)







