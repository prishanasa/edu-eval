# Feedback analysis utilities for EduEval AI

def analyze_score_trend(history):
    """Analyze score trend from evaluation history"""
    if not history or len(history) < 2:
        return "Not enough data for trend analysis"
    scores = [h["marks"] for h in history]
    avg = sum(scores) / len(scores)
    latest = scores[-1]
    if latest > avg:
        return "Improving"
    elif latest < avg:
        return "Declining"
    else:
        return "Stable"

def get_performance_summary(history):
    """Return performance summary from history"""
    if not history:
        return {}
    scores = [h["marks"] for h in history]
    grades = [h["grade"] for h in history]
    return {
        "total_evaluations": len(history),
        "average_score": round(sum(scores) / len(scores), 1),
        "highest_score": max(scores),
        "lowest_score": min(scores),
        "most_common_grade": max(set(grades), key=grades.count),
        "trend": analyze_score_trend(history)
    }
