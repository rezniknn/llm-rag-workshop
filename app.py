import streamlit as st
from rag import ask_bot

def qa_bot(prompt):
    response = ask_bot(prompt)
    return f"Response for the prompt: {response}"

def main():
    st.title("DTC Q&A System")

    with st.form(key='rag_form'):
        prompt = st.text_input("Enter your prompt")
        response_placeholder = st.empty()
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        response_placeholder.markdown("Loading...")
        response = qa_bot(prompt)
        response_placeholder.markdown(response)

if __name__ == "__main__":
    main()