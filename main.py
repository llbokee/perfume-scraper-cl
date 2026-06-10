# main.py
# Importamos el scraper específico respetando la ruta de carpetas
from scrapers.stores.scr_fallabela import FalabellaScraper

def ejecutar_rastreo():
    print("=== MONITOR CENTRAL DE PERFUMES CHILE ===")
    
    # 1. Instanciamos el robot de Falabella
    scraper_falabella = FalabellaScraper()
    
    # 2. Link de prueba (puedes usar uno real de perfumes de Falabella si quieres probar)
    url_prueba = "https://www.falabella.com/falabella-cl/category/cat2014/Perfumes"
    
    print(f"\n[+] Iniciando extracción en la tienda...")
    
    # 3. Mandamos a ejecutar la lógica
    resultado = scraper_falabella.extract_data(url_prueba)
    
    # 4. Mostramos el diccionario final en la consola central
    print("\n=== DATOS CAPTURADOS EN SISTEMA CENTRAL ===")
    print(f"Tienda:  {resultado['store']}")
    print(f"Perfume: {resultado['name']}")
    print(f"Precio:  {resultado['price']}")
    print(f"Enlace:  {resultado['url']}")
    print("==========================================")

if __name__ == "__main__":
    ejecutar_rastreo()