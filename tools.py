# tools.py

def generate_job_description(role: str, level: str, stage: str) -> str:
    return f"We are hiring a {level} {role} for our {stage}-stage startup. You'll build core products."

def suggest_sourcing_strategy(role: str) -> str:
    return f"Post the {role} job on LinkedIn, Wellfound, HackerNews Jobs, and Reddit."

def plan_interview_process(role: str, level: str) -> str:
    return (
        f"Interview Plan for {level} {role}:\n"
        "- Screening Call\n"
        "- Technical Interview\n"
        "- Culture Fit Round\n"
        "- Final Decision"
    )
