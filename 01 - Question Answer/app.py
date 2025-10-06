
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm = GoogleGenerativeAI(model="gemini-2.5-flash-lite", api_key=api_key)

#Function to return the response
def load_answer(question):
    answer=llm.invoke(question)
    return answer


#App UI starts here
st.set_page_config(page_title="question_answer", page_icon=":robot:")
st.header("Ask Me Anything 🤖")

#Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input=get_text()


submit = st.button('Generate')  

#If generate button is clicked
if submit:
    with st.spinner("Thinking.."):
        response = load_answer(user_input)
    st.success("Done!")
    st.subheader("Answer:")
    st.write(response)

