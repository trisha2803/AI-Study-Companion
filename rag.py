import os

from dotenv import load_dotenv
from groq import Groq

from src.retriever import search
from src.prompts import create_rag_prompt


# Load environment variables
load_dotenv()


# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY was not found in the .env file."
    )


# Create Groq client
client = Groq(api_key=api_key)


# =========================================================
# RELEVANCE THRESHOLD
# =========================================================

MAX_DISTANCE = 1.0


# =========================================================
# ANSWER WITH RAG
# =========================================================

def ask_question(
    question,
    mode="Ask Question",
    k=3,
    conversation_history=None
):

    # Create better retrieval query using previous conversation
    retrieval_query = question

    if conversation_history:

        previous_messages = conversation_history[-4:]

        previous_context = []

        for message in previous_messages:

            previous_context.append(
                message["content"]
            )

        retrieval_query = (
            "Previous conversation: "
            + " ".join(previous_context)
            + "\nCurrent question: "
            + question
        )

    # Retrieve relevant study material
    retrieved_chunks = search(
        retrieval_query,
        k=k,
        max_distance=MAX_DISTANCE
    )


    # -----------------------------------------------------
    # Reject unsupported questions
    # -----------------------------------------------------

    if not retrieved_chunks:

        return (
            "The answer is not available in the provided "
            "study material.",
            []
        )


    # Create grounded prompt
    prompt = create_rag_prompt(
        question,
        retrieved_chunks,
        mode,
        conversation_history
    )


    # Send to Groq
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )


    # Get answer
    answer = response.choices[0].message.content

    return answer, retrieved_chunks


# =========================================================
# ANSWER WITHOUT RAG
# =========================================================

def ask_without_rag(question):

    prompt = f"""
You are an AI assistant.

Answer the following question using your general knowledge.

Do not use any student study material.
Do not retrieve information from the student's documents.

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content

    return answer


# =========================================================
# DIRECT TERMINAL TESTING
# =========================================================

if __name__ == "__main__":

    question = input(
        "Enter your question: "
    )


    # Test RAG
    rag_answer, sources = ask_question(
        question
    )


    print(
        "\n===== ANSWER WITH RAG =====\n"
    )

    print(rag_answer)


    print(
        "\n===== SOURCES ====="
    )

    shown_sources = set()


    for source in sources:

        source_key = (
            source["source"],
            source["page"]
        )


        if source_key not in shown_sources:

            print(
                f"- {source['source']} "
                f"(Page {source['page']})"
            )

            shown_sources.add(
                source_key
            )


    # Test No-RAG
    no_rag_answer = ask_without_rag(
        question
    )


    print(
        "\n===== ANSWER WITHOUT RAG =====\n"
    )

    print(no_rag_answer)