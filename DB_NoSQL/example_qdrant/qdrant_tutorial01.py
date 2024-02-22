from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import PointStruct
import openai 

COLLECTION_NAME = "Lyrics"

def connection():
    client = QdrantClient("http://localhost:6333")

    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            distance=models.Distance.COSINE,
            size=1536),
        optimizers_config=models.OptimizersConfigDiff(memmap_threshold=20000),
        hnsw_config=models.HnswConfigDiff(on_disk=True, m=16, ef_construct=100)
    )

    return client

def get_embedding(text, model_name):
    response = openai.Embedding.create(
        input=text,
        engine=model_name
    )
    return response['data'][0]['embedding']

def upsert_vector(client, vectors, data):
    for i, vector in enumerate(vectors):
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=[PointStruct(id=i,
                                vector=vectors[i],
                                payload=data[i])]
        )

    print("upsert finish")

def search_from_qdrant(client, vector, k=1):
    search_result = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=k,
        append_payload=True,
    )
    return search_result

def main():

    EMBEDDING_MODEL_NAME = "embedding-ada-002"
    openai.api_base = "https://japanopenai2023ironman.openai.azure.com/"
    openai.api_key = "yourkey"
    openai.api_type = "azure"
    openai.api_version = "2023-03-15-preview"

    qclient = connection()

    data_objs = [
        {
            "id": 1,
            "lyric": "我會披星戴月的想你，我會奮不顧身的前進，遠方煙火越來越唏噓，凝視前方身後的距離"
        },
        {
            "id": 2,
            "lyric": "而我，在這座城市遺失了你，順便遺失了自己，以為荒唐到底會有捷徑。而我，在這座城市失去了你，輸給慾望高漲的自己，不是你，過分的感情"
        }
    ]
    embedding_array = [get_embedding(text["lyric"], EMBEDDING_MODEL_NAME)
                       for text in data_objs]


    upsert_vector(qclient, embedding_array, data_objs)

    query_text = "工程師寫城市"
    query_embedding = get_embedding(query_text, EMBEDDING_MODEL_NAME)
    results = search_from_qdrant(qclient, query_embedding, k=1)
    print(f"尋找 {query_text}:", results)

if __name__ == '__main__':
    main()