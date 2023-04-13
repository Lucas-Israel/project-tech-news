import time
import requests
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


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    # URL = "https://app.betrybe.com/"
    URL = "https://blog.betrybe.com"
    # URL = "https://httpbin.org/delay/5"
    a = fetch(URL)
    # b = scrape_updates(a)
    b = scrape_next_page_link(a)
    print(b)
