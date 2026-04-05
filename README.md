# 🎓 EduEval AI — Academic Answer Evaluation System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red)
![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-green)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

> An intelligent system that automatically evaluates descriptive student answers using RAG, FAISS vector search, and LLaMA-3.3 — delivering marks, grade, concept analysis, and feedback in under 2 seconds.

🚀 **Live Demo:** https://edueval-ai.streamlit.app
📁 **Author:** Prisha Nasa | Manipal University Jaipur

---

## 📌 What It Does

EduEval AI lets faculty upload their marking criteria as a PDF. When a student answer is submitted, the system retrieves the most relevant chunks from the syllabus using FAISS vector search and passes them to a Large Language Model for evaluation. The result includes marks, grade, concepts covered, concepts missing, strengths, weaknesses, detailed feedback, and a model answer.

---

## 🏗️ System Architecture
---

## Features

| Feature | Description |
|---------|-------------|
| PDF Knowledge Base | Upload any syllabus, marking scheme, or textbook PDF |
| Semantic Retrieval | FAISS finds the most relevant reference chunks per question |
| LLM Evaluation | LLaMA-3.3 70B produces rubric-aligned marks and feedback |
| Explainable Results | Concepts covered, concepts missing, strengths, weaknesses |
| Model Answer | AI-generated model answer for student learning |
| Batch Evaluation | Evaluate entire class via CSV upload |
| Persistent Index | FAISS index saved to disk — survives app restarts |
| Score Visualization | Plotly gauge chart with colour-coded grade |

---

## 🛠️ Tech Stack

| Technology | Role |
|-----------|------|
| Python 3.11 | Core language |
| Streamlit | Web UI |
| Groq API LLaMA-3.3 70B | LLM evaluation engine |
| FAISS IndexFlatIP | Vector similarity search |
| Sentence Transformers all-MiniLM-L6-v2 | Text embeddings 384-dim |
| PyMuPDF | PDF text extraction |
| LangChain Text Splitters | Intelligent chunking |
| Plotly | Score gauge visualization |
| Pandas | Batch evaluation and data handling |

---

## 🚀 Quick Start

### Step 1 — Get a FREE Groq API Key
Go to https://console.groq.com → Sign up → API Keys → Create Key

### Step 2 — Set up environment
```bash
conda create -n evaluator python=3.11 -y
conda activate evaluator
conda install -c conda-forge faiss-cpu -y
pip install -r requirements.txt
```

### Step 3 — Run the app
```bash
streamlit run app.py
```

Open http://localhost:8501 and paste your Groq API key in the sidebar.

---

## 📁 Project Structure
---

## 📊 How Evaluation Works

The system sends three things to the LLM:
1. The question
2. The student answer
3. Retrieved context from uploaded PDFs via FAISS

The LLM returns:
- marks_awarded — score out of configured maximum
- grade — A+ to F
- concepts_covered — what the student got right
- concepts_missing — gaps in the answer
- strengths — positive aspects
- weaknesses — areas to improve
- detailed_feedback — constructive written feedback
- improved_answer — model answer the student can learn from

---

## 📦 Batch Evaluation CSV Format
```csv
student_name,question,student_answer
Alice,What is RAG?,RAG stands for Retrieval Augmented Generation...
Bob,Explain FAISS,FAISS is a library for efficient similarity search...
```

---

## 📈 ML Accuracy Evaluation Results

| Metric | Value |
|--------|-------|
| Pearson Correlation AI vs Human | 0.9219 |
| Within 1 Mark Agreement | 100% |
| Grade Match Accuracy | 84.0% |
| Linear Regression R2 | 0.9140 |
| Best ML Model | Random Forest 72% accuracy |

---

## 🔮 Future Scope

- Supabase database integration for permanent student result storage
- OCR module for scanned handwritten answer sheets
- Multi-language support
- Direct ePAD system API integration
- Plagiarism detection module
