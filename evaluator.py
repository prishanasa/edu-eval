<<<<<<< HEAD
"""
Evaluator — sends question + student answer + RAG context to the Groq LLM
and parses the structured evaluation response.
"""

import json
import re
from groq import Groq

# ── Model config ─────────────────────────────────────────────────────────────
GROQ_MODEL   = "llama-3.3-70b-versatile"   # Free, fast, high quality
MAX_TOKENS   = 1500
TEMPERATURE  = 0.2                  # Low = more consistent scoring


# ── Prompt template ──────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are an expert academic evaluator.
Your job is to evaluate a student's descriptive answer against reference material retrieved from the course syllabus/textbook.

You MUST respond with ONLY a valid JSON object — no markdown fences, no explanation outside JSON.

JSON schema (follow exactly):
{
  "marks_awarded": <integer 0-10>,
  "max_marks": 10,
  "percentage": <float>,
  "grade": <"A+" | "A" | "B" | "C" | "D" | "F">,
  "concepts_covered": [<string>, ...],
  "concepts_missing": [<string>, ...],
  "strengths": [<string>, ...],
  "weaknesses": [<string>, ...],
  "detailed_feedback": "<2-4 sentences of constructive feedback>",
  "improved_answer": "<a model answer the student can learn from, 3-6 sentences>"
}

Grading scale:
  9-10 → A+,  8 → A,  7 → B,  5-6 → C,  3-4 → D,  0-2 → F
"""

USER_PROMPT_TEMPLATE = """QUESTION:
{question}

STUDENT'S ANSWER:
{student_answer}

REFERENCE MATERIAL (from course syllabus/textbook):
{context}

Evaluate the student's answer strictly based on the reference material above.
Award marks out of 10 based on concept coverage, correctness, and clarity.
Return ONLY the JSON object."""


class Evaluator:
    """Wraps the Groq API and handles prompt construction + response parsing."""

    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)

    def evaluate(self, question: str, student_answer: str, context: str) -> dict:
        """
        Run the evaluation.  Returns a parsed dict on success,
        or a dict with 'error' key on failure.
        """
        user_msg = USER_PROMPT_TEMPLATE.format(
            question=question,
            student_answer=student_answer,
            context=context if context else "No reference material available. Evaluate based on general knowledge.",
        )

        try:
            response = self.client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user",   "content": user_msg},
                ],
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS,
            )
            raw_text = response.choices[0].message.content.strip()
            return self._parse_response(raw_text)

        except Exception as e:
            return {"error": str(e)}

    # ── Response parsing ─────────────────────────────────────────────────────

    def _parse_response(self, text: str) -> dict:
        """Extract JSON from the LLM response robustly."""
        # Strip markdown fences if the model added them anyway
        text = re.sub(r"```(?:json)?", "", text).strip().rstrip("`").strip()

        try:
            data = json.loads(text)
            return self._validate(data)
        except json.JSONDecodeError:
            # Try to find JSON block inside the text
            match = re.search(r"\{.*\}", text, re.DOTALL)
            if match:
                try:
                    data = json.loads(match.group())
                    return self._validate(data)
                except json.JSONDecodeError:
                    pass
            return {"error": f"Could not parse LLM response:\n{text}"}

    def _validate(self, data: dict) -> dict:
        """Ensure required keys exist; fill defaults for optional ones."""
        required = ["marks_awarded", "grade", "concepts_covered",
                    "concepts_missing", "detailed_feedback", "improved_answer"]
        for key in required:
            if key not in data:
                data[key] = "N/A"

        # Ensure numeric fields are correct types
        if "marks_awarded" in data:
            try:
                data["marks_awarded"] = int(data["marks_awarded"])
            except (ValueError, TypeError):
                data["marks_awarded"] = 0

        if "percentage" not in data or data["percentage"] == "N/A":
            try:
                data["percentage"] = round(data["marks_awarded"] / 10 * 100, 1)
            except Exception:
                data["percentage"] = 0.0

        data.setdefault("max_marks", 10)
        data.setdefault("strengths",  [])
        data.setdefault("weaknesses", [])
        return data
=======
from vector_store import retrieve_context
from prompts import build_evaluation_prompt
from sentence_transformers import SentenceTransformer
import numpy as np

# Dummy LLM function (replace with OpenAI / HF later)
def call_llm(prompt):
    """
    Replace this with actual API call:
    - OpenAI GPT
    - HuggingFace model
    """
    return "LLM response based on prompt:\n" + prompt[:500]


# ------------------------------
# Concept Similarity Utility
# ------------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')

def similarity_score(text1, text2):
    emb1 = model.encode([text1])
    emb2 = model.encode([text2])
    sim = np.dot(emb1, emb2.T) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
    return float(sim)


# ------------------------------
# Main Evaluation Function
# ------------------------------
def evaluate_answer(question, student_answer):
    # Step 1: Retrieve syllabus-grounded context (RAG)
    context = retrieve_context(question)

    # Step 2: Build prompt for LLM reasoning
    prompt = build_evaluation_prompt(
        question=question,
        student_answer=student_answer,
        context=context
    )

    # Step 3: Call LLM (mock / real)
    llm_feedback = call_llm(prompt)

    # Step 4: Compute simple coverage score
    sim = similarity_score(student_answer, context)

    if sim > 0.7:
        score = 5
    elif sim > 0.5:
        score = 3
    else:
        score = 1

    return {
        "context_used": context,
        "score": score,
        "similarity": sim,
        "feedback": llm_feedback
    }
>>>>>>> 1a2b3350ade651a153a44dbc49d1cb094333612d
