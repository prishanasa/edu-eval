# Error handling utilities for EduEval AI

def handle_api_error(error):
    """Handle Groq API errors gracefully"""
    error_str = str(error)
    if "decommissioned" in error_str:
        return "Model unavailable. Please check Groq API settings."
    elif "rate_limit" in error_str:
        return "Rate limit reached. Please wait a moment and try again."
    elif "authentication" in error_str:
        return "Invalid API key. Please check your Groq API key."
    elif "timeout" in error_str:
        return "Request timed out. Please try again."
    else:
        return f"Unexpected error: {error_str}"

def validate_inputs(question, answer):
    """Validate user inputs before evaluation"""
    if not question or not question.strip():
        return False, "Question cannot be empty."
    if not answer or not answer.strip():
        return False, "Student answer cannot be empty."
    if len(answer.strip()) < 10:
        return False, "Answer is too short to evaluate meaningfully."
    if len(question.strip()) < 5:
        return False, "Question is too short."
    return True, "Valid"
