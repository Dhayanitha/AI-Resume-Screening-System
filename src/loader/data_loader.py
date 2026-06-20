import os 
from src.loader.file_loader import load_resume_file

def load_resumes(folder_path):
    resumes = []
    seen = set()
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        print(" Processing:", file)
        if file.endswith((".pdf",".docx",".txt")):
            text = load_resume_file(file_path)
            if not text or len(text.strip()) < 20:
                continue
            print("   Extracted text length:", len(text))
            if text and text not in seen:
               resumes.append(text)
               seen.add(text)
    return resumes

def load_job_description(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        job_desc = f.read()
    return job_desc

