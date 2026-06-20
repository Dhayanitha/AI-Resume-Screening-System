import re 

def highlight_text(resume_text,keywords):
    highlighted =resume_text
    for word in keywords:
        if len(word)<3:
            continue
        pattern = re.compile(rf"\b({re.escape(word)})\b",re.IGNORECASE)
        highlighted = pattern.sub(r"<mark>\1</mark>",highlighted)
    return highlighted