import streamlit as st
from transformers import pipeline
import re

# Set page config
st.set_page_config(page_title="QA System", layout="wide")

# Load the QA pipeline once and cache it
@st.cache_resource
def load_qa_model():
    return pipeline("question-answering", model="timpal0l/mdeberta-v3-base-squad2")

qa_pipeline = load_qa_model()

st.title("Question & Answering System")
st.markdown("Ask a question based on a given context. The model will answer only if confident.")

# Inputs
context = st.text_area(" Enter Context Paragraph:", height=250, placeholder="Paste or type your paragraph here...")
question = st.text_input("? Enter Your Question:", placeholder="Type your question here...")

if st.button(" Get Answer"):
    if not context.strip():
        st.error("!!! Please fill the context before asking the question.")
    elif not question.strip():
        st.error("!!! Please enter a question.")
    else:
        try:
            result = qa_pipeline(question=question, context=context)
            answer = result.get('answer', '').strip()
            score = result.get('score', 0.0)
            score_percent = round(score * 100, 2)

            # Check if answer is blank
            if not answer:
                st.warning(" The model did not find a reliable answer in the context.")
                st.markdown(f"**Confidence Score:** {score_percent}%")
                st.stop()

            # Relevance check (basic keyword overlap)
            question_keywords = set(re.findall(r'\w+', question.lower()))
            context_keywords = set(re.findall(r'\w+', context.lower()))
            overlap = question_keywords & context_keywords

            # Highlight answer in context
            def highlight_answer(text, ans):
                pattern = re.escape(ans)
                return re.sub(pattern, f"**🟨{ans}🟨**", text, flags=re.IGNORECASE)

            st.markdown("###  Answer Result")

            if score_percent >= 70:
                if len(overlap) == 0:
                    st.warning(" High confidence, but question appears unrelated to context.")
                st.success(f" Answer: {answer}")
                st.markdown(f" **Confidence Score:** {score_percent}%")
                st.markdown("###  Context with Highlight:")
                st.markdown(highlight_answer(context, answer))
            elif 50 <= score_percent < 70:
                st.warning(f" Model is moderately confident ({score_percent}%). Answer may not be fully reliable.")
                st.info(f" Possible Answer: {answer}")
                st.markdown(" The context might be too short or the question unclear.")
                st.markdown(highlight_answer(context, answer))
            elif 40 <= score_percent < 50:
                st.error(f" Low confidence ({score_percent}%). Answer may be incorrect.")
                st.info(f" Answer: {answer}")
                st.markdown(" Consider refining your question or adding more context.")
            else:
                st.error(f" Very Low Confidence ({score_percent}%)")
                st.markdown("The model is unsure about the answer. No answer shown.")
                st.markdown("Tip: Try asking a more relevant or clear question.")

        except Exception as e:
            st.error(f" Error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using [Hugging Face Transformers](https://huggingface.co/models) and Streamlit")
