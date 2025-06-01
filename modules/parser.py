import re

def extract_keywords(text):
    return re.findall(r'\b[A-Z][a-zA-Z0-9+\-#]*\b(?:\s[A-Z][a-z]+)?', text)

def extract_skills_from_jd_by_section(jd_text):
    must_have, nice_to_have, extracted_skills = [], [], []
    must_keywords = ["must-have", "required", "requirements", "you should have"]
    nice_keywords = ["nice to have", "preferred", "bonus", "plus"]

    jd_text = jd_text.replace("\r", "").strip()
    lines = jd_text.split("\n")
    current_section = None

    for line in lines:
        line_clean = line.strip()
        line_lower = line_clean.lower()

        if not line_clean or len(line_clean) < 3:
            continue

        if any(kw in line_lower for kw in must_keywords):
            current_section = "must"
            continue
        elif any(kw in line_lower for kw in nice_keywords):
            current_section = "nice"
            continue

        if line_clean.startswith(("-", "*", "•")):
            skill = line_clean.lstrip("-•*").strip()
            extracted_skills.append((current_section, skill))

    for section, skill_line in extracted_skills:
        keywords = extract_keywords(skill_line)
        if section == "must":
            must_have.extend(keywords)
        elif section == "nice":
            nice_to_have.extend(keywords)

    return sorted(set(must_have)), sorted(set(nice_to_have))
