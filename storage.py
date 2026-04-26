import sqlite3
import json

def save_to_sqlite(articles, db="news.db"):
    conn = sqlite3.connect(db)
    conn.execute("""CREATE TABLE IF NOT EXISTS articles
        (title TEXT, source TEXT, date TEXT, url TEXT UNIQUE, description TEXT)""")
    for a in articles:
        try:
            conn.execute("INSERT INTO articles VALUES (?,?,?,?,?)",
                (a["title"], a["source"], a["publishedAt"], a["url"], a.get("description","")))
        except sqlite3.IntegrityError:
            pass
    conn.commit()
    conn.close()

def save_to_json(articles, filename="news.json"):
    with open(filename, "w") as f:
        json.dump(articles, f, indent=2)
    print(f"Saved to {filename}")

def load_from_sqlite(db="news.db"):
    conn = sqlite3.connect(db)
    rows = conn.execute("SELECT * FROM articles").fetchall()
    conn.close()
    return [{"title":r[0],"source":r[1],"publishedAt":r[2],"url":r[3],"description":r[4]} for r in rows]