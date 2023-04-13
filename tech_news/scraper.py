import time
import requests
import re
from parsel import Selector


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


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    # URL = "https://blog.betrybe.com"
    # URL = "https://blog.betrybe.com/tecnologia/arquivo-bin/"
    # URL = "https://blog.betrybe.com/noticias/axie-infinity-reabre-transacoes-apos-perder-bilhoes/"
    # URL = "https://blog.betrybe.com/carreira/curriculo-para-primeiro-emprego/"
    # URL = "https://blog.betrybe.com/carreira/empowerment-lideranca-o-que-e/"
    URL = "https://blog.betrybe.com/carreira/gatilho-mental-tudo-sobre/"
    a = fetch(URL)
    # b = scrape_updates(a)
    # b = scrape_next_page_link(a)
    b = scrape_news(a)
    print(b)
