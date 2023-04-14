import time
import requests
import re
from parsel import Selector

from tech_news.database import (
    create_news,
    # find_news,
    # get_collection,
    # insert_or_update,
    # search_news,
)


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        header = {"user-agent": "Fake user-agent"}
        result = requests.get(url, headers=header, timeout=3)
    except requests.ReadTimeout:
        return None
    else:
        if result.status_code == 200:
            return result.text
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    if html_content is None:
        return []
    return selector.css(".cs-overlay-link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".next::attr(href)").get()


def formater(string):
    regex = r"\xa0|<[^>]*>"
    to_return = re.sub(regex, "", string)
    if to_return[-1] == " ":
        to_return = to_return[:-1]
    return to_return


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    return {
        "url": selector.css("head link[rel='canonical']::attr(href)").get(),
        "title": formater(selector.css(".entry-title::text").get()),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "reading_time": int(
            selector.css(".meta-reading-time::text").re_first(r"\d*")
        ),
        "summary": formater(
            selector.xpath('//div[contains(@class, "entry-content")]/p').get(),
        ),
        "category": selector.css(".label::text").get(),
    }


def full_list_link(amount):
    URL = "https://blog.betrybe.com/"
    new_list = []
    articles_per_page = 12
    count = 0
    while URL and count < (amount + 1):
        fetch_result = fetch(URL)
        new_list.extend(scrape_updates(fetch_result))
        URL = scrape_next_page_link(fetch_result)
        count += articles_per_page
    return new_list


# Requisito 5
def get_tech_news(amount):
    full_list = full_list_link(amount)
    new_list = []
    for index, url in enumerate(full_list):
        if index < amount:
            new_fetch = fetch(url)
            new_list.append(scrape_news(new_fetch))
    create_news(new_list)
    return new_list


if __name__ == "__main__":
    a = get_tech_news(13)
