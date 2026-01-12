from utils.openai_client import analyze_resume

def analyze_resume_controller(resume_text: str) -> dict:
    """
    Controller for resume analysis.
    """
    if not resume_text:
        return {"error": "Resume text is required"}
    
    analysis = analyze_resume(resume_text)
    return {"analysis": analysis}
