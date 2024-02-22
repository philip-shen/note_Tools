'''
https://qdrant.tech/documentation/quick-start/
'''
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import PointStruct
from qdrant_client.http.models import Filter, FieldCondition, MatchValue
from qdrant_client.http.models import Distance, VectorParams


COLLECTION_NAME = "test_collection"#"Lyrics"

'''
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
'''
def connection():
    client = QdrantClient("http://localhost:6333")
    
    client.delete_collection(collection_name=COLLECTION_NAME)

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=4, distance=Distance.DOT),
    )

    return client

def collection(client):
    client.upsert(
        collection_name=COLLECTION_NAME,
        wait=True,
        points=[
            PointStruct(id=1, vector=[0.05, 0.61, 0.76, 0.74], payload={"city": "京都"}),
            PointStruct(id=2, vector=[0.19, 0.81, 0.75, 0.11], payload={"city": ["大阪", "奈良"]}),
            PointStruct(id=3, vector=[0.36, 0.55, 0.47, 0.94], payload={"city": ["大阪", "滋賀"]}),
            PointStruct(id=4, vector=[0.18, 0.01, 0.85, 0.80], payload={"city": ["奈良", "兵庫"]}),
            PointStruct(id=5, vector=[0.24, 0.18, 0.22, 0.44], payload={"count": [0]}),
            PointStruct(id=6, vector=[0.35, 0.08, 0.11, 0.44]),
        ]
    )

def search(client):
    search_result = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=[0.2, 0.1, 0.9, 0.7], 
        query_filter=Filter(
            must=[
                FieldCondition(
                    key="city",
                    match=MatchValue(value="奈良")
                )
            ]
        ),
        limit=3
    )

    print(search_result[0])
    # ScoredPoint(id=4, score=1.362, ...)

if __name__ == '__main__':
    client = connection()
    collection(client)
    search(client)