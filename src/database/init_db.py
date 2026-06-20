from src.database.db import get_connection

def init_database():

    conn = get_connection()

    cursor = conn.cursor()

    # resumes table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT
    )
    """)

    # rankings table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rankings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        score REAL,
        transformer_score REAL,
        tfidf_score REAL,
        skill_score REAL,
        llm_summary TEXT
    )
    """)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    init_database()