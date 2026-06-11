import sqlite3

def create_db():
    connection = sqlite3.connect("perfumes.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS perfumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slug_uni TEXT UNIQUE NOT NULL,
            name_general TEXT NOT NULL,
            gender TEXT,
            description TEXT,
            chords TEXT,
            output_notes TEXT   
            )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices_perfumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            perfume_id INTEGER NOT NULL,
            store TEXT NOT NULL,
            price INTEGER NOT NULL,
            price_offer INTEGER NULL,
            url_product TEXT NOT NULL,
            date_registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (perfume_id) REFERENCES perfumes (id) ON DELETE CASCADE 
            )
        """)
    # ON DELETED CASCADE para borrar todo los datas en caso de eliminar un perfume
    connection.commit()
    connection.close()
    print(True)
if __name__ == "__main__":
    create_db()