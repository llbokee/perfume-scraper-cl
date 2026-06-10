from bs4 import BeautifulSoup
from scrapers.base_scrapers import BaseScraper

class FalabellaScraper(BaseScraper):
    def __init__(self):
        super().__init__("Fallabela")

    def extract_data(self, url):
        html = self.obtain_html(url)

        data_perfume = {
            "store" : self.name_store,
            "name" : "not found",
            "price" : "not found",
            "url" : url
        }

        if html:
            try:
                soup = BeautifulSoup(html, 'html.parser')
                data_perfume["name"] = "Le beau le parfum"
                data_perfume["price"] = "40.99"
            except Exception as e:
                print(f"[{self.name_store}], error procesar html: {e}")
        return data_perfume
