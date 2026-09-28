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

---

## 5. System Workflow

The AI Study Companion follows a Retrieval-Augmented Generation (RAG) workflow.

1. **PDF Upload:** Students provide their study materials in PDF format.
2. **Text Extraction:** PyPDF extracts text from the uploaded documents, including page information.
3. **Text Processing:** The extracted text is divided into smaller chunks for efficient retrieval.
4. **Embedding Generation:** Sentence Transformers converts text chunks into numerical embeddings using `all-MiniLM-L6-v2`.
5. **Vector Storage:** FAISS stores and searches the embeddings to find relevant content.
6. **Question Processing:** The student's question is converted into an embedding and matched with relevant study material.
7. **Answer Generation:** The retrieved content is sent to the Groq LLM to generate a grounded answer.
8. **Source Citation:** The system displays the source document and page number when available.

---

## 6. Key Features

* **Personalized Learning:** Answers questions using student-provided study materials.
* **Context-Based Answers:** Retrieves relevant information before generating responses.
* **Simple Explanations:** Helps students understand difficult concepts.
* **Study Material Generation:** Creates summaries, MCQs, viva questions, flashcards and revision questions.
* **Conversation Context:** Supports follow-up questions using conversation history.
* **Source References:** Displays document names and page numbers for retrieved information.
* **Out-of-Context Handling:** Can indicate when the required answer is not found in the available material.
* **RAG Comparison:** Supports comparison between answers generated with and without retrieved study context.

---

## 7. Installation and Setup

### Prerequisites

* Python 3.10 or a compatible version
* pip
* A Groq API key

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Study-Companion
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure the Groq API Key

Set your API key as an environment variable named `GROQ_API_KEY`, or configure it using Streamlit secrets according to your application code.

Never upload your actual API key to GitHub.

### Step 4: Run the Application

```bash
streamlit run app.py
```

Open the local URL shown in your terminal to use the application.

---

## 8. Evaluation

The project uses the SQuAD 2.0 dataset for question-answering evaluation.

The evaluation aims to examine:

* Answer relevance and correctness.
* The ability to handle questions that cannot be answered from the available context.
* Differences between responses generated without RAG and responses generated with retrieved context.

Evaluation results and metrics should be added here after running the experiments. The dataset alone does not establish the system's accuracy.

---

## 9. Limitations

* Answer quality depends on the content and readability of the uploaded PDFs.
* Incorrect or incomplete text extraction may affect retrieval.
* The generated answer may still contain errors, even when relevant context is retrieved.
* Response quality depends partly on the language model and the retrieved passages.
* The system requires access to the Groq API for model responses.

---

## 10. Future Improvements

* Improve retrieval accuracy and document processing.
* Support more document formats.
* Improve answer evaluation using additional metrics.
* Enhance the user interface and learning experience.
* Add more personalized revision and progress-tracking features.

---

## 11. Author

**Trisha H**
Computer Science and Engineering
Siddaganga Institute of Technology, Tumakuru
