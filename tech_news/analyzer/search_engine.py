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
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    # inputs = ["bacana", "BACANA", "2", "Titulo invalido"]

    # for BUSCA in inputs:
    #     a = search_by_title(BUSCA)
    #     print(a)

    inputs = ["2021-04-04", "2022-04-07", "2023-05-14", "04-04-2021"]

    for BUSCA in inputs:
        a = search_by_date(BUSCA)
        print(a)
