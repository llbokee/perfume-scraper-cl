# IA
import sqlite3

def probar_mi_base():
    print("=== INICIANDO PRUEBA DE LA BASE DE DATOS ===")
    
    # 1. Nos conectamos a tu base de datos recién creada
    connection = sqlite3.connect("perfumes.db")
    cursor = connection.cursor()
    
    try:
        # 2. SIMULACIÓN: Fragrantica guarda un objeto maestro
        print("\n[+] Insertando un perfume de prueba (Simulando Fragrantica)...")
        cursor.execute("""
            INSERT OR IGNORE INTO perfumes (slug_uni, name_general, gender, description, chords, output_notes)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            "jean-paul-gaultier-le-male-elixir",
            "Le Male Elixir",
            "Masculino",
            "Un perfume dulce y avainillado lanzado en 2023.",
            '["vanilla", "sweet", "amber"]', # Lo guardamos como texto simulando un JSON
            '["lavanda", "menta"]'
        ))
        
        # Recuperamos el ID que la base de datos le asignó automáticamente a este perfume
        cursor.execute("SELECT id FROM perfumes WHERE slug_uni = 'jean-paul-gaultier-le-male-elixir'")
        perfume_id = cursor.fetchone()[0]
        print(f"-> Perfume guardado con éxito. ID generado: {perfume_id}")
        
        # 3. SIMULACIÓN: Las tiendas chilenas guardan precios amarrados a ese ID
        print("\n[+] Insertando precios de diferentes tiendas...")
        
        # Precio de Falabella (Con oferta)
        cursor.execute("""
            INSERT INTO prices_perfumes (perfume_id, store, price, price_offer, url_product)
            VALUES (?, ?, ?, ?, ?)
        """, (perfume_id, "Falabella", 110990, 95990, "https://falabella.com/le-male"))
        
        # Precio de Elite Perfumes (Sin oferta)
        cursor.execute("""
            INSERT INTO prices_perfumes (perfume_id, store, price, price_offer, url_product)
            VALUES (?, ?, ?, ?, ?)
        """, (perfume_id, "Elite Perfumes", 89990, None, "https://eliteperfumes.cl/le-male"))
        
        # 4. LA PRUEBA DE FUEGO: Hacer la consulta relacional (Unir los cuadernos)
        print("\n[+] Consultando los datos cruzados desde el backend:")
        cursor.execute("""
            SELECT p.name_general, pr.store, pr.price, pr.price_offer, pr.date_registered
            FROM perfumes p
            JOIN prices_perfumes pr ON p.id = pr.perfume_id
            WHERE p.id = ?
        """, (perfume_id,))
        
        resultados = cursor.fetchall()
        
        print("\n==================================================")
        for fila in resultados:
            nombre, tienda, precio_normal, precio_oferta, fecha = fila
            print(f"Perfume: {nombre} | Tienda: {tienda}")
            print(f"  - Precio Normal: ${precio_normal}")
            print(f"  - Precio Oferta: ${precio_oferta if precio_oferta else 'No tiene'}")
            print(f"  - Capturado el:  {fecha}")
            print("-" * 50)
            
    except Exception as e:
        print(f"[-] Algo falló en la prueba: {e}")
        
    finally:
        # Cerramos sin guardar permanentemente (o puedes cambiarlo a connection.commit() si quieres dejar los datos guardados)
        connection.commit()
        connection.close()
        print("\n=== PRUEBA FINALIZADA COMPLETA ===")

if __name__ == "__main__":
    probar_mi_base()