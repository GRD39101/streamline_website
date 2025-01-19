import streamlit as st

st.set_page_config(page_title="My webpage",page_icon = ":tada:",layout="wide")

st.title('Hi there my name is George Dean III :wave:')
st.subheader("I am putting my python knowledge to test for both frontend and backend development somewhat to build websites and much more.")
st.text("I am using streamlit to build a site.")
st.text("On the 2nd go around, I will update this to ask you questions.")
name = st.text_input("What is your name? Type it below...")
if(st.button("Submit")):
    result = name.title()
    st.success(result)
    st.write(f"Hello, {result}!")

