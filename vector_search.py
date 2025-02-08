pipeline = [
    {
        "$vectorSearch": {
            "index": "vectorPlotIndex",
            "path": "plot_embedding",
            "queryVector": embedding,
            "numCandidates": 100,
            "filter": {"year": {"$gt": 2010}},
            "limit": 10
        }
    },
    {
        "$project": {
            "title": 1,
            "plot": 1,
            "year": 1,
            "score": {"$meta": "vectorSearchScore"}
        }
    }
]

x = collection.aggregate(pipeline)
