import json
from pathlib import Path
from datetime import datetime


# --------------------------------------------------
# CONVERSATION STORAGE
# --------------------------------------------------

CONVERSATION_FOLDER = Path("conversations")

CONVERSATION_FOLDER.mkdir(
    exist_ok=True
)


# --------------------------------------------------
# CREATE CONVERSATION TITLE
# --------------------------------------------------

def create_title(question):
    """
    Create a short title from the first question.
    """

    if not question:
        return "New Conversation"

    words = question.strip().split()

    title_words = words[:6]

    title = " ".join(title_words)

    title = title.rstrip("?")

    if title:
        title = title[0].upper() + title[1:]

    if len(words) > 6:
        title += "..."

    return title


# --------------------------------------------------
# SAVE OR UPDATE CONVERSATION
# --------------------------------------------------

def save_conversation(
    messages,
    filename=None
):
    """
    Save a new conversation or update
    an existing conversation.
    """

    if not messages:
        return None

    # ----------------------------------------------
    # Create a new filename if needed
    # ----------------------------------------------

    if filename is None:

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )

        filename = (
            f"conversation_{timestamp}.json"
        )

    filepath = (
        CONVERSATION_FOLDER / filename
    )


    # ----------------------------------------------
    # Find first user question
    # ----------------------------------------------

    first_question = ""

    for message in messages:

        if message.get("role") == "user":

            first_question = message.get(
                "content",
                ""
            )

            break


    # ----------------------------------------------
    # Create title
    # ----------------------------------------------

    title = create_title(
        first_question
    )


    # ----------------------------------------------
    # Create conversation object
    # ----------------------------------------------

    conversation = {
        "title": title,

        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "messages": messages
    }


    # ----------------------------------------------
    # Save JSON
    # ----------------------------------------------

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            conversation,
            file,
            indent=4,
            ensure_ascii=False
        )


    return filepath


# --------------------------------------------------
# LOAD CONVERSATIONS
# --------------------------------------------------

def load_conversations():
    """
    Load all saved conversations.
    """

    conversations = []

    for filepath in sorted(
        CONVERSATION_FOLDER.glob("*.json"),
        reverse=True
    ):

        try:

            with open(
                filepath,
                "r",
                encoding="utf-8"
            ) as file:

                conversation = json.load(
                    file
                )


            conversation["filename"] = (
                filepath.name
            )


            conversations.append(
                conversation
            )


        except Exception:

            continue


    return conversations


# --------------------------------------------------
# DELETE CONVERSATION
# --------------------------------------------------

def delete_conversation(filename):
    """
    Delete a saved conversation.
    """

    filepath = (
        CONVERSATION_FOLDER / filename
    )


    if filepath.exists():

        filepath.unlink()

        return True


    return False