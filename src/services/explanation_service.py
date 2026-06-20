import asyncio

from src.explainability.explainer import generate_explanation
from src.explainability.highlighter import highlight_text
from src.explainability.llm_explainer import (
    generate_llm_explanation
)

async def build_explanations(
    ranked_data,
    clean_job,
    job_skills
):

    tasks = []

    for item in ranked_data:

        tasks.append(
            generate_llm_explanation(
                clean_job,
                item["clean_resume"],
                item["skill_matches"],
                item["final_score"]
            )
        )

    llm_results = await asyncio.gather(*tasks)

    results = []

    for idx, item in enumerate(ranked_data):

        explanation = generate_explanation(
            clean_job,
            item["clean_resume"],
            job_skills,
            item["skills"],
            item["final_score"]
        )

        highlighted = highlight_text(
            item["clean_resume"],
            item["skill_matches"]
        )

        results.append({
            "rank": idx + 1,

            "final_score": float(item["final_score"]),

            "score_breakdown": {
                "transformer": float(item["transformer"]),
                "tfidf": float(item["tfidf"]),
                "skill": float(item["skill_score"])
            },

            "skill_matched": item["skill_matches"],

            "matched_keywords":
                explanation["matched_keywords"],

            "summary":
                explanation["summary"],

            "highlighted_resume":
                highlighted[:500],

            "llm_summary":
                llm_results[idx]
        })

    return results