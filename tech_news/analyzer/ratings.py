from tech_news.database import get_collection


# Requisito 10
def top_5_categories():
    new_list = []
    collection = get_collection()
    pipeline = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]
    to_return = collection.aggregate(pipeline=pipeline)
    for element in to_return:
        new_list.append(element["_id"])
    return new_list


if __name__ == "__main__":
    a = top_5_categories()
    for b in a:
        print(b)
