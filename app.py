import streamlit as st

from src.rag import (
    ask_question,
    ask_without_rag
)

from src.conversation_manager import (
    save_conversation
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Study Companion",
    page_icon="📚",
    layout="wide"
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


if "conversation_file" not in st.session_state:

    st.session_state.conversation_file = None


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title(
    "📚 Study Companion"
)

st.sidebar.write(
    "Your personal AI tutor"
)


# --------------------------------------------------
# NEW CHAT
# --------------------------------------------------

if st.sidebar.button(
    "➕ New Chat",
    use_container_width=True
):

    st.session_state.messages = []

    st.session_state.conversation_file = None

    st.rerun()


st.sidebar.divider()


# --------------------------------------------------
# STUDY MODE
# --------------------------------------------------

study_mode = st.sidebar.selectbox(
    "Choose a study mode:",
    [
        "Ask Question",
        "Summarize",
        "Explain Simply",
        "Give Example",
        "Generate MCQs",
        "Viva Questions",
        "Flashcards",
        "Revision Questions"
    ]
)


# --------------------------------------------------
# CLEAR CURRENT CHAT
# --------------------------------------------------

if st.sidebar.button(
    "🗑️ Clear Current Chat",
    use_container_width=True
):

    st.session_state.messages = []

    st.session_state.conversation_file = None

    st.rerun()


# --------------------------------------------------
# MAIN PAGE
# --------------------------------------------------

st.title(
    "📚 AI Study Companion"
)

st.write(
    "Your personal AI tutor powered by "
    "Retrieval-Augmented Generation (RAG)."
)


# --------------------------------------------------
# CURRENT CONVERSATION
# --------------------------------------------------

if st.session_state.messages:

    st.subheader(
        "💬 Current Conversation"
    )


    for message in st.session_state.messages:

        if message["role"] == "user":

            st.markdown(
                "### 👤 You"
            )

            st.write(
                message["content"]
            )


        else:

            st.markdown(
                "### 🤖 AI Study Companion"
            )

            st.write(
                message["content"]
            )


# --------------------------------------------------
# ASK QUESTION
# --------------------------------------------------

question = st.text_input(
    "Ask something about your study material:"
)


if st.button(
    "Generate",
    use_container_width=True
):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )


    else:

        # ------------------------------------------
        # Generate answer
        # ------------------------------------------

        with st.spinner(
            "Searching your study material..."
        ):

            answer, sources = ask_question(
                question,
                mode=study_mode,
                conversation_history=(
                    st.session_state.messages
                )
            )


        # ------------------------------------------
        # Save user message
        # ------------------------------------------

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )


        # ------------------------------------------
        # Save AI response
        # ------------------------------------------

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


        # ------------------------------------------
        # Save / update same conversation
        # ------------------------------------------

        saved_file = save_conversation(
            st.session_state.messages,
            st.session_state.conversation_file
        )


        # ------------------------------------------
        # Remember conversation filename
        # ------------------------------------------

        if saved_file:

            st.session_state.conversation_file = (
                saved_file.name
            )


        # ------------------------------------------
        # Display answer
        # ------------------------------------------

        st.subheader(
            "🤖 Answer"
        )

        st.write(
            answer
        )


        # ------------------------------------------
        # Display sources
        # ------------------------------------------

        if sources:

            st.subheader(
                "📖 Sources"
            )

            shown_sources = set()


            for source in sources:

                source_key = (
                    source["source"],
                    source["page"]
                )


                if source_key not in shown_sources:

                    st.write(
                        f"• {source['source']} "
                        f"— Page {source['page']}"
                    )

                    shown_sources.add(
                        source_key
                    )


# --------------------------------------------------
# RAG VS NO-RAG
# --------------------------------------------------

st.divider()


st.subheader(
    "🔬 RAG vs. No-RAG Comparison"
)


st.write(
    "Compare the answer produced by the LLM without "
    "student study material against the answer produced "
    "using RAG and your study material."
)


comparison_question = st.text_input(
    "Enter a question for comparison:",
    key="comparison_question"
)


if st.button(
    "Compare RAG vs No-RAG",
    use_container_width=True
):

    if not comparison_question.strip():

        st.warning(
            "Please enter a question for comparison."
        )


    else:

        with st.spinner(
            "Generating both answers..."
        ):

            no_rag_answer = ask_without_rag(
                comparison_question
            )


            rag_answer, rag_sources = ask_question(
                comparison_question,
                mode="Ask Question",
                conversation_history=None
            )


        # ------------------------------------------
        # Display comparison
        # ------------------------------------------

        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "❌ Without RAG"
            )

            st.write(
                no_rag_answer
            )


        with col2:

            st.subheader(
                "✅ With RAG"
            )

            st.write(
                rag_answer
            )


        # ------------------------------------------
        # RAG sources
        # ------------------------------------------

        if rag_sources:

            st.subheader(
                "📖 RAG Sources"
            )

            shown_sources = set()


            for source in rag_sources:

                source_key = (
                    source["source"],
                    source["page"]
                )


                if source_key not in shown_sources:

                    st.write(
                        f"• {source['source']} "
                        f"— Page {source['page']}"
                    )

                    shown_sources.add(
                        source_key
                    )