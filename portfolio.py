import streamlit as st

st.set_page_config(page_title="George Dean III Portfolio", page_icon=":computer:", layout="wide")

st.title("George Dean III 💻")
st.subheader("Computer Information Systems | Software Engineering & Data Analytics")

# Objective Section
st.markdown("### 🎯 Objective")
st.write("""
Results-driven Computer Information Systems student with hands-on experience as a Software Engineering and Data Analyst Co-Op at Bosch Rexroth. 
Seeking a full-time role in Cloud Engineering, Business & Data Analytics, Systems Administration, or Backend Engineering. 
Proven ability to develop innovative solutions, automate processes, and leverage emerging technologies to drive operational efficiency.
""")

# Education Section
st.markdown("### 🎓 Education")
st.write("""
**Clemson University** | Clemson, SC
Bachelor of Science in Computer Information Systems
Expected Graduation: December 2025
""")

# Certifications Section
st.markdown("### 📜 Certifications")
certifications = [
    "IBM - What is Data Science? (Jul 2023)",
    "Google – Technical Support Fundamentals (Jan 2022)",
    "Neo4j – Neo4j Fundamentals (Jun 2024)",
    "Neo4j – Cypher Fundamentals (Jun 2024)",
    "IBM – Data Analysis with Python (Nov 2024)"
]
for cert in certifications:
    st.write(f"- {cert}")

# Skills Section
st.markdown("### 💻 Technical Skills")
col1, col2 = st.columns(2)
with col1:
    st.write("""
    **Programming Languages:**
    - Python
    - C++
    - C
    - C#
    - SQL
    """)
with col2:
    st.write("""
    **Tools & Technologies:**
    - Git
    - Neo4j
    - Power BI
    - Jupyter Notebook
    - MS Excel
    """)

# Projects Section
st.markdown("### 🚀 Projects")
projects = [
    "Personal Portfolio Website (HTML, JavaScript, CSS)",
    "Recommendation Tool (Neo4j, Python, Postman)",
    "PDF Extractor Tool (Python, Jupyter Notebook, Excel)"
]
for project in projects:
    st.write(f"- {project}")

# Experience Section
st.markdown("### 💼 Professional Experience")

# Bosch Rexroth Experience
st.markdown("#### Software Engineering and Data Analyst Co-Op | Bosch Rexroth")
st.write("""
- Developed a Python script improving PDF-to-Excel conversion times by 90%
- Created a Neo4j-based recommendation system reducing shop floor claims by 75%
- Applied machine learning techniques to predict pump/motor breakdowns
- Utilized Git for version control and collaborated using Agile methodologies
""")

# Clemson University Experience
st.markdown("#### Work Study-Library Security Officer | Clemson University")
st.write("""
- Implemented an efficient badge scanning system, reducing unauthorized access incidents by 20%
- Conducted regular security rounds and maintained a safe library environment
- Received commendations for exceptional performance and professionalism
""")

# Walmart Experience
st.markdown("#### Stocker, Team Lead | Walmart")
st.write("""
- Revamped inventory management system, reducing stockouts by 20%
- Led a team of 15 associates, achieving 15% increase in productivity
- Implemented streamlined restocking procedures, decreasing stocking time by 30%
- Successfully trained and onboarded 10 new stockers
""")

# Chick-fil-A Experience
st.markdown("#### Cashier, Team Lead | Chick-fil-A")
st.write("""
- Boosted drive-thru order accuracy by 10%
- Led team to achieve 98% customer satisfaction rating during peak hours
- Implemented cost-saving measures resulting in 5% decrease in operational expenses
- Managed a team of 6 cashiers effectively
""")

# Contact Information
st.markdown("### 📞 Contact Information")
st.write("""
- **Email:** georgedeaniii@example.com
- **LinkedIn:** [George Dean III](https://www.linkedin.com/in/yourprofile)
- **GitHub:** [GRD39101](https://github.com/GRD39101)
""")
