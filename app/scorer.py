def calculate_authenticity_score(analysis: dict) -> int:
    score = 100

    red_flags = analysis["red_flags"]
    buzzwords = analysis["buzzwords"]
    skills = analysis["skills"]

    score -= len(red_flags) * 12
    score -= len(buzzwords) * 4

    if len(skills) > 15:
        score -= 10

    if len(skills) < 3:
        score -= 15

    if score < 0:
        score = 0

    return score


def get_score_label(score: int) -> str:
    if score >= 80:
        return "Strong Authenticity"

    if score >= 60:
        return "Moderate Authenticity"

    if score >= 40:
        return "Needs Improvement"

    return "High Risk of Overclaiming"


def generate_suggestions(analysis: dict) -> list:
    suggestions = []

    if analysis["buzzwords"]:
        suggestions.append("Reduce generic buzzwords and replace them with measurable achievements.")

    if analysis["red_flags"]:
        suggestions.append("Add project proof for every major technical skill you mention.")

    if len(analysis["skills"]) > 15:
        suggestions.append("Avoid listing too many skills. Keep only skills you can explain in interviews.")

    if len(analysis["skills"]) < 3:
        suggestions.append("Add relevant technical skills with project-based proof.")

    if not suggestions:
        suggestions.append("Your resume looks consistent. Add metrics and links to make it even stronger.")

    return suggestions
