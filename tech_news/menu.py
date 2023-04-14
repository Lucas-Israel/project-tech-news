import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)


def key_guard_clausules(key):
    if key == 0:
        inputed_key = input("Digite quantas notícias serão buscadas:")
        get_tech_news(int(inputed_key))
        return
    if key == 1:
        inputed_key = input("Digite o título:")
        return search_by_title(inputed_key)
    if key == 2:
        inputed_key = input("Digite a data no formato aaaa-mm-dd:")
        return search_by_date(inputed_key)
    if key == 3:
        inputed_key = input("Digite a categoria:")
        return search_by_category(inputed_key)
    return top_5_categories()


# Requisitos 11 e 12
def analyzer_menu():
    key = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair."""
    )

    if not key:
        return print("Opção inválida")

    inted_key = int(key)

    if inted_key == 5:
        return print("Encerrando script")
    if inted_key > 5:
        return sys.stderr.write("Opção inválida\n")

    result = key_guard_clausules(inted_key)

    if result is None:
        return

    print(result)


if __name__ == "__main__":
    analyzer_menu()
