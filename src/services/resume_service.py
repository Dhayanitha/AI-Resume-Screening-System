from src.loader.data_loader import load_resumes

from src.services.preprocessing_service import (
    preprocess_job,
    preprocess_resumes
)

from src.services.scoring_service import (
    calculate_scores
)

from src.services.explanation_service import (
    build_explanations
)

from src.storage.save_results import save_results

from src.config.settings import (
    RESUME_FOLDER,
    TOP_K
)

from src.repositories.ranking_repository import (
    save_ranking
)

async def process_resumes(request):

    # load resumes
    resumes = load_resumes(RESUME_FOLDER)

    # preprocess
    job_data = preprocess_job(
        request.job_description
    )

    clean_resumes = preprocess_resumes(resumes)

    # scoring
    scored = calculate_scores(
        job_data["clean_job"],
        clean_resumes,
        job_data["job_skills"]
    )

    # filtering
    filtered = []

    for i, item in enumerate(scored):

        if item["final_score"] < request.min_score:
            continue

        if request.required_skills:

            required = set(
                map(str.lower, request.required_skills)
            )

            resume_skills = set(
                map(str.lower, item["skills"])
            )

            if not required.issubset(resume_skills):
                continue

        item["resume"] = resumes[i]

        filtered.append(item)

    # ranking
    ranked = sorted(
        filtered,
        key=lambda x: x["final_score"],
        reverse=True
    )

    ranked = ranked[:TOP_K]

    # explanations
    results = await build_explanations(
        ranked,
        job_data["clean_job"],
        job_data["job_skills"]
    )

    for result in results:
        save_ranking(result)

    # save
    file_name = save_results(results)

    return {
        "file_saved": file_name,
        "rankings": results
    }