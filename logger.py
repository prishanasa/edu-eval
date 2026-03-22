# Logging utility for EduEval AI
import datetime

LOG_FILE = "eval_log.txt"

def log_evaluation(question, marks, grade, eval_time):
    """Log each evaluation with timestamp"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Q: {question[:50]}... | Marks: {marks}/10 | Grade: {grade} | Time: {eval_time}s\n"
    try:
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Logging failed: {e}")

def get_recent_logs(n=10):
    """Return last n log entries"""
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
        return lines[-n:] if len(lines) >= n else lines
    except FileNotFoundError:
        return []
