# Text preprocessing utilities for EduEval AI

import re

def clean_text(text):
    """Clean extracted PDF text"""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    text = text.strip()
    return text

def remove_special_characters(text):
    """Remove unwanted special characters"""
    return re.sub(r'[^a-zA-Z0-9\s.,;:!?()-]', '', text)

def normalize_whitespace(text):
    """Normalize multiple spaces and newlines"""
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()

def preprocess_answer(answer):
    """Full preprocessing pipeline for student answers"""
    answer = clean_text(answer)
    answer = normalize_whitespace(answer)
    return answer

def preprocess_chunk(chunk):
    """Full preprocessing pipeline for PDF chunks"""
    chunk = clean_text(chunk)
    chunk = normalize_whitespace(chunk)
    return chunk
