from pathlib import Path

import streamlit as st
from PIL import Image

# Path 
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Davis'_CV.pdf"
profile_pic = current_dir / "assets" / "Davis_pic_tr_best.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Davis Digital CV"
PAGE_ICON = ":wave:"
NAME = "Davis Onyeoguzoro"
DESCRIPTION = """
Data Analyst. A result-oriented professional with strong analytical skills that helps organizations make data-driven decisions.
"""
EMAIL = "davisonyeas1@gmail.com"
SOCIAL_MEDIA = {
    "Portfolio Website": "https://davisonyeas.github.io/portfolio/",
    "LinkedIn": "https://www.linkedin.com/in/davis-onyeoguzoro/",
    "GitHub": "https://github.com/Davisonyeas",
    "Twitter": "https://twitter.com/Davisonyeas1",
}
# PROJECTS = {
#     "🏆 Sales Dashboard - Comparing sales across three stores",
#     "🏆 Income and Expense Tracker - Web app with NoSQL database",
# }

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDF_byte = pdf_file.read()

profile_pic = Image.open(profile_pic)


col_1, col_2 = st.columns(2, gap="small")

with col_1:
    st.image(profile_pic)

with col_2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDF_byte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# SOFT SKILLS
st.write("#")
st.subheader("Transferable Soft Skills")
st.write(
    """
- ✔️ Written and verbal communication skills, as well as people skills, SFIA complaint
- ✔️ Project management, procurement and strong analytical skills
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Excellent leader and team-player that displays a strong sense of initiative on tasks
"""
)

st.write("#")
st.subheader("Technical Skills")

col_3, col_4, col_5 = st.columns(3, gap="small")

with col_3:
    st.write("""
    👨‍💻 PROGRAMMING
- ✔️ Python
- ✔️ SQL
- ✔️ JavaScript
- ✔️ R
- ✔️ Git
""")
with col_4:
    st.write("""
    📊 DATA VISUALIZATION
- ✔️ Tableau
- ✔️ Power BI
- ✔️ Matplotlib
- ✔️ Plotly
- ✔️ Seaborn
- ✔️ Ms Excel
""")
with col_5:
    st.write("""
    💻 CORE COMPETENCIES
- ✔️  Databases 🗄️
- ✔️  Data Analytics 📈
- ✔️  Machine Learning 🤖
- ✔️  Backend Development ⚙️
""")


# --- WORK HISTORY ---
st.write("#")
st.write("---")
st.subheader("Work History")


# --- JOB 1
st.write("🚧", "**Data Scientist | Greysoft Technologies**")
st.write("01/2022 - Present")
st.write(
    """
- ► Chief Instructor and organizer of data science bootcamp (GreyData School) with over 50 students.
- ► Performed targeted advertising campaigns that generated over 60% more sales from different customer groups.
- ► Utilized analytical and technical expertise to reveal hidden customer behavioural patterns and shared insights through reports to the management.
"""
)

# --- JOB 2
st.write("#")
st.write("🚧", "**Full Stack Developer | Dixre Entreprises**")
st.write("07/2021 - 12/2021")
st.write(
    """
- ► Programmed, monitored, implemented, tested and reviewed multiple web and mobile applications with full involvement in the logistics and transportation web app project.
- ► Instructed at the Web development bootcamp.
"""
)

# --- JOB 3
st.write("#")
st.write("🚧", "**System Analyst | Mouka Ltd**")
st.write("03/2016 - 12/2016")
st.write(
    """
- ► Collaborated with Business Analysts, Project Leads and IT team to resolve issues and ensured solutions are viable and consistent.
- ► Regulated and participated in training sessions and workshops on system processes.
- ► Conducted regular preventive and corrective maintenance of the various systems.
"""
)



# --- VOLUNTEERING ---
st.write("#")
st.write("---")
st.subheader("Volunteering")


# --- JOB 1
st.write("🚧", "**Team Lead | AI/ML Lead | Greysoft Technologies**")
st.write("04/2022 - Present")
st.write(
    """
- ► Provided services to the University by mentoring over 20 students as well as worked on various projects for the school.
"""
)

# --- JOB 2
st.write("#")
st.write("🚧", "**Data Science Instructor | Data Science Nigeria**")
st.write("01/2022 - Present")
st.write(
    """
- ► Provided learner support, assisted and motivated struggling learners, and encouraged those who were excelling.
"""
)



# --- Awards & Achievements ---
st.write("---")
st.write("#")
st.subheader("Awards & Achievements")

# --- Awd 1
st.write("🏆", "**Outstanding Leadership Award**")
st.write("Google Developer Student Clubs")
st.write(
    """
- ► Recognized for exceptional leadership and dedicated service towards the success of GDSC.
"""
)

# --- Awd 2
st.write("🏆", "**Distinguished Service Award**")
st.write("Google Developer Groups")
st.write(
    """
- ► Appreciated for helping the community in bridging the gap between theory and practical at the University community.
- ► Appreciated for going above and beyond to benefit the well-being of others.
"""
)


# --- PROJECTS ---
st.write("#")
st.write("---")
st.subheader("Projects")


# --- VOL 1
st.write("📈", "**Stock Price Prediction**")
st.write("🔗 [Click Here to view project](https://davisonyeas-stock-prediction-main-m0nu4u.streamlitapp.com/)")
st.write("Predictive Analytics - Python, Ms Excel, SQL, Web Scraping, Real-Time, Pandas")
st.write(
    """
- ► The aim is to predict the future value of the financial stocks of top companies based on historical and real-time data along with news analysis.
"""
)

# --- VOL 2
st.write("🧑‍🦲", "**Facial Recognition System**")
st.write("🔗 [Click Here to view project](https://www.davisonye.github.io)")
st.write("Machine Learning - Python, Ms Excel, Sci-kit learn, Computer Vision, Numpy")
st.write(
    """
- ► A  type of bio metric technique that is capable of detecting, tracking, identifying or verifying human faces from an image or video captured using a camera.
"""
)