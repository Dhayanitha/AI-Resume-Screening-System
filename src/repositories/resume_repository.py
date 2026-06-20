from src.database.db import get_connection

def save_resume(content):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO resumes (content)
        VALUES (?)
        """,
        (content,)
    )

    conn.commit()

    conn.close()