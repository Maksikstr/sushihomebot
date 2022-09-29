import requests
from bs4 import BeautifulSoup
import json

headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}


def url_get():
    url = "https://sushihome.by/menu/sety/"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")  # html.parser

    data = soup.find("ul", class_="products columns-4")
    card = data.find_all("li")
    for i in card:
        card_url = i.find("a").get("href")
        yield card_url


def result_json():
    result_data = []
    for card_url in url_get():
        response = requests.get(card_url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("main", class_="site-main")
        name = data.find("p", class_="product_title entry-title").text
        price = data.find("span", class_="woocommerce-Price-amount amount").text
        content = data.find("div", class_="woocommerce-product-details__short-description").text.replace("\n", "")
        discription = data.find("div",
                                class_="woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content wc-tab").text
        url_img = data.find("img").get("src")
        result_data.append(
            {
                "картинка": url_img,
                "имя": name,
                "цена": price,
                "состав": content,
                "описание": discription
            }
        )
        print(result_data)
    with open("result_data.json", "w") as file:
        json.dump(result_data, file, indent=2, ensure_ascii=False)


def main():
    result_json()


if __name__ == "__main__":
    main()
