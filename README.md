# 📚 AI Study Companion — Personalized RAG Tutor

## 1. Project Overview

AI Study Companion is a personalized AI tutor that answers students' questions using their own study material.

The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from student-provided PDF documents and provide grounded answers with source and page citations.

The project demonstrates the difference between:

- LLM without grounding
- LLM + RAG + student-specific knowledge

---

## 2. Objectives

The main objectives of the project are:

- Answer questions from student study material.
- Provide simple explanations.
- Summarize study material.
- Give examples.
- Generate MCQs.
- Generate viva questions.
- Generate flashcards.
- Generate revision questions.
- Maintain conversation context.
- Show source document and page number.
- Refuse to answer when the required information is not available in the study material.
- Compare RAG answers with answers generated without RAG.

---

## 3. Technologies Used

### Programming Language
- Python

### User Interface
- Streamlit

### PDF Processing
- PyPDF

### Embeddings
- Sentence Transformers
- `all-MiniLM-L6-v2`

### Vector Database
- FAISS

### Large Language Model
- Groq API
- Model: `openai/gpt-oss-20b`

### Dataset Evaluation
- SQuAD 2.0

---

## 4. Student Dataset

The current student study corpus contains:

**10 PDF documents**

The documents include study material such as:

- ADA
- Computer Programming / CPS
- HSS
- TCP/IP networking

The PDFs are stored in:

```text
data/pdfs/