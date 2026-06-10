import requests

class BaseScraper:
    def __init__(self, name_store):
        self.name_store = name_store
        #bot que usaremos para entrar a la paginas web y acceder luego a su informacion
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    # funcion general para acceder a la informacion de la pagina
    def obtain_html(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                return response.text
            print(f"[{self.name_store}], Connection error: [{response.status_code}]")
            return None
        except Exception as e:
            print(f"[{self.name_store}], url [{url}], error: {e}")
            return None