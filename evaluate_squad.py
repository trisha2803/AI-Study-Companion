from datasets import load_dataset

from src.retriever import search


# =========================================================
# SQuAD 2.0 UNSUPPORTED QUESTION EVALUATION
# =========================================================

# Same relevance threshold used by the RAG system
MAX_DISTANCE = 1.0

# Number of SQuAD 2.0 unanswerable questions to test
NUM_QUESTIONS = 20


print("=" * 60)
print("SQuAD 2.0 Unsupported Question Evaluation")
print("=" * 60)


# =========================================================
# LOAD SQUAD 2.0
# =========================================================

print("\nLoading SQuAD 2.0 dataset...")

dataset = load_dataset(
    "rajpurkar/squad_v2",
    split="validation"
)


# =========================================================
# SELECT UNANSWERABLE QUESTIONS
# =========================================================

unanswerable_questions = [
    item
    for item in dataset
    if len(item["answers"]["text"]) == 0
]


print(
    f"Total unanswerable questions available: "
    f"{len(unanswerable_questions)}"
)


# Use a fixed number of questions
test_questions = unanswerable_questions[
    :NUM_QUESTIONS
]


print(
    f"Testing {len(test_questions)} "
    "unanswerable questions."
)


# =========================================================
# RUN RETRIEVAL TEST
# =========================================================

correct_rejections = 0


print("\nRunning evaluation...\n")


for number, item in enumerate(
    test_questions,
    start=1
):

    question = item["question"]


    # Search the student's study material
    results = search(
        question,
        k=3,
        max_distance=MAX_DISTANCE
    )


    # No sufficiently relevant material
    # means the system correctly rejects
    # the unsupported question.

    if not results:

        correct_rejections += 1

        result = "CORRECTLY REJECTED"

    else:

        result = "RETRIEVED MATERIAL"


    print(
        f"{number:02d}. {question}"
    )

    print(
        f"    Result: {result}"
    )

    print()


# =========================================================
# CALCULATE RESULT
# =========================================================

total = len(test_questions)


if total > 0:

    rejection_rate = (
        correct_rejections / total
    ) * 100

else:

    rejection_rate = 0


# =========================================================
# DISPLAY FINAL RESULTS
# =========================================================

print("=" * 60)

print("Evaluation Results")

print("=" * 60)

print(
    f"Total questions tested: {total}"
)

print(
    f"Correctly rejected: {correct_rejections}"
)

print(
    f"Unsupported-question rejection rate: "
    f"{rejection_rate:.2f}%"
)

print("=" * 60)