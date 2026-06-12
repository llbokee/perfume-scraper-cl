import pandas as pd
import sqlite3
import json

def test_write_dbset():

    route_files = "dataset_fragnatica.csv"

    try:

        df = pd.read_csv(
            route_files, 
            encoding="ISO-8859-1",
            nrows=10,
            on_bad_lines='skip',
            sep=None,
            engine='python'
        )

        print("conectando db")
        connection = sqlite3.connect("perfumes.db")
        cursor = connection.cursor()

        print("Insertando datos")
        for index, fila in df.iterrows():
            slug_original = fila['Perfume']
            brand = fila['Brand']
            gender = fila['Gender']
            name_clean = slug_original.replace('-', ' ').title()

            top_notes_row = fila['Top']
            if pd.notna(top_notes_row):
                list_notes = [note.strip() for note in top_notes_row.split(',')]
                output_notes_json = json.dumps(list_notes)
            else:
                output_notes_json = json.dumps([])

            description = f"Perfume de la marca {brand.title()} obtenido del dataset."
            chords_json = json.dumps([])
            print("Guardando")
            cursor.execute("""
                INSERT OR IGNORE INTO perfumes (slug_uni, name_general, brand, gender, description, chords, output_notes)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (slug_original, name_clean, brand, gender, description, chords_json, output_notes_json))
            
            print(f"[+] Preparado para DB: {name_clean} | {brand}")

            print("Guardado")
            
        connection.commit()
        connection.close()

    except FileNotFoundError:
        print(f"Error de ruta: '{route_files}'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_write_dbset()