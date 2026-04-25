from app.utils import normalize_text


def extract_skills(text: str, skills: list) -> list:
    text = normalize_text(text)
    found_skills = []

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(set(found_skills))


def detect_buzzwords(text: str, buzzwords: list) -> list:
    text = normalize_text(text)
    found_buzzwords = []

    for word in buzzwords:
        if word.lower() in text:
            found_buzzwords.append(word)

    return sorted(set(found_buzzwords))


def detect_skill_project_mismatch(text: str, extracted_skills: list) -> list:
    text = normalize_text(text)
    red_flags = []

    project_keywords = ["project", "built", "developed", "created", "implemented", "designed"]

    has_project_section = any(keyword in text for keyword in project_keywords)

    if len(extracted_skills) >= 8 and not has_project_section:
        red_flags.append("Many technical skills are listed, but project evidence is weak or missing.")

    if "machine learning" in [s.lower() for s in extracted_skills]:
        ml_keywords = ["model", "dataset", "training", "accuracy", "prediction", "classification"]
        if not any(keyword in text for keyword in ml_keywords):
            red_flags.append("Machine Learning is mentioned, but no model/dataset/result evidence was found.")

    if "react" in [s.lower() for s in extracted_skills]:
        frontend_keywords = ["component", "frontend", "ui", "website", "web app"]
        if not any(keyword in text for keyword in frontend_keywords):
            red_flags.append("React is mentioned, but frontend project evidence is weak.")

    return red_flags


def detect_unrealistic_skill_claims(extracted_skills: list) -> list:
    red_flags = []

    advanced_ai_skills = {"Deep Learning", "TensorFlow", "PyTorch", "Computer Vision", "NLP"}
    cloud_devops_skills = {"Docker", "AWS", "Kubernetes"}
    beginner_skills = {"HTML", "CSS", "Python", "C"}

    skill_set = set(extracted_skills)

    if len(skill_set.intersection(advanced_ai_skills)) >= 4 and len(skill_set.intersection(beginner_skills)) <= 1:
        red_flags.append("Advanced AI skills are listed heavily, but basic software fundamentals appear limited.")

    if len(skill_set.intersection(cloud_devops_skills)) >= 2 and "Linux" not in skill_set:
        red_flags.append("Cloud/DevOps tools are mentioned, but Linux is missing, which may look inconsistent.")

    if len(skill_set) > 18:
        red_flags.append("Too many skills are listed. This may look like keyword stuffing.")

    return red_flags
