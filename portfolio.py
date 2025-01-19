import streamlit as st

# Use a relative path from your GitHub repository
image_path = 'images/Screenshot 2025-01-19 at 4.50.54 PM.png'

# Alternative: Use a direct GitHub raw image URL
# image_path = 'https://raw.githubusercontent.com/YourUsername/YourRepo/main/images/YourImage.png'

st.title('Hi there is my name is George Dean III :wave:')
st.subheader("I am creating a portfolio website to showcase my skills and experience.")
st.text("I am using streamlit to build a site.")

# Optional: Display the image
st.image(image_path, caption='Clemson Tiger Paw')

st.markdown('<h2>College</h2>', unsafe_allow_html=True)
st.markdown('<h2>Experience</h2>', unsafe_allow_html=True)
st.markdown('<h2>Skills</h2>', unsafe_allow_html=True)
