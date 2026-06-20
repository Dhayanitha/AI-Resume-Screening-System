import os 
import json 
import hashlib
import asyncio
from openai import AsyncOpenAI

CACHE_FILE = "data/cache/llm_cache.json"
os.makedirs("data/cache",exist_ok=True)

#load cache 
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE,"r") as f :
        CACHE = json.load(f)
else:
    CACHE ={}

def _make_key(job_text,resume_text):
    raw = job_text[:200]+resume_text[:200]
    return hashlib.md5(raw.encode()).hexdigest()

def _save_cache():
    with open(CACHE_FILE, "w") as f:
        json.dump(CACHE, f, indent=4)

async def generate_llm_explanation(job_text,resume_text,skills,score):
    key = _make_key(job_text,resume_text)
    
    # cache hit
    if key in CACHE:
        return CACHE[key]
    
    api_key = os.getenv("OPENAI_API_KEY")

    #fallback 
    if not api_key:
        result = (
            f"Matches {len(skills)} skills "
            f"with score {round(score, 2)}. "
            f"Good fit for this role."
        )
        CACHE[key] = result
        _save_cache()
        return result 
    
    #LLM (async)
    try:
        client = AsyncOpenAI(api_key=api_key)
        prompt = f"""
        Job:{job_text[:200]}
        Resume:{resume_text[:200]}
        Skills:{skills}
        Score:{score}

        Explain fit in 2 lines.
        """
        response = await client.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[{"role":"user","content":prompt}],
            max_tokens=60 
        )

        result = response.choices[0].message.content
        CACHE[key]= result
        _save_cache()
        return result
    except Exception as e:
        return f"LLM error: {str(e)}"
