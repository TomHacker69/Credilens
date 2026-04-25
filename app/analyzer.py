from app.rules import (
    extract_skills,
    detect_buzzwords,
    detect_skill_project_mismatch,
    detect_unrealistic_skill_claims
)


def analyze_resume(text: str, skills: list, buzzwords: list) -> dict:
    extracted_skills = extract_skills(text, skills)
    detected_buzzwords = detect_buzzwords(text, buzzwords)

    mismatch_flags = detect_skill_project_mismatch(text, extracted_skills)
    unrealistic_flags = detect_unrealistic_skill_claims(extracted_skills)

    red_flags = mismatch_flags + unrealistic_flags

    return {
        "skills": extracted_skills,
        "buzzwords": detected_buzzwords,
        "red_flags": red_flags
    }
