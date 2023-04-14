from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    new_list = []
    if not title:
        return new_list
    search_content = search_news({"title": {"$regex": title, "$options": "i"}})
    for element in search_content:
        new_list.append((element["title"], element["url"]))

    return new_list


# Requisito 8
def search_by_date(date):
    new_list = []
    if not date:
        return new_list
    try:
        new_date_format = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
    except ValueError:
        raise ValueError("Data inválida")

    search_content = search_news(
        {"timestamp": {"$regex": new_date_format, "$options": "i"}}
    )
    for element in search_content:
        new_list.append((element["title"], element["url"]))

    return new_list


# Requisito 9
def search_by_category(category):
    new_list = []
    if not category:
        return new_list
    search_content = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    for element in search_content:
        new_list.append((element["title"], element["url"]))

    return new_list
