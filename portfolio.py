import streamlit as st
import base64

# Function to convert image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to your image
image_path = '/Users/georgedeaniii/Desktop/Screenshot 2025-01-19 at 4.50.54 PM.png'

# Convert image to base64
img_base64 = get_base64_of_bin_file(image_path)

# Custom CSS with base64 image
st.markdown(f"""
<style>
.header-clemson {{
    background-image: url('data:image/png;base64,{img_base64}');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    padding: 20px;
    color: white;
}}
</style>
""", unsafe_allow_html=True)

# Rest of your existing code remains the same
st.title('Hi there is my name is George Dean III :wave:')
st.subheader("I am creating a portfolio website to showcase my skills and experience.")
st.text("I am using streamlit to build a site.")

st.markdown('<h2 class="header-clemson">College</h2>', unsafe_allow_html=True)
st.markdown('<h2 class="header-clemson">Experience</h2>', unsafe_allow_html=True)
st.markdown('<h2 class="header-clemson">Skills</h2>', unsafe_allow_html=True)
