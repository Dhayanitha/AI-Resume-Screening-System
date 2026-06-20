from src.database.db import get_connection

def save_ranking(result):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO rankings (
            score,
            transformer_score,
            tfidf_score,
            skill_score,
            llm_summary
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            result["final_score"],
            result["score_breakdown"]["transformer"],
            result["score_breakdown"]["tfidf"],
            result["score_breakdown"]["skill"],
            result["llm_summary"]
        )
    )

    conn.commit()

    conn.close()